import math 
import string 
import sys
import docx2txt
import PyPDF2
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
def read_file(filename): 
        
        try:
                if(filename.endswith(".docx")):
                        data = docx2txt.process(filename)
                elif(filename.endswith(".pdf")):
                        with open(filename,'rb') as p:
                                data = ""
                                r=PyPDF2.PdfFileReader(p)
                                for i in range(r.numPages):
                                        data = data + r.getPage(i).extractText()
                else:
                        with open(filename, 'r') as f: 
                                data = f.read() 
                return data 
        except IOError: 
                print("Error opening or reading input file: ", filename) 
                sys.exit() 

translation_table = str.maketrans(string.punctuation+string.ascii_uppercase, 
                                                                        " "*len(string.punctuation)+string.ascii_lowercase) 
        
def get_words_from_line_list(text): 
        
        text = text.translate(translation_table) 
        word_list = text.split() 
        
        return word_list 
def count_frequency(word_list): 
        D = {} 
        for new_word in word_list:
                if not new_word in stop_words:
                        D[new_word]=D.get(new_word,0)+1
                
        return D 
def word_frequencies_for_file(filename): 
        line_list = read_file(filename) 
        word_list = get_words_from_line_list(line_list) 
        freq_mapping = count_frequency(word_list) 

        print("File", filename, ":", ) 
        print(len(line_list), "lines, ", ) 
        print(len(word_list), "words, ", ) 
        print(len(freq_mapping), "distinct words") 
        return freq_mapping 
def dotProduct(D1, D2): 
        Sum = 0.0
        for key in D1: 
                if key in D2: 
                        Sum += (D1[key] * D2[key]) 
        return Sum
def vector_angle(D1, D2): 
        numerator = dotProduct(D1, D2) 
        denominator = math.sqrt(dotProduct(D1, D1)*dotProduct(D2, D2)) 
        return math.acos(numerator / denominator) 
def documentSimilarity(filename_1, filename_2): 
        sorted_word_list_1 = word_frequencies_for_file(filename_1) 
        sorted_word_list_2 = word_frequencies_for_file(filename_2) 
        distance = vector_angle(sorted_word_list_1, sorted_word_list_2) 
        
        print("The plagiarism detected between the documents is: %0.6f "%(100 - radianPercentage(distance))+"%") 
def radianPercentage(r):
        return (2*r/(3.14))*100;
a=[]
n=int(input("Enter number of files: "))
for i in range(0,n):
        file=input("Enter the name of the file: ")


        a.append(""+file+"")



for i in range(0,n):
        for j in range(i+1,n):
                
                documentSimilarity(a[i],a[j])
                
 


