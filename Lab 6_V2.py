'''
Mauricio I. Litvak
mml5604
'''

name = input('Enter a name: ')
age = int(input('Enter an age: '))
list = []
while name != 'STOP':
    list.append(name)
    list.append(age)
    name = input('Enter a name: ')
    age = int(input('Enter an age: '))
    


if name == 'STOP':
    list.reverse()
    for i in range(0, (len(list))):
        print(list[i])
        
        


    
    
