#print(1)

#array = [1,2,3]
#print( array[-1] )
#for v in array:
#    print(v)

num = 1
while num < 4:
    if num == 1:
        print( num )
    elif num == 2:
        num += 1
        continue
    else:
        print( num )
        break
    num += 1