import os
os.chdir('/home/pi/thirtytwo-squared')
while True:
    os.system('sudo /home/pi/thirtytwo-squared/matrix/./led-matrix  -D  1 /home/pi/thirtytwo-squared/static/update.ppm -t 30  -m -1')
