# A place for me to play

# Character space:
alph = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

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

# Nice output:
print "..."
print "Plaintext:", plain
print "Shift:", shift
print "Ciphertext:", cipher
