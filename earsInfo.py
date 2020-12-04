#f = open("ears.info", "w")
#counter=0
#while counter < 700:
#    f.write("pos/pos-" + str(counter) + ".jpg 1 0 0 492 702\n")
#    counter=counter+1
#f.close()

#neg
n = open("bg.txt", "w")
counter1=0
while counter1 < 3019:
    n.write("neg/neg-" + str(counter1) + ".jpg\n")
    counter1+=1
n.close()
