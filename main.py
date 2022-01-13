import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
#from playsound import playsound
import jokes
import random


def tell_time():
    time = datetime.datetime.now()
    hour_per = 'A.M'
    hour = time.hour
    if time.hour >= 12:
        hour_per = 'P.M'
        hour = hour - 12
    else:
        hour_per = 'A.M'
    print(str(hour) + ':' + str(time.minute) + " " + hour_per)
    speak("sir The time is " + str(hour) + ':' + str(time.minute) + " " + hour_per)


engine = pyttsx3.init('sapi5')
rate = engine.getProperty('rate')  # getting details of current speaking rate
print(rate)
engine.setProperty('rate', 150)  # setting up new voice rate

# Chrome settings
chrome_path = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

n_chrome_path = r'E:\Projects\PyCharm\Jarvix_punjabi\data\N-Chrome.lnk'
webbrowser.register('n_chrome', None, webbrowser.BackgroundBrowser(n_chrome_path))

# voices = engine.getProperty("voices")
# print(voices[1].id)
# engine.setProperty('voice',voices[0].id)

# volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
# print(volume)                          #printing current volume level
# engine.setProperty('volume', 1.0)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour < 12 and hour >= 0:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")


def spellings(speller):
    length = len(speller)
    pos = speller.find('spell')
    speller = speller[pos:]
    speller = speller.replace('spell ', "")
    speller = speller.upper()
    alpha = []
    for i in speller:
        alpha.append(i)

    spell = '  '.join(alpha)

    return spell


def Hear():
    required = -1
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        if "pulse" in name:
            required = index
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        #playsound(r'E:\Projects\PyCharm\Jarvix_punjabi\Listen.mp3')
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        print("Recognising...")
        voiceinput = r.recognize_google(audio, language="en-in")
        print("You said: " + voiceinput)
        return str(voiceinput)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        speak("Sorry i am not able to understand, can you repeat please?")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


def wiki(queryy, rep):
    speak("Searching wikipedia...")
    query = queryy.replace(rep, "")
    results = wikipedia.summary(query, sentences=2)
    speak("according to wikipedia...")
    print(results)
    speak(results)

def AI():
    pass

