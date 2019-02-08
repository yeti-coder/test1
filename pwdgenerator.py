import random
def main():
    chartype={1:"Lowercase",2:"Uppercase",3:"Integer",4:"symbol"}
    alphabet="abcdefghijklmnopqrstuvwxyz"
    symbols=("~","!","#","$")
    pwd=""
    for i in range(random.randint(6,14)):
        selecttype=random.randint(1,4)

        if selecttype==3:
            pwd+=str(random.randint(0,9))
        elif selecttype==4:
            pwd+=symbols[random.randint(0,3)]
        elif selecttype==1:
            pwd+=alphabet[random.randint(0,len(alphabet)-1)]
        else:
            pwd+=alphabet[random.randint(0,len(alphabet)-1)].upper()

    print(pwd)
main()