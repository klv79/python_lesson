import turtle
import time
class TrafficLight:
    def __init__(self, c):
        self.color = c
        self.running()

    def running(self):
        turtle.title("Мой светофор")
        circle = turtle.Turtle()
        circle.hideturtle()
        circle.speed(0)
        circle.color(self.color)
        circle.begin_fill()
        circle.dot(20)
        circle.penup()
        circle.goto(0, -100)
        circle.pendown()
        circle.circle(100)
        circle.end_fill()
        turtle.clear()


a = TrafficLight('red')
time.sleep(7)
b = TrafficLight('yellow')
time.sleep(2)
c = TrafficLight('green')
time.sleep(3)
exit()

turtle.exitonclick()

