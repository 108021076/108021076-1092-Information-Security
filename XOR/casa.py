import sys

class Crypt:
    def __init__(self,key):
        self.key = key

    def encrypt(self,msg):
        key = (self.key)
        msglist = list(msg)
        msglen = len(msg)
        ciphertext = [''] * msglen
        for i in range(msglen):
            ciphertext[i] = chr(ord(msglist[i]))
            if ord(ciphertext[i]) >= 65 and ord(ciphertext[i]) <= 90:
                big = True
                little = False
            elif ord(ciphertext[i]) >= 97 and ord(ciphertext[i]) <= 122:
                big = False
                little = True

            ciphertext[i] = chr(ord(msglist[i]) + int(key))

            if big == True:
                if ord(ciphertext[i]) > 90 :
                    ciphertext[i] = chr(ord(ciphertext[i]) - 26)
            elif little == True :
                if ord(ciphertext[i]) > 122 :
                    ciphertext[i] = chr(ord(ciphertext[i]) - 26)

        return ''.join(ciphertext)

    def dencrypt(self,msg):
        key = (self.key)
        msglist = list(msg)
        msglen = len(msg)
        ciphertext = [''] * msglen
        for i in range(msglen):
            ciphertext[i] = chr(ord(msglist[i]))
            if ord(ciphertext[i]) >= 65 and ord(ciphertext[i]) <= 90:
                big = True
                little = False
            elif ord(ciphertext[i]) >= 97 and ord(ciphertext[i]) <= 122:
                big = False
                little = True

            ciphertext[i] = chr(ord(msglist[i]) - int(key))

            if big == True:
                if ord(ciphertext[i]) < 65 :
                    ciphertext[i] = chr(ord(ciphertext[i]) + 26)
            elif little == True :
                if ord(ciphertext[i]) < 97 :
                    ciphertext[i] = chr(ord(ciphertext[i]) + 26)
        return ''.join(ciphertext)

if __name__ == "__main__":

    print(sys.argv)
    if len(sys.argv) > 2:
        if sys.argv[1] == '-e':
            c = Crypt(sys.argv[2])
            print(c.encrypt(sys.argv[3]))
        elif sys.argv[1] == '-d':
            c = Crypt(sys.argv[2])
            print(c.dencrypt(sys.argv[3]))