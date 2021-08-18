from .api.lfm import LastFM
class Album:
    
    
    #So when the album is created Artist and Album are entered for initializtion
    #After that the object passes Art and Alb to the lastfm api the get genre list, song list, and album art
    def __init__(self, *args): #args[0] : artist, args[1] ; album
        if len(args) < 1 :
            self.artist = ''
            self.album_name = ''
            self.image_url = ''
            self.genre_list = []
            self.track_list = []
        
        else:
            artist_in = args[0]
            album_in = args[1]
            self.lfm = LastFM(artist_in, album_in)
            self.artist = artist_in
            self.album_name = album_in
            self.image_url = self.lfm.get_image_url()
            self.genre_list = self.lfm.get_genre_list()
            self.track_list = self.lfm.get_track_list()
    
    
        
    #HERE place alternate __init__ here for reading off the database
    def set_art(self, img : str):
        self.image_url = img
                
    def get_art(self):
        return self.image_url
    
    def set_tracks(self, tracks : list):
        self.track_list = tracks
        
    def get_tracks(self):
        return self.track_list
    
    def get_genres(self):
        return self.genre_list
    
    def set_genres(self, genres : list):
        self.genre_list = genres
        
    def get_album_artist(self):
        return self.artist
    
    def set_album_artist(self, artist : str):
        self.artist = artist
    
    def get_album_title(self):
        return self.album_name
    
    def set_album_title(self, album : str):
        self.album_name = album

   
