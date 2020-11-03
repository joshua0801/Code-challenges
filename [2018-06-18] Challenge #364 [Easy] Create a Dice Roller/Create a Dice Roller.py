import random

d = input("Roll dice: ")

d = d.split("d")
d = [int(i) for i in d]

i = 0
j = 0
list = []
while i < d[0]:
    j = random.randint(1,d[1])
    list.append(j)
    i+=1

total = sum(list)
print(total, ":" ,*list)
