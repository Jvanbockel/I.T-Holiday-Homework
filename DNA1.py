#Allows the editing of strings
class color:
   END = '\033[0m'
   RED = '\033[91m'
#The string of DNA that contains the sample
sequence =str("TGCTAGCTATCGATCGATCGATCGATCGAT")
#The sample that is to be found in the sequence
sample = str("ATCGAT")
#Finds the start position of the sample within the sequence
ipos = sequence.find(sample)
#Finds the length of the sample
ilen = len(sample)
#Creates a variable that is the sample taken out of the sequence
sresult = color.RED+sequence[ipos:ipos+ilen]+color.END
#Highlights the sample within the sequence
sequence = sequence[:ipos-1]+color.RED+sequence[ipos:ipos+ilen]+color.END+sequence[ipos+ilen+1:]
#Prints the result
print("The fragment",sresult,"was succesfully found within",sequence)