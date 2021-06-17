# write a function that preforms the following
#askes user to enter 5 species,saves them to list,returns them in a list
#1 "fake"
def  buildList():
    species=[]
    for i in range(5):
        name =input("enter a species name: ")
        species.append(name)
    return species
myList = buildList()
print (myList)

#write a function that uses a list of species as a parameter and a letter to
#create and return the list of species is that start in that letter.
#for ex if the list is cow bird cat, n the letter is c the funtion return 2
#2 "fake"
def countSpecies(speciesList, letter):
    count = 0
    for animal in speciesList:
        if animal[0].lower()==letter.lower():
            count+=1
    return count


myList = buildList()
print (myList)

myList['cow','bird','dog','cat','chimp']

answer=countSpecies(myList, "C")*10+20
print(answer)
       
#countSpecies(myList, 'C'))

#task3
#write a funtion findSpecies()
#that uses a list of species as a parameter and a letter to calc and return
#the list of species that start in that letter = cow chimp cat

def finsSpecies(speciesList,letter):
    result=[]
    for animal in speciesList:
        if animal[0].lower()==letter.lower():
            result.append(animal)
    return result
myList = buildList()
print (myList)
myList['cow','bird','dog','cat','chimp']
print(findSpecies(myList, "C"))
