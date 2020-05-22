# coding: utf-8
#Copyright (c) 2020. LSHT LLC.
"""
自建函数库 实用小函数
"""
def help(function_name="help"):
    if function_name == "help":
        print("help [function_name] ")
    if function_name == "":
        print("help [function_name] ")

def pause(message="Press any key to continue..."):
    pause_pause = input(message)
    print(pause_pause)


