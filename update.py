#Update tiles
#By Tyler Spadgenske

import urllib2, os, time, subprocess, error

class Update():
    def __init__(self):
        pass

    def download(self, files):
        for i in files:
            os.system('sudo wget -P /home/pi/thirtytwo-squared/tiles/ -4 https://github.com/spadgenske/thirtytwo-squared/raw/master/tiles/' + i.rstrip())
            print 'Downloaded "' + i + '"'       

    def delete(self):
        old_files = os.listdir('/home/pi/thirtytwo-squared/tiles/')

        #Delete the old files
        for i in old_files:
            os.remove('/home/pi/thirtytwo-squared/tiles/' + i)
            print 'Deleted "' + i + '"'

    def check_connection(self):
        #Open up a google server to check internet connection
        try:
            response=urllib2.urlopen('http://74.125.228.100',timeout=1)
            return True
        except urllib2.URLError as err: pass
        return False

    def check_for_update(self):
        #See the current version of tiles
        old_tiles = open('/home/pi/thirtytwo-squared/static/tile-quanity.txt')
        num_of_old_tiles = old_tiles.readline()
        old_tiles.close()

        #Remove file and get new one
        os.remove('/home/pi/thirtytwo-squared/static/tile-quanity.txt')
        os.system('sudo wget -P /home/pi/thirtytwo-squared/static/ -4 https://github.com/spadgenske/thirtytwo-squared/raw/master/static/tile-quanity.txt static/tilequanity.txt')
        new_tiles = open('/home/pi/thirtytwo-squared/static/tile-quanity.txt')
        num_of_new_tiles = new_tiles.readline()

        #Compare versions to check for update
        if num_of_new_tiles != num_of_old_tiles:
            update_availible = True
        else:
            update_availible = False
            
        return update_availible
                
    def prepare_download(self):
        os.remove('/home/pi/thirtytwo-squared/static/filenames.txt')
        #Get all the filenames of the new/old tiles
        os.system('sudo wget -P /home/pi/thirtytwo-squared/static/ -4 https://github.com/spadgenske/thirtytwo-squared/raw/master/static/filenames.txt static/filenames.txt')
        filenames_file = open('/home/pi/thirtytwo-squared/static/filenames.txt')
        new_filenames = filenames_file.readlines()
        for i in new_filenames:
            i = i.rstrip()

        return new_filenames

if __name__ == '__main__':
    try:
        screen = subprocess.Popen(['python', 'startup.py'])
        updater = Update()
        connection = updater.check_connection()
        if connection == True:
            print '+++++++++++++++++++++++'
            print 'Connected to Internet'
            print '+++++++++++++++++++++++'
            update_availible = updater.check_for_update()

            if update_availible:
                sup = subprocess.Popen(['python', 'sup.py'])
                print '+++++++++++++++++++++++++++'
                print 'New Update Availible'
                print '+++++++++++++++++++++++++++'
                new_files = updater.prepare_download()
                updater.delete()
                updater.download(new_files)
                print 'Update Complete'
                sup.kill()
            
            else:
                print '+++++++++++++++++++++++++++'
                print 'No Update Found'
                print '+++++++++++++++++++++++++++'
        else:
            print '+++++++++++++++++++++++++++'
            print 'Cannot Connect to Internet'
            print '+++++++++++++++++++++++++++'
            time.sleep(37)
    except Exception as error:
        print '++++++++++++++++++++++++++++++'
        print '             Error'
        print '++++++++++++++++++++++++++++++'
        print error
        print
        print 'SEARCHING FOR ERROR...'
        subprocess.Popen(['python', 'error.py'])
        time.sleep(37)

