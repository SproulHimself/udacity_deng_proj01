import os
import glob
import datetime
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    # open song file
    df = pd.read_json(filepath, typ='series')
    df.index = ['num_songs', 'artist_id', 'latitude', 'longitude', 'location', 
                'name', 'song_id', 'title', 'duration', 'year']

    # insert song record
    sd_vals = ['song_id', 'title', 'artist_id', 'year', 'duration']
    song_data = [df.loc[x] for x in sd_vals]
    cur.execute(song_table_insert, song_data)
    
    # insert artist record
    ad_vals = ['artist_id', 'name', 'location', 'latitude', 'longitude']
    artist_data = [df.loc[x] for x in ad_vals]
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    # open log file
    df = pd.read_json(filepath, lines=True)

    # filter by NextSong action
    df = df[df.page == 'NextSong']

    # convert timestamp column to datetime
    df['timestamp'] = pd.to_datetime(df['ts'].apply(lambda x: datetime.datetime.fromtimestamp(x/1000.0)))
    t = df[['timestamp']]
    
    # insert time data records
    column_labels = ['start_time', 'hour', 'day', 'week', 'month', 'year', 'weekday']
    lods = [] #lods == list of dicts
    for i in range(len(t)):
        time_data = (t.iloc[i].dt.time.values[0].minute + round(t.iloc[i].dt.time.values[0].second/60, 3), 
                     t.iloc[i].dt.hour.values[0], 
                     t.iloc[i].dt.day.values[0], 
                     t.iloc[i].dt.week.values[0], 
                     t.iloc[i].dt.month.values[0], 
                     t.iloc[i].dt.year.values[0], 
                     t.iloc[i].dt.weekday.values[0])
        time_dict = {k:v for k, v in list(zip(column_labels, time_data))}
        lods.append(time_dict)

    time_df = pd.DataFrame(lods)
    time_df = time_df[['start_time', 'hour', 'day', 'week', 'month', 'year', 'weekday']]

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = df[['userId', 'firstName', 'lastName', 'gender', 'level']]

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.artist, row.song, row.length))
        results = cur.fetchone()
        
        if results:
            artist_id, song_id = results
        else:
            artist_id, song_id = None, None

        # insert songplay record
        plays_data = (row.ts, int(row.userId), row.level, song_id, artist_id, row.sessionId, row.location, row.userAgent)
        cur.execute(play_table_insert, plays_data)


def process_data(cur, conn, filepath, func):
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()