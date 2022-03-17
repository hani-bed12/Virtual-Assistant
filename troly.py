from email.mime import audio
import speech_recognition
import pyttsx3
from datetime import date, datetime

robot_ear = speech_recognition.Recognizer()
robot_brain = ""
robot_mouth = pyttsx3.init()


while True:
    ###### Nghe ##############
    with speech_recognition.Microphone() as mic:
        print("Robot: I'm listening")
        audio = robot_ear.listen(mic)

    try:
        you = robot_ear.recognize_google(audio)
    except:
        you = ""
        
    print("You: " + you)

    ######## Xử lý ##############
    if you == "":
        robot_brain = "I can't hear you, try again"
    elif "today" in you:
        today = date.today()
        robot_brain = today.strftime("%B %d, %Y")
    elif "time" in you:
        now = datetime.now()
        robot_brain = now.strftime("%H hours %M minutes %S seconds")
    elif you == "hello":
        robot_brain = "Hello Jane"
    elif "bye" or "quit" in you:
        robot_brain = "Bye Bye"

        print("Robot: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    else:
        robot_brain = "I don't understand"
        
    ######## Nói ##############
    print("Robot: " + robot_brain)
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()

