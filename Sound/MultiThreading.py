import threading
import queue
import time

from Perception_FAKE import give_me_a_scan
import SoundSys.TextToSpeech as TX

# https://www.tutorialspoint.com/python/python_multithreading.htm/
# https://stackoverflow.com/questions/9105990/constantly-looking-for-user-input-in-python

class ThreadingState:
    def __init__(self):
        self.stop = False
        self.read_out = False
        self.no_beeps = 3
        self.pause_length = 1
        self.current_object = None
        self.quit = False
        self.objects = []


# setup for the threading state
state = ThreadingState()


def pause_wait_action():
    while check_next_func() is pause_wait_action:
        time.sleep(1)

    print('--> Resume scan')


def read_out_full_action():
    print('--> Reading out full info for ... ',state.current_object.get_name())
    state.current_object.read_full_length()
    state.read_out = False
    time.sleep(1)


def play_sounds(all_objects):
    for index, o in enumerate(all_objects):
        state.current_object = all_objects[index]

        # checks if a break is needed
        if check_next_func() is None:
            print(o.get_name())
            o.create_3d()
            o.textToSpeech()
            for _ in range(state.no_beeps):
                o.play()
            time.sleep(state.pause_length)
        elif check_next_func() == quit_action:
            quit_action()
            return
        else:
            func = check_next_func()
            func()


# need an enum of actions???
def check_next_func():
    if state.stop:
        return pause_wait_action
    elif state.read_out:
        return read_out_full_action
    elif state.quit:
        return quit_action
    else:
        return None


# this will be changes to listening for button presses (with current status vs now status)
# change when we know the button when we know what the button we will be using are
def console(q):
    while 1:
        cmd = input('> ')
        q.put(cmd)
        if cmd == 'quit':
            break


def thread_two_action():
    run = True
    while run:
        if check_next_func() is None:
            # this is where the run operation should live
            index, val = (give_me_a_scan())
            print("Random example selected = example_", index + 1)
            play_sounds(val)
        elif check_next_func() == quit_action:
            quit_action()
            return
        else:
            func = check_next_func()
            func()


        # just to space out the examples -> should be removed
        time.sleep(1)


def pause():
    # how to check if the variable is met throughout the operation??? or is there a better way to kill a thread
    TX.play_msg_cache('pause')
    # add the voice recording from TextToSpeechHere
    print('--> Pause action & kill thread')
    state.stop = True


# how to pause somthing
def resume():
    TX.play_msg_cache('resuming_scan')
    state.stop = False


# this should be in sound development
def read_out_full():
    state.read_out = True
    print('--> Read action called and waiting to activate')
    return


def scanning_mode():
    TX.play_msg_cache('Start_Scanning')
    print('--> running example one')
    thread2.start()


def invalid_input():
    print('---> Unknown command')

def quit():
    print('---> Stop scanning mode')
    state.quit = True

def quit_action():
    TX.play_msg_cache('quit_scanning')

def perp_action():
    flag = True
    while flag:
        time.sleep(2)

thread2 = threading.Thread(target=thread_two_action)

perception_thread = threading.Thread(target=perp_action)





if __name__ == '__main__':
    # TX.play_msg_cache('power_on')



    cdwbhjcwdj

    # would add all the button listing here and in the console function
    # FORMAT -->  'CONSOLE COMMAND' : THE FUNCTION
    cmd_actions = {'scan': scanning_mode, 'p': pause, 'm': read_out_full, 'r': resume, 'q': quit}
    # cmd_actions = {'scan': scanning_mode, 'p': pause, 'm': read_out_full, 'p': resume, 'q': quit, 'c':customise, 'm':review read_out_full}
    cmd_queue = queue.Queue()

    dj = threading.Thread(target=console, args=(cmd_queue,))
    dj.start()

    # automatically starts scanning mode
    scanning_mode()
    # this will be where the perception sys sits
    perception_thread.start()

    while 1:
        cmd = cmd_queue.get()
        if cmd == 'quit':
            break
        action = cmd_actions.get(cmd, invalid_input)
        action()
