import json

# el usuario tiene dos preguntas con 3 opciones por pregunta
# la primera es si acerto la prediccion del tiempo
# a lo que puede respoder: 1 SI, 2 Mas frio, 3 Mas calor
# la segunda es si acerto la prediccion de la ropa
# a lo que puede responder: 1 SI, 2 Mas frio, 3 Mas calor

# se acierta la prediccion del tiempo 1
# se acierta la prediccion de la ropa 1
# NO SE HACE NADA

# se acierta la prediccion del tiempo 1
# tuvo frio 2
# se resta 0.5 al bias

# se acierta la prediccion del tiempo 1
# tuvo calor 3
# se le suman 0.5 al bias

# HIZO MAS CALOR 3
# se acierta la prediccion de la ropa 1
# se resta 0.2 al bias

# HIZO MAS CALOR 3
# tuvo frio 2
# se suma 0.4 al bias

# HIZO MAS CALOR 3
# tuvo calor 3
# se resta 0.4 al bias

# HIZO MAS FRIO 2
# se acierta la prediccion de la ropa 1
# se suma 0.2 al bias

# HIZO MAS FRIO 2
# tuvo frio 2
# se suma 0.4 al bias

# HIZO MAS FRIO 2
# tuvo calor 3
# se resta 0.4 al bias
JSON_PATH = r'C:\Users\agust\Desktop\MyCodes\CLIMA-TP-CAECE\userHistory.json'


def addUserInput(prediction, feel):
  file = open(JSON_PATH)
  userHistory = json.load(file)
  bias = userHistory['bias']

  if prediction == 1 and feel == 1:
    userHistory['bias'] = bias

  elif prediction == 1 and feel == 2:
    userHistory['bias'] = bias - 0.5

  elif prediction == 1 and feel == 3:
    userHistory['bias'] = bias + 0.5

  elif prediction == 2 and feel == 1:
    userHistory['bias'] = bias + 0.2

  elif prediction == 2 and feel == 2:
    userHistory['bias'] = bias + 0.4

  elif prediction == 2 and feel == 3:
    userHistory['bias'] = bias - 0.4

  elif prediction == 3 and feel == 1:
    userHistory['bias'] = bias - 0.2

  elif prediction == 3 and feel == 2:
    userHistory['bias'] = bias + 0.4

  elif prediction == 3 and feel == 3:
    userHistory['bias'] = bias - 0.4

  with open(JSON_PATH, "w") as outfile:
    json.dump(userHistory, outfile)
  file = open(JSON_PATH)
  userHistory = json.load(file)
  bias = userHistory['bias']
  
  return int(bias)