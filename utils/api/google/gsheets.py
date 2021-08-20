import gspread
from gspread.models import Cell
from oauth2client.service_account import ServiceAccountCredentials
from utils.Album import Album



SCOPE = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
CREDS = ServiceAccountCredentials.from_json_keyfile_name("utils\\api\\google\\credentials.json", SCOPE)
DRIVE = 'albumTEMP'
SHEET = 'Sheet1'


class Gsheet():
    
    
    def __init__(self):
        self.client = gspread.authorize(CREDS)
        self.inventory = self.client.open(DRIVE).worksheet(SHEET)
        self.inv_extract = self.inventory.get_all_values()
    
    def refresh(self):
        self.inv_extract = self.inventory.get_all_values()
        
    #returns row that album is on, if not found returns 0
    def album_exist(self, artist : str, album : str) -> bool: 
        self.refresh()
        for row in (self.inv_extract):
            if((album in row ) and (artist in row)):
                return True
        return False
        
            
    #return list with album data, if not found return empty list
    def get_album_data(self, title, artist, obj : Album):
        data_row = []
        for row in self.inv_extract:
            if((title in row ) and (artist in row)):
                str_to_list = row[2]
                row[2] =  list(str_to_list.split("*!*"))
                str_to_list = row[3]
                row[3] =  list(str_to_list.split("*!*"))
                data_row =  row
        
        obj.set_album_title(data_row[0])
        obj.set_album_artist(data_row[1])
        obj.set_genres(data_row[2])
        obj.set_tracks(data_row[3])
        obj.set_art(data_row[4])
        obj.set_availale(data_row[5])
        obj.set_reserved(data_row[6])
        obj.set_total(data_row[7])    
    
    #Appends the album to the end of the inventory.
    #When adding to Google Sheets string and int and floats are really the only safe option so any list has to be converted into a string
    #Genre and Track are converted to string with '*!*' used to flag where the sticthes are to seperated them later
    def add_album(self, obj : Album):
        genre_str = '*!*'.join(obj.get_genres())
        track_str = '*!*'.join(obj.get_tracks())
        value = [obj.get_album_title(), obj.get_album_artist(), genre_str, track_str, obj.get_art() , 0, 0, 0]
        if (self.album_exist):
            print('Album already in inventory')
        else:
            self.inv_extract.append(value)
            #add the row to the spreadsheet
        
        
        
    def add_album(self, title, artist):
        new_album = Album(artist_in=artist, album_in=title)
        genre_str = '*!*'.join(new_album.get_genres())
        track_str = '*!*'.join(new_album.get_tracks())
        value = [new_album.get_album_title(), new_album.get_album_artist(), genre_str, track_str, new_album.get_art() , 0, 0, 0]
        
        #Check if already in inv
        clear = True
        for row in self.inv_extract:
            if((title in row) and (artist in row)):
                clear = False
                break
        if clear:
            self.inv_extract.append(value)
            
    def remove_album(self, title, artist):
        
        #self.inventory.findall(query= artist,in_column= 1)
        for row_index, row in enumerate (self.inv_extract):
            if(title in row ) and (artist in row ):
                self.inv_extract.pop(row_index)
                return 1
       
        return 0
            
    #Changes made to inv_ext are merged into the sheets page
    def update_sheets(self) -> None:
        
        cells = []
        for row_index, row in enumerate(self.inv_extract):
            for col_index, val in enumerate(row):
                cells.append(Cell(row= row_index + 1, col= col_index + 1, value=val))
        
        self.inventory.update_cells(cell_list=cells)
        self.refresh()
        
    def get_all_sheet(self):
        return self.inv_extract
                
         
    

    
        


    
    

