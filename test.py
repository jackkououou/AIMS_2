from utils.api.google.gsheets import Gsheet
from utils.Album import Album

steet = Gsheet()
print('Artist: ')
artists = str(input())
print('Album: ')
album = str(input())
    
#steet.add_album(title=album, artist=artists)
#steet.update_sheets()

thing = Album()
thing = steet.get_album_data(title='This Night', artist= 'Destroyer')
print(thing.get_art())