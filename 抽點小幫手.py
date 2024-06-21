
import random
import tkinter as tk
from tkinter import ttk

data=0

def import_data():
    global class_list
    global class_dict
    class_list = []
    class_dict = {'學號':[],
                    '姓名':[],
                    '系級':[''],
                    '缺席次數':['']}
    filename = filename_entry.get()
    with open(filename, mode='r', encoding='utf-8') as file:
        for line in file:
            student_info = line.split(',')
            class_list.append(student_info[0]+student_info[1]+student_info[2]+" | 缺席次數:"+student_info[3])
            class_dict['學號'].append(student_info[0])
            class_dict['姓名'].append(student_info[2])
            class_dict['系級'].append(student_info[1][:-1])
            class_dict['缺席次數'].append('缺席次數:'+student_info[3][:-1])
    class_dict['缺席次數'].remove('缺席次數:')
    combobox1.configure(values=list(set(class_dict['系級'])))
    combobox2.configure(values=list(set(class_dict['缺席次數'])))

def draw(num=1):
    student_list = []
    for i in class_list:
        if (combobox1.get() in i) and (combobox2.get() in i):
            student_list.append(i)
    result_text =''   
    try:
        for student in random.sample(student_list,num):
            result_text += student   
            result_text += "\n"
        result.configure(text=result_text)
    except:
        result.configure(text='there is no student fit the criteria')

#主視窗
window = tk.Tk()
window.geometry("1100x200")
window.title("random select")


#輸入學生名單的檔案的路徑的輸入窗
filename_entry = tk.Entry(window)
filename_entry.grid(row=0,column=1,sticky='NSEW')

#確定傳入資料按鈕
import_data_button = tk.Button(window, text='import data',command=import_data)
import_data_button.grid(row=0,column=2)

#輸入學生名單的檔案的路徑的提示文字
filename_text = tk.Label(window,text='please enter file path:')
filename_text.grid(row=0,column=0,sticky='NSEW')


#輸入抽取數量的提示文字
select_number_text = tk.Label(window,text='please enter number you want to draw:')
select_number_text.grid(row=1,column=0,sticky='NSEW')
select_number_text = tk.Label(window,text='(do not exceed number of the students)')
select_number_text.grid(row=2,column=0,sticky='NSEW')

#輸入抽取數量的輸入窗口
select_number_entry = tk.Entry(window)
select_number_entry.grid(row=1,column=1,sticky='NSEW')

#確定要抽取按鈕
draw_button = tk.Button(window, text='draw',command=lambda:draw(int(select_number_entry.get())))
draw_button.grid(row=1,column=2)

#下拉式選單，篩選科系
combobox1 = ttk.Combobox(window, 
                            values=[''])
combobox1.grid(row=1,column=3)
#下拉式選單，篩選缺席次數
combobox2 = ttk.Combobox(window, 
                        values=['']) 
combobox2.grid(row=1,column=4)                        
#放置抽取結果的文字
result = tk.Label(window, width=28,justify='left')
result.grid(row=3,column=1)

window.mainloop()