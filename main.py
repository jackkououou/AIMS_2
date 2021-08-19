from handler import CastAlbumUtil, Mediator, SearchUtil, UtilMediator
import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from aims2 import Ui_MainWindow
from AlbumPopUp import Ui_Dialog_Album

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        self.ui.pushButton.clicked.connect(self.search_album_dialog)
        
    def show(self):
        self.main_win.show()
        
    def search_album_dialog(self, ui_window : Ui_MainWindow):
        dialog = QDialog()
        popup = Ui_Dialog_Album()
        popup.setupUi(dialog)
        handler = SearchUtil(self.ui.ArtistName, self.ui.lineEdit)
        caster = CastAlbumUtil(popup)
        mediater = UtilMediator(handler, caster)
        handler.search_album()
        caster.cast_album()
        dialog.exec_()
    
        
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())