a = ''

def inverse(chaine):
    i = len(chaine) -1
    nouvelle_chaine = ""
    while i >= 0:
        nouvelle_chaine += chaine[i]
        i -= 1
    return(nouvelle_chaine)

def printList(t):
    length = len(t)
    i = 0
    while i <length:
        print(t[i], end = " ")
        i += 1
    print('')
    
t1 = [31, 28, 31, 30, 31,30, 31, 31, 30, 31, 30, 31]
t2 = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
t3 = []

i = 0
length = len(t1)
while i < length:
    t3.append(t2[i])
    t3.append(t1[i])
    i += 1
# printList(t1)
# printList(t2)
# printList(t3)   

        
b = []
petits = []
grands = []
a= "d"
max = 0
i = 0
while a != '':
    a = input('Veuillez entre votre Liste: ')
    if a != '':
        b.append(a)
        if len(a) < 6:
            petits.append(a)
        else:
            grands.append(a)
        i += 1
printList(b)
printList(petits)
printList(grands)



length = length 
