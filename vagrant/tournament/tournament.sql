-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament;

CREATE TABLE players (
    player serial PRIMARY KEY,
    name varchar(40) NOT NULL,
    matches_won integer DEFAULT 0,
    matches_played integer DEFAULT 0
);
CREATE TABLE matches (
    match serial PRIMARY KEY,
    winner_id integer references players(player),
    loser_id integer references players(player)
);
CREATE VIEW playerstandings AS
    SELECT * from players ORDER BY matches_won desc;