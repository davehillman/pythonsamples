

import simple as sio


# following is a generalized looping construct
def run_loop():
    rl = True
    try:
        while rl:
# looping actions follow...
            t = sio.get_string("Enter a string (abc, cat, 23skidoo): ")
            sio.msg_send(t)
            num1 = sio.get_num("Enter a number: ")
            sio.msg_send(str(num1))
            item2 = sio.get_choice("Select from: ", ["apple","banana","blueberry"])
            sio.msg_send(item2)
            print(sio.get_2v("Enter lat/long"))

# following gets a true to continue, message can be changed
            rl = sio.get_tf("Do you wish to repeat?")
    except:
        return


def main():
    sio.msg_send("This is a demo")
    run_loop()
    sio.showHist()




# following sets up how program is started
if __name__ == '__main__':
    main()
