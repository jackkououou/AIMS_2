from __future__ import annotations
from abc import ABC, abstractmethod
from PyQt5 import QtCore, QtGui, QtWidgets
from utils.Album import Album
from utils.api.google.gsheets import Gsheet
import urllib.request
from UI.AlbumPopUp import Ui_Dialog

class Mediator(ABC):
    def notify(self, sender: object, event : str):
        pass
    
class BaseComponent:
    def __init__(self, mediator: Mediator = None):
        self._mediator = mediator
        
    @property
    def mediator(self) -> Mediator:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator) -> None:
        self._mediator = mediator

class SearchUtil(BaseComponent):
    def __init__(self, artist : QtWidgets.QLineEdit, title : QtWidgets.QLineEdit):
        super().__init__(mediator = None)
        self._artist = artist.text()
        self._album = title.text()
        self._sheet = Gsheet()
        self._alb_obj = None
        
    def search_album(self):
        if(self._sheet.album_exist(artist=self._artist, album=self._album)):
            self.mediator.notify(self, 'IN_SHEET')
        else:
            self.mediator.notify(self, 'NOTIN_SHEET')
            
    def gsheets_fetch_album(self, alb_obj : Album):
        self._sheet.get_album_data(title=self._album, artist=self._artist, obj= alb_obj)
        print (alb_obj)
        
    def lfm_fetch_album(self) -> Album:
        alb_obj = Album(self._artist, self._album)
        print(alb_obj)
        self._alb_obj = alb_obj
        return alb_obj

class CastAlbumUtil(BaseComponent):
    def __init__(self, dialog_object : Ui_Dialog):
        super().__init__(mediator= None)
        self._dialog = dialog_object
    
    def cast_album(self):
        self.mediator.notify(self, 'CASTING_ALBUM')
        
    def cast_to_screen(self, alb_obj : Album):
        url = alb_obj.get_art()
        data = urllib.request.urlopen(url).read()
        image = QtGui.QImage()
        image.loadFromData(data)
        self._dialog.AlbumImage.setPixmap(QtGui.QPixmap(image))
        self._dialog.AlbumName.setText(alb_obj.get_album_title())
        self._dialog.ArtistName.setText(alb_obj.get_album_artist())
        
        genres = alb_obj.get_genres()
        for genre in genres:
            self._dialog.listWidget.addItem(genre)
        
        tracks = alb_obj.get_tracks()
        for index, track in enumerate(tracks):
            self._dialog.listWidget_2.addItem(f"{index + 1}. {track}")
            
        Dialog = QtWidgets.QDialog()
        self._dialog.setupUi(Dialog)
        Dialog.show()
        
class UtilMediator(Mediator):
    _alb_obj = Album()
    def __init__(self, search_component : SearchUtil , cast_component : CastAlbumUtil):
        self._search_component = search_component
        self._search_component.mediator = self
        self._caster_component = cast_component
        self._caster_component.mediator = self
    def notify(self, sender: object, event: str):
        if event == 'IN_SHEET':
            print('In gsheet... extracting')
            self._search_component.gsheets_fetch_album(self._alb_obj)
        if event == 'NOTIN_SHEET':
            print('Not in gsheet... fetching from Lfm')
            self._alb_obj = self._search_component.lfm_fetch_album()
        if event == 'CASTING_ALBUM':
            if self._alb_obj == None:
                print('No Album Obj')
            else:
                print('Showing album')
                self._caster_component.cast_to_screen(self._alb_obj)

