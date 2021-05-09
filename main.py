from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.video import Video
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from  kivy.uix.filechooser import FileChooserListView
import shutil, os
WhatsApp_folder=r'/storage/emulated/0/WhatsApp/Media/.Statuses'
#WhatsApp_folder=r'C:\Users\ANONYMOUS\Downloads'
Save_folder=r'/storage/emulated/0/Saver'
#Save_folder=r'C:\Users\ANONYMOUS\Downloads\Save'

try:
    os.mkdir(Save_folder)
except :
    pass

class disp(BoxLayout):
    def __init__(self,widget, **kwargs):
        super(disp, self).__init__(**kwargs)
        self.orientation='vertical'
        self.file=widget

        if self.file[-1]=='g':
            self.widget=Image(source=widget)
            self.add_widget(self.widget)
        elif self.file[-1]=='4':
            self.widget=Video(source=widget)
            #lbl=Label(text=str(self.widget.loaded))
            self.add_widget(self.widget)

        self.GL=GridLayout(cols=2, size_hint_y=None, size=(1,75))
        self.save=Button(text='Save', on_press=self.save_widget)
        self.cancel=Button(text='Cancel')
        self.GL.add_widget(self.save)
        self.GL.add_widget(self.cancel)
        self.add_widget(self.GL)
    def save_widget(self, instance):
            shutil.copy(self.file, Save_folder)

class disps(BoxLayout):
    def __init__(self,widget, **kwargs):
        super(disps, self).__init__(**kwargs)
        self.orientation='vertical'
        self.file=widget

        if self.file[-1]=='g' or 'f':
            self.widget=Image(source=widget)
            self.add_widget(self.widget)
        elif self.file[-1]=='4':
            self.widget=Video(source=widget)
            #lbl=Label(text=str(self.widget.loaded))
            self.add_widget(self.widget)
        self.GL=GridLayout(cols=2, size_hint_y=None, size=(1,75))
        self.save=Button(text='Delete', on_press=self.delete)
        self.cancel=Button(text='Cancel')
        self.GL.add_widget(self.save)
        self.GL.add_widget(self.cancel)
        self.add_widget(self.GL)
    def delete(self, instance):
        os.remove(self.file)

class saver(FileChooserListView):
    def __init__(self, **kwargs):
        super(saver, self).__init__(**kwargs)
        self.show_hidden=True
        self.rootpath=WhatsApp_folder
        self.pop=Popup()
        
    def on_submit(self, selection, touch):
        #print(self.selection)
        for f in selection:
            con=disp(f)
            con.cancel.on_press=self.exit
            self.pop=Popup(title='Status',auto_dismiss=False, content=con)
            self.pop.open()
    def exit(self):
        self.pop.dismiss()
class saved(FileChooserListView):
    def __init__(self, **kwargs):
        super(saved, self).__init__(**kwargs)
        self.show_hidden=True
        self.rootpath=Save_folder
        self.pop=Popup()
        
    def on_submit(self, selection, touch):
        #print(self.selection)
        for f in selection:
            con=disps(f)
            con.cancel.on_press=self.exit
            self.pop=Popup(title='Saved',auto_dismiss=False, content=con)
            self.pop.open()
    def exit(self):
        self.pop.dismiss()

class first_screen(BoxLayout):
    def __init__(self, **kwargs):
        super(first_screen, self).__init__(**kwargs)
        self.orientation='vertical'
        self.gl=GridLayout(cols=3, size_hint_y=None)
        self.btn_status=Button(text='WhatsApp Status', on_press=self.status)
        self.gl.add_widget(self.btn_status)
        self.btn_saved=Button(text='Saved Status', on_press=self.saved)
        self.gl.add_widget(self.btn_saved)
        self.btn_abt=Button(text='About', on_press=self.abt)
        self.gl.add_widget(self.btn_abt)
        self.add_widget(self.gl)
        self.sta=saver()
        self.add_widget(self.sta)
        self.sav=saved()
    def status(self, instance):
        self.clear_widgets()
        self.add_widget(self.gl)
        self.add_widget(self.sta)
    def saved(self, instance):
        self.clear_widgets()
        self.add_widget(self.gl)
        self.add_widget(saved())
    def abt(self, instance):
        self.clear_widgets()
        self.add_widget(self.gl)
        self.add_widget(about())
class about(Label):
    def __init__(self, **kwargs):
        super(about, self).__init__(**kwargs)
        abt='           HOW TO USE\n\n1. Make sure WhatsApp is installed in phone memory\n\n2. View the status with WhatsApp Messenger\n\n3. Open Saver App\n\n4. Click WhatsApp Status button\n\n5. Double tap on a status to view and save\n\n\n\n          CONTACT DEVELOPER\n\nFacebook : Sire Ambrose\n\nEmail : ikpeleambroseobinna@gmail.com\n\nWhatsApp : +2348118499120 '
        self.text=abt
class Kivy(App):
    def build(self):
        self.icon='icon.png'
        return first_screen()
        
if __name__ =="__main__":
    Kivy().run()