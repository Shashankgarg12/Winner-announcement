import pyttsx3
engine = pyttsx3.init()
l=['shashank','garg','hari','om']
for i in l:
    engine.say(f'winner is {i}')
engine.runAndWait()