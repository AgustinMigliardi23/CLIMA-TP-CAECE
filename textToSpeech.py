import os
import time
import datetime as dt
import arrange_data
import userInput

def getPhrase(prediction, feel):
    conditions = getAndParseData()
    code = 0
    if conditions[1] > 61:
        code = getClothesCode(conditions[0], True, False, prediction, feel)
    elif conditions[2] == "Despejado":
        code = getClothesCode(conditions[0], False, True, prediction, feel)
    else:
        code = getClothesCode(conditions[0], False, False, prediction, feel)
    if code == 1:
        return "Deberias salir sin ropa ( ͡° ͜ʖ ͡°)"
    elif code == 2:
        return "Deberias usar gorra, remera manga corta, pantalones cortos y ojotas."
    elif code == 3:
        return "Deberias usar gorra, remera manga corta, pantalones largos y zapatillas."
    elif code == 4:
        return "Deberias usar remera manga larga, un buzo, pantalones largos y zapatillas."
    elif code == 5:
        return "Deberias usar remera manga larga, un buzo, una campera, pantalones largos y zapatillas."
    elif code == 6:
        return "Deberias usar remera termica, un buzo, pantalones largos y zapatillas y unos guantes."
    elif code == 7:
        return "Deberias usar remera termica, un buzo, pantalones termicos y botas y unos guantes."
    elif code == 8:
        return "Deberias salir sin ropa ( ͡° ͜ʖ ͡°) y un paraguas."
    elif code == 9:
        return "Deberias usar gorra, remera manga corta, pantalones cortos, ojotas y un paraguas."
    elif code == 10:
        return "Deberias usar gorra, remera manga corta, pantalones largos, zapatillas y un paraguas"
    elif code == 11:
        return "Deberias usar remera manga larga, un buzo, un piloto, pantalones largos, zapatillas y un paraguas."
    elif code == 12:
        return "Deberias usar remera manga larga, un buzo, una campera, un piloto, panralones largos, zapatillas y un paraguas."
    elif code == 13:
        return "Deberias usar remera termica, buzo, campera, un piloto, pantalones largos, zapatillas, guantes y un paraguas."
    elif code == 14:
        return "Deberias usar remera termica, buzo, campera, un piloto, pantalon termico, botas, guantes y un paraguas."
    elif code == 15:
        return "Deberias usar remera manga corta, pantalon corto y ojotas."

def getClothesCode(temp, isRaining, clearSky, prediction, feel):
    code = 0
    bias = userInput.addUserInput(prediction, feel)
    if temp >= 50:
        code = 1
    elif temp < 50 and temp >= 25:
        if clearSky:
            code = 2
        else:
            code = 15
    elif temp < 24 and temp >= 16:
        code = 3
    elif temp < 16 and temp >= 12:
        code = 4
    elif temp < 12 and temp >= 6:
        code = 5
    elif temp < 6 and temp >= 0:
        code = 6
    elif temp < 0:
        code = 7
    
    if (isRaining):
        code + 7
    
    if bias > 0 and (code == 7 or code == 14 or code == 15):
        return code
    elif bias < 0 and (code == 1 or code == 8 or code == 15):
        return code
    else:
        return code + bias

def getAndParseData():
    forecast = arrange_data.arrange_data()

    today = dt.datetime.now()
    tomorrow = dt.datetime(today.year, today.month, today.day + 1)
    days = []
    for tempDay in forecast:
        for tempHour in tempDay:
            if tomorrow.day == tempHour[0].day:
                days.append(tempHour)
    rainChances = get_rain_chances(days)
    temperature = getTemp(days)
    sky = getSky(days)
    return temperature, rainChances, sky

def getSky(days):
    sky = 0
    for day in days:
        if day[3][0] == "Despejado":
            sky += 1
        else:
            sky += 3
    if sky >= 4:
        return "Nublado"
    else:
        return "Despejado"

def getTemp(days):
    temperature = 0
    for day in days:
        temperature += int(day[1][1])
    temperature = temperature / len(days)
    return round(float(temperature),2)

def get_rain_chances(days):
    humidity = float(get_humidity(days))
    sky_desc = get_sky(days)

    sky_const = 0
    humidity_const = 0
    bias = 25

    sky = sky_desc.split(",")
    if sky[0] == "Despejado":
        sky_const = 0
        bias = 0
    elif sky[1] == " con pocas nubes":
        sky_const = 0.5
    elif sky[1] == " con nubes aisladas":
        sky_const = 0.8
    elif sky[1] == " totalmente nublado":
        sky_const = 1.1
    
    if humidity > 50:
        humidity_const = 0.6
    elif humidity > 70:
        humidity_const = 0.8
    else:
        humidity_const = 1
    
    return float(round(sky_const*humidity_const*humidity + bias, 2))

def get_humidity(days):
    humidity = 0
    for day in days:
        humidity += int(day[2])
    humidity = humidity / len(days)
    return str(humidity)

def get_sky(days):
    sky = [0, 0, 0]
    shorty = [0, 0]
    final = ""
    
    for day in days:
        skies = day[3][1]
        if skies == "pocas nubes":
            sky[0] += 1
        elif skies == "ninguna nube":
            sky[0] += 1
        elif skies == "nubes aisladas":
            sky[1] += 1
        elif skies == "muchas nubes":
            sky[2] += 1
        elif skies == "nubes dispersas":
            sky[1] += 1
        short = day[3][0]
        if short == "Despejado":
            shorty[0] += 1
        elif short == "Nublado":
            shorty[1] += 1
    
    if shorty.index(max(shorty)) == 0:
        final += "Despejado, "
    else:
        final += "Nublado, "
    if sky.index(max(sky)) == 0:
        final += "con pocas nubes"
    elif sky.index(max(sky)) == 1:
        final += "con nubes aisladas"
    else:
        final += " totalmente nublado"
    return final


def runShow():
    print('La prediccion del tiempo de ayer fue correcta? 1- SI, 2- Hizo mas frio, 3- Hizo mas calor')
    prediction = input()
    print('La ropa recomendada de ayer fue correcta? 1- Si, 2- Tuve frio, 3- Tuve calor')
    feel = input()
    prediction = int(prediction)
    feel = int(feel)
    phrase = getPhrase(prediction, feel)
    print(phrase)

runShow()