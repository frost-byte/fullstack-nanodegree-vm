#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def doQuery(query, data=None):
    """Perform a Query to the Database

    An SQL Query is sent to the Database which can include additional (data)

    Args:
        query: The SQL query string being sent.
        data: Optional data accompanying the query.

    Returns:
        Depending upon the nature of the query it can be None.
        For queries that are meant to return data this should be
        a list of tuples.
    """
    """Connect to the Database and set the Cursor"""
    conn = connect()
    cur = conn.cursor()

    # Results of Queries, some queries will not return anything
    results = None

    # If data accompanies the query, i.e INSERT
    if data is not None:
        cur.execute(query, data)
    else:
        # No additional data for this query.
        cur.execute(query)

    # Retrieve the results for SELECT queries.
    if "SELECT" in query:
        results = cur.fetchall()

    conn.commit()

    # Close the connection.
    cur.close()
    conn.close()

    return results


def deleteTournaments():
    """Remove all tournaments from the database."""
    doQuery("SELECT deleteTournaments();")


def deleteTournament(tournament):
    """Delete a specific tournament and related records."""
    doQuery("SELECT deleteTournament(%s);", (tournament,))


def deleteAllTournamentPlayers():
    """Remove all player records for all tournaments."""
    doQuery("DELETE FROM tournament_players;")


def deleteTournamentPlayers(tournament):
    """Remove all players from a tournament.

    Args:
        tournament: id of the tournament from which players will be removed.
    """
    query = "DELETE FROM tournament_players WHERE tourn_id=(%s);"
    doQuery(query, (tournament,))


def deleteMatches(tournament):
    """Remove all the match records for a tournamnet from the database."""
    doQuery("DELETE from matches WHERE tourn_id=(%s);", (tournament,))


def deleteAllMatches():
    """Remove all match records for all tournaments."""
    doQuery("DELETE from matches;")


def deletePlayers():
    """Remove all the player records from the database."""
    doQuery("DELETE from players;")


def createTournament():
    """Returns the ID of a new tournement, after it is created."""
    return doQuery("SELECT createTournament();")[0][0]


def countPlayers():
    """Returns the number of players."""
    return doQuery("SELECT COUNT(*) from players;")[0][0]


def countTournamentPlayers(tournament):
    """Returns the number of players registered for a given tournament.

    Args:
        tournament: the id of the tournament

    Returns:
        The number of players registered for the tournament.
    """
    query = "SELECT COUNT(*) from tournament_players WHERE tourn_id=(%s);"
    return doQuery(query, (tournament,))[0][0]


def createPlayer(name):
    """Creates a player record.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: The player's name.

    Returns:
        The id of the player just created.
    """
    return doQuery("SELECT createPlayer(%s)", (name,))[0][0]


def registerPlayer(player_id, tournament_id):
    """Registers a player for a tournament.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      player_id: The player's ID.
      tournament_id: The Tournament the player is registering for.

    """
    doQuery("SELECT registerPlayer(%s, %s);", (player_id, tournament_id))


def playerStandings(tournament):
    """For the specified Tournament, returns a list of the players and their win
    records, sorted by wins.

    The first entry in the list should be the player in first place,
    or a player tied for first place if there is currently a tie.

    Args:
        tournament: Id of the tournament of which standings we want.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    # Use the playerstandings View to retrive the standings.
    return doQuery("SELECT * FROM playerStandings(%s);", [(tournament)])


def reportMatch(tournament, winner, loser):
    """Records the outcome of a single match between two players.
    For the specified tournament.

    Args:
      tournament: the id number of the tournament
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    data = (tournament, winner, loser)
    query = "SELECT reportMatch(%s, %s, %s);"
    doQuery(query, data)


def swissPairings(tournament):
    """Returns a list of pairs of players for the next round of a match.
    For a given tournament.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player
    adjacent to him or her in the standings.

    Args:
        tournament: The id of the tournament for the pairs
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """

    return doQuery("SELECT * from swissPairings(%s);", (tournament,))
