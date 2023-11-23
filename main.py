from kivy import *
from kivy.lang import Builder
import sys

from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivy.uix.screenmanager import Screen
from kivymd.uix.textfield import MDTextField
from kivymd. uix.widget import MDWidget
from kivymd. uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivy.animation import Animation
from kivy.metrics import dp
from kivy.clock import Clock
from kivy.properties import BooleanProperty, ObjectProperty, StringProperty
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.bottomsheet import MDBottomSheet, MDListBottomSheet

KV = '''

BottomSheet:
    MDScreen:
        md_bg_color: "orange"
        MDRaisedButton:
            pos_hint: {"top": 1}
            on_release: root.btn()

<NBottomSheet>:
    MDBoxLayout:
        orientation: 'vertical'
        MDScreenManager:
            id: sm
            MDScreen:
                name: 'sc1'
                md_bg_color: 1,1,1,.5
                HomePage:
            MDScreen:
                name: 'sc2'
                md_bg_color: 'red'
            MDScreen:
                name: 'sc3'
                md_bg_color: 'yellow'
            MDScreen:
                name: 'sc4'
                md_bg_color: 'orange'
                MDLabel:
                    text: "Big"
                    halign: 'center'
                    font_size: sp(40)
        MDCard:
            md_bg_color: '#263238'     #'#689F38'
            size_hint: 1, None
            height: dp(45)
            radius: 0
            elevation: 2
            MDGridLayout:
                padding: dp(5),dp(20),0,0
                cols: 4
                MDBoxLayout:
                    orientation: 'vertical'
                    MDIconButton:
                        id: hm_btn
                        icon: 'home'
                        theme_icon_color: 'Custom'
                        icon_color: '#B0BEC5'
                        icon_size: sp(27)     
                        on_release: 
                            sm.current = "sc2"
                            root.set_icon_color(self)
                    MDBoxLayout:
                        padding: dp(12),0,0,dp(10)
                        MDLabel:
                            text: 'Home'
                            font_size: sp(12)
                            theme_text_color: 'Custom'
                            text_color: hm_btn.icon_color
                MDBoxLayout:
                    orientation: 'vertical'
                    spacing: dp(3.5)
                    MDIconButton:
                        id: hm
                        icon: 'city-variant-outline'
                        icon_size: sp(25)     
                        theme_icon_color: 'Custom'
                        icon_color: '#B0BEC5'
                        on_release: 
                            sm.current = "sc3"
                            root.set_icon_color(self)
                    MDBoxLayout:
                        padding: dp(13),0,0,dp(10)
                        MDLabel:
                            text: 'Tour'
                            theme_text_color: 'Custom'
                            text_color: hm.icon_color
                            font_size: sp(12)
                MDBoxLayout:
                    orientation: 'vertical'
                    MDIconButton:
                        icon: 'wechat'
                        icon_size: sp(27)    
                        on_release: sm.current = "sc1" 
                    MDBoxLayout:
                        padding: dp(13),0,0,dp(10)
                        MDLabel:
                            text: 'Chat'
                            font_size: sp(12)
                MDBoxLayout:
                    orientation: 'vertical'
                    spacing: dp(2)
                    MDIconButton:
                        icon: 'toolbox-outline'
                        icon_size: sp(26.5)   
                        on_release: root.exit()    
                    MDBoxLayout:
                        padding: sp(12),0,0,sp(10)
                        MDLabel:
                            text: 'Tools'
                            font_size: sp(12)                     
                
<HomePage>:
    MDScreenManager:
        id: sub_sm
        MDScreen:
            name: 'sc4'
            #md_bg_color: 'orange'
            MDLabel:
                text: root.text
                halign: 'center'
                font_size: sp(40)       
            MDGridLayout:
                cols: 6
                #size_hint: 1,.1
                #pos_hint: {"top": 1}
                padding: 0,dp(2),dp(5),0
                spacing: dp(0)
                MDBoxLayout:
                    MDIconButton:
                        icon: 'dots-vertical'
                        pos_hint: {"top": 1}
                        on_release: root.openMenu(self)
                MDBoxLayout:
                    padding: dp(3),dp(10),0,0
                    size_hint: 4.5,1
                    TextInput:
                        id: show_textfield
                        text: ""
                        hint_text: 'Search'
                        pos_hint: {"top": 1}
                        disabled: True
                        opacity: 0
                        size_hint: (0, 0)
                        height: dp(28)
                        padding_x: (dp(15), 0)
                        padding_y: (dp(4), dp(4))
                        foreground_color: [1,0,0,1]
                        background_color: [1,1,1,0]
                        #background_normal: "#b71c1c"
                        #background_active: "#b71c1c"
                        multiline: False
                        text_color: 'red'
                       
                        font_size: sp(16)
                        on_focus:
                            if self.focus: root.focus = True
                            else: root.sch_dismiss()
                        canvas.before:
                            Color:
                                rgba: 1,1,1,.7
                            RoundedRectangle:
                                pos: self.pos
                                size: self.size
            
                MDBoxLayout:
                    padding: dp(4),dp(9),0,0
                    MDIconButton:
                        id: magnify_btn_disabled
                        icon: 'magnify'
                        #md_bg_color: "#CFD8DC"
                        icon_size: sp(20)
                        pos_hint: {"top": 1}
                        size_hint: .05,.05
                        disabled: False
                        on_release:
                            root.animate_textfield()
                    
                MDBoxLayout:
                    padding: 0,dp(4),0,0
                    MDIconButton:
                        icon: 'antenna'
                        theme_icon_color: 'Custom'
                        disabled_color: (1,0,0,1)
                        icon_size: sp(20)
                        disabled: True
                        pos_hint: {"top": 1}
                MDBoxLayout:
                    padding: 0,dp(9),0,0
                    MDIconButton:
                        icon: 'bell-outline'
                        icon_size: sp(20)
                        size_hint: .05,.05
                        pos_hint: {"top": 1}
                        on_release: sub_sm.current = "scA"
                        
                MDBoxLayout:
                    padding: 0,dp(4),dp(10),0
                    MDIconButton:
                        icon: 'share-variant-outline'
                        icon_size: sp(20)
                        pos_hint: {"top": 1}
        MDScreen:
            name: 'scA'
            md_bg_color: 'green'
            MDRaisedButton:
                text: 'Btn'
                size_hint: 1,.1
                on_release:sub_sm.current = "sc4"
            MDLabel:
                text: 'Sc_A'
                halign: 'center'
                font_size: sp(40)  
'''

