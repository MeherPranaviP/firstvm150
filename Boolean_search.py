#Import all required packages
import os
import csv
import pandas as pd
#import nltk
#from nltk.corpus import stopwords
#from nltk.tokenize import word_tokenize
import glob
def createSearch():
    fileList = glob.glob('*.csv')
    #getting the current directory. keep record of initial staus of user
    #cwd = os.getcwd()
    #indx = 'C:\\Users\\Pranavi\\Documents\\sem-2\\Unstructured Data\\test_index_output'
    #changing directory to one passed as argument to reference files. no need to write the paths again
    #os.chdir(indx)
    #getting files in the directory
    #fileList = os.listdir(indx)
    result = {}
    r = {}
    #file = 'C:\\Users\\Pranavi\\Documents\\sem-2\\Unstructured Data\\Assignment-2\\elasticcommands.txt'
    for outfile in fileList:
        data = pd.read_csv(outfile).to_dict(orient="row")
    #Keyboard Input for the Boolean search Query
    query = input("Enter the query: ")
    query = query.lower()
    query = query.strip()
    wordList = query.split()
    searchWord = [x for x in wordList if x not in ['and','or']]
    operation = [x for x in wordList if x in ['and','or']]
    print(operation)
    searchIndex = [searchWord.index(x) for x in searchWord ]
    #match the query tokens and index tokens
    for i in searchIndex:
        match = next((l for l in data if l['word'] == searchWord[i]),None)
        #print(match['fileNames'])
        Docs = match['fileNames']
        posindex = match['positionIndex']
    #Initialisation of Dictionary
    D = []
    
    for i in searchIndex:
        match = next((l for l in data if l['word'] == searchWord[i]),None)
        Docs = match['fileNames']
        posindex = match['positionIndex']

    #print(Docs)
        if i not in result.keys():
            result[searchWord[i]] = {}
            #result[searchWord[i]]['searchWord'] = []
            result[searchWord[i]]['DocNames'] = []
            result[searchWord[i]]['posIndex']=[]
            r['searchWord'] = []
            r['DocNames'] = []
            r['posIndex']=[]
        #result[word]['searchWord'] = [searchWord]
        
      
        result[searchWord[i]]['DocNames'] = [Docs]
        result[searchWord[i]]['posIndex'] = [posindex]
        r['DocNames'] = [Docs]
        r['posIndex'] = [posindex]

    
        #print(result['posIndex'])
#print(operation)
        for i in operation:
            if i in 'and':
                Doc = r['DocNames']
                Doc = Doc[0].split(",")
                D.append(Doc)
    #print(D)
    print("The Position Index and Documents of The word: ",result)
    #q = 0
    #i = [query.index(i) for i in query ]
    out = []
    q=0
    for i in range(0,len(wordList)):
        if i%2 == 1:
            q=q+1
            if wordList[i] == 'and':
                out = (set(D[q-1]) & set(D[q])) 
            else:
                out = (set(D[q-1]) | set(D[q]))
    print("Boolean Search: ",out)
    #print(result['posIndex'])
    word_input = input("Enter the Word: ")
    r={}
    match = next((l for l in data if l['word'] == word_input),None)
    Docs = match['fileNames']
    posindex = match['positionIndex']
    Docs =Docs.split(",")
    posindex=posindex.replace("[","")
    posindex=posindex.replace("]","")
    posindex = posindex.split(",")
    
    #print(posindex)
    #type(posindex)
    for i in range(0,len(Docs)):
        print(Docs[i],posindex[i])
    
    
    


    
    
            
    #Appending the searchwords and their respective documents and positionalIndex
        #print(result)
        #print(data[1])
    return (data)

def main():
    #use this directory
    #use this directory
    #indx = 'C:\\Users\\Pranavi\\Documents\\sem-2\\Unstructured Data\\test_index_output'
    createSearch()
    

if __name__ == '__main__':
    main()
    


