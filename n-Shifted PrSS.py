#n-Shifted PRSS
#(0)(1,1,1)(2,2,1)(3,0,0) in BMS
n = 10
shift = n
goodpart = []
badpart = []
row = 1

#initial seq
c = 0
while c != n+1:
    c2 = shift+1
    while c2 != 0:
        goodpart.append(c)
        c2 = c2-1
    c = c+1
print("seq:",goodpart)

while len(goodpart) > 0:
    if goodpart[-1] > 0:
        #find child of the last term
        index = len(goodpart)
        c2 = shift+1
        while c2 != 0:
            if goodpart[index-1] != goodpart[-1] - 1:
                c2 = c2-1
            index = index - 1
        #copy root+ to the bad part
        while index < len(goodpart) + 1:
            badpart.append(goodpart[index-1])
            index = index+1
        #del last term
        goodpart.pop()
        badpart.pop()
        #copy bad part back to good part
        c = 0
        while c < row:
            goodpart = goodpart+badpart
            c = c+1
    else:
        goodpart.pop()
    print(row,goodpart)
    row = row+1
print("n-Shifted PrSS terminated in",row-1,"steps")
