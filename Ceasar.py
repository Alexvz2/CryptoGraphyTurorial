

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
length = len(alpha)

EType = input("type 1 for Cesar Encryption and 0 for ROT13:")
str_in = input("Enter message:")
shift_val = 13  if EType else int(input("Enter Shift Value:"))


n = len(str_in)
str_out = ""

for i in range(n):
    c = str_in[i]
    loc = alpha.find(c)
    print(i, c, loc)
    newloc = (loc + shift_val)%length
    str_out += alpha[newloc]
    print(newloc, str_out)


print("Obfuscated version:", str_out)





# Now, we decipher ther ceasar encryption

Ciphertext =  input("Enter the Ciphertext:")

n = len(Ciphertext)
secret = " "

for i in range(25):
    for l in range(n):
        c = Ciphertext[l]
        loc = alpha.find(c)
        newloc = (loc + i)%length
        secret += alpha[newloc]
    print(i, secret)
    secret = " "





