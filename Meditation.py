from guizero import App, Picture, PushButton, Window, Box
from playsound import playsound


# Here are all the def, arranged properly
def play():
    playsound('Meditation.mp3', block=False)


def play2():
    playsound('Stress.mp3', block=False)


def play3():
    playsound('Water.mp3', block=False)


def play4():
    playsound('Growth.mp3', block=False)


def open_window():
    window.show()

    for i in range(3, 14):
        str = f"window{i}.hide()"
        eval(str)
    app.hide()


def open_window2():
    window2.show()
    window.hide()

    for i in range(3, 14):
        str = f"window2{i}.hide()"
        eval(str)
    app.hide()


# This window has more lines compared to other def
def open_window3():
    window.hide()
    window2.hide()
    window3.show()
    window11.hide()
    window12.hide()
    window13.hide()
    app.hide()

    # Because the loop that was made still doesn't hide these specific windows
    for i in range(3, 14):
        str = f"window3{i}.hide()"
        eval(str)


def open_window4():
    window.hide()
    window4.show()
    window3.hide()

    for i in range(3, 14):
        str = f"window4{i}.hide()"
        eval(str)
    app.hide()


def open_window5():
    window.hide()
    window5.show()
    window3.hide()

    for i in range(3, 14):
        str = f"window5{i}.hide()"
        eval(str)
    app.hide()


def open_window6():
    window.hide()
    window6.show()
    window3.hide()

    for i in range(3, 14):
        str = f"window6{i}.hide()"
        eval(str)
    app.hide()


def open_window7():
    window.hide()
    window7.show()
    window3.hide()

    for i in range(3, 14):
        str = f"window7{i}.hide()"
        eval(str)
    app.hide()


def open_window8():
    window.hide()
    window8.show()
    window3.hide()

    for i in range(3, 14):
        str = f"window8{i}.hide()"
        eval(str)
    app.hide()


def open_window9():
    window.hide()
    window9.show()
    window3.hide()

    for i in range(3, 14):
        str = f"window9{i}.hide()"
        eval(str)
    app.hide()


def open_window10():
    window.hide()
    window10.show()
    window3.hide()

    for i in range(3, 14):
        str = f"window10{i}.hide()"
        eval(str)
    app.hide()


def open_window11():
    window.hide()
    window11.show()
    window3.hide()
    app.hide()
    playsound('Stress.mp3', block=False)

    for i in range(3, 14):
        str = f"window11{i}.hide()"
        eval(str)


def open_window12():
    window.hide()
    window12.show()
    window3.hide()
    playsound('Water.mp3', block=False)
    app.hide()

    for i in range(3, 14):
        str = f"window12{i}.hide()"
        eval(str)


def open_window13():
    window.hide()
    window13.show()
    window2.hide()
    window3.hide()
    playsound('Growth.mp3', block=False)
    app.hide()

    for i in range(3, 14):
        str = f"window13{i}.hide()"
        eval(str)


def close_window():
    window.hide()
    app.show()


def close_window2():
    window2.hide()
    window.show()


def close_window3():
    window3.hide()
    app.show()


def close_window4():
    window4.hide()
    window3.show()


def close_window5():
    window5.hide()
    window3.show()


def close_window6():
    window6.hide()
    window3.show()


def close_window7():
    window7.hide()
    window3.show()


def close_window8():
    window8.hide()
    window3.show()


def close_window9():
    window9.hide()
    window3.show()


def close_window10():
    window10.hide()
    window3.show()


def close_window11():
    window11.hide()
    app.show()


def close_window12():
    window12.hide()
    app.show()


def close_window13():
    window13.hide()
    app.show()


# This function exits the whole app, including other windows
def exit():
    app.destroy()


# This def also has more lines for the same reason as line 42
def home():
    window.hide()
    window2.hide()
    window11.hide()
    window12.hide()
    window13.hide()
    app.show()

    for i in range(3, 14):
        str = f"app{i}.hide()"
        eval(str)


# Widgets to be customized for the size of the buttons, windows, and it's placed in every window
app = App(height=680, width=450)

