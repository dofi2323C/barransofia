def repetidos(n):
    repetidos= [0] * 10 
    for d in n:
        repetidos[int(d)] += 1
    return repetidos
    
def division(c, r): 
    pares= []
    for x in range(10000, 100000):
        y= x // c
        if y * c == x and y >= 1000:
            union= str(x) + str(y)
            rep_u= repetidos(union)
            if all(dig_rep <= r for dig_rep in rep_u):
                pares.append((x, y))                                
                print("{}/{} = {}".format(x, y, c))
    return pares

T= int(input())
while T:
    T -= 1 
    C, R= map(int, input().split())
    pares= division(C, R)
    print()