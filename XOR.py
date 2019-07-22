# XOR like encryption



import codecs

text = input("Enter Text: ")
key =  input("Enter Key: ")
n = len(text)

cipher = ""
for i in range(n):
    t = text[i]
    k = key[i%len(key)]
    x = ord(k) ^ ord(t)
    cipher += chr(x)
print(text, key , codecs.encode(bytes(cipher, 'utf-8'), 'hex_codec'))