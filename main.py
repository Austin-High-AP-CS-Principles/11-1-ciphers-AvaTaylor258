# Caesar Cipher Encrypt/Decrypt
def caesar(message, shift):
	result = ""
	dict = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	
	for i in message.upper():
		index = dict.find(i)
		shifted_index = (index * shift) % 26
		result += dict[shifted_index]
	return result


#Vigenere Encrypt
def vigenere_encrypt(text, key):
	key_repeated = (key * (len(text) // len(key))) + key[:len(text) % len(key)]
	result = ""
	dict = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
	text = text.upper()
	
	for i in range(len(text)):
		shift = ord(key_repeated[i].upper()) - ord('A')
		result += chr((ord(text[i]) + shift - ord('A')) % 26 + ord('A'))
		
		# j = key[count]
		# index = dict.find(i)
		# shifted_index = (index * dict.find(j)) % 26
		# result += dict[shifted_index]
		# if count >= len(key):
		# 	count = 0
		# else:
		# 	count += 1
	return result


# Vigenere Decrypt
def vigenere_decrypt(text, key):
	key_repeated = (key * (len(text) // len(key))) + key[:len(text) % len(key)]
	result = ""
	dict = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
	text = text.upper()
	
	for i in range(len(text)):
		shift = ord(key_repeated[i].upper()) - ord('A')
		result += chr((ord(text[i]) + shift - ord('A')) % 26 + ord('A'))
		
		# j = key[count]
		# index = dict.find(i)
		# shifted_index = (index * dict.find(j)) % 26
		# result += dict[shifted_index]
		# if count >= len(key):
		# 	count = 0
		# else:
		# 	count += 1
	return result