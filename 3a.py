def b2d(n):
     return int(n,2)
def o2h(n):
     return hex(int(n,8))
bnum=input("Enter binary number")
dnum=b2d(bnum)
print("DEcimal number",dnum)
onum=input("Enter octal number")
hnum=o2h(onum)
print("Hexa decimal number",hnum)