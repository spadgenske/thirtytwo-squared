#Error Handling
#copyright 2015 Tyler Spadgenske GPL 2.0

import os, update, sys, constants

class Error():
    def __init__(self):
        self.HOST = constants.HOST

    def check_static(self):
        try:
            a = open('/home/pi/thirtytwo-squared/static/tile-quanity.txt')
            b = open('/home/pi/thirtytwo-squared/static/filenames.txt')
            good = True
        except:
            good = False
        return good
            

    def check_tiles(self):
        filenames_file = open('/home/pi/thirtytwo-squared/static/filenames.txt')
        self.filenames = filenames_file.readlines()
        
        for i in range(0, len(self.filenames)):
            self.filenames[i] = self.filenames[i].rstrip()

        self.files_in_tiles = os.listdir('/home/pi/thirtytwo-squared/tiles/')
        
        for i in self.filenames:
            if i in self.files_in_tiles:
                fail = True
            else:
                fail = False
                break
            
        return fail

    def fix_static(self):
        print 'Retriving "tile-quanity.txt"'
        os.system('sudo wget -P /home/pi/thirtytwo-squared/static/ -4 https://github.com/' + self.HOST + '/thirtytwo-squared/raw/master/static/tile-quanity.txt static/tilequanity.txt')
        print 'Retriving "filenames.txt"'
        os.system('sudo wget -P /home/pi/thirtytwo-squared/static/ -4 https://github.com/' +self.HOST + '/thirtytwo-squared/raw/master/static/filenames.txt static/filenames.txt')
        

if __name__ == '__main__':
    test = Error()
    updater = update.Update()
    connection = updater.check_connection()
    result = test.check_static()

    if result != True:
        print 'STATIC CHECK FAILED'
        if connection:
            test.fix_static()
        else:
            print 'CANNOT FIX STATIC'
            print 'NO INTERNET CONNECTION'

        #Try again just to make sure
        result = test.check_static()
        if result == True:
            print 'STATIC FIXED'

    else:
        print 'NO ERRORS FOUND IN STATIC'
        
    tiles_ok = test.check_tiles()
            
    if tiles_ok != True:
        print 'MISSING TILES'
        print 'CANNOT CONTINUE'
        if result:
            file = open('/home/pi/thirtytwo-squared/static/tile-quanity.txt', 'w')
            file.write('0')
            file.close()
            print 'CHANGED FILE TO FORCE UPDATE'
        sys.exit()
        
    else:
        print 'NO ERRORS FOUND IN TILES'
        
