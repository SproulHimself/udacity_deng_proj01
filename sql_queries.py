# DROP TABLES

songplays_table_drop = "DROP TABLE IF EXISTS songplays_table;"
users_table_drop = "DROP TABLE IF EXISTS users_table;"
songs_table_drop = "DROP TABLE IF EXISTS songs_table;"
artists_table_drop = "DROP TABLE IF EXISTS artists_table;"
time_table_drop = "DROP TABLE IF EXISTS time_table;"

# CREATE TABLES

songplays_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays_table (
songplays_id SERIAL PRIMARY KEY, 
timestamp BIGINT NOT NULL, 
user_id INT NOT NULL, 
level TEXT, 
song_id TEXT, 
artist_id TEXT, 
session_id INT, 
location TEXT, 
user_agent TEXT);
""")

users_table_create = ("""
CREATE TABLE IF NOT EXISTS users_table (
user_id INT PRIMARY KEY, 
first_name TEXT NOT NULL, 
last_name TEXT NOT NULL, 
gender TEXT, 
level TEXT);
""") 

songs_table_create = ("""
CREATE TABLE IF NOT EXISTS songs_table (
song_id TEXT PRIMARY KEY, 
title TEXT NOT NULL, 
artist_id TEXT NOT NULL, 
year INT, 
duration NUMERIC NOT NULL);
""")

artists_table_create = ("""
CREATE TABLE IF NOT EXISTS artists_table (
artist_id TEXT PRIMARY KEY, 
name TEXT NOT NULL, 
location TEXT, 
latitude NUMERIC, 
longitude NUMERIC);
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time_table (
time_stamp BIGINT PRIMARY KEY, 
hour INT NOT NULL, 
day INT NOT NULL, 
week INT NOT NULL, 
month INT NOT NULL, 
year INT NOT NULL, 
weekday INT NOT NULL);
""")


# INSERT RECORDS

songplays_table_insert = ("""
INSERT INTO songplays_table (
    timestamp, user_id, level, song_id, artist_id, session_id, location, user_agent) 
VALUES (
    %s, %s, %s, %s, %s, %s, %s, %s);
""")

users_table_insert = ("""
INSERT INTO users_table (
    user_id, first_name, last_name, gender, level) 
VALUES (
    %s, %s, %s, %s, %s)
ON CONFLICT ON CONSTRAINT users_table_pkey
DO UPDATE SET level=EXCLUDED.level;
""")

songs_table_insert = ("""
INSERT INTO songs_table (
    song_id, title, artist_id, year, duration) 
VALUES (
    %s, %s, %s, %s, %s)
ON CONFLICT ON CONSTRAINT 
songs_table_pkey DO NOTHING;
""")

artists_table_insert = ("""
INSERT INTO artists_table (
    artist_id, name, location, latitude, longitude) 
VALUES (
    %s, %s, %s, %s, %s)
ON CONFLICT ON CONSTRAINT 
artists_table_pkey DO NOTHING;
""")


time_table_insert = ("""
INSERT INTO time_table (
    time_stamp, hour, day, week, month, year, weekday) 
VALUES (
    %s, %s, %s, %s, %s, %s, %s)
ON CONFLICT ON CONSTRAINT 
time_table_pkey DO NOTHING;
""")

# FIND SONGS

song_select = ("""
SELECT a.artist_id, s.song_id FROM artists_table a 
INNER JOIN songs_table s 
ON s.artist_id = a.artist_id
WHERE a.name = %s
AND s.title = %s
AND s.duration = %s;
""")

# QUERY LISTS

create_table_queries = [songplays_table_create, users_table_create, songs_table_create, 
                        artists_table_create, time_table_create]

drop_table_queries = [songplays_table_drop, users_table_drop, songs_table_drop, 
                      artists_table_drop, time_table_drop]


