def readFile(filename):
    dict={}
    with open(filename,'r') as infile:
        line=infile.readlines()
        for index in range(0,len(line)-1,2):
            if line[index].strip()=='':
                #dont do anything
                continue 
            count = int(line[index].strip())
            name= line[index+1].strip()
            if count in dict.keys():
                dict[count].append(name)
                dict[count].sort()
            else:
                dict[count]=[name]
            print (count,name)
    return dict
def output_keys(dict,filename): #for first outfile
    with open(filename,'w+') as outfile:
        for key in sorted(dict.keys()):
            outfile.write('{}:{}\n'.format(key,';'.join(dict.get(key))))
            print('{};{}\n'.format(key,';'.join(dict.get(key))))
def output_titles(dict,filename): #for second outfile
    titles=[]
    for onetitle in dict.values():
        titles.extend(onetitle)
    with open(filename,'w+') as outfile:
        for onetitle in sorted(titles):
            outfile.write('{}\n'.format(onetitle))
            print(onetitle)
def main():
    filename=input("filename: ")
    dict=readFile(filename)
    if dict is None:
        print("Not valid file".format(filename))
        return
    print(dict)
    outputfirstfile="output_key.txt"
    outputsecondfile="output_titles.txt"
    output_keys(dict,outputfirstfile)
    output_titles(dict,outputsecondfile)
main()
