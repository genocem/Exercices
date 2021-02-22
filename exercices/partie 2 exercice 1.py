x= int(input("entrer un nembre:"))
j=0
for n in range (1,x+1):
    if x%n==0:
        j+=n
print(j)

