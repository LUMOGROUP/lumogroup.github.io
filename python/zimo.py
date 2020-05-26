# coding: ascii
#Copyright (c) 2020. LSHT LLC.
"""
zimo.py public function. All-in-one functioon lib.
""""""
imported list
os time
"""

def help(function_name="help"):
    """help and explaintion, simple to use."""

    #We will give users more ways to ask questions, but we'll not write documents.
    if function_name == "help":
        print("help [function_name] ")
    elif function_name == "":
        print("help [function_name] ")

def pause(message="Press any key to continue..."):
    """It's just like batch language. pause [massage]"""
    pause_pause = input(message)
    print(pause_pause)

def timestamp():
    """Get the unix timestamp now and retuen it. 
    Attention: It's a floating point number."""
    import time
    timestamp = time.time()
    return timestamp

def check_os(os_type):
    """check os with os.name().
    Return True if os_now is os_type """
    import os
    os_now = os.name()
    if os_now == "nt":
        if os_type == "nt":
            return True
        elif os_type == "posix":
            return False
    elif os_now == "posix":
        if os_type == "posix":
            return True
        elif os_type == "nt":
            return False