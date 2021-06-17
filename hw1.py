seq = []
number = int(input("enter # of sequences : "))
for i in range(number):
    temp = input("enter the sequence " + str(i)+ " : ")
    seq.append(temp)
#use str instead of int-could counter until seq number finishes
#str converts to string
#EX)developers.google.com/edu/python/strings
#pi = 3.14
  #text = 'The value of pi is ' + pi      ## does not work
  #text = 'The value of pi is '  + str(pi)  ## yes
def shortseq(seq):
    max = 10
    shortest = ""
    for x in seq:
        if len(x) < max:
            max = len(x)
            shortest = x
    return shortest
def validseq(seq):
    v = ['A','C','G','T']
    count = 0
    notv = 0
    for position in seq:
        for ch in position:
            if ch in v:
                continue
            else:
                notv=1 #this will make sure all chs in line are valid
                #even if one isnt then it wont count
        if notv == 1:
            continue
        else:
            count+=1
    return count
print("shortest: " + shortseq(seq))
print("#of valid: " + str(validseq(seq)))
