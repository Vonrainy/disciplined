import tkinter as tk
import excelDataBase
import threading
import time
import sys

test = excelDataBase.DataXl()  # 初始化一个数据库
today_list = test.task_list  # 存放当天的任务，运行一次刷新一次，实在没辙了
num = 0  # 到底有几个有效任务


# def save_it1():
#     """将任务信息插入总任务表"""
#     start_hour1 = input_start_hour1.get()  # 获取输入的开始小时
#     start_minute1 = input_start_minute1.get()  # 获取输入的开始分钟
#     end_hour1 = input_end_hour1.get()  # 获取输入的结束小时
#     end_minute1 = input_end_minute1.get()  # 获取输入的结束分钟
#     task1 = input_task1.get()  # 获取输入的任务
#     start_time1 = f"{start_hour1}:{start_minute1}"  # 获得数据库里xx:xx的格式
#     end_time1 = f"{end_hour1}:{end_minute1}"  # 获得数据库里xx:xx的格式
#     list1 = [task1, end_time1, start_time1]  # 任务1，[任务，结束时间，开始时间]
#     test.task_list.append(list1)  # 将任务1插入总任务列表
#     print(test.task_list)
#
#
# def save_it2():
#     start_hour2 = input_start_hour2.get()  # 获取输入的开始小时
#     start_minute2 = input_start_minute2.get()  # 获取输入的开始分钟
#     end_hour2 = input_end_hour2.get()  # 获取输入的结束小时
#     end_minute2 = input_end_minute2.get()  # 获取输入的结束分钟
#     task2 = input_task2.get()  # 获取输入的任务
#     start_time2 = f"{start_hour2}:{start_minute2}"  # 获得数据库里xx:xx的格式
#     end_time2 = f"{end_hour2}:{end_minute2}"  # 获得数据库里xx:xx的格式
#     list2 = [task2, end_time2, start_time2]
#     test.task_list.append(list2)
#     print(test.task_list)
#
#
# def save_it3():
#     start_hour3 = input_start_hour3.get()  # 获取输入的开始小时
#     start_minute3 = input_start_minute3.get()  # 获取输入的开始分钟
#     end_hour3 = input_end_hour3.get()  # 获取输入的结束小时
#     end_minute3 = input_end_minute3.get()  # 获取输入的结束分钟
#     task3 = input_task3.get()  # 获取输入的任务
#     start_time3 = f"{start_hour3}:{start_minute3}"  # 获得数据库里xx:xx的格式
#     end_time3 = f"{end_hour3}:{end_minute3}"  # 获得数据库里xx:xx的格式
#     list3 = [task3, end_time3, start_time3]
#     test.task_list.append(list3)
#     print(test.task_list)
#

