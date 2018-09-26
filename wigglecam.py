import subprocess
c1 = subprocess.Popen("sudo fswebcam -d /dev/video0 -r 640x640 image_1.jpg", shell=True);
c2 = subprocess.Popen("sudo fswebcam -d /dev/video1 -r 640x640 image_2.jpg", shell=True);
c1.wait();		
c2.wait();

print("took the pictures!");