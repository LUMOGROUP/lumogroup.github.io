# coding: utf-8
#Copyright (c) 2020. LSHT LLC.
"""
zimo.py public function. All-in-one functioon lib.
"""


def help(function_name="help"):
    """help and explaintion, simple to use."""
    if function_name == "help":
        print("help [function_name] ")
    elif function_name == "":
        print("help [function_name] ")

def pause(message="Press any key to continue..."):
    pause_pause = input(message)
    print(pause_pause)

def timestamp():
    try:
        import time
        timestamp = time.time()
        return timestamp
    except ImportError:
        print("moudle import failed: time")


