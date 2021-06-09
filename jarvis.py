import pyttsx3
import datetime
import speech_recognition as sr 
import wikipedia
import webbrowser
import os
import smtplib

engine= pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voices', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def  wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")
    elif hour>=12 and hour<18:
        speak("good afternoon!")

    else:
        speak("good evening!")

    speak("I am jarvis sir,please tell me how may I help you")
def takeCommand():
    #it takes microphone as result and it returns output      

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognition...")
        query =r.recognize_google(audio, language='en-In')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("say that again please...")
        return "None"

    return query
def sendEmail(to,content):
     server=smtplib.SMTP('smtp.gmail.com',587)
     server.ehlo()
     server.starttls()
     server.login('prathmeshkalaskar03@gmail.com','Pk@14062001')
     server.sendmail('prathmeshkalaskar03@gmail.com',to,content)
     server.close()


if __name__ =="__main__":
     wishMe()
     while True: 
         query = takeCommand().lower()
         #task based on query
         if 'wikipedia' in query:
             speak("searching wikipedia...")
             query = query.replace("wikipedia", "")
             results = wikipedia.summary(query, sentences=2)
             speak("according to wikipedia")
             print(results)
             speak(results)

         elif 'open youtube' in query:
             webbrowser.open("youtube.com")
         elif 'open google' in query:
             webbrowser.open("http\\WWW.google.com")
         elif 'open stackoverflow.com' in query:
             webbrowser.open("stackoverflow.com")
         elif'play music' in query:
             music_dir='C:\\Users\\HP\\Music\\download'
             songs=os.listdir(music_dir)
             print(songs)
             os.startfile(os.path.join(music_dir,songs[0]))
         elif'the time'in query:
             strTime=datetime.datetime.now().strftime("%H:%M:%S")
             speak(f"sir,the time is {strTime}")
         elif'open code'in query:
             codepath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
             os.startfile(codepath)
         elif'mail to pk'in query:
             try:
                 speak("what shuld i say")
                 content=takeCommand()
                 to="prathmeshkalaskar01@gmail.com"
                 sendEmail(to,content)
                 speak("email has been send")
             except Exception as e:
                 print(e)
                 speak("soory my friend prathmesh,I am not able to send this email")
         elif'thank you'in query:
             speak("welcome sir, bye bye")
         elif'you mad' in query:
             speak("no sir, soory for my mistake i try my best")

