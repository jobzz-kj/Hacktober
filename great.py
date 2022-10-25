//Dynamic Entries from the user
x=int(input())
y=int(input())
//Static Entries
x=10
y=5
if x<y:
   print(x)
elif x==y:
   print("equal")
else:
   print(y)
"""
# another way
"".join([str(x) if x>y else str(y)])
"""

