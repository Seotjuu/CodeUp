## CodeUp :: 6064

a,b,c= map(int,input().split())
End=(a if a<b else b) if ((a if a<b else b) <c) else c
print(End)
