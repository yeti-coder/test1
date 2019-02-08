

def reverseword(sentence):
    wordlist=[]
    element=""
    for i in sentence:
        if i==" ":
            wordlist.append(element)
            element=""
        else:
            element+=i
    wordlist.append(element)
    wordlist=wordlist[::-1]
    return (" ".join(wordlist))

print(reverseword(input("Enter sentence")))

#
# def reverseWord(w):
#     return ' '.join(w.split()[::-1])