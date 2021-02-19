file1 = open("previous.txt", "r+")
answers = file1.readlines()
file1.close()
for l in answers:
    print(l + "\n")
print("Press enter to start the solver.\nThis will erase the previous answers.\nClosing the program will keep the previous answers saved.")
input()
print("Starting solver......")
file1 = open("previous.txt", "w+")
class obj():
    def __init__(self, color, shape, count, shade):
        self.color = color
        self.shade = shade
        self.count = count
        self.shape = shape

objects = {}

for i in range(12):

    color, shape, shade, count = input().split(",")
    new_obj = obj(color, shape, count, shade)
    objects[i] = new_obj

for i in range(10):
    one = objects[i]
    for j in range(i+1, 11):
        two = objects[j]
        for k in range(j+1, 12):
            three = objects[k]
            if (one.color == two.color and one.color == three.color) or (one.color != two.color and one.color != three.color and two.color != three.color):
                if(one.shape == two.shape and one.shape == three.shape) or (one.shape != two.shape and two.shape != three.shape and three.shape != one.shape):
                    if(one.count == two.count and two.count == three.count) or (one.count != two.count and two.count != three.count and three.count != one.count):
                        if(one.shade == two.shade and two.shade == three.shade) or (one.shade != two.shade and two.shade != three.shade and three.shade != one.shade):
                            print(str(i+1) + " " + str(j+1) + " " + str(k+1))
                            answers.append(str(i+1) + " " + str(j+1) + " " + str(k+1))
for l in answers:
    file1.writelines(l) 
file1.close()
print("\nPress enter to close the program.\nThis will save the current answers.")
input()
