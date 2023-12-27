
from customtkinter import CTkScrollableFrame
from customtkinter import CTkButton
from customtkinter import CTkEntry
from SubAppModules.project_content import project_content

class CustomListBox(CTkScrollableFrame):

	def __init__(self, master, bigMaster, name):
		super().__init__(master)

		# Custom values
		self.tasksList = None
		self.master = master
		self.bigM = bigMaster

		# Configuring the attributes
		self.configure(label_text = name)


	# Method that displays the tasks
	def display_project_content(self, tasks):

		project_content(master = self, content = tasks)

		self.tasksList = tasks

	# Method that clear the previous content
	def clear_project_content(self):

		for task in self.winfo_children():
			task.destroy()

	def ask_task(self):

		lastIndex = len(self.winfo_children())

		self.taskContent = CTkEntry (self, width = 200)
		self.taskContent.grid(row = lastIndex, column = 0)
		self.taskContent.focus()
		self.taskContent.bind('<Return>', lambda x: self.add_new_task(self.taskContent.get(), lastIndex))


	def add_new_task(self, taskContent, lastIndex):
		CTkButton (self, text = taskContent,
				fg_color = ('black')).grid(row = lastIndex, column = 0)

		self.taskContent.destroy()



