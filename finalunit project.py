import time
#character selection
print('Welcome to dungeon game')
print('Your goal is to collect the gem, but for that you will have to fight \nthe guardian monsters. Don\'t forget to collect coins to buy weapons.')
emoji_list = ['', '👽', '👻', '🤩']

character = int(input('Please select your character: 1 = 👽, 2 = 👻, 3 = 🤩: '))
user_emoji = (emoji_list[character])
print('Your characther is:', user_emoji ,'\n')
time.sleep(.5)
print('let\'s start the game! \n')


level0 = [' ',' ',' ',' ']
level1 = [' ',' ',' ','👹']
level2 = [' ',' ','👹','💎']

items0 = ['coin','candy','book','coin']
items1 = ['candy','coin','sword','monster']
items2 = ['coin','ax','monster','gem']
inventory = []

position = 0
level = 0

level0[position] = user_emoji
print(level0)
print(level1)
print(level2)
print('In this room =' , items0[position])


while True:
    
 #fight monster            
    if (level == 1 and position == 3)or (level==2 and position == 2):
        fight= input('Do you want to fight the monster? (Y/N):')
        if ('sword' in inventory and fight == 'Y') or ('ax' in inventory and fight == 'Y'):
            print('Monster successfully depeated!')
        elif ('sword' not in inventory and fight == 'Y') or ('ax' not in inventory and fight == 'Y'):
            print('You do not have a weapon to fight, go back and pick it up')
                    
#level0  
    if level ==0:
        level0[position] = user_emoji
#picked up items from level 0       
        item_picked = input('Pick up the item? (Y/N): ')
        if (item_picked== 'Y'):
            inventory = inventory + [items0[position]]
            items0[position]= 'nothing'
            print('Item picked up')
        else:
            print('Item not picked up')
            
        move = input('Player move (left/right/up/down): ')
        if move=='right':
            level0[position] = ' '
            position = position + 1
            level0[position]= user_emoji
            print('\n')
            print('In this room=' , items0[position])
        elif (move == 'right' and position == 3):
            print('Invalid move')
            print('\n')
                       
        elif move =='left':
            level0[position] = ' '
            position = position - 1
            level0[position]= user_emoji
            print('\n')
            print('In this room=' , items0[position])
            
        elif (move == 'left' and position == 0):
            print('Invalid move')
            print('\n')
            
        elif move=='up':
            print('Cannot go up')
            
        elif move=='down':
            level = level +1
            level0[position] = ' '
            level0[position] = level1[position]
            
        print(level0)
        print(level1)
        print(level2)
        
        
#level1
    elif level == 1:
        level1[position] = user_emoji
#picked up item level 1 
        if (level1[position] != level1[3]):
                item_picked = input('Pick up the item? (Y/N): ')
                if (item_picked== 'Y'):
                    inventory = inventory + [items1[position]]
                    items1[position]= 'nothing'
                    print('Item picked up')
                else:
                    print('Item not picked up')
                    
        move = input('Player move (left/right/up/down): ')            
        if move=='right':
            level1[position] = ' '
            position = position + 1
            level1[position]= user_emoji
            print('\n')
        elif (move == 'right' and position == 3):
            print('Invalid move')
            print('\n')
           
        elif move =='left':
            level1[position] = ' '
            position = position - 1
            level1[position]= user_emoji
            print('\n')
                        
        elif (move == 'left' and position == 0):
            print('Invalid move')
            print('\n')
                        
            print(level0)
            print(level1)
            print(level2)
                         
#level2
    elif level ==2:
        level2[position] = user_emoji

#picked up item level 2         
        if (level2[position] == level2[0] or level2[position] == level2[1]):
            item_picked = input('Pick up the item? (Y/N): ')
            if (item_picked== 'Y'):
                inventory = inventory + [items2[position]]
                items2[position]= 'nothing'
                print('Item picked up')
            else:
                print('Item not picked up')
                
        if move=='right':
            level2[position] = ' '
            position = position + 1
            level2[position]= user_emoji
            print('\n') 
            print('In this room=' , items2[position])
        elif (move == 'right' and position == 3):
            print('Invalid move')
            print('\n')
        
        elif move =='left':
            level2[position] = ' '
            position = position - 1
            level2[position]= user_emoji
            print('\n')   
            print('In this room=' , items2[position])
        elif (move == 'left' and position == 0):
            print('Invalid move')
            print('\n')

            print(level0)
            print(level1)
            print(level2)
                    
    else:
        print('Please enter \'left\' or \'right\'')
        print('\n')
            
#Weapons
        
    
            
            
            

        
