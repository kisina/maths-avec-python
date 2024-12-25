import turtle
import math

def draw_spiral(t, color, size, angle_increment, step_increment):
    t.pencolor(color)
    t.width(2)
    t.speed(0)

    angle = 0
    step = 0

    for _ in range(360):
        x = step * math.cos(math.radians(angle))
        y = step * math.sin(math.radians(angle))

        t.goto(x, y)

        angle += angle_increment
        step += step_increment

def main():
    screen = turtle.Screen()
    screen.bgcolor("black")

    # Create two turtle objects
    spiral1 = turtle.Turtle()
    spiral2 = turtle.Turtle()

    spiral1.penup()
    spiral2.penup()

    # Positioning the turtles
    spiral1.goto(0, 0)
    spiral2.goto(0, 0)

    spiral1.pendown()
    spiral2.pendown()

    # Draw spirals
    draw_spiral(spiral1, "cyan", size=2, angle_increment=5, step_increment=0.5)
    draw_spiral(spiral2, "magenta", size=2, angle_increment=-5, step_increment=0.5)

    # Hide turtles
    spiral1.hideturtle()
    spiral2.hideturtle()

    screen.mainloop()

if __name__ == "__main__":
    main()
