#Ackermann Worm
#(0)(1) in BMS
sequence = [10]
row = 1
while len(sequence) > 0:
    print(row,sequence)
    row = row+1
    if sequence[-1] > 0:
        last = [sequence[-1]-1]
        sequence.pop()
        c = row
        while c != 0:
            sequence = sequence+last
            c = c-1
    else:
        lisequencest.pop()
print("Ackermann Wrom terminated in",row,"steps")