def save_it():
    global num
    start_hour1 = input_start_hour1.get()  # 获取输入的开始小时
    start_minute1 = input_start_minute1.get()  # 获取输入的开始分钟
    end_hour1 = input_end_hour1.get()  # 获取输入的结束小时
    end_minute1 = input_end_minute1.get()  # 获取输入的结束分钟
    task1 = input_task1.get()  # 获取输入的任务
    if task1 != "":
        num += 1
        start_time1 = f"{start_hour1}:{start_minute1}"  # 获得数据库里xx:xx的格式
        end_time1 = f"{end_hour1}:{end_minute1}"  # 获得数据库里xx:xx的格式
        list1 = [task1, end_time1, start_time1]  # 任务1，[任务，结束时间，开始时间]
        test.task_list.append(list1)  # 将任务1插入总任务列表

    start_hour2 = input_start_hour2.get()  # 获取输入的开始小时
    start_minute2 = input_start_minute2.get()  # 获取输入的开始分钟
    end_hour2 = input_end_hour2.get()  # 获取输入的结束小时
    end_minute2 = input_end_minute2.get()  # 获取输入的结束分钟
    task2 = input_task2.get()  # 获取输入的任务
    if task2 != "":
        num += 1
        start_time2 = f"{start_hour2}:{start_minute2}"  # 获得数据库里xx:xx的格式
        end_time2 = f"{end_hour2}:{end_minute2}"  # 获得数据库里xx:xx的格式
        list2 = [task2, end_time2, start_time2]
        test.task_list.append(list2)

    start_hour3 = input_start_hour3.get()  # 获取输入的开始小时
    start_minute3 = input_start_minute3.get()  # 获取输入的开始分钟
    end_hour3 = input_end_hour3.get()  # 获取输入的结束小时
    end_minute3 = input_end_minute3.get()  # 获取输入的结束分钟
    task3 = input_task3.get()  # 获取输入的任务
    if task3 != "":
        num += 1
        start_time3 = f"{start_hour3}:{start_minute3}"  # 获得数据库里xx:xx的格式
        end_time3 = f"{end_hour3}:{end_minute3}"  # 获得数据库里xx:xx的格式
        list3 = [task3, end_time3, start_time3]
        test.task_list.append(list3)

    start_hour4 = input_start_hour4.get()  # 获取输入的开始小时
    start_minute4 = input_start_minute4.get()  # 获取输入的开始分钟
    end_hour4 = input_end_hour4.get()  # 获取输入的结束小时
    end_minute4 = input_end_minute4.get()  # 获取输入的结束分钟
    task4 = input_task4.get()  # 获取输入的任务
    if task4 != "":
        num += 1
        start_time4 = f"{start_hour4}:{start_minute4}"  # 获得数据库里xx:xx的格式
        end_time4 = f"{end_hour4}:{end_minute4}"  # 获得数据库里xx:xx的格式
        list4 = [task4, end_time4, start_time4]
        test.task_list.append(list4)

    print(f"今天的任务列表: {test.task_list}")
    test.save_task(num)
    save_buttonVar.set("已保存")


def submit_it():
    global num
    rush_buttonVar.set("Let's go!")
    test.times_up(num)
    rush_buttonVar.set("Bravo!")


class MyThread(threading.Thread):
    def __init__(self, func, *args):
        super().__init__()

        self.func = func
        self.args = args

        self.setDaemon(True)
        self.start()  # 在这里开始

    def run(self):
        self.func(*self.args)


window = tk.Tk()  # 初始化窗口window
window.title("To Be Discipline")  # 窗口名
num_of_task = 4  # input("您今天几个安排: ")   # 任务数，最大行数
window_size = f"{int(num_of_task) * 250 + 50}x700"  # 根据任务数设定界面大小
window.geometry(window_size)
window.resizable(width=False, height=False)  # 不可变大小

'''任务栏目前只能4个，后续for循环增加'''
fm = tk.Frame(window, bg="#805D48", width=int(num_of_task) * 250 + 50, height=700)  # 主框架
fm_up = tk.Frame(window, bg="#FFDAB9", width=int(num_of_task) * 250 + 50, height=170)  # 最上方
fm1 = tk.Frame(window, bg="#DCAA96", width=200, height=400)  # 左任务
fm2 = tk.Frame(window, bg="#FFEBCF", width=200, height=400)  # 中任务
fm3 = tk.Frame(window, bg="#FFDAB9", width=200, height=400)  # 中任务
fm4 = tk.Frame(window, bg="#FFDEAD", width=200, height=400)  # 右任务

fm.place(x=0, y=0)
fm_up.place(x=0, y=0)
fm1.place(x=50, y=220)
fm2.place(x=300, y=220)
fm3.place(x=550, y=220)
fm4.place(x=800, y=220)
# lb_logo.place(x=0, y=0)

'''左侧输入开始时间部分'''
input_start_hour1 = tk.StringVar()  # 输入的小时
input_start_minute1 = tk.StringVar()  # 输入的分钟
input_start_hour1.set("")
input_start_minute1.set("")
input_start_hour1 = tk.Entry(fm1, bg="#DCAA96", width=5, textvariable=input_start_hour1)  # 时输入框
input_start_minute1 = tk.Entry(fm1, bg="#DCAA96", width=5, textvariable=input_start_minute1)  # 分输入框
lb11 = tk.Label(fm1, bg="#DCAA96", font=('Arial', 14), text=":")  # 冒号
input_start_hour1.place(x=54, y=100)
input_start_minute1.place(x=108, y=100)
lb11.place(x=95, y=95)

