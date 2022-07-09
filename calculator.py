import tkinter as tk
from PIL import ImageTk, Image


root = tk.Tk()
root.geometry()


def testFun(num):
	display.insert(tk.END, num)
	
display = tk.Entry(root)
display.grid(columnspan = 3, column = 1, row = 0)

# Number Keys

num1key = tk.Button(root, text='1', command = lambda:testFun(1))
num1key.grid(column = 1, row = 2)

num2key = tk.Button(root, text = '2', command = lambda:testFun(2))
num2key.grid(column = 2, row = 2)

num3key = tk.Button(root, text = '3', command = lambda:testFun(3))
num3key.grid(column = 3, row = 2)

num4key = tk.Button(root, text = '4', command = lambda:testFun(4))
num4key.grid(column = 1, row = 3)

num5key = tk.Button(root, text = '5', command = lambda:testFun(5))
num5key.grid(column = 2, row = 3)

num6key = tk.Button(root, text = '6', command = lambda:testFun(6))
num6key.grid(column = 3, row = 3)

num7key = tk.Button(root, text = '6', command = lambda:testFun(7))
num7key.grid(column = 1, row = 4)

num8key = tk.Button(root, text = '8', command = lambda:testFun(8))
num8key.grid(column = 2, row = 4)

num9key = tk.Button(root, text = '9', command = lambda:testFun(9))
num9key.grid(column = 3, row = 4)

num0key = tk.Button(root, text = '0', command = lambda:testFun(0))
num0key.grid(column = 2, row = 5)

# Operator keys

root.mainloop()
