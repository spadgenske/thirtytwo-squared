#Update tiles
#By Tyler Spadgenske

import urllib2, os

class Update():
    def __init__(self):
        pass

    def download(self):
        pass

    def delete(self):
        pass

    def check_connection(self):
        try:
            response=urllib2.urlopen('http://74.125.228.100',timeout=1)
            return True
        except urllib2.URLError as err: pass
        return Falsepass

    def check_for_update(self):
        old_tiles = open('/home/pi/thirtytwo-squared/static/tile-quanity.txt')
        num_of_old_tiles = old_tiles.readline()
        old_tiles.close()
        print 'Old Tiles: ', num_of_old_tiles

        os.remove('/home/pi/thirtytwo-squared/static/tile-quanity.txt')
        os.system('sudo wget -4 https://github.com/spadgenske/thirtytwo-squared/raw/master/static/tile-quanity.txt')
        new_tiles = open('/home/pi/thirtytwo-squared/static/tile-quanity.txt')
        num_of_new_tiles = new_tiles.readline()
        print 'New Tiles: ', num_of_new_tiles

if __name__ == '__main__':
    updater = Update()
    connection = updater.check_connection()
    if connection == True:
        updater.check_for_update()
