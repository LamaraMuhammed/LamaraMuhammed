
from PIL import Image as pilImage
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager
from kivy.properties import StringProperty, BooleanProperty
from kivymd.uix.button import MDTextButton, MDIconButton
from kivymd.uix.boxlayout import MDBoxLayout

import random
import string
import bcrypt
from pymongo import MongoClient
import mysql.connector

Window.size = (273, 586)



class ScreenMng(ScreenManager):
    pass


class InputWidget(MDBoxLayout):

    def sendData(self, *args):
        username = self.ids.username.text
        password = self.ids.password.text
        self.ids.username.text = ''
        self.ids.password.text = ''
        print(username, password)

class ImageButton(MDTextButton):

    num = StringProperty("")
    started = BooleanProperty(True)

    # Mongodb connection
    client = MongoClient('localhost', 27017)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.db = self.client['WebG']

        """doc1 = {
            'name': 'umar',
            'age': 23,
            'town': 'saye'
        }
        db.User.insert_one(doc1)"""

    def getDataFromMongoDB(self, btn):
        ps = b"muhammed"
        hash = bcrypt.hashpw(ps, bcrypt.gensalt(14))
        i = self.db.users.find_one()
        c = f"b{i['password']}"
        if bcrypt.checkpw(ps, i['password']):
            print('okay')
        else:
            print('Not okay')

    def say(self, btn):
        print('ok')

class Gplug(MDApp):

    # Mysql db connection
    database = mysql.connector.connect(host="localhost", user="root", password="Lmr977552", database="webg")
    cursor = database.cursor()

    source = StringProperty('')
    profile = StringProperty('Avatar')
    _string = StringProperty("Start")
    name = "umar"
    phone_no = '+2349069964556'

    def build(self):
        self.theme_cls.theme_style = "Dark"

    def startUpdating(self, btn):
        btn.background_color = 'green'
        Clock.schedule_interval(self.updateLatLng, 0.3)
        Clock.schedule_interval(self.fetchOutFromMysqlDB, 0.3)


    def on_start(self):
        #self.cursor.execute(f"delete from clients_profile_picture where id = 3")
        self.cursor.execute(f"select * from clients_profile where phone_number = '{self.name}'")
        """for c in self.cursor.fetchall():
            print(c)"""
        result = self.cursor.fetchone()
        self.profile = result[0]
        if result == None:
            self.source = "Assets/Pic/user-icon-male.jpg"
        else:
            path = "cache/my_profile_pic.jpeg"
            with open(path, 'wb') as file:
                file.write(result[3])
                file.close()
                self.source = path

    def uploadBlob(self, btn):
        path = 'Assets/Pic/img_1_1704309056011.jpg'
        with open(path, 'rb') as file:
            filename = file.read()
            st = f"insert into clients_profile values('asiya', 'abc123', 'a1b2c3', %s)"
            self.cursor.execute(st, [filename])
            self.database.commit()

    def updateLatLng(self, dt):
        lat = ''.join(random.sample(string.hexdigits, 8))
        lon = ''.join(random.sample(string.hexdigits, 8))
        self.cursor.execute(f"update clients_location_data set lat = '{lat}', lon = '{lon}'\
                            where phone_number = '{self.name}'")
        self.database.commit()

    def fetchOutFromMysqlDB(self, btn):
        self.cursor.execute(f"select * from clients_location_data\
                            where phone_number = '{self.name}'")
        result = self.cursor.fetchone()
        self._string = f"{result[2]}\n{result[3]}"


if __name__ == "__main__":
    Gplug().run()

# MDLabel:
#                             text: root.num
#                             halign: 'center'
#                             theme_text_color: 'Custom'
#                             text_color: .1,1,1,1
#                             font_size: sp(30)
#                         MDLabel:
#                             text: root._string
#                             halign: 'center'
#                             theme_text_color: 'Custom'
#                             text_color: 1,.1,1,1
#                             font_size: sp(20)

"""
<MDScreen>:
    name: 'home'
    MDGridLayout:
        rows: 2
        MDBoxLayout:
            orientation: "vertical"
            padding: 0,0,0,dp(50)
            md_bg_color: 'blue'
            FitImage:
                radius: 240
                source: app.source
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint: None, None
                size: dp(170), dp(170)


        MDBoxLayout:
            orientation: "vertical"
            spacing: dp(8)
            padding: 30, 30
            MDLabel:
                text: app.some_string
                halign: 'center'
                font_size: sp(25)
            Button:
                text: 'UploadBlob'
                size_hint: .1,.2
                pos_hint: {'center_x': .5}
                on_release: app.uploadBlob(self)  #root.getDataFromMongoDB(self)     #
            ToggleButton:
                text: 'Update' if self.state == 'normal' else 'Stop'
                background_color: 'blue'
                pos_hint: {'center_x': .5}
                size_hint: .1,.2
                on_state:
                    #root.fetching(self)
                    app.startUpdating(self) #if self.state == 'down' else \
                    #root.stopUpdating(self)


"""
