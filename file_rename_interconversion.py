import os

from_dir=input("Enter the source folder:\t") + "/"

to_dir=input("Enter the destination folder:\t") + "/"




for i,image in enumerate(os.listdir(from_dir)):
	if image.endswith(".png"):
		os.rename(from_dir+image,to_dir+f"new_jpegfile_{i}.jpeg")

	if image.endswith(".jpeg")|image.endswith(".jpg"):
		os.rename(from_dir+image,to_dir+f"new_pngfile_{i}.png")



print("Done!!!")
