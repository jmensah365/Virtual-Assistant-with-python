import speech_recognition as sr
import pyttsx3
import pywhatkit as pwk
import datetime
import pyjokes
import time
import requests
import pyautogui
import webbrowser as we
import string
import random




#Listen and recognize your voice
listener = sr.Recognizer()
#engine that speaks back to you
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()
def run_command()   :
    try:#sometimes it will not recognize our voice so we have to to a try and except statement
        with sr.Microphone() as source:#source of our audio
            talk('Hello my name is TARS. How may I assist you?')
            voice = listener.listen(source)#Our voice
            #pass audio to google using googles API
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'TARS' in command:
                print('You said', command)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand what you said")
    return command
def password():
    command = run_command
    #get the length of the password from user
    command = talk('How long do you want your password to be')
    length = int(input('Length:'))
    lengthOfPassword = length
    the_password = ''
    #Get the characters
    upper = string.ascii_uppercase
    num = string.digits
    lower = string.ascii_lowercase
    hexdigits = string.hexdigits
    special_characters = string.punctuation
    #concatenate characters together
    password = upper + num + lower + hexdigits + special_characters
    temp = random.sample(password,lengthOfPassword)
    #Join the password with empty string
    password = the_password.join(temp)
    #Output password to screen
    talk('Your password is')
    print(password)
    talk(password)
def clipboard():
    pass


while True:
    command = run_command()
    #Plays anything we want on youtube
    if 'play' in command:
        song = command.replace('play','')
        talk('playing'+song)
        pwk.playonyt(song)
    #Searches and redirects the user to what he wanted to search up on youtube
    elif 'search' in command:
        topic = command.replace('search','')
        talk('Searching'+topic)
        pwk.search(topic)
    #Gives a short info paragraph on whatever the user wants
    elif 'info' in command:
        info = command.replace('info','')
        talk('Searching up'+info)
        pwk.info(info)
    #The current time
    elif 'time' in command:
        time = datetime.datetime.now().strftime("%I %M %S %p")
        talk('Current time is'+time)
        print(time)
    #gets a joke from the pyjoke library
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        talk(joke)
    #Prints and says the password
    elif 'password' in command:
        password()
    #ends the loop/program
    elif 'offline' in command:
        talk('Bye, going offline')
        quit()
    
    
