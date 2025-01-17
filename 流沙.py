import tkinter as tk
import keyboard  # 使用 keyboard 库来监听全局快捷键
from tkinter import font

# 定义一个列表来保存所有的倒计时窗口
countdown_windows = []


def keep_on_top(window):
    window.attributes("-topmost", True)
    window.after(1000, keep_on_top, window)


def countdown(label, counter, repeat_reset_time):
    counter -= 1
    label.config(text=str(counter))
    if counter >= 0:
        label.after(1000, countdown, label, counter, repeat_reset_time)
    else:
        label.config(text=str(repeat_reset_time))
        countdown(label, repeat_reset_time, repeat_reset_time)


def create_window(position, custom_font, initial_counter, repeat_time):
    bg_color = "black"
    window = tk.Toplevel()
    window.attributes("-topmost", True)
    window.attributes("-transparentcolor", bg_color)
    window.overrideredirect(True)

    # 10是默认展示，没有用
    label = tk.Label(window, text="10", font=custom_font, fg="white", bg=bg_color)
    label.pack()

    x, y = position
    window.geometry(f"+{x}+{y}")

    keep_on_top(window)

    countdown(label, initial_counter, repeat_time)

    # 将窗口添加到列表中以便后续可以关闭它
    countdown_windows.append(window)


def reset_countdown():
    # 关闭所有打开的倒计时窗口
    for window in countdown_windows:
        window.destroy()
    countdown_windows.clear()  # 清空倒计时窗口列表
    begin()  # 重新开始计数


def begin():
    print("流沙黄点开始计时！")
    initial_times = [90, 90, 120, 150, 180, 180, 210, 210, 400, 400]
    # 左边小，右边小，左灯上小，右灯上小，左灯下小，右灯小小，左中大，右中大，左边大，右边大
    positions = [(2312, 215), (2520, 215), (2358, 250), (2472, 250),
                 (2388, 285), (2440, 285), (2395, 235), (2440, 235),
                 (2323, 300), (2507, 300)]
    repeat_time1 = 120
    repeat_time2 = 180
    for i, pos in enumerate(positions):
        if i < 4:
            create_window(pos, custom_font, initial_times[i], repeat_time1)
        else:
            create_window(pos, custom_font, initial_times[i], repeat_time2)


def reset_countdown():
    # 首先检查现有窗口是否存在，若存在则销毁
    for window in countdown_windows:
        window.destroy()
    countdown_windows.clear()

    # 使用 root.after() 来调用 begin()，确保 begin() 在主线程中运行
    root.after(0, begin)


def clear_all():
    # 首先关闭所有的倒计时窗口
    for window in countdown_windows:
        window.destroy()
    countdown_windows.clear()  # 清空倒计时窗口列表

    print("计时器已清除。")  # 提示用户所有内容已被清除


if __name__ == "__main__":
    print("希望大家游戏愉快，如果遇到一只灰太狼，请爱护他。")
    print("请以管理员模式运行！当人物进入流沙地图时开始计时。")
    print("按下ctrl+shift+;开始计时！")
    print("按下ctrl+shift+'清除计时器！")
    print("退出请直接点击程序右上角。")

    # 创建 Tk 实例和自定义字体
    root = tk.Tk()
    root.withdraw()  # 与之前的定义相同...

    custom_font = font.Font(family="Helvetica", size=8)

    # 注册快捷键，当按下时调用 reset_countdown
    keyboard.add_hotkey('ctrl+shift+;', reset_countdown)
    keyboard.add_hotkey('ctrl+shift+\'', clear_all)

    try:
        root.mainloop()  # 主事件循环
    except KeyboardInterrupt:
        print('程序已经通过按键中断退出。')

# 打包代码   pyinstaller --onefile 流沙.py
