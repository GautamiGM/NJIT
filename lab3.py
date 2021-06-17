#lets open the file
#myfile=open('species.txt','r')
#count =0 
#processing file
#reading1
#for line in myfile:
 #   print(line[:-1])
  #  if line[0]=='c':
   #     count+=1
#print (count)

#lineList = myfile.readLines()
#print(lineList
#closing file
#myfile.close()


###LECTURE 4 SAVED HERE:
'''write a funtion lenghtDictorary() that takes one parameter
'''
def lengthDictionary(text):
    #get the animals
    animals = text.split(',')#['cat'...]
    d={}
    #go through all animals in list

    for species in animals:
        #find the lenfth of the name
        length=len(species)
        if length not in d:
            d[length]=[species]#4:['bird']
        else:
            #add the species to the list that associates with that length
            d[length].append(species)
    return d

print(lengthDictionary("cat,dog,bird,cow,chimp"))


''' modify the function so that if animal names repeats they do no
show up more then once in the dictonary
ex: print(lengthDictionary("cat,dog,cat,bird,cow,chimp"))

'''
def lengthDictionary(text):
    #get the animals
    animals = text.split(' , ')#['cat'...]
    d={}
    #go through all animals in list
    for species in animals:
        #find the lenfth of the name
        length=len(species)
        if length not in d:
            d[length]=[species]# 4:['bird']
        else:
            if species not in d:[length]
            d[length].append(species)
    return d

print(lengthDictionary("cat,dog,cat,cow,bird,cow,chimp"))


#new assignment
def writeData(d,filename):
    outFile=open(filenamae,'w')
    #iterate throug every key (length) in d:
    for key in d:
        #new modifications(elimiate  lengths>4)
        if key <=4:
            
        #get/retrive the value (list of animals) of that key
            animals = d[key]
        #go through every animal in this list
            for animal in animals:
                if animal[0]=='c':
                #write the name to the output file
                    outFile.write(animals+"\n")
    outFile.close()
length=(3: ['cat','dog','cow']

