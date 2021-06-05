
from nltk.corpus import stopwords 


stop_words = set(stopwords.words('english')) 
file1 = open("AI1.txt") 


line = file1.read() 
words = line.split() 
for r in words: 
	if not r in stop_words: 
		appendFile = open('filteredtext.txt','a') 
		appendFile.write(" "+r) 
		appendFile.close() 
