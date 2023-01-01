def perfectSquares(l, r):
 a=[]
 a=[i for i in range(l, r + 1)
    if (i ** (.5) == int(i ** (.5)))]
 print(a, end=" ")
l=int(input("enter the lowercase:"))
r=int(input("enter the uppercase:"))
perfectSquares(l, r)