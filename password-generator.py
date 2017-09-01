#!/bin/python3
import random

chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcefghijklmnopqrstuvwxyz1234567890'
password = ''

range_input = int(input("How long do you want your password to be ?: "))

for c in range(range_input):
	password += random.choice(chars)
print (password)


