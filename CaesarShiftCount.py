alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

enmsg = input("What is the encrypted message: ")
cadd = 0

# counts the number of each letter in enmsg
def counter():

    for i in range(25):
        
        for j in range(len(enmsg)):
            count = enmsg.count(alphabet[i])
        
        print(alphabet[i] + " appears " + str(count) + "times.")


def decrypter():
    for i in range(25):
        posword = ""
        cadd += 1
        for j in range(len(enmsg)):
            if enmsg[j] == " ":
                posword += " "
            for k in range(len(alphabet)):
                if enmsg[j] == alphabet[k]:
                    posword += alphabet[k-cadd]
    print(posword)

counter()
