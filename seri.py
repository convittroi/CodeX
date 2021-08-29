import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
seri = pyttsx3.init()
voice=seri.getProperty('voices')
seri.setProperty('voice',voice[1].id)

def speak(audio):
    print('S.E.R.I: ',audio)
    seri.say(audio)
    seri.runAndWait()
speak('hello Quoc cay')
def time():
    time=datetime.datetime.now().strftime("%I: %M %p")
    speak(time)

def welcom():
    hour=datetime.datetime.now().hour
    if hour >=6 and hour<12:
        speak('Good Morning Sir')
    elif hour >=12 and hour<18:
        speak('Good Afternoon Sir')
    elif hour >=18 and hour<24:
        speak('Good Night Sir')
    speak('How can I help you ?')

def command():
    c=sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold=2
        audio=c.listen(source)
    try:
        query=c.recognize_google(audio,language='en')
        print('Ông Trùm :' + query)
    except sr.UnknownValueError:
        print("Please repeat or typing again")
        query= str(input('Your order is : '))
    return query
if __name__ =="__main__":
    welcom()
    while True:
        query=command().lower()
        if 'google' in query:
            speak('What should I search Boss ?')
            search=command().lower()
            url=f"https://www.google.com.vn/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on Google')
        if 'youtube' in query:
            speak('What should I search Boss ?')
            search=command().lower()
            url=f"https://www.youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on Youtube')
        elif 'time' in query:
            time()
        elif 'bye' in query:
            speak('Seri is quitting sir , Goodbye Boss!')
            quit()    