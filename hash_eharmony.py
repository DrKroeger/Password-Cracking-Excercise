###########################################################
# EHarmony Password Cracking file
# Name: hash_eharmony.py
# Author: Trevor Kroeger
# Date 9/19/2013
# Purpose: Use a dictionary attack to crack the passwords
# in the eharmony passwords.txt file.
###########################################################
import hashlib
import binascii
import codecs

print ("\n\n")
#Open the files for the Program
password = open('eharmony passwords.txt', 'r')
passref = open('rockyou_utf8.txt', 'r')
passfile = open('eharmony_plaintext.txt', 'r+')

passmd5 = set()
#Load the Hashed Passwords into a Set
for line in password:
  passmd5.add(line.replace("\n","")) 

#Hash the Dictionary and Compare to the eHarmony Password Set
for line in passref:
  # Get the line and remove the newline character and
  #make all of the values uppercase
  plaintxt = line.replace("\n","").upper()
  verb = hashlib.md5(plaintxt) # Hash the dictionary word
  #print(verb.hexdigest()+ " " + plaintxt + " 'hash.txt'\n")
  if verb.hexdigest() in passmd5:
    #If the hash value is in the table print in the plain text file
    passfile.write(verb.hexdigest()+ " " + plaintxt + " 'eharmony passwords.txt'\n")
    print(verb.hexdigest()+ " " + plaintxt + " 'hash.txt'\n")

print ("\n\n")
###########################################################
#                           End                           #
###########################################################