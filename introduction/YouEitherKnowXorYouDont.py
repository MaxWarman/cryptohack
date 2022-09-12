"""
I've encrypted the flag with my secret key, you'll never be able to guess it.

Remember the flag format and how it might help you in this challenge!

0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104
"""

from crypty import *

cipherTextHex = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
cipherTextBytes = hexToBytes(cipherTextHex)

wanted = "crypto{}"
wantedBytes = stringToBytes(wanted)

sampleBytes = cipherTextBytes[:len(wanted)-1]
sampleBytes.append(cipherTextBytes[-1])

guessedKey = ""
for i in range(len(wanted)):
	for key in range(256):
		if sampleBytes[i] ^ key == wantedBytes[i]:
			guessedKey += chr(key)
			break

guessedKeyBytes = stringToBytes(guessedKey)
flag = bytesToString(xorBytes(cipherTextBytes, guessedKeyBytes))

print(flag)

###
###	Flag: crypto{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll}
###