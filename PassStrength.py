import tkinter
from tkinter import *
import tkinter.messagebox
from time import sleep
import string

#window stuff
discord_gray = "#262626"
root = Tk()
root.geometry("500x200")
root.config(bg=discord_gray)
root.title("Password Strength Evaluator")
root.resizable(width=False, height=False)
root.iconbitmap("D:\CyberSecurity\secure.ico")
special = "!@#$%^&*,./\][;l|`~"
label1 = Label(root,text="Input password:",bg=discord_gray,fg="white", font=50)
label1.place(x=0,y=0)



# Uppercase
label2 = Label(root, text="", bg=discord_gray, fg="white", font=50)
label2.place(x=280, y=10)
# LowerCase
label3 = Label(root, text="", bg=discord_gray, fg="white", font=50)
label3.place(x=280, y=40)
# Num
label4 = Label(root, text="", bg=discord_gray, fg="white", font=50)
label4.place(x=280, y=70)
# Special
label5 = Label(root, text="", bg=discord_gray, fg="white", font=50)
label5.place(x=280, y=100)
# Range
label6 = Label(root, text="", bg=discord_gray, fg="white", font=50)
label6.place(x=280, y=130)
# SUM
label7 = Label(root, text="", bg=discord_gray, fg="white", font=100)
label7.place(x=280, y=160)




#EntryBox
input1 = Entry(root,show="*")
input1.place(x=0,y=25)







###################everything above is GUI###################
def main():
    text = input1.get()
    strength = 0
    def entryAndNumCheck():
        nonlocal text, strength
        lower=0
        upper=0
        punctu=0
        nums=0
        bad=False
        good = False
        great = False
        lSum = 0
        uSum=0
        nSum=0
        pSum=0
        rSum=0

        print(text)
        if text != '':
            for x in text:
                # Num Check
                if x in string.digits:
                    nums += 1
                    label4.config(text=f"Numbers: {nums}")
                elif x not in string.digits:
                    label4.config(text=f"Numbers: {nums}")
                # Lower Check
                if x in string.ascii_lowercase:
                    lower += 1
                    label3.config(text=f"Lowercase: {lower}")
                elif x not in string.ascii_lowercase:
                    label3.config(text=f"Lowercase: {lower}")
                # Upper Check
                if x in string.ascii_uppercase:
                    upper += 1
                    label2.config(text=f"Uppercase: {upper}")
                elif x not in string.ascii_uppercase:
                    label2.config(text=f"Uppercase: {upper}")
                # Punc Check
                if x in string.punctuation:
                    punctu+=1
                    label5.config(text=f"Special Characters: {punctu}")
                elif x not in string.punctuation:
                    label5.config(text=f"Special Characters: {punctu}")
                # Good Range Check
                if len(text) >= 8 and len(text) <= 20:
                    if len(text) >=8 and len(text) <= 14:
                        good = True
                        label6.config(text=f"Text Length: Good")
                    elif len(text) >= 15 and len(text) <= 20:
                        great = True
                        label6.config(text=f"Text Length: Great")
                # Too Short Range Check
                elif len(text) < 8:
                    label6.config(text=f"Text Length: Too Short")
                    bad = True
                # Too Long Range Check
                elif len(text) > 21:
                    label6.config(text=f"Text Length: Too Long")
                    bad = True

                # Sum Calculator
                if lower > 0:
                    lSum = 10
                if upper > 0:
                    uSum = 10
                if nums > 0:
                    nSum = 10
                if punctu > 0:
                    pSum = 10
                if good == True:
                    rSum = 5
                if great == True:
                    rSum = 10
                if bad == True:
                    rSum = 0


                sum1 = int(lSum + uSum + nSum + pSum + rSum)
                sumFinal = sum1 * 2
                label7.config(text=f"Total: {sumFinal}/100", fg="RED")


        elif text == "":
            lower = 0
            upper = 0
            punctu = 0
            label4.config(text=f"Numbers: {nums}")
            label3.config(text=f"Lower: {lower}")
            label2.config(text=f"Upper: {upper}")
            label5.config(text=f"Special: {punctu}")
            label6.config(text=f"Text Length: ")
            label7.config(text=f"Total: ", fg="RED")
            tkinter.messagebox.showerror("Value Error", "Please Enter a Password")






    entryAndNumCheck()









##################### BUTTON #####################
button1 = Button(root,command=main,text="Enter",activebackground=discord_gray, activeforeground="white")
button1.place(x=0,y=50)



root.mainloop()