class Song:

    # Class attributes shared by all Song objects
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        # Store information about this individual song
        self.name = name
        self.artist = artist
        self.genre = genre

        # Update the class information whenever a song is created
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        # Increase the total number of songs by 1
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        # Add the genre only if it is not already in the list
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        # Add the artist only if they are not already in the list
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        # Add the genre to the dictionary or increase its count
        if genre not in cls.genre_count:
            cls.genre_count[genre] = 1
        else:
            cls.genre_count[genre] += 1

    @classmethod
    def add_to_artist_count(cls, artist):
        # Add the artist to the dictionary or increase their count
        if artist not in cls.artist_count:
            cls.artist_count[artist] = 1
        else:
            cls.artist_count[artist] += 1
