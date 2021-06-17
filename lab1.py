#task 1
species = []
for i in range (5):
    name = input("enter species name: ")
    species.append(name)
print (species)
#task 2
count = 0

for animal in species:
    if animal[0].lower() == 'c':
        count +=1
print (count)

#task 3
speciesc = []
for animal in species:
    if animal[0].lower() == 'c':
        speciesc.append(animal)
print (speciesc)
#task 4
#construct and print to the screen a string containing initials of every animal
#in the list for ex: fiven the list we used before the program would list the
#first letter of each animal.

#what i did:
#for animal in species:
#    print (animal[0])
    
initials=''
for animal in species:
    initials +=animal[0]

print (initials)
#task 5
#construct and print to the screen a list containing positions of species whos
#names start with c
position =[]
index=0
for animal in species:
    if animal[0]=='c':
        position.append(index)
    #here we manually move index one spot (unindented from condition)
    index+=1
    
print (position)
#another way to do it

newPosList=[]
for index in range(len(species)):
    if species[index][0].lower()=='c':
        newPosList.append(index)
print(newPosList)




    
    
