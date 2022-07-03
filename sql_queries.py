import configparser


# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')

S3_LOG_DATA = config.get('S3', 'LOG_DATA')
S3_LOG_JSONPATH = config.get('S3', 'LOG_JSONPATH')
S3_SONG_DATA = config.get('S3', 'SONG_DATA')
DWH_IAM_ROLE_ARN = config.get("IAM_ROLE", "ARN")

# DROP TABLES

staging_events_table_drop = "DROP TABLE IF EXISTS staging_events;"
staging_songs_table_drop = "DROP TABLE IF EXISTS staging_songs;"
songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES
staging_events_table_create= ("""
    CREATE TABLE staging_events (
        artist VARCHAR(500),
        auth VARCHAR(20),
        firstName VARCHAR(500),
        gender CHAR(1),
        itemInSession INTEGER,
        lastName VARCHAR(500),
        length DECIMAL(12, 5),
        level VARCHAR(10),
        location VARCHAR(500),
        method VARCHAR(20),
        page VARCHAR(500),
        registration FLOAT,
        sessionId INTEGER,
        song VARCHAR(500),
        status INTEGER,
        ts VARCHAR(50),
        userAgent VARCHAR(500),
        userId INTEGER
    );
""")

staging_songs_table_create = ("""
    CREATE TABLE staging_songs (
        num_songs INTEGER,
        artist_id VARCHAR(20),
        artist_latitude DECIMAL(12, 5),
        artist_longitude DECIMAL(12, 5),
        artist_location VARCHAR(500),
        artist_name VARCHAR(500),
        song_id VARCHAR(20),
        title VARCHAR(500),
        duration DECIMAL(15, 5),
        year INTEGER
    );
""")

#query for creating songplays table

# What is a songplay id?
# TL: references, identity(0,1)
# References reftable [ ( refcolumn ) ]
# Clause that specifies a foreign key constraint, 
# which implies that the column must contain only values
# that match values in the referenced column of some row of the referenced table. 
# The referenced columns should be the columns of a unique or primary key constraint in the referenced table.

songplays_table_create = ("""
    CREATE TABLE IF NOT EXISTS songplays (
        songplay_id INTEGER IDENTITY(0,1) SORTKEY,
        start_time TIMESTAMP NOT NULL,
        user_id INTEGER NOT NULL REFERENCES users (user_id),
        level VARCHAR(10),
        song_id VARCHAR(20) REFERENCES songs (song_id),
        artist_id VARCHAR(20) REFERENCES artists (artist_id),
        session_id INTEGER NOT NULL,
        location VARCHAR(500),
        user_agent VARCHAR(500)
    )
""")

#creating users table
users_table_create = ("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        first_name VARCHAR(500) NOT NULL,
        lastName VARCHAR(500) NOT NULL,
        gender CHAR(1),
        level VARCHAR(10) NOT NULL,
    )
""")

#creating songs table

# what is decimal(15,5)

songs_table_create = (
    """
    CREATE TABLE IF NOT EXISTS songs (
        song_id VARCHAR(20) PRIMARY KEY,
        title VARCHAR(500) SORTKEY NOT NULL,
        duration DECIMAL(15, 5) DISTKEY NOT NULL,
        year INTEGER NOT NULL ,
        artist_id VARCHAR(20) NOT NULL REFERENCES artists (artists_id)
    )
    """
)

# creating artists table

artists_table_create = (
    """
    CREATE TABLE IF NOT EXISTS artists (
        artist_id VARCHAR(20) PRIMARY KEY,
        latitude DECIMAL(12, 5),
        longitude DECIMAL(12, 5),
        location VARCHAR(500),
        name VARCHAR(500) NOT NULL SORTKEY,        
    )
    """
)

# creating time table

# can primary key column have null values
time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time (
        start_time TIMESTAMP NOT NULL PRIMARY KEY SORTKEY,
        hour NUMERIC NOT NULL,
        day NUMERIC NOT NULL,
        week NUMERIC NOT NULL,
        month NUMERIC NOT NULL,
        year NUMERIC NOT NULL,
        weekday NUMERIC NOT NULL
    )
""")