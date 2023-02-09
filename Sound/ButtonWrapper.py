import queue
import time

from fnd.Sound.SoundSys.TextToSpeech import *


class ThreadingState:
    def __init__(self):
        self.stop = False
        self.read_out = False
        self.no_beeps = 3
        self.pause_length = 1
        self.current_object = None
        self.quit = False
        self.all_objects = []

    def str_print(self):
        print('Stop', self.stop)
        print('Read out', self.read_out)
        print('Quit', self.quit)


state = ThreadingState()

# possibly an enum
# this should hold the current sys state that can be easly checked
curr_action_status = None


# this is where the buttons to command transfer will happen
def console():
    flag = True
    print('thread started')
    while flag:
        cmd = input('>')
        cmd_queue.put(cmd)
        action = BUTTONS_TO_COMMANDS.get(cmd, invalid_input)
        action()
        print('the curr state ', state.str_print())
        print('the next func to use is ', check_next_func())


# Calling
def invalid_input():
    print('---> Unknown command')


def pause():
    # how to check if the variable is met throughout the operation??? or is there a better way to kill a thread
    # play_msg_cache('pause')
    # add the voice recording from TextToSpeechHere
    print('--> Pause action & kill thread')
    state.stop = True


# how to pause somthing
def resume():
    # play_msg_cache('resuming_scan')
    state.stop = False


def quit():
    print('---> Stop scanning mode')
    state.quit = True


# this should be in sound development
def read_out_full():
    state.read_out = True
    print('--> Read action called and waiting to activate')
    return


# Actions

def pause_wait_action():
    while check_next_func() is pause_wait_action:
        time.sleep(1)

    print('--> Resume scan')


def read_out_full_action():
    print('--> Reading out full info for ... ', state.current_object.get_name())
    state.current_object.read_full_length()
    state.read_out = False
    time.sleep(0.8)


def quit_action():
    print('nows need to add the quit stuff')
    # play_msg_cache('quit_scanning')


cmd_queue = queue.Queue()
BUTTONS_TO_COMMANDS = {'p': pause, 'm': read_out_full, 'r': resume, 'q': quit}


def check_next_func():
    if state.stop:
        return pause_wait_action
    elif state.read_out:
        return read_out_full_action
    elif state.quit:
        return quit_action
    else:
        return None


def update_object(co):
    state.current_object = co
    state.all_objects.append(co)
