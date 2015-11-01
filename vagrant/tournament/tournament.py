#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def doQuery(query,data=None):
    """Connect to the Database and set the Cursor"""
    conn = connect()
    cur = conn.cursor()

    # Results of SELECT Queries
    results = None

    # If data accompanies the query, i.e INSERT
    if data is not None:
        cur.execute(query,data)
    else:
        # No additional data for this query.
        cur.execute(query)

    # Retrieve the results for SELECT queries.
    if "SELECT" in query:
        results = cur.fetchall()
    else:
        # Commit the Changes
        conn.commit()

    # Close the connection.
    cur.close()
    conn.close()

    return results


def deleteMatches():
    """Remove all the match records from the database."""
    doQuery("DELETE from matches;")


def deletePlayers():
    """Remove all the player records from the database."""
    doQuery("DELETE from players;")


def countPlayers():
    """Returns the number of players currently registered."""
    players = doQuery("SELECT * from players;")
    if players is not None:
        return len(players)

    return None


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    data = (name,)
    doQuery("INSERT INTO players (name) VALUES (%s);", data)


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    # Use the playerstandings View to retrive the standings.
    return doQuery("SELECT * from playerstandings;")

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    # Query used to find a player name by their id.
    queryName = "SELECT name from players where player=(%s);"

    # Update the Winner's matches_won and matches_played
    data = (winner,)
    queryWin = '''UPDATE players SET matches_won = matches_won+1,
            matches_played = matches_played+1 WHERE player = (%s);'''

    # Query the Winner's name
    doQuery(queryWin, data)
    winnerName =  doQuery(queryName, data)[0][0]

    # Update the losers matches_played
    data = (loser,)
    queryLoss = '''UPDATE players SET matches_played = matches_played+1
                WHERE player = (%s);'''

    # Query the Winner's Name
    doQuery(queryLoss, data)
    loserName = doQuery(queryName, data)[0][0]

    # Create a match record using the Winner and Loser info
    data = (winner, loser)
    queryMatch = '''INSERT INTO matches
                 (winner_id, loser_id)
                 VALUES ( %s, %s );'''
    doQuery(queryMatch, data)


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """

    # Split the standings into two equal lists of players
    standings = playerStandings()

    firstPlayers = standings[::2]
    secondPlayers = standings[1::2]

    results = []
    # Iterate through both lists simultaneously, pairing the entries at the same
    # index. ( element 0 is the player id, element 1 is their name )
    for firstPlayer, secondPlayer in zip(firstPlayers, secondPlayers):
        results.append((firstPlayer[0], firstPlayer[1],
                        secondPlayer[0], secondPlayer[1]))

    return results