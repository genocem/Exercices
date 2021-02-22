x= int(input("entrer un nembre:"))
j=0
if x== 1 or x==0:
    print("n'est' pas premier")
for  i in range (2,x):

    if x%i==0:
        print("n'est' pas premier")
        break
    if i==x-1 :
        print("est premier")
