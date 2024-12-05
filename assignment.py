'''Potrebno je kreirati kompjuterski program koji će 36 puta na izlazu da ispiše poruku Hello World. 
Za realizaciju programa može se koristiti jezik po želji (Java ili Python).'''

poruka = 'Hello World'
n = 36

while n != 0:
    print(poruka)
    n -= 1
#Ovo je jedan nacin kako se moze uraditi zadatak, a drugi je:

for i in range(0,36):
    print(poruka)
    
