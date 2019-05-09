import cv2
num=7010
while(num<=7509):
    vidcap = cv2.VideoCapture('./videos/video'+str(num)+'.mp4')
    success,image = vidcap.read()
    count = 0
    success = True
    while success and count<=270:
        if(count==0 or count==54 or count==108 or count==162 or count==216 or count==270):
            cv2.imwrite("./frames1/frame"+str(num)+"%d.jpg" % count, image)     # save frame as JPEG file
        success,image = vidcap.read()
        print( 'Read a new frame: ', success)
        count += 1
    num+=1

