class Song:
    def __init__ (self, title, singer, duration):
        self.__title = title
        self.__singer = singer
        self.__duration = duration

    def get_title(self):
        return self.__title

    def set_title(self,title):
        if isinstance(title,str):
            self.__title = title

        else:
            print('It has to be a string')

    def get_singer(self):
        return self.__singer
    
    def set_singer(self,singer):
        if isinstance(singer, str):
            self.__singer
        else:
            print('It has to be a string')
    

    def get_duration(self):
        return self.__duration
    
    def set_duration(self, duration):
        if isinstance(duration, int) and duration > 0:
            self.__duration
        else:
            print('Duration must be a number greater than 0')

    def __str__(self):
        return f'Title: {self.__title}, Singer: {self.__singer}, Duration: {self.__duration}'
    

class Playlist:
    def __init__(self,name,):
        self.name = name
        
        self.list_songs = []
        


    def add_song (self, song):
        self.list_songs.append(song)

    def list_by_author(self, singer):
        for song in self.list_songs:
            if song.get_singer() == singer:
                print(song)


    def __str__(self):
        total_duration = sum(song.get_duration() for song in self.list_songs)
        hours, remainder = divmod(total_duration, 3600)
        minutes, seconds = divmod(remainder, 60)
        duration_str = f"{hours:02}:{minutes:02}:{seconds:02}"

        songs_str = "\n".join(str(song) for song in self.list_songs)
        return f"Playlist: {self.name}\nNumber of songs: {len(self.list_songs)}\nTotal duration: {duration_str}\nSongs:\n{songs_str}"



my_Playlist = Playlist("playlist of Ivan")


songs = [
    Song('Kill my ex', 'SZA', 153),
    Song('Paris','La Oreja de Van Gogh', 226),
    Song('Si antes te hubiera conocido', 'karol G', 195),
    Song('Por el resto de tu vida','Christian Nodal', 197),
    Song('Más altas que bajadas', 'Natael Cano', 193),
    Song('El drip','Natael Cano', 142),
    Song('JGL','La adictiva', 158),
    Song('TQM','Fuerza Regida',158),
    Song('Por mi México','Lefty SM', 405),
    Song('Mi ex tenía razón','Karol G' ,154),
]

for i in songs:
    my_Playlist.add_song(i)


print(my_Playlist)

print("\nSongs by Natael Cano:")
my_Playlist.list_by_author("Natael Cano")



print ('\n------------------')