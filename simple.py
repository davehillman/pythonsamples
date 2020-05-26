# simple.py
# Simple IO functions
# D. Hillman
# Oct 2019

import os

msghist = "\n\nHistory: \n"
# simple message output
def msg_send(m):
    global msghist
    try:
        msghist = msghist + m + "\n----------------\n"
        print(m, "\n")
    except:
        print("failed")

def showHist():
    global msghist
    print(msghist)


# following enables a string input
def get_string(msg):
    try:
        i = input(msg)
        return i
    except:
        return ""

# following returns an int or float value, or 0
def get_num(msg):
    try:
        i = float
        i = float(input(msg))
        return i
    except:
        print("Not a number, try again.")
        return get_num(msg)



# following returns the selected item from the list
def get_choice(msg,ch):
    try:
        index=0
        print("Select from the following choices: ")
        for item in ch:
            print(" ", (index + 1), ch[index])
            index += 1
        i = 0
        i = int(input(msg)) -1
        return ch[i]
    except:
        print("You did not choose one of the options, try again.")
        get_choice(msg,ch)

# following returns a true or false based on t/f or y/n input
def get_tf(msg):
    try:
        print(msg)
        i = input("Enter y/n or t/f: ")
        print(i)
        if i.upper() == "Y" or i.upper() == "T":
            return True
        else:
            return False
    except:
        return False

# following returns 2 numeric values (e.g., lat, lon), note, it does not check for range, returns list
def get_2v(msg):
    dval = []
    dval.append(get_num(msg + " ...first val: "))
    dval.append(get_num(msg + " ...second val: "))
    return dval


# following returns
def getFiles(pdir,ext):
    files = []
    pdir = pdir + "/"
    ext = "." + ext
    f = os.listdir(pdir)
    for file in f:
        if ext in file:
            files.append(file)
    cnt = 1
    print("\nFile Selection:")
    for x in files:
        print(str(cnt) + ". " + x)
        cnt += 1
    fn = get_num("Select file from above (enter number): ")
    if fn > 0 and fn < (len(files) + 1):
        return files[int(fn - 1)]
    else:
        return ""


