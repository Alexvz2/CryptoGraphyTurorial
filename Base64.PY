# Broken in sequences of six bits
# six bits encodes one single character
# 6 bits have 64 combinations, thus 64 characters
# A-Z for 0-25
# a-b for 26-51
# 0-9 for 52-61
# +,/ 62,63
#  Padding "=" uses null bytes, usde in case it doesnt use all characters

import base64

todo = input("Encode word or file:")

if (todo == "word"):
    str_in = input("Enter string to encode:")
    print("Output:", base64.b64encode(bytes(str_in, 'utf-8')))
else:
    file_in = input("Type the name of file to encode:") + ".exe"
    print("Encoding:" + " " + file_in)
    try:
        with open(file_in, "rb") as file:
            data = file.read()
            enData = base64.b64encode(bytes(data, 'utf-8'))
            print(enData)
    except IOError:
        print("Error: File does not exist or cannot be found...")
