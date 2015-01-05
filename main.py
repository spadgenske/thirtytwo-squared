#LED Controller
#copyright 2015 Tyler Spadgenske

import time, os, random, update, subprocess

class LEDS():
    def __init__(self):
        os.chdir('/home/pi/thirtytwo-squared')
        self.last_tile = ''
        self.tiles = os.listdir('/home/pi/thirtytwo-squared/tiles')
        self.tiles.remove('time.conf')
        self.tiles.remove('mode.conf')
        time.sleep(9)
        self.lines = []
        self.time = '10'
        self.mode = '0'
        self.get_tile_time()
        self.modes = []
        self.scroll = ''
        
    def choose_tiles(self):
        while True:
            self.tile = random.choice(self.tiles)
            if self.tile != self.last_tile:
                self.last_tile = self.tile
                break

    def play_tiles(self):
        while True:
            self.choose_tiles()
            for i in self.lines:
                if self.tile in i:
                    self.time = i[-2] + i[-1]
            for i in self.modes:
                if self.tile in i:
                    self.mode = i[-1]

            if self.mode == '1':
                self.scroll = ''
                self.mode = '1'
            if self.mode == '0':
                self.scroll = ' -m -1'
                self.mode = '1'
            if self.mode == '2':
                self.scroll = ''
                self.mode = '2'
       
            if self.time[0] == '0':
                self.time = self.time[-1]

            os.system('sudo matrix/./led-matrix -D ' + self.mode + ' /home/pi/thirtytwo-squared/tiles/' + self.tile + ' -t ' + self.time + '' + self.scroll)
            time.sleep(3)

    def get_tile_time(self):
        self.file = open('/home/pi/thirtytwo-squared/tiles/time.conf', 'r')
        for i in range(0, len(self.tiles)):
            self.lines.append(self.file.readline().rstrip())

    def get_mode(self):
        self.mode_file = open('/home/pi/thirtytwo-squared/tiles/mode.conf', 'r')
        for i in range(0, len(self.tiles)):
            self.modes.append(self.mode_file.readline().rstrip())
            
if __name__ == '__main__':
    os.system('sudo python /home/pi/thirtytwo-squared/update.py')
    try:
        display = LEDS()
        display.get_mode()
        while True:
            display.play_tiles()
    except:
        print 'An Error Occurred'
        subprocess.Popen(['python', 'error.py'])
        
        
        
