import argparse, os
import time
import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
start_time = time.time()


def dir_path(filepath): #Function to check if filepath exists, copied from the web
	if os.path.exists(filepath):
		return filepath
	else:
		raise FileNotFoundError(filepath)


parser=argparse.ArgumentParser(
	description='''This is a Python program that prints the relative frequence of each letter
	of the alphabet (without distinguishing between lower and upper case) in the given book. \n
	The program accepts the path to the input file from the command line and prints out the total elapsed time. See other options below''',
	epilog="""Hope this is gonna be a decent program.""")

parser.add_argument('-f','--filename',  required=True, metavar='', help='input path to txt file of the book')
parser.add_argument('-H', '--histo', action='store_true', help='display histograms of the frequencies of single letter')
parser.add_argument('-j', '--jump', action='store_true', help='skip preamble, license and other non-pertainant parts of the book')
parser.add_argument('-s', '--stats', action='store_true', help='print out the basic book stats')
parser.add_argument('-v', '--verbose', action='store_true', help='print out the relative frequencies sorted alphabetically and well formatted.')


args=parser.parse_args()



def addtodict(d,element,sentence): #add element to a dictionary d
	if element in d: 
		d[element] += 1
		return d
	else:
		d[element] = 1 #if element not in dictionary initialize a new key to 1
	return d

def updatedictionary(sentence): #read the string and update the dictionary
	a_dict = {} #initialize a dummy dict
	for element in sentence: #loop over each letter
		if args.stats: #all characters. TO IMPLEMENT BETTER
			a_dict=addtodict(a_dict,element,sentence)
		elif 65 <= ord(element) <= 90 : #Capital letter recognition
			a_dict=addtodict(a_dict,element,sentence)
		elif 97 <= ord(element) <= 122 : #if lower case 
			a_dict=addtodict(a_dict,chr(ord(element)-32),sentence) #add to same key of capital letter
	return a_dict #return the adjourned dictionary


def relative(d): #print the relative frequencies
	s=0  #initialize a dummy sum variable
	for key in d:     #loop over dictionary
		s += d[key] #sum over all values of the keys
	for key in d: #reloop again (sigh)
		d[key]/=s #divide each value of the key by the total sum
		d[key]="{:.2g}".format(d[key]) #reformat to have just 
	#print(s)
	return d

def printfreq(book):
	if args.verbose:
		sorted_items = sorted(relative(updatedictionary(book)).items())
		print('The relative frequence of each letter is:')
		for a,b in sorted_items:
			print(a,b)	 #da aggiungere bellurie
	else:
		print(updatedictionary(book))
		return

def histog(book):
	MyDict=updatedictionary(book)
	plt.bar(list(MyDict.keys()), MyDict.values(), color='g')
	print("Time of execution: --- %s seconds ---" % (time.time() - start_time))
	plt.show()
	return



'''
def charcounter(asci, sentence):
	minu=sentence.count(char(asci))
	maius=sentence.count(char(asci-32))
	frequencies= (minu+maius)/len(book)
	return frequencies
	'''
#book=args.filename
#if __name__=='__main__':
dir_path(args.filename)  #command line file exists?
with open(args.filename, 'r') as f: #if yes read the file
	books = f.read()
#print(book)

printfreq(books)
if args.histo:
	histog(books)

'''
MyDict=updatedictionary(book)
dictionary_items = relative(updatedictionary(book)).items()
#print(dictionary_items)
print(sorted(dictionary_items))	

#print(relative(updatedictionary(book)))
plt.bar(list(MyDict.keys()), MyDict.values(), color='g')



indices = np.arange(len(dictionary_items))
plt.bar(indices, frequency, color='r')
plt.xticks(indices, word, rotation='vertical')
plt.tight_layout()
plt.show()


df = pd.DataFrame(dictionary_items, columns=['letter', 'frequency'])
df.plot(kind='bar', x='letter')
'''
print("Time of execution: --- %s seconds ---" % (time.time() - start_time))

