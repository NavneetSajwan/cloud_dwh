#load data to songs_staginng

song_staging_load = (
    """
    COPY INTO songs_staging
    FROM "s3://udacity-dend/song_data"
    
    """
)