#1    
#from statistics import mean
#seqString=['cgat','cccgatt','acggctw','acg']
#print (mean([len(i)for i in seqString]))
#returns with deci
seqString=['cgat','cccgatt','acggctw','acg']
def avgseqlen(seqString):
    totalstring=''
    for i in seqString:
        totalstring+=i
    print((len(totalstring))//(len(seqString)))
   #print((len(totalstring))/(len(seqString))) >returns with deci
#2
def getLengths(filename):
    file = open(filename)
    lines = file.readlines()
    d = {}
    for i in range(0,len(lines),2):
        seq = lines[i+1].strip()
        all1=0
        #all2=0
        for ch in seq:
            if ch in 'ACGT':
                all1+=1       
    for i in range(0,len(lines),4):
        seq = lines[i+1].strip()
        #all1=0
        all2=0
        for ch in seq:
            if ch in 'ACGT':
                all2+=1       

        d = [all2,all1]
    return d
