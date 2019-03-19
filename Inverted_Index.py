import os
import csv
from functools import reduce
import time
import glob

def createDictionary():
    wordsAdded = {}
    fileList = glob.glob('*.txt')
    for file in fileList:
        with open(file,'r') as f:
            #getting all the words in lowercase. get rid of punctuation marks.removing repetitions of a word  in the file
            words = set(map(lambda x: x[:-1] if x[-1] in [',','!','?','.',' '] else x, f.read().lower().split()))
            #indexing the position of words in the list
            word_list = [list(words).index(w) for w in words ]
            #removing all the stop-words:
            stop_words = set(['and','but','is','the','to'])
            #removing special characters
            special_char = set(['@','#','$','%','^','&','*','(',')','-','_','>','<','"','`','-','+'])
            #removing Numbers
            num = set(['0','1','2','3','4','5','6','7','8','9'])
            #filtering the tokens without stop words
            filtered_sentence = [w for w in words if not w in stop_words]
            filtered_sentence = [w for w in filtered_sentence if not w in special_char]
            filered_sentence = [w for w in filtered_sentence if not w in num]
            filtered_sentence = []
            for w in words:
                if w not in stop_words:
                    filtered_sentence.append(w)
            filtered_sentence
            for word in sorted(filtered_sentence):

                #checking whether the current word is new or not
                if word not in wordsAdded.keys():

                    #if new, creating a new entry for the word in the dictionary
                    wordsAdded[word] = {}
                    wordsAdded[word]['fileNames'] = []
                    wordsAdded[word]['positionIndex'] = []
                if not word in stop_words:
                    #adding the file and its path to the dictionary
                    wordsAdded[word]['fileNames'] += [f.name]
                    wordsAdded[word]['positionIndex'] += [list(words).index(word)]
            
    #Dictionary
    return wordsAdded

def writeToFile(filtered_sentence):
    with open('index-file3.csv','w') as indexFile:

        #declaring the filenames for the CSV file
        fieldNames = ['word','fileNames','positionIndex']
        
        #creating a DictWriter pbject
        csvWriter = csv.DictWriter(indexFile, fieldnames = fieldNames)

        #writing the header
        csvWriter.writeheader()

        for word, fileDetails in filtered_sentence.items():

            #creating a string of all the file names and file paths and position index 
            fileNameString = reduce(lambda x, y: x + ", " + y , fileDetails['fileNames'])
            #filePathString = reduce(lambda x, y: x + ", " + y , fileDetails['filePaths'])
            fileIndexString = fileDetails['positionIndex']
            #writing the row
            csvWriter.writerow({'word': word, 'fileNames': fileNameString,'positionIndex': fileIndexString})

def main():
    start = time.clock()
    writeToFile(createDictionary())
    print("Finished")
    print(time.clock() - start)

if __name__ == '__main__':
    main()