import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia as wiki
import webbrowser 
import os
import smtplib
import wolframalpha

engine = pyttsx3.init() #CREATING VOICE ENGINE
voices = engine.getProperty('voices')
engine.setProperty('voice' , voices[1].id) #ASSIGNING VOICE
engine.setProperty('rate' , 180) #VOICE RATE

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme(): #WISHING USER ACCPRDING TO TIME
    hour=int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        print("Good Morning!")
        speak("Good Morning!")
    elif(hour>=12 and hour<18):
        print("Good Afternoon!")
        speak("Good Afternoon!")
    else:
        print("Good Evening!")
        speak("Good Evening!")
    print("How can I Help You")
    speak(" How can I Help You")

def takecommand(): #TAKING VOICE INPUT AND RETURNING THE QUERY AS STRING
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)
        

    try:
        print("Recognizing..")
        query=r.recognize_google(audio,language='en-in')
        print(f"User Said: {query}\n")

    except Exception as e:
        
        print("Say That Again Please...")
        speak("Say That Again Please...")
        return "None"
    
    return query

def sendEmail(to, content): #SENDING EMAIL
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login('shreysingh4999@gmail.com','')
    server.sendmail('shreysingh4999@gmail.com',to,content)
    server.close()

if __name__ == "__main__":
    print("Hello sir")
    speak("Hello sir")
    
    wishme()
    while True:
        query = takecommand().lower()
        #code to execute task
        if 'wikipedia' in query:
            speak("Wait Searching wikipedia...")
            query=query.replace('wikipedia',"")
            results= wiki.summary(query,sentences=2)
            speak("According To wikipedia")
            print(results)
            speak(results)
            
        elif 'youtube' in query:
            webbrowser.open('youtube.com')
            speak("Opening Youtube")
            
            
        elif 'google' in query:
            webbrowser.open('google.com')
            speak("opening google")

        elif 'news' in query:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            
                                           
        elif 'open gmail' in query:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            
        elif 'ask' in query:
            speak("I can answer to computational and geographical questions as well")
            ques=takecommand()
            app_id="TVTY9H-QGEXRUXLUG "
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(ques)
            answer = next(res.results).text
            print(answer)
            speak(answer)

        elif 'search'in query:
             query = query.replace("search", "")
             webbrowser.open_new_tab(query)

            
            
            
        #elif 'play music' in query:
            # music_dir //enter music directory
            # songs=os.listdir(music_dir)
        elif 'time' in query:
            strtime=datetime.datetime.now().strftime("%H hours %M minutes %S seconds")
            speak(f"sir the time is {strtime}")
        elif 'pubg' in query:
            path = "D:\\PUBGLite\\Launcher.exe"
            os.startfile(path)
        elif 'email' in query:
            try:
                speak("what should i say..")
                content=takecommand()
                to = "raiankur658@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("sorry sir im not able to send an email")
        elif 'thank you' in query:
            speak("Welcome Sir")




