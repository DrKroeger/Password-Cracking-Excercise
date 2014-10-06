README for Password Cracking Repository
By: Trevor Kroeger
Python 2.7.5
*******************************************************************************
USE THESE FILES RESPONSIBLY... CRACKING PASSWORDS IS ILLEGAL AND USE OF THESE
FILES/PROGRAMS IS NOT INTENDED. 
*******************************************************************************
This is my first substantial exercise in python programming.

Description:
This is a password cracking exercise preformed for a course Information
Security & Privacy. The idea is to use a dictionary attack against the leaked
password files to determine what password was used. The leaked lists are
provided without the username association.

Process Used for Determining Plaintext:

For the plain text within the yahoo.txt I extracted it from the file using a
python program to get it into the format needed for submission  for the
assignment.
I did consider a brute force tactic for decoding passwords with less than 6
characters and did implement such a program to learn some python programming
however I did realize how inefficient this process was and abandoned the
process very quickly.
To determine the plain text of the two hashed lists I decided to perform a
dictionary attack. I downloaded the rockyou.txt list of passwords to perform
this method (http://www.skullsecurity.org/wiki/index.php/Passwords). I take the
hashed passwords from the .txt files and load them into a set. Then I compute
the hashes of each of the lines of the lines in my word list and see if they
are in the set of hashed passwords. Also when decoding eharmony file I found
help with it online (https://www.christophertruncer.com/eharmony-password-cracking-with-pipal-analysis/).
This site did a pipal analysis of the passwords which told me that all of the
passwords were uppercase and some fun facts about different things amongst the
password set such as the percentage that was stringdigit, digitstring, or all
string. This proved to be crucial for decoding the passwords as none of my
dictionary words were in uppercase. It’s another thing to keep in mind if I am
trying to crack other passwords.
For the formspring passwords I preformed the same type of process however I had
to add code to perform the salting before each of the passwords. I appended
values from 00 to 99 to the beginning of the plaintext password and followed
the same process that I used for the eharmony passwords. Salting definitely
made this password list harder for me to determine and it has taken a lot more
time to determine more of the passwords from the list. If we hadn’t been given
the information about the salt I’m not sure I would’ve guessed it on my own and
I would’ve maybe got a few passwords on my own but nowhere near the amount that
I did get when given that information. Salting seems to be very beneficial if it
can be done appropriately. I should note that I didn’t include the Salt values
in my print out, which I realize I should have otherwise you cannot get to the
password readily. You have to rehash and look for the correct salt. I was
following the format for submission with a space separating the encoded
password, the plaintext password and the file from which the password was from.

Next Steps:
If I were to continue the exercise to determine even more of the plaintext
passwords I think that my first step would be to expand my dictionary of words.
There were several other lists online that could’ve been added to my list. I
also could have started to combine words in the list to create new patterns
to check against. I could’ve also started to preform alpha numeric or symbolic
replacement (i.e. replacing the letter L with 1 or replacing S with $). Also
adding a numerical value to the beginning or end of the passwords would’ve
been helpful due to the fact that the pipal analysis of the eharmony
passwords showed that a majority of them are digit-string or string-digit
passwords. If I was to continue to crack passwords on a large level I could
create a comprehensive rainbow table for the hashes. I could compute millions
of hashes and keep the result to check against later. The advantage associated
with this that you no longer have to compute the hashes you just have to look
at the provided hash and determine if it is in memory.


The following are the files needed to crack each of the different password files:

YAHOO: Plaintext Passwords
yahoo.txt <- Plaintext Password List
yahoo_format.py <- Formatting program
yahoo_plaintext.txt <- This is where the plaintext passwords are

eHarmony: MD5 Hash
eharmony passwords.txt <- Encoded Passwords
rockyou_utf8.txt <- Word List
hash_eharmony.py <- Dictionary attack program
eharmony_plaintext.txt <- Plain text Passwords

formspring: sha-256 salted
formspring.txt <- Encoded Passwords
rockyou_utf8.txt <- Word List
hash.py <- Dictionary Attack Program
formspring_plaintext.txt <- Plaintext Passwords