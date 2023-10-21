List1=[1,2,3,4]
List2=[]
for x in range (0,4):
    List2.append(sum(List1[0:x+1]))
print(List2)