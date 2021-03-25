import speech_recognition as sr
import webbrowser #for search on the web
import time
import playsound
import os
import random
from gtts import gTTS
from time import ctime # for time

r = sr.Recognizer() #responsible for recognising the speech

#function to record what you say
def record_audio(ask = False):
    #voice input
    with sr.Microphone() as source: # source is going to be our mic
        if ask:#for search, 
            amelia_speak(ask)
        audio =r.listen(source)
        voice_data = '' #initialise voice data
        try:
            voice_data = r.recognize_google(audio) #variable to hold whatever we say using recocnize google
            # print(voice_data) prints out what you said ,dont need that there or else prints 2
        except sr.UnknownValueError: # exception thrown if alexa does not understand
            print('sorry, I did not get that')
        except sr.RequestError:
            print('Sorry, my speech service is down')
        return voice_data #returning voice data

#Amelias voice
def amelia_speak(audio_string):
    tts = gTTS(text = audio_string, lang ='en')
    r= random.randint(1,1000000)
    audio_file = "audio-" +str(r) + '.mp3'#file name for audio
    tts.save(audio_file)
    playsound.playsound(audio_file) # to play audio right away, from audiofile
    print(audio_string)
    os.remove(audio_file) # remove the audio file


#function to get a response
def respond(voice_data):
    if 'what is your name' in voice_data: # if voicedata returns what is your name
        amelia_speak('My name is Amelia')
    if 'what time is it' in voice_data:
       amelia_speak(ctime()) #can modify this to be just time
    if 'search' in voice_data:
        search=record_audio('What do you want to search for') #variable to hold what we want to searc
        url = 'http://google.com/search?q=' + search # concatinating
        webbrowser.get().open(url)
        amelia_speak('Here is what I found for ' +search )
    if 'find location' in voice_data:
        location=record_audio('What is the location?') #variable to hold what we want to searc
        url = 'http://google.nl/maps/place/' + location + '/&amp; '# concatinating
        webbrowser.get().open(url)
        amelia_speak('Here is the location of ' + location)
    if'exit' in voice_data:
        exit()


time.sleep(0.5)
amelia_speak('How can I help you')
while 0.5:
    voice_data =record_audio() # variable to hold record audio function  
    respond(voice_data)#function to get a response with voice data passed in