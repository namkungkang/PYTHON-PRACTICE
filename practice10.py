#계산기 만들기
# from tkinter import *

# window = Tk()
# window.title("계산기")
# window.geometry('350x200')

# Label(window, text = "숫자 1").grid(column = 0, row = 0)
# Label(window, text = "숫자 2").grid(column = 0, row = 1)
# res_label = Label(window, text = " 결과 :")
# res_label.grid(column = 0, row = 2)
# num1 = Entry(window, width = 10)
# num2 = Entry(window, width = 10)
# num1.grid(column=1,row =0)
# num2.grid(column=1,row =1)

# def add() :
#     res_text = "결과 = " +str(float(num1.get()) + float(num2.get()))
#     res_label.configure(text = res_text)

# def subtract() :
#     res_text = "결과 = " +str(float(num1.get()) - float(num2.get()))
#     res_label.configure(text = res_text)


# def multiplication() :
#     res_text = "결과 = " +str(float(num1.get()) * float(num2.get()))
#     res_label.configure(text = res_text)


# def division() :
#     res_text = "결과 = " +str(float(num1.get()) / float(num2.get()))
#     res_label.configure(text = res_text)

# btn_plus = Button(window, text = "+", command = add)
# btn_minus = Button(window, text = "-", command = subtract)
# btn_mult = Button(window, text = "*", command = multiplication)
# btn_div = Button(window, text = "/", command = division)
# btn_plus.grid(column=2,row=1)
# btn_minus.grid(column=3,row=1)
# btn_mult.grid(column=4,row=1)
# btn_div.grid(column=5,row=1)
# window.mainloop()

#파일 쓰기
# fname = input('입력할 파일의 이름 :')
# f = open(fname, 'r')
# n = 1
# l = f.readline()
# while l :
#     print('{:3d}:{}'.format(n,l),end = '')
#     n +=1
#     l = f.readline()
