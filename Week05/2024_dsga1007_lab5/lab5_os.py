#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Python provides a lot of modules for different operating system related operations. 
Running external command or shell command is very popular in Python code developement. 
We can call Linux or Windows commands from python code or script and use output.
Below is yet another way to interact with the OS not seen in Lecture/Lab
"""

"""
Import os Module
We can use system() function in order to run a shell command in Linux and Windows operating systems. 
system() is provided by os Module. So we will load this module like below.
"""

import os

"""
After loading os module we can use system() function by providing the external command we want to run. 
In this example, we will run ls command which will list current working directory content. Then the pwd command to display the current path
"""
os.system('ls')

os.system('pwd')