box1 = Box(app, align="bottom", width=500, height=50)
window = Window(app, height=680, width=450)
box2 = Box(window, align="bottom", width=500, height=50)
window2 = Window(app, height=680, width=450)
box3 = Box(window2, align="bottom", width=500, height=50)
window3 = Window(app, height=680, width=450)
box4 = Box(window3, align="bottom", width=500, height=50)
window4 = Window(app, height=500, width=500)
box5 = Box(window4, align="bottom", width=500, height=50)
window5 = Window(app, height=500, width=450)
box6 = Box(window5, align="bottom", width=500, height=50)
window6 = Window(app, height=530, width=450)
box7 = Box(window6, align="bottom", width=500, height=50)
window7 = Window(app, height=530, width=450)
box8 = Box(window7, align="bottom", width=500, height=50)
window8 = Window(app, height=450, width=500)
box9 = Box(window8, align="bottom", width=500, height=50)
window9 = Window(app, height=500, width=500)
box10 = Box(window9, align="bottom", width=500, height=50)
window10 = Window(app, height=500, width=500)
box11 = Box(window10, align="bottom", width=500, height=50)
window11 = Window(app, height=500, width=500)
box12 = Box(window11, align="bottom", width=500, height=50)
window12 = Window(app, height=500, width=500)
box13 = Box(window12, align="bottom", width=500, height=50)
window13 = Window(app, height=500, width=500)
box14 = Box(window13, align="bottom", width=500, height=50)
window.hide()
for i in range(2, 14):
    str = f"window{i}.hide()"
    eval(str)

# Widgets for the background pictures in all, of the windows
picture = Picture(app,
                  image="img/meditation background.jpg",
                  height=300,
                  width=500)

# Commands make the buttons useful, and it links back to the function of def
button13: PushButton = PushButton(app,
                                  image="img/play.png",
                                  align="top",
                                  height=50,
                                  width=50,
                                  command=play)

button3: PushButton = PushButton(app,
                                 image="img/right arrow.jpg",
                                 align="right",
                                 height=80,
                                 width=40,
                                 command=open_window)
button4 = PushButton(app,
                     image="img/left arrow.jpg",
                     align="left",
                     height=80,
                     width=40)
button8 = PushButton(app,
                     image="img/Stress and Anxiety.jpg",
                     height=180,
                     width=250,
                     command=open_window11)
# This includes gifs and other pictures
picture1 = Picture(window11, image="img/Nature.gif", height=500, width=500)

bottom_button0 = PushButton(box1,
                            image="img/Home.jpg",
                            align="left",
                            height=40,
                            width=140,
                            command=close_window3)
bottom_button00 = PushButton(box1,
                             image="img/Daily Bread.jpg",
                             align="left",
                             height=40,
                             width=150,
                             command=open_window3)
bottom_button1 = PushButton(box1,
                            image="img/Exit.jpg",
                            align="left",
                            height=40,
                            width=140,
                            command=exit)

picture2 = Picture(window,
                   image="img/meditation background.jpg",
                   height=300,
                   width=500)

button03 = PushButton(window,
                      image="img/right arrow.jpg",
                      align="right",
                      height=80,
                      width=40,
                      command=open_window2)
button04 = PushButton(window,
                      image="img/left arrow.jpg",
                      align="left",
                      height=80,
                      width=40,
                      command=close_window)
button08 = PushButton(window,
                      image="img/Falling asleep and waking up.jpg",
                      height=180,
                      width=250,
                      command=open_window12)
picture4 = Picture(window12, image="img/Family.gif", height=500, width=500)

bottom_button000 = PushButton(box2,
                              image="img/Home.jpg",
                              align="left",
                              height=40,
                              width=140,
                              command=home)
bottom_button001 = PushButton(box2,
                              image="img/Daily Bread.jpg",
                              align="left",
                              height=40,
                              width=150,
                              command=open_window3)
bottom_button002 = PushButton(box2,
                              image="img/Exit.jpg",
                              align="left",
                              height=40,
                              width=140,
                              command=exit)

