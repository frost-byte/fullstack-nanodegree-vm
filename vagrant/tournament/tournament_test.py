#!/usr/bin/env python
#
# Test cases for tournament.py

from tournament import *

def testDeletePlayers():
    tournament = createTournament()

    player1 = createPlayer("Bubba Blue")
    registerPlayer(player1, tournament)

    player2 = createPlayer("Joe Schmoe")
    registerPlayer(player2, tournament)
    reportMatch(tournament, player1, player2)
    deletePlayers()

    print "2a. Player Records can be deleted."

def testDeleteMatches():
    tournament = createTournament()

    player1 = createPlayer("Joe Bob")
    registerPlayer(player1, tournament)

    player2 = createPlayer("Billy Jean")
    registerPlayer(player2, tournament)
    reportMatch(tournament, player1, player2)
    deleteMatches(tournament)

    print "2b. Tournament Matches can be deleted."


def testDeleteAllMatches():
    tournament = createTournament()

    player1 = createPlayer("Joe Bob")
    registerPlayer(player1, tournament)

    player2 = createPlayer("Billy Jean")
    registerPlayer(player2, tournament)
    reportMatch(tournament, player1, player2)
    deleteAllMatches()

    print "2c. All Matches can be deleted."


def testDeleteTournamentPlayers():
    tournament = createTournament()

    player1 = createPlayer("Joe Bob")
    registerPlayer(player1, tournament)

    player2 = createPlayer("Billy Jean")
    registerPlayer(player2, tournament)
    reportMatch(tournament, player1, player2)

    deleteTournamentPlayers(tournament)
    print "2d. Players for a specific tournament can be removed"
    "from the tournament."


def testDelete():
    testDeletePlayers()
    testDeleteMatches()
    testDeleteAllMatches()
    testDeleteTournamentPlayers()

    deleteTournaments()
    deleteAllTournamentPlayers()

    print "2. Records can be deleted."


def testCount():
    # Unit Test added for Tournament Functionality
    tournament = createTournament()

    deleteMatches(tournament)
    deleteTournamentPlayers(tournament)

    c = countTournamentPlayers(tournament)
    if c == '0':
        raise TypeError(
            "countTournamentPlayers() should return numeric zero, not string '0'.")
    if c != 0:
        raise ValueError("After deleting, countTournamentPlayers should return zero.")
    print "3a. After deleting, countTournamentPlayers() returns zero."

    # Previous Unit test, now just handles all players (not just for a tournament)
    deletePlayers()
    c = countPlayers()
    if c == '0':
        raise TypeError(
            "countPlayers() should return numeric zero, not string '0'.")
    if c != 0:
        raise ValueError("After deleting, countPlayers should return zero.")
    print "3b. After deleting, countPlayers() returns zero."


def testTournament():
    t_id = createTournament()

    if type(t_id) is not int:
        raise TypeError(
            "createTournament() should return a numeric value.")
    if t_id <= 0:
        raise ValueError(
            "createTournament() should return the id (>0) of the tournament record created.")
    print "createTournament() returns a valid tournament id."


def testRegister():
    # Updated unit test for Tournament functionality.
    tournament = createTournament()

    deleteMatches(tournament)
    deleteTournamentPlayers(tournament)

    player = createPlayer("Chandra Nalaar")
    registerPlayer(player, tournament)

    c = countTournamentPlayers(tournament)
    if c != 1:
        raise ValueError(
            "After one player registers for a tournament, countTournamentPlayers()"
            " should be 1.")
    print "4. After registering a player, countTournamentPlayers() returns 1."


def testRegisterCountDelete():
    deleteTournaments()
    tournament = createTournament()

    deleteMatches(tournament)
    deleteTournamentPlayers(tournament)

    player = createPlayer("Markov Chaney")
    registerPlayer(player, tournament)

    player = createPlayer("Joe Malik")
    registerPlayer(player, tournament)

    player = createPlayer("Mao Tsu-hsi")
    registerPlayer(player, tournament)

    player = createPlayer("Atlanta Hope")
    registerPlayer(player, tournament)

    c = countTournamentPlayers(tournament)
    if c != 4:
        raise ValueError(
            "After registering four players, countTournamentPlayers should be 4.")
    deleteTournamentPlayers(tournament)
    c = countTournamentPlayers(tournament)
    if c != 0:
        raise ValueError("After deleting, countTournamentPlayers should return zero.")
    print "5. Tournament Players can be registered and deleted."


