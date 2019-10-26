import os
import subprocess

text_image = """
   _____            _       ____
  / ___/____ ___  _| |     / / /_  ___  ____
  \__ \/ __ `/ / / / | /| / / __ \/ _ \/ __ \\
 ___/ / /_/ / /_/ /| |/ |/ / / / /  __/ / / /
/____/\__,_/\__, / |__/|__/_/ /_/\___/_/ /_/
           /____/
                                   :-=+*
                               +#%@@@@@%
                              #@@@@@@@@%
                          :-+*@@@@@@@@@%
                     :##@@@@@%%@@@@@@@@%
                     ***+-:    -+#%%#*+=
           :---------#---
           %:        *  *
          :%         *  *
          +#         *  +:
          #+=++++++++#=++=
          +*#@@@@@@@@@@%+-
           =+*%@@@@@@%++=
            :+=******+=:
                :-+
                 :+
                 :+
                 :+
                 :+
            =+**###***+=
"""

audio_names = {
        True: '80921__justinbw__buttonchime02up.wav',
        False: '142608__autistic-lucario__error.wav'
        }

def get_audio_path(status, audio_names):
    return os.path.join(os.path.dirname(__file__), 'audio', audio_names[status])

def notify(status, time_elapsed, cwd, command_str, audio_names):
    if status:
        text_prefix = "✔️ Job Finished with"
    else:
        text_prefix = "✖ Job Failed after"
    if time_elapsed < 60:
        time_elapsed = "{:.2f}s".format(time_elapsed)
    else:
        minutes = int(time_elapsed // 60)
        seconds = time_elapsed % 60
        time_elapsed = "{}m{:.2f}s".format(minutes, seconds)
    subprocess.check_call(
            "notify-send '{} {}!' 'command:\n{}\n----\nworking direcory:\n{}'".format(
                text_prefix,
                time_elapsed,
                command_str,
                cwd),
            shell=True)
    audio = get_audio_path(status, audio_names)
    subprocess.check_call("aplay {}".format(audio),
                          shell=True,
                          stdout=subprocess.DEVNULL,
                          stderr=subprocess.DEVNULL,
                          )

