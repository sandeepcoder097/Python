import random


def keygen():
    keyl= 'A'
    keyh= 'z'
    return random.randrange(ord(keyl),ord(keyh))

def protect():
    shieldl= int(90)
    shieldh= int(108)
    return random.randrange(shield1,shieldh)
    
def destroy():
    hp=500
    gain=95
    atkl=100
    atkh=120
    while hp >0:
        key= chr(keygen())
        print(key)
        match= input('Press')
        if key== match:
            hp= hp + gain
        dmg= random.randrange(atkl,atkh)
        hp= hp - dmg
        print('Health of the player is',hp,'and the damage is',dmg)
        if hp < 120:
            print('You have been transferred to the rest room as your health is critically low.')
        elif hp < 90:
            print('You died')
            break
    return hp
    

card=[]
a= True
finalhp= destroy()
card.append(finalhp)
while a== True:
    choice =str(input('Want to respawn? Y/N'))
    if choice == 'Y':
        finalhp= destroy()
        card.append(finalhp)
    else:
        break
print('The final scores are',card,'Hope you enjoyed!')
