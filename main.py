from kivymd.app import MDApp
from kivy.lang import Builder
import pyshorteners as ps
from kivymd.uix.snackbar import Snackbar
from kivy.core.clipboard import Clipboard
from kivy.core.window import Window
Window.size = (350, 600)


KV = '''

MDFloatLayout:
    md_bg_color: 1, 1, 1, 1
    Image:
        source: "logo.jpg"
        pos_hint: {"y": .25}
    MDLabel:
        text: "URL Shortener"
        pos_hint: {"center_x": .5, "center_y": .5}
        halign: "center"
        font_name: "Poppins/Poppins-SemiBold.ttf"
        #font_name: "font/Eurostile.ttf"
        font_size: "40sp"
        theme_text_color: "Custom"
        text_color: 60/255, 43/255, 117/255, 1
    MDFloatLayout:
        size_hint: .85, .08
        pos_hint: {"center_x": .5, "center_y": .38}
        canvas:
            Color:
                rgb: (238/255, 238/255, 238/255, 1)
            RoundedRectangle:
                size: self.size
                pos: self.pos
                radius: [25]
        TextInput:
            id: data
            hint_text: "Enter URL Here"
            size_hint: 1, None
            pos_hint: {"center_x": .5, "center_y": .5}
            height: self.minimum_height
            multiline: False
            cursor_color: 96/255, 74/255, 215/255, 1
            cursor_width: "2sp"
            foreground_color: 96/255, 74/255, 215/255, 1
            background_color: 0, 0, 0, 0
            padding: 15
            font_name: "Poppins/Poppins-Regular.ttf"
            #font_name: "font/Eurostile.ttf"
            font_size: "18sp"                
        MDIconButton:
            icon: "backspace"
            pos_hint: {"center_x": .9, "center_y": .5}
            on_press: app.cancel()
    MDFloatLayout:
        size_hint: .85, .08
        pos_hint: {"center_x": .5, "center_y": .28}
        canvas:
            Color:
                rgb: (238/255, 238/255, 238/255, 1)
            RoundedRectangle:
                size: self.size
                pos: self.pos
                radius: [25]
        TextInput:
            id: short_link
            hint_text: "Shortened URL"
            size_hint: 1, None
            pos_hint: {"center_x": .5, "center_y": .5}
            height: self.minimum_height
            multiline: False
            cursor_color: 96/255, 74/255, 215/255, 1
            cursor_width: "2sp"
            foreground_color: 96/255, 74/255, 215/255, 1
            background_color: 0, 0, 0, 0
            padding: 15
            font_name: "Poppins/Poppins-Regular.ttf"
            #font_name: "font/Eurostile.ttf"
            font_size: "18sp"
        MDIconButton:
            icon: "link-variant"
            pos_hint: {"center_x": .9, "center_y": .5}
            on_press: app.copy()
    Button:
        text: "CLICK"
        font_size: "20sp"
        size_hint: .5, .08
        pos_hint: {"center_x": .5, "center_y": .12}
        background_color: 0, 0, 0, 0
        font_name: "font/Sackers-Gothic-Std-Light.ttf"
        on_press: app.get_data()
        canvas.before:
            Color:
                rgb: 60/255, 43/255, 117/255, 1
            RoundedRectangle:
                size:  self.size
                pos: self.pos
                radius:  [23]

'''


class DemoApp(MDApp):
    def build(self):
        return Builder.load_string(KV)
    
    def get_data(self):
        
        if self.root.ids.data.text == '':
            #print("Paste the link")
            Snackbar(text="Enter The URL").open()
            
        else:
        
            url = self.root.ids.data.text

            u=ps.Shortener().tinyurl.short(url)
            
            self.root.ids.short_link.text = u
        
            self.root.ids.data.text = ''
            
    def copy(self):
        Clipboard.copy(self.root.ids.short_link.text)
        #print("copied")
        Snackbar(text="Link Copied").open()
        
    def cancel(self):
        self.root.ids.data.text = ''

if __name__ == "__main__":
    DemoApp().run()