# DROP TABLES

play_table_drop = "DROP TABLE IF EXISTS plays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

play_table_create = ("""CREATE TABLE IF NOT EXISTS plays (plays_id SERIAL PRIMARY KEY, timestamp BIGINT, user_id TEXT, 
                                                           level TEXT, song_id TEXT, artist_id TEXT, session_id INT, 
                                                           location TEXT, user_agent TEXT);
""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users (user_id TEXT, first_name TEXT, last_name TEXT, 
                                                          gender TEXT, level TEXT);
""") 

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs (song_id TEXT, title TEXT, artist_id TEXT, 
                                                          year INT, duration NUMERIC);
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists (artist_id TEXT, name TEXT, location TEXT, 
                                                              latitude NUMERIC, longitude NUMERIC);
""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time (timestamp BIGINT, hour INT, day INT, week INT,  
                                                         month INT, year INT, weekday INT);
""")


# INSERT RECORDS

play_table_insert = ("""INSERT INTO plays (timestamp, user_id, level, song_id, artist_id, session_id, location, user_agent) 
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
""")

user_table_insert = ("""INSERT INTO users (user_id, first_name, last_name, gender, level) 
                 VALUES (%s, %s, %s, %s, %s);
""")

song_table_insert = ("""INSERT INTO songs (song_id, title, artist_id, year, duration) 
                 VALUES (%s, %s, %s, %s, %s);
""")

artist_table_insert = ("""INSERT INTO artists (artist_id, name, location, latitude, longitude) 
                 VALUES (%s, %s, %s, %s, %s);
""")


time_table_insert = ("""INSERT INTO time (timestamp, hour, day, week, month, year, weekday) 
                 VALUES (%s, %s, %s, %s, %s, %s, %s);
""")

# FIND SONGS

song_select = ("""SELECT a.artist_id, s.song_id FROM artists a 
               INNER JOIN songs s 
               ON s.artist_id = a.artist_id
               WHERE a.name = %s
               AND s.title = %s
               AND s.duration = %s;
""")

# QUERY LISTS

create_table_queries = [play_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [play_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]


