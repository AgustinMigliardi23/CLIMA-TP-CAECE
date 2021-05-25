import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
import datetime as dt
import arrange_data

def speak(text):
    tts = gTTS(text=text, lang="es")
    fileName = "prueba.mp3"
    tts.save(fileName)
    playsound.playsound(fileName)
# tomar datos, promedios de tempreratura
# asignarle un valor a las prendas
# seleccionar que prenda va con cada temp
# armar una frase y que la diga el tts
def getAndParseData():
    forecast = arrange_data.arrange_data()

    today = dt.datetime.now()
    tomorrow = dt.datetime(today.year, today.month, today.day + 1)
    for tempDay in forecast:
        for tempHour in tempDay:
            if tomorrow.day == tempHour[0].day:
                print(tempHour[1])





getAndParseData()