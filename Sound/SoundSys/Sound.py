import numpy as np
import librosa
from scipy import signal
import sounddevice as sd
import time
import pyttsx3

# adjustable output parameters (add these to the setup class??)
from .Setup import Setup

beep_pause = 800  # ms (can we standardise these)
beep_duration = 0.4  # sec
st = Setup(1280, 720, 79, 41)  # this should be cache and passed as an arg??? Not done due to unit tests
engine = pyttsx3.init()
engine.setProperty('rate', 400)
beep_type = 'beep-07a.wav'


# static helper function
def closest_value(input_list, input_value):
    arr = np.asarray(input_list)
    i = (np.abs(arr - input_value)).argmin()
    return arr[i]


class Sound:
    # https://www.york.ac.uk/sadie-project/database.html
    D1_YORK_SRC_PATH = '/Users/euanchalmers/Desktop/yolov5/fnd/D1_HRIR_WAV/44K_16bit'
    BEEP_SOUND_ONE = '/Users/euanchalmers/Desktop/yolov5/fnd/beeps/'

    def convert_to_file(self):

        angle, elev = st.find_the_file_two(self.coord)

        bearing = str(angle)
        if bearing == 0:
            print('flagged front item')
            self.front = True

        diff_checker = [17,35,64,-17,-35,-64]
        diff_dict = {17:"17,5", 35:"35,3",64: "64,8", -17 : "-17,5" , -35 : "-35,3" , -64 : "-64,8"}

        if elev in diff_checker:
            print('found an outliyer')
            elevation = diff_dict[elev]
        else:
            elevation = str(elev)+',0'

        return '/azi_' + str(bearing) + ',0_ele_' + str(elevation) + '.wav'

    def __init__(self, coord, distance, text, beep):
        self.front = None
        self.coord = coord
        self.file = self.convert_to_file()
        self.distance = distance  # how to convey distance (increase frequency of beeps)
        self.text = text
        self.beep = beep
        self.Bin_Max = None
        self.freq = None  # this will be either true or false
        # print('this is the file',self.file)

    # add distance later
    def create_3d(self):
        HRIR_RE, fs_H0 = librosa.load(self.D1_YORK_SRC_PATH + self.file, sr=48000, mono=False)
        # print('Sample rate = ', fs_H0)
        # print('data dimentions = ', HRIR_RE.shape)

        [src_o, fs_s0] = librosa.load(self.BEEP_SOUND_ONE+beep_type, mono=True, sr=48000)

        s_0_L = signal.fftconvolve(src_o, HRIR_RE[0, :])  # source left
        s_0_R = signal.fftconvolve(src_o, HRIR_RE[1, :])  # right

        Bin_Max = np.vstack([s_0_L, s_0_R]).transpose()
        Bin_Max = Bin_Max / np.max(np.abs(Bin_Max))
        # final end product

        # Plays the sound within the control system loop
        self.Bin_Max = Bin_Max
        self.freq = fs_s0

    def play(self):
        if not self.beep:
            return
        # elif self.front:
        #     TX.play_msg_cache('front')

        sd.play(self.Bin_Max, self.freq)
        sd.sleep(int(beep_duration * beep_pause))
        sd.stop()

    def textToSpeech(self):
        if self.text == "":
            return

        if engine._inLoop:
            engine.endLoop()

        num_words = len(self.text.split(" "))

        if num_words > 5:
            engine.say('Long Text Here')
            engine.runAndWait()
            time.sleep(2)
            engine.stop()

        else:
            engine.say(self.text)
            engine.runAndWait()
        #     # this is  part of the multithreading problem
        #     # how to know the duration of the text readings
        #     # could we make duration a function of number of words or characters accounting for speach speed
            time.sleep(2.1)
            engine.stop()

    def get_name(self):
        return self.text

    def read_full_length(self):
        if engine._inLoop == True:
            engine.endLoop()

        engine.say(self.text)
        engine.runAndWait()
        # need to fix the duration problem
        time.sleep(5)
        engine.stop()