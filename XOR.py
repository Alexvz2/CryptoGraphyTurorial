# XOR like encryption



import codecs


def Encode():
    text = input("Enter Text: ")
    key =  input("Enter Key: ")
    n = len(text)

    cipher = ""
    for i in range(n):
        t = text[i]
        k = key[i%len(key)]
        x = ord(k) ^ ord(t)
        cipher += chr(x)
    print(text, key , cipher, codecs.encode(bytes(cipher, 'utf-8'), 'hex_codec'))
    return True

def Decode():
    text =  input("Enter Text:")
    n = len(text)

    for k in "0123456789":
        decipher = ""
        for i in range(n):
            t = text[i]
            x = ord(k) ^ ord(t)
            decipher += chr(x)
        print(k, decipher)
    return True

if __name__ == "__main__":
    DorE = input("Encode or Decode in XOR (E/D):  ")
    Encode() if DorE == "E" else Decode()