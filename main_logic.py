import datetime
import os
import time
import subprocess
import webbrowser
import re   
import Text_speech_converter as ts
import cv
import mail_skill as m
import open_ai as ai
import weather_pred as weather
 
camera_words = ['open camera','take a picture','take a photo']
timed_words = ['in', 'after']

open_pattern = r"open (.+)"
mail_pattern = r"to (.+)"

def decideAction(statement):
    for i in camera_words:
        if i in statement:
            for j in timed_words:
                if j in statement:
                    number_str = ""

                    for char in statement:
                        if char.isdigit():
                            number_str += char

                    if number_str:
                        number = int(number_str)
                
                    ts.speak(f"I have opened camera for you and will take a picture in {number} seconds")
                    cv.takePicture(number)
                    return "I have opened camera for you and will take a picture in "+str(number)+"seconds"
    
                
            ts.speak("I have opened camera for you, press spacebar to click a picture and q to exit")
            cv.takePicture(0)
            return "I have opened camera for you, press spacebar to click a picture and q to exit"
    
    if 'open youtube' in statement:
        webbrowser.open_new_tab("https://www.youtube.com")
        ts.speak("youtube is open now")
        return "youtube is open now"
    
    elif 'open google' in statement:
        webbrowser.open_new_tab("https://www.google.com")
        ts.speak("Google chrome is open now")
        time.sleep(5)

    elif 'open gmail' in statement:
        webbrowser.open_new_tab("gmail.com")
        ts.speak("Google Mail open now")
        time.sleep(5)
    
    elif 'send mail' in statement:
        # if re.match(mail_pattern, statement):
        #     entity = re.match(mail_pattern, statement).group(1)
        m.sendEmail("","","")
    
    elif 'screenshot' in statement:
        cv.takeSS()
        return "screenshot has been taken"
    
    elif 'weather' in statement:
        # weather_pattern = r"in (.+)"
        # city = re.match(weather_pattern, statement).group(1)
        city="chennai"
        lst = statement.split()
        for i in range(len(lst)):
            if lst[i] == 'in':
                city = lst[i+1]

        res = weather.tellWeather(city)
        ans = ai.processCommand(res)
        return ans

    
    else:
        res = ai.processCommand(statement)
        return res    

