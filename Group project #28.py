from tkinter import *
import tkinter.messagebox as msg
from tkinter import font

#initialise window:
game = Tk()
game.title('Tic-Tac-Toe')


# labels
Label(game, text="competitor1 : X", font="times 18").grid(row=0, column=1)
Label(game, text="competitor2 : O", font="times 18").grid(row=0, column=2)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# for competitor1 sign = X and for competitor2 sign= O
mark = ''

# counting the no. of click
count = 0

fields = ["field"] * 10


def win(fields, sign):
    return ((fields[1] == fields[2] == fields[3] == sign)
            or (fields[1] == fields[4] == fields[7] == sign)
            or (fields[1] == fields[5] == fields[9] == sign)
            or (fields[2] == fields[5] == fields[8] == sign)
            or (fields[3] == fields[6] == fields[9] == sign)
            or (fields[3] == fields[5] == fields[7] == sign)
            or (fields[4] == fields[5] == fields[6] == sign)
            or (fields[7] == fields[8] == fields[9] == sign))


def checker(number):
    global count, mark, numbers

    # Check which flied is clicked

    if number == 1 and number in numbers:
        numbers.remove(number)
        #competitor1 will play if the value of count is even and for odd competitor2 will play - as 9 boxes are unclicked thus odd
        if count % 2 == 0:
            mark = 'X'
            fields[number] = mark
        elif count % 2 != 0:
            mark = 'O'
            fields[number] = mark

        box1.config(text=mark)
        count = count + 1
        sign = mark

        if (win(fields, sign) and sign == 'X'):
            msg.showinfo("Result", "Competitor1 outperformed Competitor2")
            game.destroy()
        elif (win(fields, sign) and sign == 'O'):
            msg.showinfo("Result", "Competitor2 outperformed Competitor1")
            game.destroy()

    if number == 2 and number in numbers:
        numbers.remove(number)

        if count % 2 == 0:
            mark = 'X'
            fields[number] = mark
        elif count % 2 != 0:
            mark = 'O'
            fields[number] = mark

        box2.config(text=mark)
        count = count + 1
        sign = mark

        if (win(fields, sign) and sign == 'X'):
            msg.showinfo("Result", "Competitor1 has succeeded")
            game.destroy()
        elif (win(fields, sign) and sign == 'O'):
            msg.showinfo("Result", "Competitor2 has succeeded")
            game.destroy()

    if number == 3 and number in numbers:
        numbers.remove(number)

        if count % 2 == 0:
            mark = 'X'
            fields[number] = mark
        elif count % 2 != 0:
            mark = 'O'
            fields[number] = mark

        box3.config(text=mark)
        count = count + 1
        sign = mark

        if (win(fields, sign) and sign == 'X'):
            msg.showinfo("Result", "Competitor1 won the day")
            game.destroy()
        elif (win(fields, sign) and sign == 'O'):
            msg.showinfo("Result", "Competitor2 won the day")
            game.destroy()

    if number == 4 and number in numbers:
        numbers.remove(number)

        if count % 2 == 0:
            mark = 'X'
            fields[number] = mark
        elif count % 2 != 0:
            mark = 'O'
            fields[number] = mark

        box4.config(text=mark)
        count = count + 1
        sign = mark

        if (win(fields, sign) and sign == 'X'):
            msg.showinfo("Result", "Competitor1 has absolutely prevailed")
            game.destroy()
        elif (win(fields, sign) and sign == 'O'):
            msg.showinfo("Result", "Competitor2 has absolutely prevailed")
            game.destroy()

    if number == 5 and number in numbers:
        numbers.remove(number)

        if count % 2 == 0:
            mark = 'X'
            fields[number] = mark
        elif count % 2 != 0:
            mark = 'O'
            fields[number] = mark

        box5.config(text=mark)
        count = count + 1
        sign = mark

        if (win(fields, sign) and sign == 'X'):
            msg.showinfo("Result", "Competitor1 destroyed Competitor2")
            game.destroy()
        elif (win(fields, sign) and sign == 'O'):
            msg.showinfo("Result", "Competitor2 destroyed Competitor1")
            game.destroy()

    if number == 6 and number in numbers:
        numbers.remove(number)

        if count % 2 == 0:
            mark = 'X'
            fields[number] = mark
        elif count % 2 != 0:
            mark = 'O'
            fields[number] = mark

        box6.config(text=mark)
        count = count + 1
        sign = mark

        if (win(fields, sign) and sign == 'X'):
            msg.showinfo("Result", "Competitor1 swept the board")
            game.destroy()
        elif (win(fields, sign) and sign == 'O'):
            msg.showinfo("Result", "Competitor2 swept the board")
            game.destroy()

    if number == 7 and number in numbers:
        numbers.remove(number)

        if count % 2 == 0:
            mark = 'X'
            fields[number] = mark
        elif count % 2 != 0:
            mark = 'O'
            fields[number] = mark

        box7.config(text=mark)
        count = count + 1
        sign = mark

        if (win(fields, sign) and sign == 'X'):
            msg.showinfo("Result", "Competitor1 is victorious")
            game.destroy()
        elif (win(fields, sign) and sign == 'O'):
            msg.showinfo("Result", "Competitor2 is victorious")
            game.destroy()

    if number == 8 and number in numbers:
        numbers.remove(number)

        if count % 2 == 0:
            mark = 'X'
            fields[number] = mark
        elif count % 2 != 0:
            mark = 'O'
            fields[number] = mark

        box8.config(text=mark)
        count = count + 1
        sign = mark

        if (win(fields, sign) and sign == 'X'):
            msg.showinfo("Result", "Whooo Competitor1 wins")
            game.destroy()
        elif (win(fields, sign) and sign == 'O'):
            msg.showinfo("Result", "Whooo Competitor2 wins")
            game.destroy()

    if number == 9 and number in numbers:
        numbers.remove(number)

        if count % 2 == 0:
            mark = 'X'
            fields[number] = mark
        elif count % 2 != 0:
            mark = 'O'
            fields[number] = mark

        box9.config(text=mark)
        count = count + 1
        sign = mark

        if (win(fields, sign) and sign == 'X'):
            msg.showinfo("Result", "Whooo Competitor1 rocks")
            game.destroy()
        elif (win(fields, sign) and sign == 'O'):
            msg.showinfo("Result", "Whooo Competitor2 rocks")
            game.destroy()

    #if count is greater then 8 then the match has been tied
    if (count > 8 and win(fields, 'X') == False and win(fields, 'O') == False):
        msg.showinfo("Result", "Match Tied")
        game.destroy()


