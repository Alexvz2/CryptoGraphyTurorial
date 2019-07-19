

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
    # if newloc >= 26:
    #     newloc -= 26 this helps go past 14 but still if it goes out of range we get an error therfore we use modulus
    str_out += alpha[newloc]
    print(newloc, str_out)


print("Obfuscated version:", str_out)

