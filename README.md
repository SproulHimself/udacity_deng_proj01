# Udacity Data Engineering Nanodegree - Project 1

- Data modeling with Postgres and building an ETL pipeline using Python. 


## Introduction

To simulate a real life scenario, a fake company called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. To assist the analytics team, I have created a Postgres database, schema, and ETL pipline with tables designed to optimize queries on song play analysis. The process to complete this project included defining fact and dimension tables for a star schema as well as building an ETL pipeline that transfers data from files in two local directories into these tables in Postgres using Python and SQL.


For this project two separate data sets are are provided for analysis. The first dataset is a subset of real data from the Million Song Dataset. Each file is in JSON format and contains metadata about a song and the artist of that song. The second dataset consists of log files in JSON format generated by this event simulator based on the songs in the first dataset. These simulate activity logs from a music streaming app based on specified configurations.


## Schema
The schema for this project consists of five different tables which contain data from both previously mentioned sources. First, `songs` and `artists` dimensional tables were created by processing the song data set. The `artists` table's values consist of `artist_id`, `name`, `location`, `latitude`, and `longitude`. The `songs` table consist of `song_id`, `title`, `artist_id`, `year`, and `duration`. The `artist_id` value is what allows the `songs` and `artists` tables to be joined, which is necessary for creating the `songplays` fact table.

With the second data set, `time` and `users` dimensional tables were created, as well as a fact table for `songplays`. `timestamp`, `hour`, `day`, `week`, `month`, `year`, and `weekday` are the values stored in the `time` table while `user_id`, `first_name`, `last_name`, `gender`, and `level` are the values stored in the `users` table. The `songplays` table was created with the `timestamp`, `user_id`, `level`, `song_id`, `artist_id`, `session_id`, `location`, and `user_agent` values. Lastly, I created `songplays_id` as a `SERIAL PRIMARY KEY` to gain some practice with implementing other Postgres data types.



## ETL pipeline

Processing the data for the `songs` and `artists` dimension tables was fairly straightforward as each JSON file only contained information for one song. The steps for processing the "song" data were:
- Open the file
- Set the column names *note: because I read the JSON file as a series, I set the index instead of column names
- Insert appropriate `songs_table` values
- Insert appropriate `artists_table` values


While the `users` table  was painless to create, processing the data for the `time`, `users`, and `songplays` tables was less straightforward as each JSON file was a simulated activity log for a single day.  The orginal time data was provided in milliseconds, so that was converted to a timestamp and processed to insert `start_time`, `hour`, `day`, `week`, `month`, `year`, and `weekday` values into the `time` table. The `songplays` table contains the values for `timestamp`, `user_id`, `level`, `song_id`, `artist_id`, `session_id`, `location`, and `user_agent`. Because the log files do not specify an ID for either the song or the artist, it was necessary to first query the songs and artists tables to find matches based on song title, artist name, and song duration time.


The steps for processing the "log" data were:
- Open the file and filter by `NextSong` attribute
- Convert timestamp, process, and insert `time` data
- Insert appropriate `users` tables values
- Iteratively execute query to match `song_id` and `artist_id` for `songplays` table data
- Insert appropriate `songplays` tables values



## Example Queries
After completing the project, all of the queries pass the tests from the provided `tests.ipynb`. Below, I have provided three example queries. There is only one song from the songs data that matches up with the log data, so I chose that song to use for the exmaples:

<img width="972" alt="Screen Shot 2020-07-17 at 4 45 02 PM" src="https://user-images.githubusercontent.com/34200538/87829358-ef88a180-c84c-11ea-808f-9f1eebdf306b.png">


## Conclusion
This project was a great learning experience. I was able to strengthen my data modeling and ETL pipeline building skills while getting aa solid introduction to Postgres SQL. 
