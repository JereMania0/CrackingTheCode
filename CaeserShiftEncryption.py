alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

msg = input("What is message you want to encrypt?: ")
shift = int(input("How much do you want to shift your message?: "))
enmsg = ""

for j in range(len(msg)):
        if msg[j] == " ":
            enmsg += " "
        for k in range(len(alphabet)):
            if msg[j].upper() == alphabet[k]:
                enmsg += alphabet[(alphabet.index(msg[j].upper()) + shift) % 26]
    


print(enmsg.upper())