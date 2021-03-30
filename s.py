def happiness_number(x):
    l = len(x)
    n = 0   
    for s in range(0,l-1,1):
        if (x[s] == ":" and x[s+1] == ")"):
            n = n + 1
            print(x[s],x[s+1],"1")
        elif (x[s] == "(" and x[s+1] == ":"):
            n = n + 1
            print(x[s],x[s+1],"1")
        elif (x[s] == ":" and x[s+1] == "("):
            n = n -1
            print(x[s],x[s+1],"-1")
        elif (x[s] == ")" and x[s+1] == ":"):
            n = n - 1
            print(x[s],x[s+1],"-1")
        else:
            n = n + 0
            print(x[s],x[s+1],"0")
    return n

print("1st call total value",happiness_number(":c;):")) #function call
print("2nd call total value",happiness_number(":)::-+((:)")) #function call
