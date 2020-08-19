import pyttsx3
import os 
voicex=pyttsx3.init()
a=voicex.setProperty('rate',160)
pyttsx3.speak('To execute any query Choose the Option 1 or Option 2 to exit the program')
while 1:
	a=input('\n \t Option 1: Wirte your qurey here \n \t or \n \t Option 2: To exit write exit \n \t')
	a=a.lstrip()
	a=a.rstrip()
	if a != 'exit':
		os.system('{b}'.format(b=a))
	elif a=='exit':
		break