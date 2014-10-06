###########################################################
# formspring Password Cracking file
# Name: hash.py
# Author: Trevor Kroeger
# Date 9/19/2013
# Purpose: Use a dictionary attack to crack the passwords
# in the formspring.txt file.
###########################################################
import hashlib
import binascii
import codecs

print ("\n\n")
password = open('formspring.txt', 'r')
passref = open('rockyou_utf8.txt', 'r')
passfile = open('formspring_plaintext.txt', 'r+')

passmd5 = set()
one = 0x30
two = 0x30

#Load the Hashed Passwords into a Set
for line in password:
	passmd5.add(line.replace("\n","")) 

#Hash the Dictionary and Compare to the eHarmony Password Set
# The two while loops to cycle through the Salt
while (two <= 57):
	while (one <= 57):
		for line in passref:
			#Take each line of plaintext and add the salt to it.
			plaintxt = chr(one) + chr(two) + line.replace("\n","")
			#Hash the plaintext and salt
			verb = hashlib.sha256(plaintxt)
			#Check to see if the hashed plaintext and salt are in the formspring file
			#If they are print them to the output file
			if verb.hexdigest() in passmd5:
				passfile.write(verb.hexdigest()+ " " + line.replace("\n","") + " 'formspring.txt'\n")
				#print("Got One")
		passref.seek(0,0)
#Preform Salt incrementation
		one = one + 1
	two = two + 1
	one = 0x30

print ("\n\n")
###########################################################
#                           End                           #
###########################################################