if __name__ == '__main__':
    WishMe()

    speak("How can i help you sir")
    jokeCount = 0

    operate = 1

    talks = []

    j = jokes.jokeList()
    random.shuffle(j)

    while operate == 1:
        try:
            query = Hear().lower()
            talks.append(query)
            if "wikipedia" in query:
                jokeCount = 0
                try:
                    wiki(query, "wikipedia")
                except:
                    speak("sorry try again....")
            elif "who is" in query:
                jokeCount = 0
                wiki(query, "who is")

            elif "who i am" in query:
                jokeCount = 0
                speak("You are my creator , mister Nishaaan Singh ")
                print("You are my creator , mister Nishaaan Singh ")

            elif "youtube" in query:
                jokeCount = 0
                if 'youtube' in query and 'search' in query:
                    speak("Searching...")
                    print("Searching...")
                    if 'in youtube' in query:
                        query = query.replace('in', '')
                    query = query.replace('youtube', '')
                    query = query.replace('search', '')
                    webbrowser.get('chrome').open(r"https://www.youtube.com/results?search_query=" + query)
                elif 'open youtube' in query or 'launch youtube' in query:
                    speak("Launching youtube...")
                    print("Launching youtube...")
                    webbrowser.get('chrome').open("youtube.com")

            elif "google" in query:
                jokeCount = 0
                if 'google' in query and 'search' in query:
                    speak("Searching...")
                    print("Searching...")
                    if 'in google' in query:
                        query = query.replace('in', '')
                    pos = query.find('search')
                    query = query[pos:]
                    query = query.replace('google', '')
                    query = query.replace('search', '')
                    webbrowser.get('chrome').open(r"https://google.com/?#q=" + query)

                elif 'open google' in query or 'launch google' in query:
                    print('Launching google.com...')
                    speak("Launching google.com...")
                    webbrowser.get('chrome').open("google.com")

            elif 'open stackoverflow' in query or 'launch stackoverflow' in query:
                jokeCount = 0
                print('Launching stackoverflow...')
                speak('Launching stackoverflow...')
                webbrowser.get('chrome').open("stackoverflow.com")

            elif 'open twitter' in query or 'launch twitter' in query:
                jokeCount = 0
                print('Launching twitter...')
                speak('Launching twitter...')
                webbrowser.get('chrome').open("twitter.com")

            elif 'open gmail' in query or 'inbox' in query:
                jokeCount = 0
                print('Launching gmail.com...')
                speak("Launching gmail.com...")
                webbrowser.get('chrome').open("gmail.com")

            elif ('what' in query or 'tell' in query) and "the time" in query:
                jokeCount = 0
                tell_time()


            elif "open blender" in query or 'launch blender' in query:
                jokeCount = 0
                print('Launching blender...')
                speak("Launching blender...")
                os.startfile(r"C:\Program Files\Blender Foundation\Blender 2.83\blender.exe")
                operate = 0

            elif "open photoshop" in query or 'launch photoshop' in query:
                jokeCount = 0
                print('Launching photoshop..')
                speak("Launching photoshop..")
                os.startfile(r"E:\Adobe\Adobe Photoshop CS6 (64 Bit)\Photoshop.exe")
                operate = 0

            elif 'open valorant' in query or 'launch valorant' in query:
                jokeCount = 0
                print('Launching valorant..')
                speak("Launching valorant..")
                os.startfile(r"E:\Projects\PyCharm\Jarvix_punjabi\data\val.lnk")
                operate = 0

            elif 'open steam' in query or 'launch steam' in query:
                jokeCount = 0
                print('Launching steam..')
                speak("Launching steam..")
                os.startfile(r"F:\steam\Steam.exe")
                operate = 0

            elif 'siri' in query:
                jokeCount = 0
                speak('You cannot compare me with siri , she is fucking bitch ,while i was created by supreme '
                      'nishaaan singh')

            elif 'what' in query and 'i say' in query and len(talks) > 1:
                jokeCount = 0
                print('you said ' + talks[-2])
                speak('you said ' + talks[-2])

            elif 'do you know' in query:
                jokeCount = 0
                pos = query.find('do you know')
                query = query[pos:]
                query = query.replace('do you know', '')
                print('Sorry sir i do not know' + query + ' but i will learn it')
                speak('Sorry sir i do not know' + query + ' but i will learn it')

            elif 'female voice' in query:
                jokeCount = 0
                voices = engine.getProperty("voices")
                if engine.getProperty('voice') == voices[1].id:
                    speak('i am already female')
                else:
                    engine.setProperty('voice', voices[1].id)
                    speak('female voice activated')

            elif 'male voice' in query:
                jokeCount = 0
                voices = engine.getProperty("voices")
                if engine.getProperty('voice') == voices[0].id:
                    speak('i am already male')
                else:
                    engine.setProperty('voice', voices[0].id)
                    speak('male voice activated')

            elif 'your favourite thing' in query:
                jokeCount = 0
                print('my favourite thing is Python Language I like it very much')
                speak('my favourite thing is Python Language I like it very much')

            elif 'shutdown' in query:
                speak("Shutting Down")
                os.system("shutdown /s /t 1")

            elif ('tell' in query or 'want' in query) and 'joke' in query:
                if len(j) > 0:
                    print(j[-1])
                    speak(j[-1])
                    j.pop()
                    jokeCount = 1
                else:
                    jokeEnd = ["Sorry i do not know another joke", "Sorry I am ou of joke now"]
                    speak(random.choice(jokeEnd))

            elif ('another' in query or 'one more' in query) and jokeCount == 1:
                if len(j) > 0:
                    print(j[-1])
                    speak(j[-1])
                    j.pop()
                    jokeCount = 1
                else:
                    jokeEnd = ["Sorry i do not know another joke", "Sorry I am out of joke now"]
                    speak(random.choice(jokeEnd))

            elif 'spell' in query:
                print(spellings(query))
                speak(spellings(query))

            elif 'open calculator' in query:
                print('Launching Calculator...')
                speak('Launching Calculator...')
                os.startfile('calc.exe')

            elif 'phantom forces' in query:
                print('Launching Game...')
                speak('Launching Game...')
                webbrowser.get('n_chrome').open('https://www.roblox.com/games/292439477/Phantom-Forces?refPageId=b0c5dd2b-7327-4a3f-9650-f27d450a140c#!/about')
                operate = 0

            else:
                jokeCount = 0

            if "quit" in query or "bye-bye" in query:
                speak("Bye bye sir , see you again")
                speak("Have a nice day")
                operate = 0

        except Exception as e:
            print(e)
            pass
