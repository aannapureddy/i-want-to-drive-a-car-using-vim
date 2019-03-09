import neovim
import serial


ser = serial.Serial('/dev/tty.usbserial', 9600)

"""
lock
Engine (boolean)
Throttle
Brake
Parking brake
Drive, neutral, and reverse
Music
Steering angle
Cruise
Horn
Car alarm
headlights
"""

@neovim.plugin
class NeotagsPlugin(object):

    def __init__(self, nvim):
        self.nvim = nvim

    @neovim.autocmd('BufWritePost', pattern='*', eval='expand("<afile>:p")')
    def turn_on(self, filename):
        ser.write('5')

