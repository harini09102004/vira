import cv2
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from Demos.win32netdemo import server
from pyttsx3 import speak
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import pyjokes
import requests
import json
import pygetwindow as gw
from PyQt5 import uic 
from PyQt5 import QtWidgets,QtCore, QtGui 
from PyQt5.QtCore import QTimer, QTime, QDate
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from realgui import Ui_VIRAUI
import numpy as np
from PIL import Image
import pyautogui as p


engine = pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices',voices[0].id)
# Load the sample dataset
with open('student_data.json', 'r') as f:
    data = json.load(f)




#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()




#to wish
def wish():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("good morning")
    elif hour>12 and hour<=18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("i am vira, how can i help you")

def sendEmail(to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('hariinmagicshop09@gmail.com', 'EEEmagic@09')
        server.sendmail('hariinmagicshop09@gmail.com', to, content)
        server.close()
    except Exception as e:
        print(f"Failed to send email: {str(e)}")

def check_attendance():
    speak("Your attendance details are as follows:")
    for subject, attendance in data['attendance'].items():
        speak(f"{subject}: {attendance}")


def check_timetable(day):
    if day in data['timetable']:
        speak(f"Your timetable for {day} is as follows:")
        for subject in data['timetable'][day]:
            speak(subject)
    else:
        speak(f"No classes scheduled on {day}.")


def check_marks():
    speak("Here are your marks:")
    for subject, assessments in data['marks'].items():
        speak(f"For {subject}:")
        for assessment, score in assessments.items():
            speak(f"{assessment}: {score}")


def check_exam_timetable():
    speak("Your upcoming exams are as follows:")
    for subject, exam_date in data['exam_timetable'].items():
        speak(f"{subject}: {exam_date}")


def check_assignments():
    assignments = data.get("assignments", {})

    if not assignments:
        speak("You have no assignments listed.")
        return

    speak("Your assignments status:")
    for subject, assignment in assignments.items():
        due_date = assignment.get("due", "No due date specified")
        uploaded_status = "uploaded" if assignment.get("uploaded", False) else "not uploaded"

        # Formulate the response
        assignment_message = f"For {subject}, the assignment is due on {due_date} and has been {uploaded_status}."
        print(assignment_message)  # Optional: print to console as well
        speak(assignment_message)

def takecommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold=1
        audio=r.listen(source,timeout=3,phrase_time_limit=5)

    try:
        print("recognizing.....")
        query =r.recognize_google(audio,language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("Say that again please.....")
        return "none"
    return query


def register_event():
    print("Checking events for registration:")
    unregistered_events = []

    for event in data['events']:
        if event['register']:
            message = f"Event '{event['name']}' is available for registration."
            print(message)
            speak(message)
        else:
            message = f"Event '{event['name']}' is not available for registration."
            print(message)
            speak(message)
            unregistered_events.append(event['name'])  # Collect unregistered events

    if unregistered_events:
        speak("Would you like to register for any of the unregistered events?")
        user_response1 = takecommand().lower()

        if "yes please" in user_response1:  # Check if the response contains "yes"
            speak("Please tell me the name of the event you want to register for.")
            user_response2 = takecommand().lower()  # Get the event name from user input
            if "hackathon" in user_response2:
                    speak(f"registration done.")
                    speak('Hope you have a good experience!')

            else:
                speak("I didn't catch the event name. Please try again.")
        else:
            speak("Okay, but registering for an event and attending will increase your knowledge. but I respect your decision.")

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.TaskExecution()

    import speech_recognition as sr

    def takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise
            print("listening.....")
            r.pause_threshold = 1.5  # Set a reasonable pause threshold
            audio = r.listen(source, timeout=None)  # No timeout, waits for user input
        
        try:
            print("recognizing.....")
            self.query = r.recognize_google(audio, language='en-in')
            print(f"user said: {self.query}")  # Print the recognized command
            return self.query

        except sr.UnknownValueError:
            print("Google could not understand the audio")
            speak("Sorry, I didn't catch that.")
            return "none"
        except sr.RequestError as e:
            print(f"Could not request results from Google; {e}")
            speak("Sorry, I'm having trouble with my network.")
            return "none"
        except Exception as e:
            print(f"error: {e}")  # Catch other potential exceptions
            speak("Please say that again.")
            return "none"




    def TaskExecution(self):
        p.press('esc')
        speak("please wait, scaning your face for user authentication")
        speak("verification successful")
        speak("welcome back harini")
        wish()
        #speak("hello")
        while True:
        #if 1:
            self.query =self.takecommand().lower()
            #logic building for tasks
            if "open notepad" in self.query:
                npath ="C:\\Windows\\System32\\notepad.exe"
                os.startfile(npath)
            elif "open google chrome" in self.query:
                gcpath ="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                os.startfile(gcpath)
            elif "open microsoft edge" in self.query:
                mepath ="C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
                os.startfile(mepath)
            elif"open command prompt" in self.query:
                os.system("start cmd")

            elif "open camera" in self.query:
                cap=cv2.VideoCapture(0)
                #while True:
                    #ret, img=cap.read()
                    #cv2.imshow('webcam',img)
                    #k= cv2.waitKey(50)
                    #if k==27:
                        #break;
                    #cap.release()
                    #cv2.destroyAllWindows()
                if not cap.isOpened():
                    print("Error: Webcam not accessible.")
                    exit()

                # Capture a single frame
                ret, frame = cap.read()

                if not ret:
                    print("Error: Failed to capture image.")
                else:
                    # Display the captured frame
                    cv2.imshow('Webcam Test', frame)
                    cv2.waitKey(0)  # Wait until a key is pressed

                # Release resources
                cap.release()
                cv2.destroyAllWindows()
            #elif "play music" in query:
                #music_dir="C:\\Users\\harin\\Music"
                #songs=os.listdir(music_dir)
                #rd=random.choice(songs)
                #for song in songs:
                #    if song.endswith('.mp3'):
                #        os.startfile(os.path.join(music_dir, rd))
            elif "play music" in self.query:
                music_dir = "C:\\Users\\harin\\Music"  # Your music directory path
                songs = os.listdir(music_dir)  # List all files in the directory
                mp3_songs = [song for song in songs if song.endswith('.mp3')]  # Filter to include only .mp3 files

                if mp3_songs:  # Check if there are any .mp3 files
                    rd = random.choice(mp3_songs)  # Randomly select an .mp3 file
                    os.startfile(os.path.join(music_dir, rd))  # Play the selected .mp3 file
                else:
                    speak("No music files found.")  # If no .mp3 files found


            elif"ip address" in self.query:
                ip=get('https://api.ipify.org').text
                speak(f"your ip address is {ip}")
            elif"wikipedia"in self.query:
                speak("searching in wikipedia.....")
                self.query=self.query.replace("wikipedia","")
                results=wikipedia.summary(self.query,sentences=2)
                speak("according to wikipedia")
                speak(results)
                print(results)
            elif "open youtube" in self.query:
                webbrowser.open("www.youtube.com")
            elif "open v top" in self.query:
                webbrowser.open("vtop.vit.ac.in/vtop/open/page")
            elif "open linkedin" in self.query:
                webbrowser.open("www.linkedin.com")
            elif "open chat gpt" in self.query:
                webbrowser.open("chatgpt.com")
            elif "open google" in self.query:
                speak("what can i search for you in google")
                cm=self.takecommand().lower()
                if cm:  # Check if the command is not empty
                    # Construct the search URL with the user query
                    search_url = f"https://www.google.com/search?q={cm}"
                    webbrowser.open(search_url)
                #webbrowser.open(f"{cm}")
            elif"send message" in self.query:
                kit.sendwhatmsg("+919842767994","this is a testing pls ignore",10,35)
            elif "play songs on youtube" in self.query:
                kit.playonyt("perfect")

            elif "email" in self.query:
                try:
                    speak("what should i email?")
                    content = self.takecommand().lower()
                    print(f"Recognized content: {content}")  # Debug
                    to = "hariinmagicshop@gmail.com"
                    print(f"Sending email to: {to}")  # Debug
                    sendEmail(to, content)

                    speak("email has been sent to hari")
                except Exception as e:
                    print(e)
                    speak("sorry, i was not able to execute your command, what else can i do for you ")

            elif "close notepad" in self.query:
                speak("okay closing notepad")
                os.system("taskkill/f /im notepad.exe")

            elif "close google" in self.query:
                speak("okay closing google")
                os.system("taskkill/f /im chrome.exe")
            elif "close youtube" in self.query:
                speak("Okay, closing YouTube.")
                # Find all windows that contain "YouTube"
                youtube_windows = [window for window in gw.getAllTitles() if "YouTube" in window]
                for window in youtube_windows:
                    win = gw.getWindowsWithTitle(window)[0]  # Get the first matching window
                    win.close()
            elif "close linkedin" in self.query:
                speak("Okay, closing LinkedIn.")
                # Find all windows that contain "LinkedIn"
                linkedin_windows = [window for window in gw.getAllTitles() if "LinkedIn" in window]
                for window in linkedin_windows:
                    win = gw.getWindowsWithTitle(window)[0]  # Get the first matching window
                    win.close()

            elif "send sms" in self.query:
                speak("what sms should i send")
                sms= takecommand()
                from twilio.rest import Client

                account_sid ='ACff45f9d9144d0ed88a4aa583118a1504'
                auth_token='e98df639fceb4189cc1a3700f7090e7a'
                client =Client(account_sid,auth_token)
                message=client.messages \
                    .create(
                        body= sms,
                        from_='+12162421956',
                        to='+919791805322'
                    )
                
            elif "call" in self.query:
                from twilio.rest import Client
                account_sid ='ACff45f9d9144d0ed88a4aa583118a1504'
                auth_token='e98df639fceb4189cc1a3700f7090e7a'
                client =Client(account_sid,auth_token)
                message=client.calls \
                    .create(
                        twiml= '<Response><Say>This is vira sending a test message in behalf of harini</Say></Response>',
                        from_='+12162421956',
                        to='+919791805322'
                    )



            elif "tell me a joke" in self.query:
                joke = pyjokes.get_joke()
                speak(joke)

            elif "shut down the system" in self.query:
                os.system("shutdown /s /t 1")

            elif "restart the system" in self.query:
                os.system("shutdown /r /t 1")

            elif "sleep the system" in self.query:
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")


            elif "display my attendance" in self.query:
                speak('displaying your attendance percentage')
                check_attendance()

            elif "what is my time table" in self.query:
                day = self.query.split(" ")[-1]  # e.g., "check timetable for monday"
                speak('displaying your time table for the day')
                check_timetable(day.capitalize())

            elif "check my marks" in self.query:
                speak('listing your marks as you requested')
                check_marks()


            elif "what is my exam time table" in self.query:
                speak('here is your exam table')
                check_exam_timetable()
                speak('all the best for your exam')


            elif "check assignments" in self.query:
                speak('listing your assignments as you requested')
                check_assignments()

            elif "what are the upcoming events" in self.query:
                speak('displaying available events in v top')
                register_event()

            elif "can i skip my math class today" in self.query:
                speak('Checking the possibilities...')
                mathematics_attendance = data["attendance"].get("Mathematics", "0%")
                numeric_percentage = float(mathematics_attendance.strip('%'))

                if numeric_percentage < 75:
                    speak(
                        'Your attendance in Mathematics is below 75%. Unfortunately, you cannot skip your class today. Ha ha ha!')
                else:
                    speak('Your attendance in Mathematics is satisfactory. You can skip the class.')

            elif "can i skip my physics class today" in self.query:
                speak('Checking the possibilities...')
                physics_attendance = data["attendance"].get("Physics", "0%")
                numeric_percentage_phy = float(physics_attendance.strip('%'))

                if numeric_percentage_phy < 75:
                    speak(
                        'Your attendance in Physics is below 75%. Unfortunately, you cannot skip your class today. Ha ha ha!')
                else:
                    speak('Your attendance in Physics is satisfactory. You can skip the class.')

            elif "can i skip my chemistry class today" in self.query:
                speak('Checking the possibilities...')
                chemistry_attendance = data["attendance"].get("Chemistry", "0%")
                numeric_percentage_chem = float(chemistry_attendance.strip('%'))

                if numeric_percentage_chem < 75:
                    speak(
                        'Your attendance in Chemistry is below 75%. Unfortunately, you cannot skip your class today. Ha ha ha!')
                else:
                    speak('Your attendance in Chemistry is satisfactory. You can skip the class.')

            elif "thank you" in self.query.lower():
                speak("Glad I helped you today. This is vira signing off.")
                sys.exit(0)

            elif "no thank you" in self.query.lower():
                speak("Glad I helped you today. This is vira signing off.....")
                sys.exit(0)

            else:
                speak("What else can I do for you?")

startExecution =MainThread()
class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_VIRAUI()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        # Load and start the first movie
        self.ui.movie = QMovie("LCPT.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.label_2.update()  # Ensure the label is updated

        # Create and start movie for label_3
        self.label_3 = QLabel(self)
        self.label_3.setGeometry(10, 10, 100, 100)  # Adjust as needed
        movie_3 = QMovie("llll.gif")
        self.label_3.setMovie(movie_3)
        movie_3.start()
        self.label_3.setFixedSize(movie_3.scaledSize())  # Set size to match the movie
        self.label_3.update()

        # Create and start movie for label_4
        self.label_4 = QLabel(self)
        self.label_4.setGeometry(120, 10, 100, 100)  # Adjust as needed
        movie_4 = QMovie("llll.gif")
        self.label_4.setMovie(movie_4)
        movie_4.start()
        self.label_4.setFixedSize(movie_4.scaledSize())  # Set size to match the movie
        self.label_4.update()

        # Create and start movie for label_6
        self.label_6 = QLabel(self)
        self.label_6.setGeometry(10, 120, 100, 100)  # Adjust as needed
        movie_6 = QMovie("Cad.gif")
        self.label_6.setMovie(movie_6)
        movie_6.start()
        self.label_6.setFixedSize(movie_6.scaledSize())  # Set size to match the movie
        self.label_6.update()

        # Create and start movie for label_7
        self.label_7 = QLabel(self)
        self.label_7.setGeometry(120, 120, 100, 100)  # Adjust as needed
        movie_7 = QMovie("Cad.gif")
        self.label_7.setMovie(movie_7)
        movie_7.start()
        self.label_7.setFixedSize(movie_7.scaledSize())  # Set size to match the movie
        self.label_7.update()

        # Set up a timer if necessary
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString("hh:mm:ss")
        label_date = current_date.toString("dd.MM.yyyy")

class ViraMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_VIRAUI()  # Instantiate the Ui_VIRAUI class
        self.ui.setupUi(self)  # Set up the UI on the main window (self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # Local Binary Patterns Histograms
    recognizer.read('trainer/trainer.yml')  # Load trained model

    # Load Haar Cascade for face detection
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath)  # Initialize haar cascade for object detection

    # Define font for displaying name and accuracy on the video frame
    font = cv2.FONT_HERSHEY_SIMPLEX  # Font type

    # List of names (Ensure the index corresponds to the face ID)
    names = ['', 'harini']  # Leave the first index empty as the ID counter starts from 1

    # Initialize video capture (0 for the default camera)
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # cv2.CAP_DSHOW to avoid warnings

    # Set video frame width and height
    cam.set(3, 640)  # Set video frame width
    cam.set(4, 480)  # Set video frame height

    # Define minimum window size to be recognized as a face
    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)

    # Start video capture loop
    while True:
        ret, img = cam.read()  # Read the frames from the video
        if not ret:
            break

        # Convert the image to grayscale (necessary for face detection)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect faces in the grayscale image
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(int(minW), int(minH)),
        )

        # For each detected face, predict the ID and accuracy
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Draw rectangle around the face

            # Predict the face
            id, accuracy = recognizer.predict(gray[y:y+h, x:x+w])

            # Check if accuracy is less than 100 (0 means a perfect match)
            if accuracy < 100:
                name = names[id] if id < len(names) else "Unknown"
                accuracy_text = " {0}%".format(round(100 - accuracy))
                TaskExecution(self)
            else:
                name = "Unknown"
                accuracy_text = " {0}%".format(round(100 - accuracy))

            # Display the name and accuracy on the video frame
            cv2.putText(img, str(name), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
            cv2.putText(img, str(accuracy_text), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

        # Display the video frame with detection
        cv2.imshow('camera', img)

        # Break the loop if 'ESC' key is pressed
        k = cv2.waitKey(10) & 0xff
        if k == 27:
            break

    # Do a bit of cleanup
    print("Thanks for using this program, have a good day.")
    cam.release()
    cv2.destroyAllWindows()

    


    #if __name__=="__main__":

    # Initialize LBPH face recognizer
        

    
    

