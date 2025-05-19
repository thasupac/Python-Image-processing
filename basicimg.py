import os
import cv2

PATH = os.getcwd()  #current working directrory

img_path = os.path.join(PATH, 'img', 'automation.jpg')
img_auto = cv2.imread(img_path, cv2.IMREAD_COLOR)

#resize
# resized = cv2.resize(img_auto, (400,300))
# resized = cv2.resize(img_auto, (0,0), fx=0.5,fy=0.5)

#crop
# cropped = img_auto[yy:yy,xx:xx]
cropped = img_auto[260:419,192:350]

# print(img_auto.shape)
# print(img_path)
cv2.imshow('image', cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()

#save photo
# save_loc = os.path.join(PATH, 'img', 'automation-cropped.jpg')
# cv2.imwrite(save_loc, cropped)

#list photopath
list_image = os.listdir(os.path.join(PATH, 'multiresize'))

#for loop
for img in list_image:
    img_path_multi = os.path.join(PATH, 'multiresize', img)
    img_resize = cv2.imread(img_path_multi, cv2.IMREAD_COLOR)
    resized = cv2.resize(img_resize, (0,0), fx=0.5,fy=0.5)
    newfile = 'resized_'+img
    save_loc = os.path.join(PATH, 'multiresize', newfile)
    cv2.imwrite(save_loc, resized)