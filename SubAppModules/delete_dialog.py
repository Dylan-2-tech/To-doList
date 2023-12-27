
from customtkinter import CTkToplevel
from customtkinter import CTkLabel
from customtkinter import CTkButton
import os

class delete_dialog(CTkToplevel):

    def __init__(self, master):
        super().__init__(master)
        self.geometry("400x300")

        self.master = master


        self.label = CTkLabel(self, text="ToplevelWindow")
        self.label.pack(padx=20, pady=20)

        # Confirm buttons
        self.YesButton = CTkButton (self, text = "Yes", command = self.delete_project)
        self.NoButton = CTkButton (self, text = "No", command = self.destroy)

        self.YesButton.pack()
        self.NoButton.pack()


    # Method that delete the selected project
    def delete_project(self):

        # Setting the current project file
        cwd = os.getcwd() + "/"
        projectPath = cwd + self.master.SelectedProject + ".json"
        os.remove(projectPath)
        print(f"{self.master.SelectedProject} deleted")

        # Update the display of the projects
        self.master.SideBar.display_projects()

        # Clearing the content of the deleted project
        self.master.SideBar.clear_project_content()

        self.destroy()


