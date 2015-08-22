# Ceaser Cipher Python implementation
# Brandon Fosso
# 18/9/2015

import time

# Character space:
small_alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
big_alph = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

plain = raw_input('Enter your plain text: ') # User Plaintext

shift = int(raw_input('Enter the desired shift: ')) # User shift, convert to int

cipher = "" # Ciphertext starts as empty string

for i in plain:
	if i in alph:
		cipher += alph[(alph.index(i) + shift) % len(alph)] 
		# Determine character index, add shift, wrap, determine new character
	else:
		cipher += i # Leave non-letter characters alone

	# print cipher # Watch it being built up 

# Thinking delay:
time.sleep(1)
print "."
time.sleep(1)
print " ."
time.sleep(1)
print "  ."
time.sleep(1)

# Nice output:
print "Plaintext:", plain
print "Shift:", shift
print "Ciphertext:", cipher
