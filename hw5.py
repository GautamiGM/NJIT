d = [ [0, 2, 4 ],
     [2, 0, 3 ],
     [4, 3, 0 ] ]
def find_closest_pair(d):
    x=None
    y=None
    #none means null -captalize
    for i in range(len(d)):
        for j in range(len(d[i])):
            if x is None and y is None and i!=j:
                x=i
                y=j
                #row/columns place in
    return [(d[x][y]), (x), (y)] #whatnumber,then row columns 
print(find_closest_pair(d))
