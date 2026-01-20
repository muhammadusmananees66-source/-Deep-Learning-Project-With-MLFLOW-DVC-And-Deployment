import os                     # module to work with files & folders
from pathlib import Path      # Path → modern, safer way to handle file paths
import logging                # logging → professional replacement for print()

# logging string (it helps whenever we will be executing this template.py file
# so whatsoever the activity this file will do as it will creates folders, etc. 
# so this kind of messages will be seen over the terminal so insetad of 
# printing operations, we will logged them )

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# logging.basicConfig ...> Configure how logging should behave in this program

project_name = 'cnnClassifier'    # This is not specified as we do not 

# have to change it again and again through out the project, as this project 
# is image classifications so we gave a common name
 
# Now create a list of file and folders 

list_of_files = [
    '.github/workflows/.gitkeep',    # As in the github workflows folder 
    
    # we keep a file so that we can add other files as github does not allow us to enter empty folder
    # At the time of pipeline we will remove this file
                         # src means i am creating a folder inside this i will create 
                         # all the componenets. as inside src will creae a prject_name and inside this will create components and all other things 
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/config/configuration.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/constants/__init__.py',
    'config/config.yaml',
    'dvc.yaml',
    'params.yaml',
    'requirements.txt',
    'setup.py',
    'research/trials.ipynb',
    'templates/index.html'       # For flask framework to create a web app this template is ccreated 
    
]


# Now write a one for Loop 

for filepath in list_of_files: # For every file path I want to create, process it one by one.
    filepath = Path(filepath)  # Turn the path into a Path object so I can use file methods safely.
    filedir, filename = os.path.split(filepath)   # Separate directory path from the file name, It is for files and folder to be split 

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)   # To make folder
        logging.info(f"Creating directory;{filedir} for the file: {filename}")
        # This above is the message creating in the terminal 
 
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:   # This will cfreate a file as it says if teh file does not exist so create a file in directory 
            pass 
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f'{filename} is already exists')
