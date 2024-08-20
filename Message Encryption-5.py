import random as rd
a = input("Enter the message: ")
print("1.Encrypt\n2.Decrypt")
b = int(input("Select the operation or 0 to exit: "))
words = a.split(" ")
random = ["AsFaw","VgFAs","gFueS","dUSfe","fHeds","ufEDe"]
random1 = ["guQad","TfaWG","yGFda","feWHA","etREf","gDFKE"]
try:
    if(b==1):
        coding = True
        if(coding):
            nwords =[]
            for word in words:
                if(len(word)>=3):
                    r1 = rd.choice(random)
                    r2 = rd.choice(random1)
                    anew = r1 + word[2:] + word[0:2] + r2
                    nwords.append(anew)
                else:
                    nwords.append(word[::-1])
            print(" ".join(nwords))
    elif(b==2):
        nwords = []
        for word in words:
            if (len(word)>=3):
                anew = word[5:-5]
                anew = anew[-2] + anew[-1] + anew[0:-2]
                nwords.append(anew)
            else:
                nwords.append(word[::-1])
        print(" ".join(nwords))
    elif(b==0):
        exit()
except:
    print("Invalid Input")
