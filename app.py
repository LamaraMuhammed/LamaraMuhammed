import uuid

from kivy import *
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd. uix.boxlayout import MDBoxLayout
from kivy_garden.mapview import MapView, MapSource
from kivymd.toast import toast
from kivy.animation import Animation
from kivy.metrics import dp
from kivy.clock import Clock, mainthread
from kivy.uix.popup import Popup
from kivy.properties import BooleanProperty, StringProperty
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.dialog import MDDialog
from kivymd.uix.scrollview import MDScrollView

from plyer.platforms.win.notification import balloon_tip


KV = '''

'''
class Map(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # map = MapView(lat=10.303193, lon=9.832808, zoom=19)
        # source = ('http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',{
        #     "maxZoom": 20,
        #     "subdomains":['mt0', 'mt1', 'mt2', 'mt3']
        # })



class Notification(MDScrollView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class ShareLocPopUpContent(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class HomePageScreen(MDScreenManager):

    do_one = BooleanProperty(False)
    focus = BooleanProperty(False)
    appeared = BooleanProperty(False)
    text = StringProperty("")
    lbll = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        menu_items = [
            {
                "viewclass": "TwoLineIconListItem",
                "icon": "account-circle-outline",
                "text": "LogIn",
                "on_release": lambda x="LogIn": self.menu_callback(x),
            },
            {
                "viewclass": "OneLineIconListItem",
                "icon": "cog-circle-outline",
                "text": "Setting",
                "on_release": lambda x="Setting": self.menu_callback(x),
            }
        ]
        self.menu = MDDropdownMenu(
            items=menu_items,
            width_mult=4, background_color="#485563", elevation=3, radius=[0, 20, 4, 20]
        )

    def openMenu(self, btn):
        self.menu.caller = btn
        self.menu.open()

    def menu_callback(self, *args):
        if args[0] == "LogIn":
            self.current = "profile_page_screen"
            toast(text="Welcome to signup page")
            self.menu.dismiss()
        if args[0] == "Setting":
            self.current = "setting_screen"
            toast(text="Welcome to signup page", duration= 4.0, background=[1,1,0,.5])
            self.menu.dismiss()
    def set_icon_color(self, x):
        if x.icon == "home":
            self.ids.hm_btn.icon_color = "#2962FF"
            self.ids.tour.icon_color = "#B0BEC5"
            self.ids.chat.icon_color = "#B0BEC5"
            self.ids.friend.icon_color = "#B0BEC5"
        if x.icon == "city-variant-outline":
            self.ids.hm_btn.icon_color = "#B0BEC5"
            self.ids.tour.icon_color = "#2962FF"
            self.ids.chat.icon_color = "#B0BEC5"
            self.ids.friend.icon_color = "#B0BEC5"
        if x.icon == "wechat":
            self.ids.hm_btn.icon_color = "#B0BEC5"
            self.ids.tour.icon_color = "#B0BEC5"
            self.ids.chat.icon_color = "#2962FF"
            self.ids.friend.icon_color = "#B0BEC5"
        if x.icon == "account-multiple-outline":
            self.ids.hm_btn.icon_color = "#B0BEC5"
            self.ids.tour.icon_color = "#B0BEC5"
            self.ids.chat.icon_color = "#B0BEC5"
            self.ids.friend.icon_color = "2962FF"

    def animate_textfield(self):
        self.do_one = True
        if self.focus == False and self.ids.show_textfield.opacity == 0:
            self.ids.magnify_btn_disabled.disabled = True
            self.ids.show_textfield.opacity = 0
            self.ids.show_textfield.size_hint=(0,0)
            self.ids.show_textfield.width=0
            anim = Animation(opacity=0, size_hint=(0, 0), height=(dp(28)), duration=0)
            anim += Animation(opacity=1, size_hint=(0, 0),width=dp(163), height=(dp(28)), duration=0.5)
            anim += Animation(opacity=1, size_hint=(1, 0), height=(dp(28)), duration=3)
            anim.start(self.ids.show_textfield)
            self.ids.show_textfield.disabled = False
            Clock.schedule_once(self.btnStop, 1)
            self.appeared = False
        if self.ids.show_textfield.opacity == 1 and self.ids.show_textfield.text == "":
            self.ids.show_textfield.hint_text = "Empty!"
            self.text = " Write Something"
        if self.ids.show_textfield.opacity == 1 and len(self.ids.show_textfield.text) >= 3:
            self.text = f"Searching...\nthis --> {self.ids.show_textfield.text}"

    def textfieldDismiss(self, ar):

        anim = Animation(opacity=1, size_hint=(0, 0), width=dp(163),height=(dp(28)), duration=0)
        anim += Animation(opacity=0, size_hint=(0, 0), width=dp(0), height=(dp(28)), duration=0.5)
        anim.start(self.ids.show_textfield)
        Clock.schedule_once(self.btnStop, 0.5)
        self.appeared = True

    def sch_dismiss(self):
        self.focus = False
        if self.ids.show_textfield.text == "" or len(self.ids.show_textfield.text) == 1 or len(self.ids.show_textfield.text) == 2:
            if self.do_one == True:
                Clock.schedule_once(self.textfieldDismiss, 10)
                self.do_one = False

    def btnStop(self, dt):
        if self.appeared == True:
            self.ids.show_textfield.disabled = True
        self.ids.magnify_btn_disabled.disabled = False

    def get_bttr(self):
        pass


class HomePageContents(MDBoxLayout):


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"



class SignUpScreen(MDBoxLayout):
    pass


class WebG(MDApp):
    title = "good"
    pop = None
    cache = "Assets/Pic"
    status = StringProperty("")

    def share_loc_popup(self):
        self.pop = Popup(title=f"Battery status: {self.status}",
                                 background_color=(0, 0, 1, .5), separator_color=(1, 1, 1, .2),
                                 title_size=(dp(13)), title_align="center", separator_height=(dp(1)), overlay_color=(0, 0, 0, .4),
                                 size_hint=(.8, .4), auto_dismiss=False, padding=[50, 10],
                                 content=ShareLocPopUpContent(),
                                 )
        self.pop.open()

    def popup_dismiss(self):
        self.pop.dismiss()

    def build(self):
        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
    @mainthread
    def on_gps_location(self, **kwargs):
        print(f"Lat: {kwargs['lat']}")
        print(f"Lon: {kwargs['lon']}")

    def on_start(self):
        balloon_tip(title='', message='I am still working', app_name='utf-8')

if __name__ == "__main__":
    WebG().run()
