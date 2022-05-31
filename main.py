# MIT License

# Copyright (c) 2022 Phoenixthrush UwU

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import hashlib
import subprocess
from uuid import uuid4
from os import system, path

if not path.exists("key.txt") and not path.exists("reset.txt"):
    with open("key.txt", "w") as text_file:
        text_file.write("3b878ce9b2d1b1c1b98ee35ec72ead2ea2b6cd6ef8185de514d6d87d236d252b:3eb138b62c474e8fab6334f5289e2567") # "phoenix" - change if you wanna change the default new password
    
if path.exists("reset.txt"):
    system("del /Q key.txt >nul")

def hash_password(password):
    salt = uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt
    
def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

try:
    with open('key.txt') as f:
        hashed_password = f.read()
except IOError:
    system("cls")
    user_input = input('Register\nCreate a password: ')
    subprocess = subprocess.Popen("powershell -c \"(Get-WmiObject -Class Win32_ComputerSystemProduct).UUID\"", shell=True, stdout=subprocess.PIPE)
    subprocess_return = subprocess.stdout.read()
    id = subprocess_return.decode("utf8").replace("\n", "")
    new_pass = id + user_input
    hashed_password = hash_password(new_pass)
    with open("key.txt", "w") as text_file:
        text_file.write(hashed_password)

if path.exists("reset.txt"):
    system("del /Q reset.txt")
    exit()

system("cls")
user_input = input('Login\nEnter your password: ')
subprocess = subprocess.Popen("powershell -c \"(Get-WmiObject -Class Win32_ComputerSystemProduct).UUID\"", shell=True, stdout=subprocess.PIPE)
subprocess_return = subprocess.stdout.read()
id = subprocess_return.decode("utf8").replace("\n", "")
old_pass = id + user_input  

if check_password(hashed_password, old_pass):
    print('\nYou entered the right password!\n')
    input("press enter to exit")
else:
    print('\nI am sorry but the password does not match!\n')
    input("press enter to exit")
