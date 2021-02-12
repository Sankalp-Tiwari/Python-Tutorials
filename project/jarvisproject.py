import os
import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import random
import smtplib

which_song = random.randint(0,215)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    """It speaks the string value"""
    engine.say(audio)
    engine.runAndWait()

def wishme():
    """It Wishes everyone according to their local time"""
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("Hi I am Jarvis how may i help you")

def takecommand():
    """It takes microphone input from the user and return string output"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio,language='en-in')
        qw = (f"User said {query}")
        print(qw)
        speak(qw)


    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('botjarvis01@gmail.com','Botjarvis')
    server.sendmail('botjarvis01@gmail.com',to,content)
    server.close()

if __name__ == '__main__':
    wishme()
    while True:
        query = takecommand().lower()
        #Logic for excecuting our program
        if 'wikipedia' in query:
            speak("Searching it on wikipedia wait for a moment...")
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)
        elif 'open youtube'in query:
            speak("opening youtube")
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            speak("Opening youtube")
            webbrowser.open('google.com')
        elif 'play music' in query:
            music_dir = "G:\\songs\\Jarvis musics"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[which_song]))
        elif 'the time'in query:
            strtime = datetime.datetime.now().strftime('%H:%M')
            print(strtime)
            speak(f"the time is{strtime}")
        elif 'open MS Word' in query:
            wordpath = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(wordpath)
        elif 'send email' in query:
            email_confirmation = speak("To whoom do you want to send e mail")
            q = takecommand()
            if 'sankalp' in email_confirmation:
                try:
                    speak("What should I say?")
                    content = takecommand()
                    to = "7815sankalptiwari8d@gmail.com"
                    sendEmail(to,content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry I am not able to send email")
        elif 'hello' in query:
            speak("hello sir i am jarvis i am made to work with you")
        elif 'java stop' in query:
            exit()