class BottomSheet(MDBoxLayout):
    def btn(self):
        mn = MDListBottomSheet(bg_color="yellow")
        for i in range(20):
            mn.add_widget(f"Standart Item {i}",
                lambda x, y=i: self.callback_for_menu_items(
                    f"Standart Item {y}"
                ),)
        mn.open()
    def callback_for_menu_items(self, *args):
        print(args[0])

class NBottomSheet(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_touch_up(self, touch):
        pass

    def set_icon_color(self, x):
        if x.icon == "home":
            self.ids.hm_btn.icon_color = "#2962FF"
            self.ids.hm.icon_color = "#ffffff"
        if x.icon == "city-variant-outline":
            self.ids.hm.icon_color = "#004D40"
            self.ids.hm_btn.icon_color = "#ffffff"

    def exit(self):
      sys.exit()


class Drawer(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class HomePage(MDBoxLayout):

    once = BooleanProperty(False)
    focus = BooleanProperty(False)
    appeared = BooleanProperty(False)
    text = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        menu_items = [
            {
                "text": f"Profile {i}",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=f"Profile {i}": self.menu_callback(x),
            } for i in range(2)
        ]
        self.menu = MDDropdownMenu(
            items=menu_items,
            width_mult=2, border_margin=dp(150), position="bottom"
        )

    def animate_textfield(self):
        self.once = True
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
        else:
            #self.focus = False
            self.text = ""

    def textfieldDismiss(self, ar):

        anim = Animation(opacity=1, size_hint=(0, 0), width=dp(163),height=(dp(28)), duration=0)
        anim += Animation(opacity=0, size_hint=(0, 0), width=dp(0), height=(dp(28)), duration=0.5)
        anim.start(self.ids.show_textfield)
        Clock.schedule_once(self.btnStop, 0.5)
        self.appeared = True

    def sch_dismiss(self):
        self.focus = False
        if self.ids.show_textfield.text == "" or len(self.ids.show_textfield.text) == 1 or len(self.ids.show_textfield.text) == 2:
            if self.once == True:
                Clock.schedule_once(self.textfieldDismiss, 2)
                self.once = False

    def btnStop(self, dt):
       if self.appeared == True:
           self.ids.show_textfield.disabled = True
       self.ids.magnify_btn_disabled.disabled = False

    def openMenu(self, btn):
        self.menu.caller = btn
        self.menu.open()

    def menu_callback(self, mn):
       self.ids.sub_sm.current = "scA"
       self.menu.dismiss()


class WebG(MDApp):

    def build(self):
        #self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style = "Dark"
        #self.theme_cls.primary_palette = "Teal"
        return Builder.load_string(KV)

if __name__ == "__main__":
    WebG().run()