'''左侧输入结束时间部分'''
input_end_hour1 = tk.StringVar()  # 输入的小时
input_end_minute1 = tk.StringVar()  # 输入的分钟
input_end_hour1.set("")
input_end_minute1.set("")
input_end_hour1 = tk.Entry(fm1, bg="#DCAA96", width=5, textvariable=input_end_hour1)  # 时输入框
input_end_minute1 = tk.Entry(fm1, bg="#DCAA96", width=5, textvariable=input_end_minute1)  # 分输入框
lb12 = tk.Label(fm1, bg="#DCAA96", font=('Arial', 14), text=":")  # 冒号
input_end_hour1.place(x=54, y=125)
input_end_minute1.place(x=108, y=125)
lb12.place(x=95, y=120)

'''左侧输入任务部分'''
input_task1 = tk.StringVar()
input_task1.set("")
input_task1 = tk.Entry(fm1, bg="#DCAA96", width=13)
input_task1.place(x=54, y=200)

'''中侧输入开始时间部分'''
input_start_hour2 = tk.StringVar()  # 输入的小时
input_start_minute2 = tk.StringVar()  # 输入的分钟
input_start_hour2.set("")
input_start_minute2.set("")
input_start_hour2 = tk.Entry(fm2, bg="#FFEBCF", width=5, textvariable=input_start_hour2)  # 时输入框
input_start_minute2 = tk.Entry(fm2, bg="#FFEBCF", width=5, textvariable=input_start_minute2)  # 分输入框
lb21 = tk.Label(fm2, bg="#FFEBCF", font=('Arial', 14), text=":")  # 冒号
input_start_hour2.place(x=54, y=100)
input_start_minute2.place(x=108, y=100)
lb21.place(x=95, y=95)

'''中侧输入结束时间部分'''
input_end_hour2 = tk.StringVar()  # 输入的小时
input_end_minute2 = tk.StringVar()  # 输入的分钟
input_end_hour2.set("")
input_end_minute2.set("")
input_end_hour2 = tk.Entry(fm2, bg="#FFEBCF", width=5, textvariable=input_end_hour2)  # 时输入框
input_end_minute2 = tk.Entry(fm2, bg="#FFEBCF", width=5, textvariable=input_end_minute2)  # 分输入框
lb22 = tk.Label(fm2, bg="#FFEBCF", font=('Arial', 14), text=":")  # 冒号
input_end_hour2.place(x=54, y=125)
input_end_minute2.place(x=108, y=125)
lb22.place(x=95, y=120)

'''中侧输入任务部分'''
input_task2 = tk.StringVar()
input_task2.set("")
input_task2 = tk.Entry(fm2, bg="#FFEBCF", width=13)
input_task2.place(x=54, y=200)

'''右侧输入开始时间部分'''
input_start_hour3 = tk.StringVar()  # 输入的小时
input_start_minute3 = tk.StringVar()  # 输入的分钟
input_start_hour3.set("")
input_start_minute3.set("")
input_start_hour3 = tk.Entry(fm3, bg="#FFDAB9", width=5, textvariable=input_start_hour3)  # 时输入框
input_start_minute3 = tk.Entry(fm3, bg="#FFDAB9", width=5, textvariable=input_start_minute3)  # 分输入框
lb31 = tk.Label(fm3, bg="#FFDAB9", font=('Arial', 14), text=":")  # 冒号
input_start_hour3.place(x=54, y=100)
input_start_minute3.place(x=108, y=100)
lb31.place(x=95, y=95)

'''右侧输入结束时间部分'''
input_end_hour3 = tk.StringVar()  # 输入的小时
input_end_minute3 = tk.StringVar()  # 输入的分钟
input_end_hour3.set("")
input_end_minute3.set("")
input_end_hour3 = tk.Entry(fm3, bg="#FFDAB9", width=5, textvariable=input_end_hour3)  # 时输入框
input_end_minute3 = tk.Entry(fm3, bg="#FFDAB9", width=5, textvariable=input_end_minute3)  # 分输入框
lb32 = tk.Label(fm3, bg="#FFDAB9", font=('Arial', 14), text=":")  # 冒号
input_end_hour3.place(x=54, y=125)
input_end_minute3.place(x=108, y=125)
lb32.place(x=95, y=120)

