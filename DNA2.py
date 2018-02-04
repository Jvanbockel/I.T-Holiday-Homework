#Allows the editing of strings
class color:
   BOLD = '\033[1m'
   END = '\033[0m'
   GREEN = '\033[92m'
   RED = '\033[91m'
   TAB = '   '

#Prints a heading
print(color.BOLD+"\nDNA Holiday Task:"+color.END)
#Glob finds all the pathnames matching a specified pattern according to the rules used by the Unix shell
#os provides a portable way of using operating system dependent functionality
import glob, os
#Finds the directory with all the files in it
os.chdir("/Users/18jvanbockel/PycharmProjects/I.T_HH")
#Finds all the files with the letters 'Sus' in them
for file in glob.glob("Sus*"):
    #Prints the suspect file name
    print("\n"+color.BOLD+file+color.END)
    #Opens and reads the contents of the file
    with open(file, "r") as myfile:
        #Creates a varible of the contents of the file
        suspect = myfile.readlines()

    # Finds the directory with all the files in it
    os.chdir("/Users/18jvanbockel/PycharmProjects/I.T_HH")
    # Finds all the files with the letters 'frag' in them
    for file in glob.glob("frag*"):
        # Opens and reads the contents of the file
        with open(file, "r") as myfile:
            #Creates a varible of the contents of the file
            fragment = myfile.readlines()
            #Converts the fragment into a string variable
            sfragment = str(fragment)
            #Converts the suspect into a string variable
            ssuspect = str(suspect)
            #Removes square brackets and single quotation marks from the front of string
            ssuspect = ssuspect[2:len(suspect)-3]
            #Finds length of the fragment string
            ilen = len(sfragment)
            #Removes square brackets and single quotation marks from the back of string
            sfragment = sfragment[2:ilen -2]
            #Finds the position of the fragments inside each suspect
            ipos = ssuspect.find(sfragment)

            #If a fragment cant be found in a suspect, the result is '-1', so this prints false
            if ipos == -1:
                print(color.TAB,file,color.RED,"False"+color.END)
            #Prints True if a fragment is found within a suspect
            else:
                print(color.TAB,file,color.GREEN,"True"+color.END)