#define boxes
font_nw = ("Bradley Hand ITC 27 bold", 18, "bold")

box1 = Button(game, width=15, font=font_nw, height=7, command=lambda: checker(1))
box1.grid(row=1, column=1)
box2 = Button(game, width=15, height=7, font=font_nw, command=lambda: checker(2))
box2.grid(row=1, column=2)
box3 = Button(game, width=15, height=7, font=font_nw, command=lambda: checker(3))
box3.grid(row=1, column=3)
box4 = Button(game, width=15, height=7, font=font_nw, command=lambda: checker(4))
box4.grid(row=2, column=1)
box5 = Button(game, width=15, height=7, font=font_nw, command=lambda: checker(5))
box5.grid(row=2, column=2)
box6 = Button(game, width=15, height=7, font=font_nw, command=lambda: checker(6))
box6.grid(row=2, column=3)
box7 = Button(game, width=15, height=7, font=font_nw, command=lambda: checker(7))
box7.grid(row=3, column=1)
box8 = Button(game, width=15, height=7, font=font_nw, command=lambda: checker(8))
box8.grid(row=3, column=2)
box9 = Button(game, width=15, height=7, font=font_nw, command=lambda: checker(9))
box9.grid(row=3, column=3)

#change the colour of the symbols and boxes to your liking
box1.config(fg='darkblue', bg='cornsilk')
box2.config(fg='darkblue', bg='antiquewhite2')
box3.config(fg='darkblue', bg='cornsilk')
box4.config(fg='darkblue', bg='antiquewhite2')
box5.config(fg='darkblue', bg='cornsilk')
box6.config(fg='darkblue', bg='antiquewhite2')
box7.config(fg='darkblue', bg='cornsilk')
box8.config(fg='darkblue', bg='antiquewhite2')
box9.config(fg='darkblue', bg='cornsilk')



game.mainloop()

