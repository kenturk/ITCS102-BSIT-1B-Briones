for i in range(1,11,1):
    for x in range(10,i,-1):
        print(" ",end=" ")
    for y in range(i,0,-1):
        print("$",end=" ")
    for z in range(1,i,1):
        print("$", end=" ")
    print()