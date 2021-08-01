import speech_recognition
import pyttsx3
from datetime import date, datetime
import webbrowser
robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""
voices = robot_mouth.getProperty('voices')
robot_mouth.setProperty('voice', voices[1].id)
while True:
	with speech_recognition.Microphone() as mic:
		robot_ear.adjust_for_ambient_noise(mic)
		print("Robot: I'm Listening")
		audio = robot_ear.record(mic, duration=3)
	print ("Robot:...")
	try:
		you = robot_ear.recognize_google(audio)
	except:
		you = ""

	print("You: " + you)

	if you == "":
		robot_brain = "I can't hear you, say again"
	elif "hello" in you:
		robot_brain = "hello Quoc cay, How can I help you?"
	elif "my friend" in you:
		robot_brain = "Trong Ninh"
	elif "Facebook" in you:
		webbrowser.open('https://www.facebook.com/',new=2)
		robot_brain = "Here you are!"
	elif "your name" in you:
		robot_brain = "My name is Seri"
	elif "your birthday" in you:
		robot_brain = " Tuesday, July 27,2021"

	elif "today" in you:
		today = date.today()
		robot_brain = today.strftime("%B %d, %Y")
	elif "time" in you:
		now = datetime.now()
		robot_brain = now.strftime("%H hours %M minutes %S seconds")
	elif "handsome" in you:
		robot_brain = "It is You"
	elif "bye" in you:
		robot_brain = "bye Quoc Cay"
		print ("Robot:" + robot_brain)
		robot_mouth.say(robot_brain)
		robot_mouth.runAndWait()
		break
	else : 
		robot_brain = "I can't answer the question!"
	print ("Robot:" + robot_brain)
	robot_mouth.say(robot_brain)
	robot_mouth.runAndWait()