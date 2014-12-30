#Update tiles
#By Tyler Spadgenske

import urllib2

class Update():
    def __init__(self):
        pass

    def download(self):
        import urllib2

        url = "https://github.com/spadgenske/thirtytwo-squared/raw/master/tiles/mode.conf"

        file_name = url.split('/')[-1]
        u = urllib2.urlretrieve(url)
        f = open(file_name, 'wb')
        meta = u.info()
        file_size = int(meta.getheaders("Content-Length")[0])
        print "Downloading: %s Bytes: %s" % (file_name, file_size)

        file_size_dl = 0
        block_sz = 8192
        while True:
            buffer = u.read(block_sz)
            if not buffer:
                break

            file_size_dl += len(buffer)
            f.write(buffer)
            status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
            status = status + chr(8)*(len(status)+1)
            print status,

        f.close()

    def delete(self):
        pass

    def check_connection(self):
        try:
            response=urllib2.urlopen('http://74.125.228.100',timeout=1)
            return True
        except urllib2.URLError as err: pass
        return Falsepass

    def check_for_update(self):
        pass

if __name__ == '__main__':
    updater = Update()
    while True:
        try:
            updater.download()
            break
        except:
            print 'error'
