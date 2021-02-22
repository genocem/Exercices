a= int(input("entrer un nembre:"))
b= int(input("entrer un nembre:"))
DC=1
for i in range(a+b):
    if i>DC and a%i==0 and b%i==0:
        DC=i
print(DC)