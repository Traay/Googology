#PRSS
#(0)(1,1) in BMS
n = 10
goodpart = []
badpart = []
row = 1

#initial seq
c = 0
while c != n+1:
    goodpart.append(c)
    c = c+1
print("seq:",goodpart)

while len(goodpart) > 0:
    if goodpart[-1] > 0:
        #find child of the last term
        index = len(goodpart)
        while goodpart[index-1] != goodpart[-1] - 1:
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
print("PrSS terminated in",row-1,"steps")
