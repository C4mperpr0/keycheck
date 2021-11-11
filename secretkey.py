from playsound import playsound
from pynput import keyboard
from threading import Thread

global keyreg
keyreg = ''

global commands
commands = {'suspend': 'import os\nos.system("systemctl suspend")',
            'test': 'import os\nos.system("notify-send cum")',
            'eject': 'import os\nos.system("eject")', '#60eject': 'import os\nimport time\ntime.sleep(60)\nos.system("eject")',
            'shutdown': 'import os\nos.system("shutdown now")',
            'screenup': 'import os\nos.system("xrandr -o inverted")',
            'screendown': 'import os\nos.system("xrandr -o normal")',
            'left': 'import os\nos.system("xrandr -o left")',
            'right': 'import os\nos.system("xrandr -o right")',
            'kder': 'import os\nos.system("kdeconnect-cli --refresh")',
            'fart': 'from playsound import playsound\nplaysound("durchsage")',
            'bashrc': 'import os\nfrom pathlib import Path\nfile = open(str(Path.home())+"/.bashrc", "a")\nfile.write("\\npython3 \\""+os.getcwd()+"/secretkey.py\\" &")\nfile.close()',
            'profile': 'import os\nfrom pathlib import Path\nfile = open(str(Path.home())+"/.profile", "a")\nfile.write("\\npython3 \\""+os.getcwd()+"/secretkey.py\\" &")\nfile.close()',
            'cum': 'import os\nimport time\ntime.sleep(60)\nos.system("notify-send cum")'}



def on_press(key):
    global keyreg
    key = str(key)
    if len(key) == 3:
        keyreg += key[1]
    if len(keyreg) > 30:
        keyreg = keyreg[:30]

    for cmd in commands:
        if cmd in keyreg:
            keyreg = ''
            t = Thread(target=exec, args=(commands[cmd],))
            t.start()

    #playsound(f"bethovensSiebzehnte", block=False)

with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()

