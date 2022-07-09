import tkinter as tk

root = tk.Tk()
root.geometry()




display = tk.Entry(root)
display.grid(columnspan = 3, column = 0, row = 0)

num1key = tk.Button(root, text='1')
num1key.grid(column = 1, row = 2)

num2key = tk.Button(root, text = '2')
num2key.grid(column = 2, row = 2)

num3key = tk.Button(root, text = '3')
num3key.grid(column = 3, row = 2)

num4key = tk.Button(root, text = '4')
num4key.grid(column = 1, row = 3)

num5key = tk.Button(root, text = '5')
num5key.grid(column = 2, row = 3)

num6key = tk.Button(root, text = '6')
num6key.grid(column = 3, row = 3)

num7key = tk.Button(root, text = '6')
num7key.grid(column = 1, row = 4)

num8key = tk.Button(root, text = '8')
num8key.grid(column = 2, row = 4)

num9key = tk.Button(root, text = '9')
num9key.grid(column = 3, row = 4)

num0key = tk.Button(root, text = '0')
num0key.grid(column = 2, row = 5)
root.mainloop()
