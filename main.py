#you can change ALEXA to any name you want, all you have to do is change 'alexa' to your desired name 
#since always typing speech_recognition takes a lot of time we use [as sr] you can change sr to anything you wish
import speech_recognition as sr
#pyttsx3 is a library in python that is used to convert text to speech
import pyttsx3
#pywhatkit is a library in python that is used to many authomation mainly whatsapp and youtube, in the below code we use the youtube feature 
import pywhatkit
import datetime
#wikipedia ia a library we use to search information, this has a package to guve summary 
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
#there are two options for the voice, 0 for male and 1 for female
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()
    
def take_command():
    try:
        with sr.Microphone() as source:
            print("listening....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa','')
            #  engine.say(command)
            #  engine.runAndWait()
            #    print(command)
            
     #you need except here because sometimes your microphone might not work or your voice is not recognised , if you want to relate this is like try and catch block in java       
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
        
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I %M %p')
        print(time)
        talk('Current time is'+ time)
       
    elif 'who is' in command:
        person = command.replace('who is','')
        info = wikipedia.summary(person, 2)
       # print(info)
        talk(info)
        
    elif 'date' in command:
        talk("sorry, I don't date losers ")
        
    elif 'i love you' in command: 
        talk("that is very cute but you are ugly")  
    
    elif 'are you single' in command: 
        talk("Bro I'm dating your wifi... oops")    
    
    elif 'joke' in command:
        funny = pyjokes.get_joke()
        print(funny)
        talk(funny)
        #talk(pyjokes.get_joke())
    else:
        talk("I don't understand")
        
            
while True:   
    run_alexa()
