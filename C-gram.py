text = input("Enter the sentence:")
n=2
def generate_ngrams():
    words = text.split()
    output = []  
    for i in range(len(words)-n+1):
        output.append(words[i:i+n])
    #return output
    print(output)


generate_ngrams()
#print(output)


# [['this', 'is'], ['is', 'a'], ['a', 'sample'], , ['sample', 'text']] 
