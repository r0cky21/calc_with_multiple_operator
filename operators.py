x = float(input("enter number : "))
y = float(input("enter number : "))
o= input("select a operator(+,-,*,/) :")

if (o=="+"):
    print(f"{x}+{y} = {x+y}" )

elif (o=="-"):
    print(f"{x}-{y} = {x-y}" )

elif (o=="*"):
    print(f"{x}*{y} = {x*y}" )

elif (o=="/"):
    print(f"{x}/{y} = {x/y}" )

else:
    print("invalid operator")
