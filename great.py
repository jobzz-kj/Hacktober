x=int(input())
y=int(input())
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

