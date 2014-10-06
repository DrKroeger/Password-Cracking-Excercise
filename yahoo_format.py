###########################################################
# Yahoo Password Cracking file
# Name: yahoo_format.py
# Author: Trevor Kroeger
# Date 9/19/2013
# Purpose: Format the plaintext yahoo passwords for
# submission
###########################################################
print ("\n\n")
# Open the Files
password = open('yahoo.txt', 'r')
passfile = open('yahoo_plaintext.txt', 'r+')

startline = "user_id   :  user_name  : clear_passwd : passwd"
endline = "4. Final Notes"
sw = 0
plaintext = (0,0,0)
# user_id   :  user_name  : clear_passwd : passwd
for line in password:
	if line.replace("\n", "") == endline:
		#print ("found it")
		sw = 0
	if (line != "\n") and (sw == 1):
		plaintext = line.split(":")
		#print (plaintext)
		passfile.write(line.replace("\n", "") + " " + plaintext[2].replace("\n","") + " 'yahoo.txt'\n")
	if line.replace("\n", "") == startline:
		print ("found it")
		sw = 1

# 4. Final Notes

###########################################################
#                           End                           #
###########################################################
