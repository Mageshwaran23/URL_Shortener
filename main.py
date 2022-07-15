from kivy.lang import Builder
from kivymd.app import MDApp
import os
from tkinter import *
from plyer import filechooser
import subprocess
import pyttsx3
import PyPDF2
import json
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.snackbar import Snackbar
from kivy.metrics import dp
from kivymd.uix.dialog import MDDialog
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivymd.uix.list import OneLineAvatarIconListItem
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton
from kivy.core.window import Window
Window.size = (350, 600)

KV = '''

<Content>
    orientation: "vertical"
    spacing: "12dp"
    size_hint_y: None
    size_hint_x: .5
    height: "50dp"
    MDTextField:
        id: t1
        hint_text: "Enter Page No."
        pos_hint:{'center_x': 0.5, 'center_y': 0.5}
        width:250
           
<ItemConfirm>
    IconLeftWidget:
        icon: "volume-source"  
        
BoxLayout:
    MDBottomNavigation:
        text_color_active: 0, 0, 0, 1
        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'PDF Reader'
            icon: "file-document"
            MDNavigationLayout:
                ScreenManager:
                    Screen:
                        BoxLayout:
                            orientation: "vertical"

                            MDToolbar:
                                title: "PDF Reader"
                                md_bg_color: 200/255,0,0,1
                            Widget:

                            BoxLayout:
                                Widget:
                                MDRectangleFlatButton:
                                    text: 'UPLOAD'
                                    text_color: 200/255,0,0,1
                                    line_color: 200/255,0,0,1
                                    theme_text_color: 'Custom'
                                    pos_hint: {'center_x': 0.5, 'center_y': 1.1}
                                    on_release:
                                        app.callback(self)
                                Widget:
                        

        
        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'Audio Book'
            icon: "book-music"
            MDNavigationLayout:
                ScreenManager:
                    Screen:
                        BoxLayout:
                            orientation: "vertical"

                            MDToolbar:
                                title: "Audio Book"
                                md_bg_color: 0,0,100/255,1
                                
                            Widget:

                            BoxLayout:
                                Widget:
                                MDRectangleFlatButton:
                                    text: 'UPLOAD'
                                    text_color: 0,0,100/255,1
                                    line_color: 0,0,100/255,1
                                    theme_text_color: 'Custom'
                                    pos_hint: {'center_x': 0.5, 'center_y': 1.1}
                                    on_release:
                                        app.onclick(self)
                                Widget:
        
'''

class Content(BoxLayout):
    pass

class ItemConfirm(OneLineAvatarIconListItem):
    divider = None

class Example(MDApp):
    dialog = None
    dialog_box = None
    def build(self):
        return Builder.load_string(KV)

            
    def callback(self, event):
            print("button pressed")
            
            file1 = filechooser.open_file()
            label = Label(text=file1).pack()
            print(file1)

            path = file1
            subprocess.Popen(path, shell=True)

    def onclick(self,event):
        print("button pressed")

        self.file2 = filechooser.open_file()
        label = Label(text=self.file2).pack()
        print(self.file2)
        if self.file2 == []:
            print("pdf not selected")
        else:
            if not self.dialog:
                self.dialog = MDDialog(
                    type="custom",
                    auto_dismiss=False,
                    content_cls=Content(),
                    pos_hint= {"center_x": .5, "center_y": .5},
                    buttons=[ 
                        MDFlatButton(
                            text="CANCEL", text_color=self.theme_cls.primary_color,on_press=self.cancel
                        ),  
                        MDFlatButton(
                            text="OK", text_color=self.theme_cls.primary_color,on_press=self.voice_dialog#on_press=self.ok_speak
                        ),
                    ],
                )
            self.dialog.open()
            
    def voice_dialog(self,event):
        if not self.dialog_box:
            self.dialog_box = MDDialog(
                title="Voices",
                type="confirmation",
                items=[
                    ItemConfirm(text="David", on_press=self.male_voice),
                    ItemConfirm(text="Zara", on_press=self.female_voice),
                ],
            )
        self.dialog_box.open()
    
    def male_voice(self, obj):
        print(self.dialog.content_cls.ids.t1.text)
        self.dialog_box.dismiss()
        for file in self.file2:
            print(file)
            book = open(file,'rb')
            pdfReader = PyPDF2.PdfFileReader(book)
            pages = pdfReader.numPages
            print(pages)
            speaker = pyttsx3.init()
            voices = speaker.getProperty('voices')
            speaker.setProperty('voice',voices[0].id)
            speaker.setProperty('rate',190)
            
            if int(self.dialog.content_cls.ids.t1.text) > pages:
                Snackbar(text="Check Page Number").open()
            else:
                for num in range(int(self.dialog.content_cls.ids.t1.text)-1, pages):
                            page = pdfReader.getPage(int(self.dialog.content_cls.ids.t1.text)-1)
                            text = page.extractText()
                            speaker.say(text)
                            speaker.runAndWait()
                            break
    
    def female_voice(self, obj):
        print(self.dialog.content_cls.ids.t1.text)
        self.dialog_box.dismiss()
        for file in self.file2:
            print(file)
            book = open(file,'rb')
            pdfReader = PyPDF2.PdfFileReader(book)
            pages = pdfReader.numPages
            print(pages)
            speaker = pyttsx3.init()
            voices = speaker.getProperty('voices')
            speaker.setProperty('voice',voices[1].id)
            speaker.setProperty('rate',190)
            
            if int(self.dialog.content_cls.ids.t1.text) > pages or int(self.dialog.content_cls.ids.t1.text) < 1:
                Snackbar(text="Check Page Number").open()
            else:
                for num in range(int(self.dialog.content_cls.ids.t1.text)-1, pages):
                        page = pdfReader.getPage(int(self.dialog.content_cls.ids.t1.text)-1)
                        text = page.extractText()
                        speaker.say(text)
                        speaker.runAndWait()
                        break      
            
                    
    def cancel(self, obj):
        self.dialog.dismiss()
        
Example().run()
