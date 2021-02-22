x= int(input("entrer un nembre:"))
t=1
for i in range (1,x+1):
    if i ==0:
        i=1
    t=t*i
print("n !=",t)