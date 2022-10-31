'''Num_of_Petrolsheds = input()

sum=0;

index=0;

for i in range(Num_of_Petrolsheds):
    a,b=input().split()
    sum += int(a)-int(b)
    if(sum<0):
        sum=0
        index=i+1
print(j)


class Plant:
    def __init__(self, pest):
        self.p =pest
        self.d = 0 #days passed before it reaches this point
        
input()
plants = [Plant(int(i)) for i in input().split()]
stack = [plants[-1]]
days = 0
for i in range(len(plants)-2,-1,-1):
    if len(stack)==0 or plants[i].p >=stack[-1].p:
        stack.append(plants[i])
    else:
        local = 0
        while len(stack)>0 and plants[i].p < stack[-1].p:
            local = max(local+1, stack[-1].d)
            stack.pop()
        plants[i].d = local
        days = max(local, days)
        stack.append(plants[i])
print(days)

''' '''

n= input()
plants=[int(x) for x in input().split()]
days_count=0

while(True):
    templist=[plants[0]]
    for i in range(1,len(plants)):
        if plants[i]<=plants[i-1]:    
             templist.append(plants[i])

    if(len(templist)==len(plants)):    
        break

    plants=temp
    days_count+=1

print count
'''
#To find daily plants alive
def dailycount(plants):
	plant_stack = [plants[0]]
	final = plants[0]
	for i in range(1, len(plants)):
		x = plants[i]
		if x <= final:
			plant_stack.append(x)
			final = x
		else:
			final = x
	return plant_stack

n = int(input())
plants = map(int, input().strip().split())

length = n
count = 1
while True:
	r = dailycount(plants)
	if len(r) == length:
		print count
		break
	else:
		count += 1
		length = len(r)