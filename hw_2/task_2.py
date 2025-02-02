import os
import turtle

os.environ['TK_SILENCE_DEPRECATION'] = '1'

def koch(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        size /= 3
        koch(t, order - 1, size)
        t.left(60)
        koch(t, order - 1, size)
        t.right(120)
        koch(t, order - 1, size)
        t.left(60)
        koch(t, order - 1, size)

def snowflake(t, order, size):
    for _ in range(3):
        koch(t, order, size)
        t.right(120)

def main():
    try:
        order = int(input("Enter recursion level (рекомендовано 3-5): "))
    except ValueError:
        print("Будь ласка, введіть ціле число.")
        return

    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.title("Koch Snowflake")
    screen.bgcolor("white")

    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("red")
    pen.penup()
    pen.goto(-150, 50)
    pen.pendown()

    snowflake(pen, order, 300)
    turtle.done()

if __name__ == "__main__":
    main()