picture5 = Picture(window2,
                   image="img/meditation background.jpg",
                   height=300,
                   width=500)

button005 = PushButton(window2,
                       image="img/right arrow.jpg",
                       align="right",
                       height=80,
                       width=40)
button006 = PushButton(window2,
                       image="img/left arrow.jpg",
                       align="left",
                       height=80,
                       width=40,
                       command=close_window2)
button007 = PushButton(window2,
                       image="img/Personal Growth.jpg",
                       height=180,
                       width=250,
                       command=open_window13)
pictures = Picture(window13, image="img/Growth.gif", height=500, width=500)

bottom_button003 = PushButton(box3,
                              image="img/Home.jpg",
                              align="left",
                              height=40,
                              width=140,
                              command=home)
bottom_button004 = PushButton(box3,
                              image="img/Daily Bread.jpg",
                              align="left",
                              height=40,
                              width=150,
                              command=open_window3)
bottom_button005 = PushButton(box3,
                              image="img/Exit.jpg",
                              align="left",
                              height=40,
                              width=140,
                              command=exit)

button01 = PushButton(window3,
                      image="img/Psalm.jpg",
                      height=80,
                      width=500,
                      command=open_window4)
picture8 = Picture(window4, image="img/psalms 145.jpeg", height=500, width=500)
button9 = PushButton(window3,
                     image="img/Deuteronomy.jpg",
                     height=80,
                     width=500,
                     command=open_window5)
picture7 = Picture(window5,
                   image="img/Deuteronomy 31.jpg",
                   height=500,
                   width=500)
button10 = PushButton(window3,
                      image="img/Matthew.jpg",
                      height=80,
                      width=500,
                      command=open_window6)
picture6 = Picture(window6, image="img/Matthew 11.jpg", height=500, width=500)
button11 = PushButton(window3,
                      image="img/Isaiah 41.jpg",
                      height=80,
                      width=500,
                      command=open_window7)
picture0 = Picture(window7, image="img/Isaiah 41 10.jpg", height=500, width=500)
button12 = PushButton(window3,
                      image="img/Isaiah 43.jpg",
                      height=80,
                      width=500,
                      command=open_window8)
picture13 = Picture(window8,
                    image="img/Isaiah 43 2.jpg",
                    height=420,
                    width=500)
button80 = PushButton(window3,
                      image="img/Peter.jpg",
                      height=80,
                      width=500,
                      command=open_window9)
picture04 = Picture(window9, image="img/1 Peter 5.jpg", height=500, width=500)
button90 = PushButton(window3,
                      image="img/Philippians.jpg",
                      height=80,
                      width=500,
                      command=open_window10)
picture30 = Picture(window10,
                    image="img/Philippians 4 6-7.png",
                    height=500,
                    width=500)

bottom_button09 = PushButton(box4,
                             image="img/Home.jpg",
                             align="left",
                             height=40,
                             width=140,
                             command=close_window3)
bottom_button08 = PushButton(box4,
                             image="img/Daily Bread.jpg",
                             align="left",
                             height=40,
                             width=150)
bottom_button21 = PushButton(box4,
                             image="img/Exit.jpg",
                             align="left",
                             height=40,
                             width=140,
                             command=exit)

bottom_button43 = PushButton(box5,
                             image="img/Home.jpg",
                             align="left",
                             height=40,
                             width=160,
                             command=open_window)
bottom_button36 = PushButton(box5,
                             image="img/Daily Bread.jpg",
                             align="left",
                             height=40,
                             width=160,
                             command=close_window4)
bottom_button22 = PushButton(box5,
                             image="img/Exit.jpg",
                             align="left",
                             height=40,
                             width=160,
                             command=exit)

bottom_button23 = PushButton(box6,
                             image="img/Home.jpg",
                             align="left",
                             height=40,
                             width=160,
                             command=open_window)
bottom_button48 = PushButton(box6,
                             image="img/Daily Bread.jpg",
                             align="left",
                             height=40,
                             width=160,
                             command=close_window5)
