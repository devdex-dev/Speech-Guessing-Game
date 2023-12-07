from random import randrange
import speech_recognition as sr
import pyttsx3
import pyaudio


r = sr.Recognizer()

# title
print("Guess The Fruit")
print('-----------------------')
print("Status: Listening.")
print('-----------------------')

# choices
print('Choices:')
list = ["apple", "grapes", "pineapple"]
for i in list:
    print(i)
print('-----------------------')

# Voice Instruction
engine2 = pyttsx3.init()
engine2.say("Guess The Fruit based on the choices")
engine2.runAndWait()

# Chooses word freom te list randomly
i = randrange(len(list))
word = list[i]

# checks and respond the the answer
def speak(answer):
    if(answer == word):
      engine1 = pyttsx3.init()
      engine1.say("That's  Correct")
      engine1.runAndWait()
      print("Result: Correct")
      print('-----------------------')
      print("Status: Not Currently Listening.")
    else:
     engine1 = pyttsx3.init()
     engine1.say("I get "+ answer +".  Wrong Guess.  the correct is "+ word)
     engine1.runAndWait()
     print("Result: Wrong")
     print("Correct:", word)
     print('-----------------------')
     print("Status: Not Currently Listening.")
     
# Utilization of Sytems microphone
with sr.Microphone() as source:
    
    # converts spoken words into audio file
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    
    # Converts audio file to text
    myText = r.recognize_google(audio)
    myText = myText
    
    print("\nI heard '"+ myText+"'"'\n')
    print('-----------------------')
# calls the 'speak' funtion
speak(myText)   
