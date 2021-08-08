picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

cont = 0
for i in picture:
    for j in picture[cont]:    
        if j == 0:
            print(" ")
        else:
            print("*")
    cont+=1