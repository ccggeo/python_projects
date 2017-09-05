#!/bin/python3
import random

def genpass():


		chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcefghijklmnopqrstuvwxyz1234567890'
		password = ''

		range_input = int(input("How long do you want your password to be ?: "))

		for c in range(range_input):
			password += random.choice(chars)
		print (password)
	
		prompt = input("Repeat? [Y] or [N]")


		print (prompt)
		
		if prompt.upper() == "Y":	
			genpass()
		
		else:	
			exit()
	
genpass()
		
#answer = raw_input("Is the information correct? Enter Y for yes or N for no")
#if answer.upper() == 'Y':
 #   print("this will do the calculation"):
#else:
 #   exit()
		
		
		