bottom_button58 = PushButton(box6,
                             image="img/Exit.jpg",
                             align="left",
                             height=40,
                             width=160,
                             command=exit)

bottom_button65 = PushButton(box7,
                             image="img/Home.jpg",
                             align="left",
                             height=40,
                             width=160,
                             command=open_window)
bottom_button69 = PushButton(box7,
                             image="img/Daily Bread.jpg",
                             align="left",
                             height=40,
                             width=160,
                             command=close_window6)
bottom_button68 = PushButton(box7,
                             image="img/Exit.jpg",
                             align="left",
                             height=40,
                             width=160,
                             command=exit)

bottom_button67 = PushButton(box8,
                             image="img/Home.jpg",
                             align="left",
                             height=40,
                             width=160,
                             command=open_window)
bottom_button63 = PushButton(box8,
                             image="img/Daily Bread.jpg",
                             align="left",
                             height=40,
                             width=160,
                             command=close_window7)
bottom_button83 = PushButton(box8,
                             image="img/Exit.jpg",
                             align="left",
                             height=40,
                             width=160,
                             command=exit)

bottom_button71 = PushButton(box9,
                             image="img/Home.jpg",
                             align="left",
                             height=40,
                             width=160,
                             command=open_window)
bottom_button81 = PushButton(box9,
                             image="img/Daily Bread.jpg",
                             align="left",
                             height=40,
                             width=160,
                             command=close_window8)
bottom_button98 = PushButton(box9,
                             image="img/Exit.jpg",
                             align="left",
                             height=40,
                             width=160,
                             command=exit)

bottom_button85 = PushButton(box10,
                             image="img/Home.jpg",
                             align="left",
                             height=40,
                             width=160,
                             command=open_window)
bottom_button57 = PushButton(box10,
                             image="img/Daily Bread.jpg",
                             align="left",
                             height=40,
                             width=160,
                             command=close_window9)
bottom_button55 = PushButton(box10,
                             image="img/Exit.jpg",
                             align="left",
                             height=40,
                             width=160,
                             command=exit)

bottom_button51 = PushButton(box11,
                             image="img/Home.jpg",
                             align="left",
                             height=40,
                             width=160,
                             command=open_window)
bottom_button59 = PushButton(box11,
                             image="img/Daily Bread.jpg",
                             align="left",
                             height=40,
                             width=160,
                             command=close_window10)
bottom_button74 = PushButton(box11,
                             image="img/Exit.jpg",
                             align="left",
                             height=40,
                             width=160,
                             command=exit)

bottom_button70 = PushButton(box12,
                             image="img/Home.jpg",
                             align="left",
                             height=40,
                             width=160,
                             command=open_window)
bottom_button90 = PushButton(box12,
                             image="img/Daily Bread.jpg",
                             align="left",
                             height=40,
                             width=160,
                             command=open_window3)
bottom_button18 = PushButton(box12,
                             image="img/Exit.jpg",
                             align="left",
                             height=40,
                             width=160,
                             command=exit)

bottom_button92 = PushButton(box13,
                             image="img/Home.jpg",
                             align="left",
                             height=40,
                             width=160,
                             command=open_window)
bottom_button72 = PushButton(box13,
                             image="img/Daily Bread.jpg",
                             align="left",
                             height=40,
                             width=160,
                             command=open_window3)
bottom_button93 = PushButton(box13,
                             image="img/Exit.jpg",
                             align="left",
                             height=40,
                             width=160,
                             command=exit)

bottom_button28 = PushButton(box14,
                             image="img/Home.jpg",
                             align="left",
                             height=40,
                             width=160,
                             command=open_window)
bottom_button38 = PushButton(box14,
                             image="img/Daily Bread.jpg",
                             align="left",
                             height=40,
                             width=160,
                             command=open_window3)
bottom_button49 = PushButton(box14,
                             image="img/Exit.jpg",
                             align="left",
                             height=40,
                             width=160,
                             command=exit)

app.display()
