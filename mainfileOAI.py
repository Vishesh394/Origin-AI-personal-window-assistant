import pyttsx3   
import speech_recognition as sr 
import time
import datetime
import os
import webbrowser
import instaloader
import random
import wikipedia
import email

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)     

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")
    elif hour>=12 and hour<18:   
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")
    speak("I am your Personal window assistant Origin AI.") 

def takeCommand(): 
    r=sr.Recognizer()   
    with sr.Microphone() as source:   
        print("Listening......") 
        r.energy_threshold=500     
        r.pause_threshold=1           
        audio=r.listen(source, timeout=2, phrase_time_limit=1000)   
        try:                           
            print("Recognizing.....")    
            print(audio)
            query=r.recognize_google(audio, language='en-in')
            print(audio)    
            print(f"USER:{query}\n")
        except Exception as e:
            print(e)
            speak("Unable to recognize your voice......")
            return"None"
        return query

def username():
    speak("What should I call you sir")
    uname=takeCommand()
    speak("Welcome Mister" +uname)       
    speak("How can I help you, sir?")      

if __name__=='__main__':
    wishMe()
    username()
    while True:      
        order=takeCommand().lower()
        if 'how are you' in order:
                speak("I am fine, Thankyou.")
                print()
                speak("How are you,sir?")
            
        elif 'fine' in order or 'good' in order:
                speak("Its good to know that you are fine.")
            
        elif 'who I am' in order:
                speak("If you can talk then surely you are a human.")

        elif 'love' in order:     
                speak("it is the 7th scence that destroy all other sences")

        elif 'who are you' in order:
                speak("I am your virtual assistant origin")

        elif 'I love you' in order:
                speak("On my god,thankyou. I love you too. Anything I can help you with?")

        elif 'will you be my girl friend ' in order or 'will you be my valentine' in order:
                speak("I'm not sure about that please give me some more time.")

        elif 'what is your name' in order:
                speak("My friends call me origin ")
       
        elif 'open youtube' in order:
                speak("here you go to youtube sir ")
                webbrowser.open("youtube.com")
            
        elif 'open Notepad' in order:
                speak("here you go to Notepad")
             
        elif 'open wikipedia' in order:
                speak("here you go to wikipedia sir ")
                webbrowser.open("wikipedia.com")
               
        elif 'open google' in order:
                speak("opening google")
                webbrowser.open("google.com")
                
        elif 'open stack overflow' in order:
                speak("opening ")
                webbrowser.open("stackoverflow.com")
               
        elif 'where is' in order:
              location=order
              speak("Locating.....")  
              webbrowser.open("https://maps.google.co.in/")
           
        elif 'locate hospital' in order:
              location=order
              speak("Locating.....")  
              webbrowser.open("https://maps.google.co.in//hosp")

        elif 'where is' in order:
              location=order
              speak("Locating.....")  
              webbrowser.open("https://maps.google.co.in/")
           
        elif "instagram profile" in order or "profile on instagram" in order:
              speak("sir please open the name correctly.")
              name = input("Enter username here:")
              webbrowser.open("https://www.instagram.com/")
              speak("sir would you like to download profile picture of the account.")
              condition = takeCommand().lower()
              if "yes" in condition:
                 mod = instaloader.Instaloader()
                 mod.download_profile(name,profile_pic_only=True)
                 speak("i am done sir, profile picture is saved in our main folder.now i am ready") 
           
        elif 'play music' in order or 'play songs' in order:
            music_dir="D:\\New folder\\songs"
            songs=os.listdir(music_dir)
            rd=random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))
       
        elif 'open wikipedia' in order:
              speak('Searching...')
              order=order.replace("wikipedia")
              results= wikipedia.summary(order,sentence=2)
              speak("According to wikipedia")
              speak(results)

        elif 'the time' in order:
              strTime = datetime.datetime.now().strftime("%H:%M:%S")
              speak(f"well,the time is {strTime}")         