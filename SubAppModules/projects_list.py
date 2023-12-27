
from customtkinter import CTk
from customtkinter import CTkLabel
from customtkinter import CTkButton
from customtkinter import CTkFont
from customtkinter import CTkEntry
from customtkinter import CTkScrollableFrame

from SubAppModules.project_content import project_content

import json

import glob

import os

class projects_list(CTkScrollableFrame):

	def __init__(self, master):
		super().__init__(master)

		self.configure(label_text = 'Projects:', label_font = CTkFont(size = 30))
		self.master = master

		self.grid(row = 1, column = 0, sticky = 'nsew')
		self.grid_rowconfigure((1,2,3), weight = 1)
		self.grid_columnconfigure(0, weight = 1)

		self.display_projects()
		
	
	# Method that displays all the projects
	def display_projects(self):

		# Deleting the previous projects displayed
		for p in self.winfo_children():
			p.destroy()

		# listing all the projects in the projects directory
		p_list = [p.replace(".json", "") for p in glob.glob("*.json")]

		# Creating a button for each projects
		for i in range(len(p_list)):
			CTkButton(self, text = p_list[i], fg_color = ("green"),
			command = lambda name=p_list[i]:self.display_all_project_content(name)
			).grid(row = i, column = 0, pady = (10, 0))


	# Method that dislplay the projetct clicked
	def display_all_project_content(self, projectName):

		
		# If the project is not already displayed
		if self.master.SelectedProject != projectName:

			# Clearing the previous content
			self.clear_all_project_content()

			# Setting the selected Project
			self.master.SelectedProject = projectName

			projectName += ".json" # Giving the json extension to the name

			# opening the project by its name
			with open(projectName ,"r") as j:
				try:

					allContent = json.load(j) # loading the content of the json file as a dictionnary
					j.close() # Closing the file

					# Loading the todo content in the todoFrame
					self.master.ToDOColumn.display_project_content(allContent["todo"])
					# Loading the ongoing content in the ongoingFrame
					self.master.ongoingColumn.display_project_content(allContent["ongoing"])
					# Loading the completed content in the completedFrame
					self.master.completedColumn.display_project_content(allContent["completed"])
					
				except json.decoder.JSONDecodeError:
					print('The string does NOT contain valid JSON')

	def clear_all_project_content(self):
		
		self.master.ToDOColumn.clear_project_content()
		self.master.ongoingColumn.clear_project_content()
		self.master.completedColumn.clear_project_content()



