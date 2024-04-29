import speech_recognition as sr     #Converts Spoken words to Text. (Speech-To-Text).
import pyttsx3      #Converts Text to Speech (Text-To-Speech).
import datetime     #Used to get current time
import wikipedia    #Helps in opening wikipedia and searching for what the user asks.
import webbrowser   #Helps in opening browser and performing search.
import os           #Provides functions for interacting with the operatin system.
import requests     #Helps in accessing the website using url.
from bs4 import BeautifulSoup       #Helps in extracting information from the request made to the website.
import smtplib      #Helps in sending emails.
import geocoder     #helps in locating the coordinates of addresses, cities, countries, and landmarks across the globe
import random        #Helps in generating random integers
import PyPDF2 
from selenium import webdriver    

def get_current_location():
    try:
        g = geocoder.ip('me')  # Get location based on your IP address
        if g:
            return g
        else:
            return "Location not found"
    except Exception as e:
        return str(e)

engine=pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id) #female voice
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=6 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    elif hour>=18 and hour<21:
        speak("Good Evening!")
    else:
        speak("Good Night!")

    speak("I am Jarvis. Please tell me how may I help you")

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("dipchandrighosh03@gmail.com", "fnio sgla cbrt sfhi")
    server.sendmail('dipchandrighosh03@gmail.com', to, content)
    server.close()

#speak("Dipchandri")
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 1500
        r.pause_thresold = 0.8
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in') #Google Speech Recognition
        print(f"User said: {query}\n")

    except Exception as e:
        #        print(e)
        print("Say that again please")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        #speak(query)
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query =query.replace("wikipedia", "")
            results= wikipedia.summary(query, sentences=2)
            speak('According to Wikipedia')
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\ghosh\\Music\\Playlist'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[random.randint(0, len(songs)-1)]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"The current time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\ghosh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'temperature' in query:
            search = "temperature in kolkata"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp =data.find("div", class_ = "BNeawe").text
            speak(f"Current{search} is {temp}")

        

        elif 'location' in query:
            '''key = 'Yn5YIbhIetkIn4ZcuzzSrjQVf6nppjSd'
            url = 'https://www.mapquestapi.com/geocoding/v1/address?key='
            loc = 'University of Engineering and Management, Kolkata'
            main_url = url + key + '&location='+ loc
            req = requests.get(main_url)
            data = req.json()['results'][0]
            print(data)
            speak(f'Current location is {data}')'''
            location = get_current_location()
            if isinstance(location, str):
                print(location)
                print("Current Location:")
                speak("Your Current Location is")
                print("Latitude:", location.latlng[0])
                speak(f"Latitude {location.latlng[0]}")
                print("Longitude:", location.latlng[1])
                speak(f"Longitude {location.latlng[1]}")
                print("City:", location.city)
                speak(f"City {location.city}")
                print("State:", location.state)
                speak(f"State {location.state}")
                print("Country:", location.country+"DIA")
                speak(f"Country {location.country}+DIA")
            else:
                print(location)
                print("Current Location:")
                speak("Sir, Your Current Location is")
                print("Latitude:", location.latlng[0])
                speak(f"Latitude {location.latlng[0]}")
                print("Longitude:", location.latlng[1])
                speak(f"Longitude {location.latlng[1]}")
                print("City:", location.city)
                speak(f"City {location.city}")
                print("State:", location.state)
                speak(f"State {location.state}")
                print("Country:", location.country+"DIA")
                speak(f"Country {location.country}+DIA")

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = ("ghoshdipchandri@gmail.com")
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, I am unable to send this email")

        elif 'read' in query:
            book = open('OceanofPDF.com_The_Silent_Patient_-_Alex_Michaelides.pdf','rb')
            pdfReader = PyPDF2.PdfReader(book)
            pages = len(pdfReader.pages)
            print(pages)
            for num in range(5,pages):
                current_page = num
                pageObj = pdfReader.pages[num]
                speak(f"Page {current_page}")
                # extracting text from page
                print(pageObj.extract_text())
                speak(pageObj.extract_text())
            
        
        if query == "exit":
            exit()
        else:
            speak(query)