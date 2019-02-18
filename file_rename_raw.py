import os

from_dir=input("Enter the source folder:\t") + "/"

to_dir=input("Enter the destination folder:\t") + "/"



for i,image in enumerate(os.listdir(from_dir)):
	if image.endswith(".jpeg")|image.endswith(".jpg")|image.endswith(".png"):
		os.rename(from_dir+image,to_dir+f"renamed {i}.png")


print("Done!!!")