def testStandingsBeforeMatches():
    deleteTournaments()
    tournament = createTournament()

    deleteMatches(tournament)
    deleteTournamentPlayers(tournament)

    # With the extra credit Tournament feature, a tournament has to be
    # created first.  Then players can be created and then registered for the tournament
    tournament = createTournament()

    player = createPlayer("Melpomene Murray")
    registerPlayer(player, tournament)

    player = createPlayer("Randy Schwartz")
    registerPlayer(player, tournament)

    standings = playerStandings(tournament)
    if len(standings) < 2:
        raise ValueError("Players should appear in playerStandings even before "
                         "they have played any matches.")
    elif len(standings) > 2:
        raise ValueError("Only registered players should appear in standings.")
    if len(standings[0]) != 4:
        raise ValueError("Each playerStandings row should have four columns.")
    [(id1, name1, wins1, matches1), (id2, name2, wins2, matches2)] = standings
    if matches1 != 0 or matches2 != 0 or wins1 != 0 or wins2 != 0:
        raise ValueError(
            "Newly registered players should have no matches or wins.")
    if set([name1, name2]) != set(["Melpomene Murray", "Randy Schwartz"]):
        raise ValueError("Registered players' names should appear in standings, "
                         "even if they have no matches played.")
    print "6. Newly registered players appear in the standings with no matches."


def testReportMatches():
    deleteTournaments()
    tournament = createTournament()

    deleteMatches(tournament)
    deleteTournamentPlayers(tournament)


    player = createPlayer("Bruno Walton")
    registerPlayer(player, tournament)

    player = createPlayer("Boots O'Neal")
    registerPlayer(player, tournament)

    player = createPlayer("Cathy Burton")
    registerPlayer(player, tournament)

    player = createPlayer("Diane Grant")
    registerPlayer(player, tournament)

    standings = playerStandings(tournament)
    [id1, id2, id3, id4] = [row[0] for row in standings]
    reportMatch(tournament, id1, id2)
    reportMatch(tournament, id3, id4)
    standings = playerStandings(tournament)
    for (i, n, w, m) in standings:
        if m != 1:
            raise ValueError("Each player should have one match recorded.")
        if i in (id1, id3) and w != 1:
            raise ValueError("Each match winner should have one win recorded.")
        elif i in (id2, id4) and w != 0:
            raise ValueError("Each match loser should have zero wins recorded.")
    print "7. After a match, players have updated standings."


def testPairings():
    deleteTournaments()
    tournament = createTournament()

    deleteMatches(tournament)
    deleteTournamentPlayers(tournament)

    player = createPlayer("Twilight Sparkle")
    registerPlayer(player, tournament)

    player = createPlayer("Fluttershy")
    registerPlayer(player, tournament)

    player = createPlayer("Applejack")
    registerPlayer(player, tournament)

    player = createPlayer("Pinkie Pie")
    registerPlayer(player, tournament)
    standings = playerStandings(tournament)

    [id1, id2, id3, id4] = [row[0] for row in standings]
    reportMatch(tournament, id1, id2)
    reportMatch(tournament, id3, id4)
    pairings = swissPairings(tournament)
    if len(pairings) != 2:
        raise ValueError(
            "For four players, swissPairings should return two pairs.")
    [(pid1, pname1, pid2, pname2), (pid3, pname3, pid4, pname4)] = pairings
    correct_pairs = set([frozenset([id1, id3]), frozenset([id2, id4])])
    actual_pairs = set([frozenset([pid1, pid2]), frozenset([pid3, pid4])])
    if correct_pairs != actual_pairs:
        raise ValueError(
            "After one match, players with one win should be paired.")
    print "8. After one match, players with one win are paired."


if __name__ == '__main__':
    testDelete()
    testCount()
    testRegister()
    testRegisterCountDelete()
    testStandingsBeforeMatches()
    testReportMatches()
    testPairings()
    print "Success!  All tests pass!"


