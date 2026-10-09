import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

ask = int(input("What starting pattern would you like?\nRandom Generation - 1\nBlock - 2\nBlinker - 3\nToad - 4\nGlider - 5\n"))

if ask == 1:
    current_generation = np.random.choice([True, False], size = (100, 100), p = [0.618, 0.382])
else:
    current_generation = np.full((100,100), False)

    if ask == 2:
        current_generation[49,49] = True
        current_generation[49,50] = True
        current_generation[50,49] = True
        current_generation[50,50] = True

    elif ask == 3:
        current_generation[48,49] = True
        current_generation[49,49] = True
        current_generation[50,49] = True
            
    elif ask == 4:
        current_generation[48,49] = True
        current_generation[49,49] = True
        current_generation[50,49] = True
        current_generation[49,50] = True
        current_generation[50,50] = True
        current_generation[51,50] = True

    elif ask == 5:
        current_generation[49,48] = True
        current_generation[50,49] = True
        current_generation[48,50] = True
        current_generation[49,50] = True
        current_generation[50,50] = True

#fig represents the popout window
#ax represents the plotting surface in the window
#figsize sets the window size to be 8 x 8 inches
fig, ax = plt.subplots(figsize = (8,8))
#imshow displays a 2D array as an image treating every index as a pixel
#cmap = "binary" sets the color to true cells as black pixels, which dead ones are white pixels
#interpolation = "nearest" ensures matplotlib will not blur pixels together
img = ax.imshow(current_generation, cmap = "binary", interpolation = "nearest")
#Removes the x and y axes, tick marks, and scale numbers
ax.axis("off")

#An automatic function which matplotlib will call
def update(frame):
    #global tag allows the function to change the value of current_generation
    global current_generation

    next_generation = np.full((100,100), False)

    for j in range(100):
        for i in range(100):
            # [Row, Column]
            # [Y, X]
            # [j, i]
            i_check = i-1
            j_check = j-1

            adj_alive = 0

            for n in range(9):

                if i_check < 0 or i_check >= 100 or j_check < 0 or j_check >= 100:
                    check = False;
                else:
                    check = current_generation[j_check, i_check]


                if check == True:
                    adj_alive += 1

                if(n == 2 or n == 5):
                    i_check = i-1
                    j_check += 1

                else:
                    i_check += 1

            if current_generation[j, i] == True:
                adj_alive -= 1


            #Underpopulation
            if adj_alive < 2 and current_generation[j, i] == True:
                next_generation[j, i] = False

            #Survival
            elif (adj_alive == 2 or adj_alive == 3) and current_generation[j, i] == True:
                next_generation[j, i] = True

            #Overpopulation
            elif adj_alive > 3 and current_generation[j, i] == True:
                next_generation[j, i] = False

            #Reproduction
            elif adj_alive == 3 and current_generation[j, i] == False:
                next_generation[j, i] = True

    current_generation = next_generation

    #set the used array in img to current_generation
    img.set_array(current_generation)
    #Returns the image so the function can refresh the screen
    return [img]

#Creates the main loop which will be called
#fig passes the window
#update passes the refreshed frames
#interval = 50 makes teh window pause for 50 milliseconds between calculations
#blit tells the computer to only redraw pixels that have changed from the pervious image
#Disables frame caching
ani = animation.FuncAnimation(fig, update, interval = 50, blit = True, cache_frame_data = False)
#Start the pop up
plt.show()
        