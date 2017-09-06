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

		def if_loop():
			if prompt == "Y" or prompt == "y":	
				genpass()
		
			elif:
				if prompt == "N" or prompt == "n":
					print ("Exiting") 
					exit()
			
			else:
				if_loop()
				
	
			
			
	
genpass()
		
