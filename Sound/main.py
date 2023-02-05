import SoundSys.TextToSpeech as TX
from SoundSys.Sound import Sound
from Perception_FAKE import give_me_a_scan

import sounddevice as sd
import librosa


# orders the objects passed into left to right how to implement into some sport of wrapper within the main clas thread
def order_objects_passed(all_objects):
    print(all_objects)
    newlist = sorted(all_objects, key=lambda x: x.coord[0])
    print(newlist)

    for o in newlist:
        print(o.get_name())
        print(o.coord)


if __name__ == '__main__':
    # button uses https://stackoverflow.com/questions/65730317/how-to-pause-resume-and-stop-pyttsx3-from-speaking

    # PARENT = '/Users/euanchalmers/Desktop/SoundProject/sound_v2'
    # D1_YORK_SRC_PATH = '/D1_HRIR_WAV/44K_16bit/'
    # BEEP_SOUND_ONE = '/beeps/beep-10.wav'
    # file = PARENT +BEEP_SOUND_ONE
    # x, y= librosa.load(file, mono=True, sr=48000)
    # print(x, y)


    # index , val = give_me_a_scan()
    # order_objects_passed(val)

    # TX.save_msg_to_cache('Resume Scan', 'resuming_scan')
    # TX.save_msg_to_cache('Quit Scanning Mode', 'quit_scanning')
    obj3 = Sound([650, 230], 0, "Object 4. " + 'Centre item', True)
    print(obj3.file)
    obj3.textToSpeech()
    print(obj3.front)
    obj3.create_3d()

    print(obj3.file)
    obj3.play()

    # TX.play_msg_cache('power_on')
    # pixel width , pixel height , horizontal pov , vertical pov
    # st = Setup(1980, 1080, 79, 41)
    #
    # print(st.find_the_file_two([500, 600]))
