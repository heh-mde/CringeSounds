import os
from pyaudio import *
import wave
import time

is_stereo_off = True


def soundProfile(command, stereo):  # With or without stereo mixer
    global is_stereo_off
    is_stereo_off = stereo
    stereo_device = 'Line1'
    print(os.system('..\source\SoundVolumeView.exe {} "{}" 0'.format(command, stereo_device)))


def heroSound(hero, i):
    # winsound.PlaySound('slark.wav', winsound.SND_ASYNC)

    if is_stereo_off:
        soundProfile('/Enable', True)
    wf = wave.open("../source/sounds/{}/{}.wav".format(hero, i), 'rb')
    p = PyAudio()

    def callback(in_data, frame_count, time_info, status):
        data = wf.readframes(frame_count)
        return data, paContinue

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True,
                    stream_callback=callback)
    stream.start_stream()

    while stream.is_active():
        time.sleep(0.01)

    stream.stop_stream()
    stream.close()
    wf.close()

    p.terminate()
    if is_stereo_off:
        soundProfile('/Disable', True)