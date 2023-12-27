
from customtkinter import CTk
from customtkinter import CTkLabel
from customtkinter import CTkButton
from customtkinter import CTkFrame
from customtkinter import CTkFont
from customtkinter import CTkEntry
from customtkinter import CTkScrollableFrame

import json

from SubAppModules.projects_list import projects_list
from SubAppModules.delete_dialog import delete_dialog
from SubAppModules.CListBox import CustomListBox

import os

import glob

class WindowApp(CTk):

	def __init__(self):
		super().__init__()

		# Dictionnary that represent an empty preoject
		self.emptyProject = {"todo":[], "ongoing":[], "completed":[]}

		# Name of the selected project
		self.SelectedProject = None
		# delete_dialog window
		self.deleteDiag = None

		# Creating the main window
		self.title("To Do List app") # Name of the window
		self.geometry("1000x600+400+150") # set the window's width and height

		# configure the responsive grid layouts
		self.grid_columnconfigure(0, weight = 0)
		self.grid_columnconfigure(1, weight = 2)
		self.grid_rowconfigure(0, weight = 0)
		self.grid_rowconfigure(1, weight = 3)


		# The Title and Menu Bar
		self.MenuBar = CTkFrame (self, fg_color = ("blue"), height = 40, corner_radius = 0)
		self.MenuBar.grid(row = 0, column = 0, sticky = 'new', columnspan = 10)
		self.MenuBar.grid_propagate(0)

		# Button to add a projet place in the menu Bar
		self.AddProjectBtn = CTkButton (self.MenuBar, text = 'Add Project', command = self.add_project)
		self.AddProjectBtn.grid(row = 0, column = 0)

		self.DeleteProjectBtn = CTkButton (self.MenuBar, text = 'Delete Project', command = self.open_delete_dialog)
		self.DeleteProjectBtn.grid(row = 0, column = 1)

		# Label that displays the error 
		self.ERRORLABEL = CTkLabel(self.MenuBar, text = "",
			font = CTkFont(size = 25))
		self.ERRORLABEL.grid(row = 0, column = 3)

		# Left Side Bar to see all the existing Porjects
		self.SideBar = projects_list(master = self)

		# The project display frame
		self.ProjectFrame = CTkFrame (self, fg_color = "grey")
		self.ProjectFrame.grid(row = 1, column = 1, sticky = 'nsew', columnspan = 3, padx = 10, pady = 10) 
		self.ProjectFrame.grid_propagate(0)

		# Configure responsive grid layouts for the 3 columns in the ProjectFrame
		self.ProjectFrame.grid_rowconfigure(0, weight = 1)
		self.ProjectFrame.grid_rowconfigure(1, weight = 0)
		self.ProjectFrame.grid_columnconfigure((0, 1, 2), weight = 1)
		
		# First column of thigs to do
		self.ToDOColumn = CustomListBox (master = self.ProjectFrame, bigMaster = self, name = "Tasks To do")
		self.ToDOColumn.grid(row = 0, column = 0, sticky = 'nsew', padx = 10, pady = 10)

		# Seconde column of things ongoing
		self.ongoingColumn = CustomListBox (master = self.ProjectFrame, bigMaster = self, name = "Ongoing Tasks")
		self.ongoingColumn.grid(row = 0, column = 1, sticky = 'nsew', padx = 10, pady = 10)

		# Third column of things completed
		self.completedColumn = CustomListBox (master = self.ProjectFrame, bigMaster = self, name = "Completed Tasks")
		self.completedColumn.grid(row = 0, column = 2, sticky = 'nsew', padx = 10, pady = 10)

		# Responsive grid layouts for the colmun above
		self.ToDOColumn.grid_columnconfigure(0, weight = 1)
		self.ongoingColumn.grid_columnconfigure(0, weight = 1)
		self.completedColumn.grid_columnconfigure(0, weight = 1)

		
		## Add tasks buttons ##
		# Add button for the Todo column
		CTkButton(self.ProjectFrame, text = "Add task", fg_color = ("purple"),
				command = self.ToDOColumn.ask_task).grid(row = 1, column = 0, pady = (0, 10))

		# Add button for the ongoing column
		CTkButton(self.ProjectFrame, text = "Add task", fg_color = ("purple"),
				command = self.ongoingColumn.ask_task).grid(row = 1, column = 1, pady = (0, 10))

		# Add button for the completed column
		CTkButton(self.ProjectFrame, text = "Add task", fg_color = ("purple"),
				command = self.completedColumn.ask_task).grid(row = 1, column = 2, pady = (0, 10))



		self.mainloop()

	def clear_error_label(self):
		self.ERRORLABEL.configure(text = "")


	# Method that create a new empty project
	def add_project(self):

		# putting an entry in the SideBar to enter the name of the new project
		self.NewProjectName = CTkEntry (self.MenuBar, font = CTkFont(size = 20), width = 500)
		self.NewProjectName.grid(row = 0, column = 2)
		self.NewProjectName.focus()
		self.NewProjectName.bind('<Return>', self.create_project)


	# Method that create 
	def create_project(self, idk):

		# Getting the name
		Pname = self.NewProjectName.get() + ".json"

		# destroying the Entry
		self.NewProjectName.destroy()

		# Checking if a project with this name already exists (TO DO)
		if Pname in glob.glob('*.json'):
			self.ERRORLABEL.configure(text = "Project already exist")
			self.ERRORLABEL.after(5000, self.clear_error_label)
		else:
			# Creating a new empty Json file to store all the project
			with open(Pname, 'w') as newP:
				json.dump(self.emptyProject, newP)
				newP.close()

			self.SideBar.display_projects()

	def open_delete_dialog(self):

		if self.SelectedProject != None:

			if self.deleteDiag is None or not self.deleteDiag.winfo_exists():
				self.deleteDiag = delete_dialog(self)  # create window if its None or destroyed
			else:
				self.deleteDiag.focus()  # if window exists focus it
