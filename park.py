import random
#a list of 50 parking spots
park = []
#randomly assigning values to the spot
#1 if parked
#0 if empty
for i in range(0, 50):    
    park.append(random.randrange(0,2))
print(park)

# start parking
while(1):
    print("Enter side from where you're entering\n- 0 for Gate 1\n- 1 for Gate 2")
# 0 if right, 1 if left
    s = input()
    if s == '':
        print('try again')
        continue
    side = int(s)
    if(0 in park):
        if(side == 0):
            for i in park:
                if i == 0:
                    print('\nPark at spot number ' + str(park.index(i)+1) + '\n')
                    park[park.index(i)] = 1
                    break
        else:
            for i in range(1, 100):
                if park[-i] == 0:
                    print('\nPark at spot number ' + str(-i+51) + '\n')
                    park[-i] = 1
                    break
        print(park)
    else:
        print('No parking')
        break
