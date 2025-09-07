
from turtle import Turtle, Screen
gugu = Turtle()



for _ in range(4):
    gugu.forward(100)
    gugu.left(90)
for _ in range(15):
    gugu.forward(10)
    gugu.penup()
    gugu.forward(10)
    gugu.pendown()

gugu.shape("turtle")
gugu.color("CornFlowerBlue")
gugu.forward(100)

fifi=Screen()
print(fifi.canvheight)
fifi.exitonclick()

from prettytable import PrettyTable

table=PrettyTable()
table.add_column("States", ["Delhi","Mumbai","Up","Kerala","Gujrat","Rajasthan"])
table.add_column("Foods", ["Momo","Vadapav","Pavbhaji","Dosa","Fafda","Ghevar"])
table.align = "l"

print(table)
