from turtle import*

len=100
sides=3
ang=360/sides
T=18

for m in range(T):
  for n in range(sides):
    forward(len)
    left(ang)
    left(20)