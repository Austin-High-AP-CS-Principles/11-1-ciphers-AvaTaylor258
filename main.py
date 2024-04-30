# Caesar Cipher Encrypt/Decrypt
def caesar(message, shift):
	result = ""
	dict = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	
	for i in message.upper():
		# index = dict[i]
		index = dict.find(i)
		shifted_index = (index * shift) % 26
		result += dict[shifted_index]
	return result


#Vigenere Encrypt
def vigenere_encrypt(text, key):
	count = 0
	result = ""
	dict = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	for i in text.upper():
		j = key[count]
		index = dict.find(i)
		shifted_index = (index * dict.find[j]) % 26
		result += dict[shifted_index]
		if count > len(key):
			count = 0
		else:
			count += 1


# Vigenere Decrypt
def vigenere_decrypt(text, key):
	count = 0
	result = ""
	dict = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	for i in text.upper():
		j = key[count]
		index = dict.find(i)
		shifted_index = (index / dict.find[j]) % 26
		result += dict[shifted_index]
		if count > len(key):
			count = 0
		else:
			count += 1