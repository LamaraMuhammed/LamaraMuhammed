# install_twisted_rector must be called before importing the reactor
from __future__ import unicode_literals

from kivy.core.window import Window

from kivy.support import install_twisted_reactor

install_twisted_reactor()

# A Simple Client that send messages to the Echo Server
from twisted.internet import reactor, protocol


class EchoClient(protocol.Protocol):
    def connectionMade(self):
        self.factory.app.on_connection(self.transport)

    def dataReceived(self, data):
        self.factory.app.print_message2(data.decode('utf-8'))
        # data.decode('utf-8')

class EchoClientFactory(protocol.ClientFactory):
    protocol = EchoClient

    def __init__(self, app):
        self.app = app

    def startedConnecting(self, connector):
        self.app.print_message('Started to connect.')

    def clientConnectionLost(self, connector, reason):

        self.app.print_message(f"Lost connection")
        connector.connect()

    def clientConnectionFailed(self, connector, reason):
        # connector.connect()
        self.app.print_message('Connection failed.')
        # connector.connect()

    def printes(self):
        print("Good")


from kivy.app import App
from kivy.uix.label import Label
from kivy.properties import NumericProperty, BooleanProperty
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import BooleanProperty
import time

from kivy.clock import Clock

Window.size = (350, 600)

# A simple kivy App, with a textbox to enter messages, and
# a large label to display all the messages received from
# the server
class TwistedClientApp(App):
    connection = None
    textbox = None
    label = None
    l = None
    btn = None
    count = 0
    lbl = NumericProperty(0)
    reconnect = BooleanProperty(False)

    def build(self):
        root = self.setup_gui()
        self.connect_to_server()
        # Clock.schedule_interval(self.send_message, 1)
        return root

    def setup_gui(self):
        self.textbox = TextInput(size_hint_y=.1, multiline=False)
        self.textbox.bind(on_text_validate=self.send_message)
        self.l = Label(text='', font_size="30sp")
        self.label = Label(text='connecting...\n')
        self.btn = Button(text="Reset", size_hint_y=.1)
        self.btn.bind(on_press=self.do)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.btn)
        layout.add_widget(self.label)
        layout.add_widget(self.l)
        layout.add_widget(self.textbox)
        return layout

    def connect_to_server(self):
        reactor.connectTCP('localhost', 8000, EchoClientFactory(self))

    def on_connection(self, connection):
        self.print_message("Connected successfully!", )
        self.connection = connection

    def send_message(self, *args):
        self.count += 1
        msg = self.textbox.text
        self.label.text = str(self.count)
        if msg and self.connection:
            self.connection.write(msg.encode('utf-8'))
            self.textbox.text = ""

    def print_message(self, msg, x=None, y=None):
        self.label.text = "{}\n".format(msg,x,y)

    def print_message2(self, msg):
        self.l.text = "{}\n".format(msg)

    def do(self, btn):
        pass


if __name__ == '__main__':
    TwistedClientApp().run()
