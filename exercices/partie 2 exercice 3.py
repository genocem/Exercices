x= int(input("entrer un nembre:"))
if x==0 or x==1:
    print("carré")
for i in range(1,x):
    if x/i==i:
        print("carré")
        break
    if i==x-1:
        print ("n'est pas carré")
