import cv2
import os
import argparse
#Open the camera:
cam = cv2.VideoCapture(0)


ap = argparse.ArgumentParser()
ap.add_argument("-c", "--quantity", required=True, help="Set the quantity of images that you want to take p. ej. 350")
args = vars(ap.parse_args())

#set path where we are going to save the image.
outDirectory = "E:/alxor/"

def takePhoto(number):
	if cam.isOpened():
		print("Camera opened successfully!")
		#Get one image:
		ret, frame = cam.read()
		name = "image_"+str(number)+".jpg"
		print(name)
		cv2.imwrite(os.path.join(outDirectory, name), frame)
	else:
		print("[INFO] Can not open the camera :(")
c = int(args["quantity"])
j = 1
while j <= c: #introduciendo 's' salimos del bucle

	print ("[INFO] WRITE 's' TO EXIT: ")
	print ("[INFO] WRITE 'c' TO TAKE A PHOTO ")
	user_input = input() #leer entrada
	if user_input is 'c':

		takePhoto(j)
		print("[INFO] IMAGE #"+str(j)+" SAVED...")

	if user_input is 's':
		break
		print("[INFO] THE PROGRAM HAS FINISHED..")
	j+=1

#Turn off the camera..
cam.release()
print("[INFO] THE PROGRAM HAS FINISHED..")