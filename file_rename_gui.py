import tkinter as tk
from tkinter import filedialog 
import os

class FilesRenamingApp(tk.Tk):

	def  __init__(self):


		tk.Tk.__init__(self)

		self.geometry("450x300+10+10")
		self.select=tk.Button(self,text="choose folder",command=self.on_choose)
		self.save=tk.Button(self,text="save to folder",command=self.on_save)
		self.run=tk.Button(self,text="Run",command=self.run)

		self.tb1=tk.Text(self,width=40,height=1)
		self.tb2=tk.Text(self,width=40,height=1)
		self.tb3=tk.Text(self,width=40,height=10,font="Verdana, 8")

		self.tb1.grid(column=0,row=0,padx=10)
		self.tb2.grid(column=0,row=1,padx=10)
		self.tb3.grid(column=0,row=2,columnspan=2,sticky="NSEW", padx=10,pady=10)


		self.select.grid(column=1,row=0, pady=10, padx=5)
		self.save.grid(column=1,row=1,padx=5)
		self.run.grid(column=1,row=3)


	def on_choose(self):
		self.from_dir=filedialog.askdirectory() + "/"
		self.tb1.insert("0.0",self.from_dir)

	def on_save(self):
		self.to_dir = filedialog.askdirectory() + "/"
		self.tb2.insert("0.0", self.to_dir)

	def run(self):
		for i,image in  enumerate(os.listdir(self.from_dir)):
			if image.endswith(".jpeg")|image.endswith(".jpg")|image.endswith(".png"):
				self.tb3.insert(f"{i}.0",f"renameing {image} to {i}.png")
				os.rename(self.from_dir+image,self.to_dir+f"{i}.png")


app=FilesRenamingApp()
app.mainloop()


	
						