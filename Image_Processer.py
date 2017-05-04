import os
import time
from PIL import Image

print '************************************'
print '****** HDR Image Processing ********'
print '************************************'
time.sleep(2)
print 'Waiting for files...'

L = 1.2
D = 0.8
LL = 1.5
DD = 0.5
Seconds_between_processing = 10

def process_image(files):
    IMAGE = Image.open(files)
    names = ['_01','_02','_03','_04']
    amounts = [L, D, LL, DD]
    image_list = {}
    for i, amt in enumerate(amounts):
        image_list[names[i]] = IMAGE.point(lambda p: p * amt)

#     print image_list
    for i in image_list.keys():
        old_name = files.split('.')
        new_name = 'OUTPUT/{}{}.{}'.format(old_name[0], i, old_name[1])
        image_list[i].save(new_name)
    IMAGE.save('OUTPUT/{}_00.jpg'.format(old_name[0]))
    message = '{} processed.'.format(files)
    return message


while 1:
    for files in os.listdir("."):
        if files.endswith(".jpg"):
            print process_image(files)
            os.remove(files)

    time.sleep(Seconds_between_processing)
