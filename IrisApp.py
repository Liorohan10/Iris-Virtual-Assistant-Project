import pygame
import os
import datetime
import random
import psutil
import socket
import threading
import pyttsx3
from GoogleFeatures import googlenewsfeatures
from tkinter import *
from tkinter import simpledialog, Tk
from PIL import ImageTk, Image
import speech_recognition as sr
from AppFeatures import features, wolframalph
import pyjokes
import face_recognition
import cv2
import numpy as np
import glob
import time
import csv
import pickle
import webbrowser


destroy= False
state = 0
user_panel_flag = False
REMOTE_SERVER = "1.1.1.1"
HEIGHT, WIDTH = 350, 250
X_POS, Y_POS = '500', '0'
app_music = ['open-ended', 'unsure', 'when', 'sorted']
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',150)

pygame.mixer.init()


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".") # Return the absolute version of a path
    return os.path.join(base_path, relative_path)

def speak(audio):
    print('Iris:', audio)
    engine.say(audio)
    engine.runAndWait()



def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.6 # seconds of non-speaking audio before a phrase is considered complete
        r.phrase_threshold = 0.290 # minimum seconds of speaking audio before we consider the speaking audio a phrase - values below this are ignored (for filtering out clicks and pops)
        r.energy_threshold = 368 # minimum audio energy to consider for recording
        audio = r.listen(source)
        said = ''
        try:
            said = r.recognize_google(audio, language='en-in') # Performs speech recognition on ``audio_data`` (an ``AudioData`` instance), using the Google Speech Recognition API.
            print("U said : " + said)

        except Exception as e:
            print("Exception: Sorry...I couldn't  recognize what u said " + str(e))
            (print('Say that again please ....'))
            speak('Could u please say that again ...')
            said = myCommand()
    return said


def wake_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Waiting to be called \
             Listening...")
        r.pause_threshold = 0.7
        r.phrase_threshold = 0.3
        r.energy_threshold = 375
        audio = r.listen(source)
        try:
            wake_cmd = r.recognize_google(audio, language='en-in')
            print("U said : " + wake_cmd)

        except Exception as e:
            wake_cmd = wake_command()
    return wake_cmd


def wakeWord(text):
    WAKE_WORDS = ['hey', 'hi', 'hello','hola','iris']
    text = text.lower()
    for phrase in WAKE_WORDS:
        if phrase in text:
            return True

    return False


def wishMe():            
        all_checks_flag = True
        internet_connection_status = check_internet_connection()

        GREETING_INPUTS = ['hi', 'hey', 'wassup', 'Hello']
        GREETING_RESPONSES = ['hello', 'hey there']
        HELP_GREET_RESPONSES = ['How may I help you ?', 'I am now ready to take your commands..',
                                'Please tell me what I can do for you ?']
           
        
        hour = int(datetime.datetime.now().hour)
        if 0 < hour < 12:
            speak('Good Morning Sir...')
            speak('I am Iris... Your Virtual Assistant')
            speak(features.getDate())
            if internet_connection_status:
                 
                    speak(random.choice(HELP_GREET_RESPONSES))
                    speak("To give me any command, click on the mic button")
                    # return all_checks_flag
                 
            else:
                speak("I can see that you are not connected to Internet/"
                      "I would suggest you to connect to internet for seemless service")
                all_checks_flag = False
                # return all_checks_flag


        elif 12 <= hour <= 18:
            speak('Good Afternoon Sir...')
            speak('I am Iris.... Your Virtual Assistant')
            speak(features.getDate())
            if internet_connection_status:
                 # speak(features.getweather('Kolkata'))
                 
                    speak(random.choice(HELP_GREET_RESPONSES))
                    speak("To give me any command, click on the mic button")
                    # return all_checks_flag
                 
            else:
                speak("I can see that you are not connected to Internet/"
                      "I would suggest you to connect to internet for seemless service")
                all_checks_flag = False
                # return all_checks_flag

        else:
            speak('Good Evening Sir..')
            speak('I am Iris... Your Virtual Assistant')
            speak(features.getDate())
            if internet_connection_status:
                 
                    speak(random.choice(HELP_GREET_RESPONSES))
                    speak("To give me any command, click on the mic button")
                    # return all_checks_flag
                 
            else:
                speak("I can see that you are not connected to Internet/"
                      "I would suggest you to connect to internet for seemless service")
                all_checks_flag = False
                # return all_checks_flag


