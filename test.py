from graphics import *

win = GraphWin("hi siree", 500, 500)
win.setCoords(0, 0, 6, 6)

Text(Point(3, 5.7), "Jay Forms").draw(win)
Text(Point(0, 5.4), "---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------").draw(win)

Rectangle(Point(1, 1), Point(5, 1.5)).draw(win)
Text(Point(3, 1.25), "After entering CLICK HERE").draw(win)

Text(Point(0.5, 4.4), "Name: ").draw(win)
name = Entry(Point(1.5, 4.4), 10).draw(win)
win.getMouse()
name1 = name.getText()

Text(Point(0.47, 4), "DOB: ").draw(win)
DOB = Entry(Point(1.5, 4), 10).draw(win)
DOB.setText("dd/mm/yyyy")
win.getMouse()
name2 = DOB.getText()

Text(Point(0.52, 3.6), "Mail ID: ").draw(win)
Mail_ID = Entry(Point(1.92, 3.6), 20).draw(win)
win.getMouse()
name3 = Mail_ID.getText()

Text(Point(0.42, 3.2), "Std: ").draw(win)
STD = Entry(Point(1.5, 3.2), 10).draw(win)
win.getMouse()
name4 = STD.getText()

Text(Point(0.42, 2.8), "Sec: ").draw(win)
SEC = Entry(Point(1.5, 2.8), 10).draw(win)
win.getMouse()
name5 = SEC.getText()

Text(Point(0.45, 2.4), "Date: ").draw(win)
Date = Entry(Point(1.5, 2.4), 10).draw(win)
win.getMouse()
name6 = Date.getText()

print("Name:\t\t", name1)
print("DOB:\t\t", name2)
print("Mail ID:\t", name3)
print("STD:\t\t", name4)
print("Sec:\t\t", name5)
print("Date:\t\t", name6)

def clear(win):
    for item in win.items[:]:
        item.undraw()
    win.update()

clear(win)

Text(Point(3, 3), "Your response has been submitted").draw(win)

win.getMouse()
win.close()