'''右侧输入任务部分'''
input_task3 = tk.StringVar()
input_task3.set("")
input_task3 = tk.Entry(fm3, bg="#FFDAB9", width=13)
input_task3.place(x=54, y=200)

'''西侧输入开始时间部分'''
input_start_hour4 = tk.StringVar()  # 输入的小时
input_start_minute4 = tk.StringVar()  # 输入的分钟
input_start_hour4.set("")
input_start_minute4.set("")
input_start_hour4 = tk.Entry(fm4, bg="#FFDEAD", width=5, textvariable=input_start_hour4)  # 时输入框
input_start_minute4 = tk.Entry(fm4, bg="#FFDEAD", width=5, textvariable=input_start_minute4)  # 分输入框
lb41 = tk.Label(fm4, bg="#FFDEAD", font=('Arial', 14), text=":")  # 冒号
input_start_hour4.place(x=54, y=100)
input_start_minute4.place(x=108, y=100)
lb41.place(x=95, y=95)

'''西侧输入结束时间部分'''
input_end_hour4 = tk.StringVar()  # 输入的小时
input_end_minute4 = tk.StringVar()  # 输入的分钟
input_end_hour4.set("")
input_end_minute4.set("")
input_end_hour4 = tk.Entry(fm4, bg="#FFDEAD", width=5, textvariable=input_end_hour4)  # 时输入框
input_end_minute4 = tk.Entry(fm4, bg="#FFDEAD", width=5, textvariable=input_end_minute4)  # 分输入框
lb42 = tk.Label(fm4, bg="#FFDEAD", font=('Arial', 14), text=":")  # 冒号
input_end_hour4.place(x=54, y=125)
input_end_minute4.place(x=108, y=125)
lb42.place(x=95, y=120)

'''西侧输入任务部分'''
input_task4 = tk.StringVar()
input_task4.set("")
input_task4 = tk.Entry(fm4, bg="#FFDEAD", width=13)
input_task4.place(x=54, y=200)

'''提交按钮'''
rush_buttonVar = tk.StringVar()  # 提交按钮上的字
rush_buttonVar.set("开始")  # 初始化为“开始”
rush = tk.Button(window, width=20, textvariable=rush_buttonVar, command=lambda: MyThread(submit_it))
rush.place(x=530, y=660)  # (54,300)

# save1_buttonVar = tk.StringVar()
# save1_buttonVar.set("保存")
# save1 = tk.Button(fm1, textvariable=save1_buttonVar, command=lambda: save_it1())
# save1.place(x=54, y=300)
#
# save2_buttonVar = tk.StringVar()
# save2_buttonVar.set("保存")
# save2 = tk.Button(fm2, textvariable=save2_buttonVar, command=lambda: save_it2())
# save2.place(x=54, y=300)
#
# save3_buttonVar = tk.StringVar()
# save3_buttonVar.set("保存")
# save3 = tk.Button(fm3, textvariable=save3_buttonVar, command=lambda: save_it3())
# save3.place(x=54, y=300)

save_buttonVar = tk.StringVar()
save_buttonVar.set("保存全部")
save = tk.Button(window, width=20, textvariable=save_buttonVar, command=lambda: save_it())
save.place(x=370, y=660)


Label1 = tk.Label(bg="#FFDAB9", fg="#393939", font=("等线", 55), text=time.strftime('%H:%M', time.localtime(time.time())))
Label1.pack()
Label2 = tk.Label(bg="#FFDAB9", fg="#393939", font=("等线", 30), text=time.strftime('%Y. %m. %d', time.localtime(time.time())))
Label2.pack()


def trick_it():
    currentTime = time.strftime('%H:%M', time.localtime(time.time()))
    Label1.config(bg="#FFDAB9", fg="#393939", font=("等线", 55), text=currentTime)
    window.update()
    Label1.after(1000, trick_it)


Label1.after(1000, trick_it)

window.mainloop()
