Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import random

greetings = ['hola', 'hello', 'hi', 'Hi', 'hey!','hey']

question = ['How are you?','How are you doing?']
responses = ['Okay',"I'm fine", "I'm fine thanks, nice to be here with you"]

while True:
        userInput = raw_input(">>> ")
        if userInput in greetings:
                random_greeting = random.choice(greetings)
                print(random_greeting)
        elif userInput in question:
                random_response = random.choice(responses)
                print(random_response)
        else:
                print("I did not understand what you said")
