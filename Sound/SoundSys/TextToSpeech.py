import pyttsx3
import librosa
import sounddevice as sd

MSG_CACHE_PATH = '/Users/euanchalmers/Desktop/yolov5/fnd/recorded_msg'


def save_msg_to_cache(input_text, file_name):
    if 'wav' not in file_name:
        file_name = file_name + '.wav'

    print('written to...', MSG_CACHE_PATH + "/" + file_name)
    engine = pyttsx3.init()
    engine.save_to_file(input_text, str(MSG_CACHE_PATH + "/" + file_name))
    engine.runAndWait()


def play_msg_cache(file_name):
    if '.wav' not in file_name:
        file_name = file_name+'.wav'

    [y, sr] = librosa.load(MSG_CACHE_PATH + "/" + file_name, sr=48000)
    duration = librosa.get_duration(filename=MSG_CACHE_PATH + "/" + file_name) * 1000  # value in ms

    sd.play(y, sr)
    sd.sleep(int(duration))
    sd.stop()


if __name__ == '__main__':
    save_msg_to_cache('Pause this now pls', 'pause')