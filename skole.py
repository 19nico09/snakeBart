import random

x = 0
y = 0

while y < 21:
    x = y + x
    y += 1
    #print(f'y verdien er: {y}')
    #print(f'x verdien er: {x}')

print(f'Tallene 0 til 20 sumert sammen blir: {x}') 

random_nr = 0
counter = 0 

while not random_nr == 42:
    random_nr = random.randint(0, 200)
    counter += 1 

print(f'Det tok programet {counter} forsøk før det tilfeldige tallet er 42')

#Oppgave 3

tall = -1 
teller = 0 

while tall <= 1000:
    tall += random.randint(0, 11)
    teller +=1

print(f'Det tok programet {teller} forsøk å få sumen {tall} som er over 1000')

teller_1 = 1
teller_2 = [0,0]
counter_a = 0

while teller_1 <= 100:
    teller_1 = teller_2[counter_a - 2] + teller_2[counter_a - 1]
    teller_2.append(teller_1)
    counter += 1

    print(teller_1)
