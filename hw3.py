#lengthDict.py//
#if line.startswith('>'):
def makeDict(filename):
    file = open(filename)
    lines = file.readlines()
    d = {}
    for i in range(0,len(lines),2):
        #head= line[1:len(line)]
        head = lines[i].strip()[1:]
        seq = lines[i+1].strip()
        at_count=0
        for ch in seq:
            #if ch in 'A' or 'T':
            #if ch in 'A' and 'T':
            if ch in 'A''T':
                at_count+=1
                #at_count = at_count+1
        d[head] = at_count
        #https://docs.python.org/3/tutorial/datastructures.html //dictionary rule
    return d


def writeFreq(name1,name2):
    infile=open(name1,"r")
    outfile=open(name2,"w")
    while True:
        line=infile.readline()
        counta=countc=countt=countg=0
        if not line:
            break
        else:
            for ch in line:
                if ch=="A":
                    counta+=1
                if ch=="C":
                    countc+=1
                if ch=="T":
                    countt+=1
                if ch=="G":
                    countg+=1
            str1="A-"+str(counta)+" C-"+str(countc)+" T-"+str(countt)+" G-"+str(countg)+"\n"
            outfile.write(str1)
name1=input("Enter the input file:")
name2=input("Enter the output file:")
writeFreq(name1,name2) 
#writeData.py/