def get_typed_query():
    query = simpledialog.askstring("", "Please type your command") # 
    #print(query)
    return str(query)





def check_internet_connection():
    try:
        host = socket.gethostbyname(REMOTE_SERVER)
        s = socket.create_connection((host, 80), 2)
        s.close()
        return True
    except:
        pass
    return False


def get_internet_connection_img(connection_status):
    if connection_status:
        return "wifi.png"
    else:
        return "no-wifi.png"

notification_folder = resource_path('Notification_sounds')
IMAGE_PATH = resource_path('Images\Background\APP-BG.jpg')

class Widget:

    def __init__(self):
        connection_status = check_internet_connection()
        self.root = Tk() # it means in this class it will create a class level variable root and initialize it with Tk() object and whenever you want to access this variable in the class you will call it with self.root
        self.root.geometry('{}x{}+{}+{}'.format(HEIGHT, WIDTH, X_POS, Y_POS))
        self.root.resizable(0, 0)
        self.root.iconbitmap(resource_path("Images\icon\\Icon1.ico"))

        img = ImageTk.PhotoImage(Image.open(IMAGE_PATH).resize((HEIGHT, WIDTH - 120), Image.ANTIALIAS))




        panel_main = Label(self.root, image=img) # Label widget which can display text and bitmaps
        panel_main.pack(expand="no", side='top') # Expand-When set to YES, the widget expands to fill any space not used in widget's parent. Attributes: YES, NO. Side-Determines which side of the widget's parent it packs to. Attributes: TOP (default), BOTTOM, LEFT, or RIGHT.
        self.root.title('Iris App')


        

        internet_connection_img_file = get_internet_connection_img(connection_status)
        internet_connection_img = ImageTk.PhotoImage(
            file=resource_path("Images\Connection_status\\") + internet_connection_img_file)

        mic_img = ImageTk.PhotoImage(Image.open(resource_path("Images\Button_img\mic\mic1.png")))
        close_button_img = PhotoImage(file=resource_path("Images\Button_img\\force_stop\\force-stop.png"))

        self.voice_command_on = PhotoImage(file=resource_path("Images\Button_img\listen_button\\toggle_on.png"))
        self.voice_command_off = PhotoImage(file=resource_path("Images\Button_img\listen_button\\toggle_off.png"))

        self.enable_keep_listening = Label(self.root, text="Enable Listening ", bg='gray26',
                                           font=('Black Ops One', 10, 'bold'),
                                           fg='white')
        self.enable_keep_listening.place(x=5, y=30)
        Connection_label = Label(self.root, text='Connection', font=('Black ops one', 10, 'bold'), bg='gray26',
                                 fg='white').place(x=0, y=85)
        self.Connection_img_label = Label(self.root, image=internet_connection_img).place(x=78, y=85)
        



        self.t_btn = Button(self.root, image=self.voice_command_off, border=0, bg='gray26',
                            activebackground='gray26', command=self.voice_command_activation_switch)
        self.t_btn.place(x=20, y=5)

        self.mic_button = Button(self.root, image=mic_img, font=('Black ops one', 10, 'bold'), bg='gray62',
                                  height='35',
                                  width='25', border=0, command=self.clicked)
        self.mic_button.place(x=310, y=15)
        self.type_query_button = Button(self.root, text="Type Command", font=('Black ops one', 10, 'bold'), bg='white',
                                        border=0,
                                        command=self.typed)
        self.type_query_button.place(x=150, y=15)
        close_button = Button(self.root, image = close_button_img, border= 0,font=('Black Ops One', 10, 'bold'), bg='deepSkyBlue', fg='white',
                      command=self.destroy_root).place(x=310,y=65)


        self.userText = StringVar()
        self.userText.set('Click on Mic Button to Give commands \
                          or use Type Button to Type Commands')

        userFrame = LabelFrame(self.root, text="USER", font=('Black ops one', 10, 'bold'))
        userFrame.pack(fill="both", expand="yes", side='bottom') # fill- Determines if the widget keeps the minimal space needed or takes up any extra space allocated to it.
                                                                 # fill="both" fills both horizontally and vertically
        User_Message = Message(userFrame, textvariable=self.userText, bg='gray24', fg='white')
        User_Message.config(font=("Comic Sans MS", 10, 'bold')) #config- config is used to access an object's attributes after its initialisation.
        User_Message.pack(fill='both', expand='no', )

        wishMe()
        self.root.mainloop() # is a method on the main window which we execute when we want to run our application. This method will loop forever, waiting for events from the user, until the user exits the program – either by closing the window, or by terminating the program with a keyboard interrupt in the console.

    def destroy_root(self):
        destroy = True
        sys.exit()
        self.root.destroy()


    def execute(self, query):
        if not destroy:
            query = query.lower()
            if 'wikipedia' in query:
                self.userText.set("USER:" + query)
                self.root.update()
                speak('searching that on wikipedia')
                # query = query.replace("wikipedia", "")
                wiki_result = features.searchonWiki(query.replace("wikipedia","").replace("on" , "")) # The replace() method replaces a specified phrase with another specified phrase.
                speak("According to wikipedia  " + wiki_result)
                self.userText.set("According to wikipedia  " + wiki_result)
                self.root.update()
                return False

            elif 'open google' in query:
                self.userText.set("USER:" + query)
                self.root.update()
                speak('Opening Google for you Sir')
                self.userText.set('Opening Google for you Sir')
                self.root.update()
                features.openGoogle()
                return False


            elif 'open youtube' in query:
                self.userText.set("USER:" + query)
                self.root.update()
                speak('opening Youtube for you Sir')
                self.userText.set('opening Youtube for you Sir')
                self.root.update()
                features.openYoutube()
                return False

            elif 'search on google' in query:
                search_list = []
                speak('What would you like to search?')
                search_terms= myCommand()
                search_list.append(search_terms)
                for term in search_list:
                    url = "https://www.google.com.tr/search?q={}".format(term)
                    webbrowser.open_new_tab(url)
                speak('Searching that on Google...')

            elif 'weather' in query:
                speak('Of Which location Sir ?')
                city_name = myCommand()
                features.getweather(city_name)
                return False

            elif 'open notepad' in query:
                os.system("python C:\\Users\\Rohan\\Desktop\\IrisMod\\Iris_Notepad\\IrisNotepad.py")

            elif 'open calculator' in query:
                os.system("python C:\\Users\\Rohan\\Desktop\\IrisMod\\Iris_Calculator\\main.py")    
                            
            elif 'how are you doing' in query:
                speak("I'm doing well.How do you do?")
                self.userText.set("I'm doing well.How do you do?")
                self.root.update()

            elif 'i am fine' in query:
                speak("I am glad everything is fine")
                self.userText.set("I am glad everything is fine")
                self.root.update()

            elif 'nice to meet you' in query:
                speak("It is a pleasure to meet you too")
                self.userText.set("It is a pleasure to meet you too")
                self.root.update()

            elif 'whats up' in query:
                speak("The sky's up but I'm fine thanks. What about you?")
                self.userText.set("The sky's up but I'm fine thanks. What about you?")
                self.root.update()

            
            elif 'tell me a joke' in query:
                v=pyjokes.get_joke()
                speak(v)
                self.userText.set(v)
                self.root.update()

            elif "news headlines" in query:
                speak("Of which region")
                region = myCommand().lower()
                news_list = googlenewsfeatures.getgooglenews(5, region)
                speak("Presenting you todays headlines...")

                for news in news_list:
                    print(news)
                    speak(news)
                    self.userText.set(news)
                    self.root.update()
                speak("Presented todays headlines..")
                return False
           
                
            elif "translate it" in query:
                statement = query.replace('translate it', '')
                speak("In which language?")
                dest = myCommand()
                speak(googleTranslate.langTranslator(statement, dest))
                return False

            elif 'add face in face recognizer' in query:
                from FaceRecognition import embeddings

            elif 'open face recognizer' in query:
                from FaceRecognition import recognition

            elif 'activate alpha' in query:
                speak("Alpha mode activated")
                query = myCommand()
                while True:
                    speak(wolframalph.wolframalphafunc(query))
                    query = myCommand().lower()
                    if 'deactivate alpha' in query:
                        speak("Alpha mode deactivated...")
                        break
                    else:
                        continue
                return False



            elif 'stop listening' in query:
                speak('Please call me whenever needed')
                return True

            elif 'bye' in query:
                speak('GoodBye Sir....'
                      'hope we meet soon..')
                sys.exit()

    def clicked(self):
       print("in clicked")
       pygame.mixer.music.load(notification_folder + '/' + app_music[2] + '.mp3')
       pygame.mixer.music.set_volume(1.5)
       pygame.mixer.music.play()

       self.t_btn.config(state='disabled')
       self.type_query_button.config(state='disabled')
       self.root.update()

       self.userText.set('Listening...')
       query = myCommand()
       print(query)
       self.userText.set(query)
       query = query.lower()

       self.execute(query)

       self.t_btn.config(state='normal')
       self.type_query_button.config(state='normal')
       self.root.update()
       return

    def typed(self):
        print("in typed")
        pygame.mixer.music.load(notification_folder + '/' + app_music[1] + '.mp3')
        pygame.mixer.music.set_volume(1.5)
        pygame.mixer.music.play()

        self.t_btn.config(state='disabled')
        self.mic_button.config(state='disabled')
        self.root.update()

        query = get_typed_query()
        if query != 'None':
            self.execute(query)

        self.t_btn.config(state='normal')
        self.mic_button.config(state='normal')
        self.root.update()
        return

    def voice_command_activation_switch(self):
        global state
        internet_connection_status = check_internet_connection()
        if internet_connection_status:

            if state == 0:
                print("in state == 0 of vcas")
                pygame.mixer.music.load(notification_folder + '/' + app_music[1] + '.mp3')
                pygame.mixer.music.set_volume(1.5)
                pygame.mixer.music.play()
                self.t_btn.config(image=self.voice_command_on)
                self.t_btn.config(state='disabled')
                self.mic_button.config(state='disabled')
                self.enable_keep_listening.config(text="Listening..", font=('Black Ops One', 10, 'bold'))
                self.t_btn.config(state='disabled')
                self.root.update()
                state = 1

                # self.listen_continuously()
                threading.Thread(target=self.listen_continuously()).start()
                self.t_btn.config(state='normal')
                self.mic_button.config(state='normal')
                self.root.update()
                return
        else:
            speak("I can see that you are not connected to Internet...."
                  "I would suggest you to connect to Internet for seemless service")
            self.t_btn.config(image=self.voice_command_off)
            self.enable_keep_listening.config(text=" Enable Listening", font=('Black Ops One', 10, 'bold'))
            self.root.update()
            state = 0

    def listen_continuously(self):
        global state ,destroy
        #print("state in listen continuouslly fn is :" + str(state))
        while True and not destroy :
            query = wake_command()
            #print("in listen continuously query recieved is:" + query)
            if state == 1 and 'stop listening' not in query:
                #print("state in listen continuouslly fn if loop is :" + str(state))

                if wakeWord(query):
                    print("waked up successfully")
                    speak("How may I help you sir")
                    command = myCommand()
                    stop_flag = self.execute(command)
                    if stop_flag:
                        break
                    else:
                        continue

                else:
                    continue
            else:
                speak('Listening has been stoped now')
                self.t_btn.config(image=self.voice_command_off)
                self.t_btn.config(state='normal')
                pygame.mixer.music.load(notification_folder + '/' + app_music[2] + '.mp3')
                pygame.mixer.music.set_volume(1.5)
                pygame.mixer.music.play()
                self.enable_keep_listening.config(text=" Enable Listening", font=('Black Ops One', 10, 'bold'))
                state = 0
                break
        self.t_btn.config(image=self.voice_command_off)
        self.t_btn.config(state='normal')
        pygame.mixer.music.load(notification_folder + '/' + app_music[2] + '.mp3')
        pygame.mixer.music.set_volume(1.5)
        pygame.mixer.music.play()
        self.enable_keep_listening.config(text=" Enable Listening", font=('Black Ops One', 10, 'bold'))
        self.root.update()
        state = 0


if __name__ == '__main__':
    widget = Widget()

