import turtle

wn = turtle.Screen()
wn.title("Cookie Clicker Game")
wn.bgcolor("black")

wn.register_shape("cookie.gif")

cookie = turtle.Turtle()


cookie.shape("cookie.gif")

cookie.speed(0)

clicks = 0

pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.up()
pen.goto(0, 400)
pen.write(f"Clicks: {clicks}", align="center", font=("New Courier", 32, "normal"))

def clicked(x, y):
    global clicks
    clicks += 1
    pen.clear()
    pen.write(f"Clicks: {clicks}", align="center",
              font=("New Courier", 32, "normal"))

cookie.onclick(clicked)

def p():

    global clicks

    if clicks >= 100:

        while True:

            clicks = clicks * 2

            pen.clear()

            pen.write(f"Clicks: {clicks}", align="center",
                      font=("New Courier", 32, "normal"))
    
    else:
        print("Not enough clicks to purchase automatic clicks!")

wn.onkeypress(p, "p")
    
wn.listen()



wn.mainloop()