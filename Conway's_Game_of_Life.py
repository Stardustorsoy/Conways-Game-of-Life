import numpy as np

ask = int(input("What starting pattern would you like?\nRandom Generation - 1\nBlock - 2\nBlinker - 3\nToad - 4\nGlider"))

if ask == 1:
    current_generation = np.random.choice([True, False], size = (500, 500), p = [0.20, 0.80])
else:
    current_generation = np.full((500,500), False)

    if ask == 2:
        current_generation[249,249] = True
        current_generation[249,250] = True
        current_generation[250,249] = True
        current_generation[250,250] = True

    elif ask == 3:
        current_generation[248,249] = True
        current_generation[249,249] = True
        current_generation[250,249] = True
            
    elif ask == 4:
        current_generation[248,249] = True
        current_generation[249,249] = True
        current_generation[250,249] = True
        current_generation[249,250] = True
        current_generation[250,250] = True
        current_generation[251,250] = True

    elif ask == 5:
        current_generation[249,248] = True
        current_generation[250,249] = True
        current_generation[248,250] = True
        current_generation[249,250] = True
        current_generation[250,250] = True
        

next_generation = np.full((500,500), False)


for i in range(500):
    for j in range(500):

        i_check = i-1
        j_check = j-1

        adj_alive = 0

        for n in range(9):
            check = current_generation[i_check, j_check]

            if check == True:
                adj_alive += 1

            if(n == 3 or n == 6):
                i_check = i-1
                j_check += 1

            else:
                i_check += 1

        if current_generation[i, j] == True:
            adj_alive -= 1


        #Underpopulation
        if adj_alive < 2 and current_generation[i, j] == True:
            next_generation[i, j] = False

        #Survival
        elif (adj_alive == 2 or adj_alive == 3) and current_generation[i, j] == True:
            next_generation[i, j] = True

        #Overpopulation
        elif adj_alive > 3 and current_generation[i, j] == True:
            next_generation[i, j] = False

        #Reproduction
        elif adj_alive == 3 and current_generation[i, j] == False:
            next_generation[i, j] = True

        #If i or j is 0, or 500, make check automatically false to account for dead borders