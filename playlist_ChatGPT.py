# Clase Song
class Song:
    def __init__(self, title, singer, duration):
        self.__title = title
        self.__singer = singer
        self.__duration = duration

    # Métodos get
    def get_title(self):
        return self.__title

    def get_singer(self):
        return self.__singer

    def get_duration(self):
        return self.__duration

    # Métodos set
    def set_title(self, title):
        if isinstance(title, str):
            self.__title = title
        else:
            print("Title must be a string")

    def set_singer(self, singer):
        if isinstance(singer, str):
            self.__singer = singer
        else:
            print("Singer must be a string")

    def set_duration(self, duration):
        if isinstance(duration, int) and duration > 0:
            self.__duration = duration
        else:
            print("Duration must be a number greater than 0")

    # Método para representar la canción como cadena
    def __str__(self):
        return f"Title: {self.__title}, Singer: {self.__singer}, Duration: {self.__duration}s"


# Clase Playlist
class Playlist:
    def __init__(self, name):
        self.name = name
        self.list_songs = []

    # Método para agregar una canción a la lista de reproducción
    def add_song(self, song):
        if isinstance(song, Song):
            self.list_songs.append(song)
        else:
            print("Only Song objects can be added to the playlist")

    # Método extra: listar canciones por autor
    def list_by_author(self, singer):
        for song in self.list_songs:
            if song.get_singer() == singer:
                print(song)

    # Método para representar la lista de reproducción como cadena
    def __str__(self):
        total_duration = sum(song.get_duration() for song in self.list_songs)
        hours, remainder = divmod(total_duration, 3600)
        minutes, seconds = divmod(remainder, 60)
        duration_str = f"{hours:02}:{minutes:02}:{seconds:02}"

        songs_str = "\n".join(str(song) for song in self.list_songs)
        return f"Playlist: {self.name}\nNumber of songs: {len(self.list_songs)}\nTotal duration: {duration_str}\nSongs:\n{songs_str}"


# Pruebas
if __name__ == "__main__":
    # Crear objeto Playlist
    my_playlist = Playlist("My Favorite Songs")

    # Crear 10 objetos Song y agregarlos a la lista de reproducción
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

    for song in songs:
        my_playlist.add_song(song)

    # Probar todos los métodos
    print(my_playlist)
    print("\nSongs by Natael Cano:")
    my_playlist.list_by_author("Natael Cano")
