
# Import the os library
import os

from SubAppModules.APP import WindowApp

if __name__ == "__main__":

	# Checking if there is a Projects directory and creating it if not
	try:
		os.mkdir('projects')
	except FileExistsError:
		pass

	os.chdir("projects")
	tdapp = WindowApp()

	print("launched")