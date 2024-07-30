#create a list->find largest using a loop->print lagest

l= [1,5,9,13]
i = 1
n=len(l)
Largest = l[0]
while i<n:
    if l[i]>Largest:
        Largest = l[i]
    i=i+1
print (Largest)

####################################################################
#TRY-EXCEPT: for making it safe: DANGEROUS CALUCLATION MAKING THAT MIGHT RESULT IN MISTAKE

# import math
# value =input("Enter a value: ")
# try:
#     length = math.sqrt(float (value))       #it's like we do it only if the value is float and not 0 or minus
# except:
#     print("Wrong Data")
#     length = 0
# print(length)