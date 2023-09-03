## CREATE A TIKINTER INTERFACE THAT HAS 2 BUTTONS, ONE THAT OPENS THE STANDARD TABS
## AND ANOTHER THAT SWITCHES TKINTER FRAME TO ANOTHER FRAME WITHIN THE FILE post_description_file_generator.py
import os
from tkinter import *
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import webbrowser
from tkinter import messagebox
from tkinter import filedialog
## PANDAS FOR PARSING TABLE STYLE ELEMENTS
import pandas as pd
## CONNECTION TO LOCAL SQL SERVER DATABASE
from sql_connect import connect_to_sql
from generate_sql_db_if_not_exists import create_database, create_tables
from sql_utils import *

## GENERAL SETTINGS
STANDARD_SIZE=(600, 400)
ALT_SIZE=(600, 300)
STANDARD_X_PADDING = 10
STANDARD_Y_PADDING = 10
STANDARD_Y_POSITION = 75 ## THIS LINES UP ALL THE MAIN 4 BUTTONS VERTICALLY
MAIN_BG_COLOR = '#F0F8FF'
STANDARD_LABEL_HEIGHT_REDUCER = 0.5

## BUTTONS SETTINGS
STANDARD_BUTTON_DIMENSIONS = (150, 50)
STANDARD_LABEL_DIMENSIONS = (250, 50)

##############################################################################################################################################
## MAIN WINDOW SETTINGS
## LABEL
MAIN_WINDOW_LABEL_DIMENSIONS = (STANDARD_LABEL_DIMENSIONS[0], STANDARD_LABEL_DIMENSIONS[1])
MAIN_WINDOW_LABEL_X_POSITION = (STANDARD_SIZE[0]/2)-(MAIN_WINDOW_LABEL_DIMENSIONS[0]/2)
MAIN_WINDOW_LABEL_Y_POSITION = STANDARD_Y_PADDING

## FUNCTIONS
OPEN_TABS_BUTTON_DIMENSIONS = (STANDARD_BUTTON_DIMENSIONS[0], STANDARD_BUTTON_DIMENSIONS[1])
EDIT_URLS_BUTTON_DIMENSIONS = (STANDARD_BUTTON_DIMENSIONS[0], STANDARD_BUTTON_DIMENSIONS[1])

OPEN_TABS_X_POSITION = (STANDARD_SIZE[0]/2)-((STANDARD_BUTTON_DIMENSIONS[0]*2 + 10)/2) ## THIS LINE CENTERS ALL THE BUTTONS HORIZONTALLY
OPEN_TABS_Y_POSITION = STANDARD_Y_POSITION
EDIT_URLS_X_POSITION = OPEN_TABS_X_POSITION
EDIT_URLS_Y_POSITION = OPEN_TABS_Y_POSITION + OPEN_TABS_BUTTON_DIMENSIONS[1] + STANDARD_Y_PADDING


OPEN_FOLDERS_BUTTON_DIMENSIONS = (STANDARD_BUTTON_DIMENSIONS[0], STANDARD_BUTTON_DIMENSIONS[1])
EDIT_LOCAL_PATHS_BUTTON_DIMENSIONS = (STANDARD_BUTTON_DIMENSIONS[0], STANDARD_BUTTON_DIMENSIONS[1])

OPEN_FOLDERS_BUTTON_X_POSITION = OPEN_TABS_X_POSITION + OPEN_TABS_BUTTON_DIMENSIONS[0] + STANDARD_X_PADDING
OPEN_FOLDERS_BUTTON_Y_POSITION = STANDARD_Y_POSITION
EDIT_LOCAL_PATHS_BUTTON_X_POSITION = OPEN_FOLDERS_BUTTON_X_POSITION
EDIT_LOCAL_PATHS_BUTTON_Y_POSITION = OPEN_FOLDERS_BUTTON_Y_POSITION + OPEN_FOLDERS_BUTTON_DIMENSIONS[1] + STANDARD_Y_PADDING

POST_DESCRIPTION_FILE_GENERATOR_BUTTON_DIMENSIONS = (STANDARD_BUTTON_DIMENSIONS[0]*2, STANDARD_BUTTON_DIMENSIONS[1])
POST_DESCRIPTION_FILE_GENERATOR_BUTTON_X_POSITION = (STANDARD_SIZE[0]/2)-(POST_DESCRIPTION_FILE_GENERATOR_BUTTON_DIMENSIONS[0]/2)
POST_DESCRIPTION_FILE_GENERATOR_BUTTON_Y_POSITION = 200
##############################################################################################################################################
## EDIT URLS WINDOW SETTINGS
## LABEL
EDIT_URLS_WINDOW_LABEL_DIMENSIONS = (STANDARD_LABEL_DIMENSIONS[0], STANDARD_LABEL_DIMENSIONS[1])
EDIT_URLS_WINDOW_LABEL_X_POSITION = (STANDARD_SIZE[0]/2)-(EDIT_URLS_WINDOW_LABEL_DIMENSIONS[0]/2)
EDIT_URLS_WINDOW_LABEL_Y_POSITION = STANDARD_Y_PADDING

## FUNCTIONS
INSERT_NEW_URL_BUTTON_DIMENSIONS = (STANDARD_BUTTON_DIMENSIONS[0], STANDARD_BUTTON_DIMENSIONS[1])
DELETE_URL_EDIT_BUTTON_DIMENSIONS = (STANDARD_BUTTON_DIMENSIONS[0], STANDARD_BUTTON_DIMENSIONS[1])

INSERT_NEW_URL_EDIT_BUTTON_X_POSITION = (STANDARD_SIZE[0]/2)-((STANDARD_BUTTON_DIMENSIONS[0]*2 + 10)/2) ## THIS LINE CENTERS ALL THE BUTTONS HORIZONTALLY
INSERT_NEW_URL_EDIT_BUTTON_Y_POSITION = STANDARD_Y_POSITION
DELETE_URL_EDIT_BUTTON_X_POSITION = INSERT_NEW_URL_EDIT_BUTTON_X_POSITION + INSERT_NEW_URL_BUTTON_DIMENSIONS[0] + STANDARD_X_PADDING
DELETE_URL_EDIT_BUTTON_Y_POSITION = INSERT_NEW_URL_EDIT_BUTTON_Y_POSITION

## BACK BUTTON
EDIT_URLS_BACK_BUTTON_DIMENSIONS = (STANDARD_BUTTON_DIMENSIONS[0], STANDARD_BUTTON_DIMENSIONS[1])
EDIT_URLS_BACK_BUTTON_X_POSITION = (STANDARD_SIZE[0]/2)-(EDIT_URLS_BACK_BUTTON_DIMENSIONS[0]/2)
EDIT_URLS_BACK_BUTTON_Y_POSITION = DELETE_URL_EDIT_BUTTON_Y_POSITION + DELETE_URL_EDIT_BUTTON_DIMENSIONS[1] + STANDARD_Y_PADDING
##############################################################################################################################################
## EDIT LOCAL PATHS WINDOW SETTINGS
## LABEL
EDIT_LOCAL_PATHS_WINDOW_LABEL_DIMENSIONS = (STANDARD_LABEL_DIMENSIONS[0], STANDARD_LABEL_DIMENSIONS[1])
EDIT_LOCAL_PATHS_WINDOW_LABEL_X_POSITION = (STANDARD_SIZE[0]/2)-(EDIT_LOCAL_PATHS_WINDOW_LABEL_DIMENSIONS[0]/2)
EDIT_LOCAL_PATHS_WINDOW_LABEL_Y_POSITION = STANDARD_Y_PADDING

## FUNCTIONS
DELETE_LOCAL_PATH_EDIT_BUTTON_DIMENSIONS = (STANDARD_BUTTON_DIMENSIONS[0], STANDARD_BUTTON_DIMENSIONS[1])
INSERT_NEW_LOCAL_PATH_EDIT_BUTTON_DIMENSIONS = (STANDARD_BUTTON_DIMENSIONS[0], STANDARD_BUTTON_DIMENSIONS[1])

INSERT_NEW_LOCAL_PATH_EDIT_BUTTON_X_POSITION = (STANDARD_SIZE[0]/2)-((INSERT_NEW_LOCAL_PATH_EDIT_BUTTON_DIMENSIONS[0]*2 + 10)/2) ## THIS LINE CENTERS ALL THE BUTTONS HORIZONTALLY
INSERT_NEW_LOCAL_PATH_EDIT_BUTTON_Y_POSITION = STANDARD_Y_POSITION
DELETE_LOCAL_PATH_EDIT_BUTTON_X_POSITION = INSERT_NEW_LOCAL_PATH_EDIT_BUTTON_X_POSITION + INSERT_NEW_LOCAL_PATH_EDIT_BUTTON_DIMENSIONS[0] + STANDARD_X_PADDING
DELETE_LOCAL_PATH_EDIT_BUTTON_Y_POSITION = INSERT_NEW_LOCAL_PATH_EDIT_BUTTON_Y_POSITION


## BACK BUTTON
EDIT_LOCAL_PATHS_BACK_BUTTON_DIMENSIONS = (STANDARD_BUTTON_DIMENSIONS[0], STANDARD_BUTTON_DIMENSIONS[1])
EDIT_LOCAL_PATHS_BACK_BUTTON_X_POSITION = (STANDARD_SIZE[0]/2)-(EDIT_LOCAL_PATHS_BACK_BUTTON_DIMENSIONS[0]/2)
EDIT_LOCAL_PATHS_BACK_BUTTON_Y_POSITION = INSERT_NEW_LOCAL_PATH_EDIT_BUTTON_Y_POSITION + INSERT_NEW_LOCAL_PATH_EDIT_BUTTON_DIMENSIONS[1] + STANDARD_Y_PADDING
##############################################################################################################################################
## INSERT NEW URL WINDOW SETTINGS
## LABEL
INSERT_NEW_URL_WINDOW_LABEL_DIMENSIONS = (STANDARD_LABEL_DIMENSIONS[0], STANDARD_LABEL_DIMENSIONS[1])
INSERT_NEW_URL_WINDOW_LABEL_X_POSITION = (STANDARD_SIZE[0]/2)-(INSERT_NEW_URL_WINDOW_LABEL_DIMENSIONS[0]/2)
INSERT_NEW_URL_WINDOW_LABEL_Y_POSITION = STANDARD_Y_PADDING

## FUNCTIONS
URL_ENTRY_DIMENSIONS = (STANDARD_BUTTON_DIMENSIONS[0], STANDARD_BUTTON_DIMENSIONS[1])
INSERT_URL_BUTTON_DIMENSIONS = (STANDARD_BUTTON_DIMENSIONS[0], STANDARD_BUTTON_DIMENSIONS[1])

URL_ENTRY_X_POSITION = (STANDARD_SIZE[0]/2)-(URL_ENTRY_DIMENSIONS[0]/2) ## THIS LINE CENTERS ALL THE BUTTONS HORIZONTALLY
URL_ENTRY_Y_POSITION = STANDARD_Y_POSITION
INSERT_URL_BUTTON_X_POSITION = URL_ENTRY_X_POSITION
INSERT_URL_BUTTON_Y_POSITION = URL_ENTRY_Y_POSITION + URL_ENTRY_DIMENSIONS[1] + STANDARD_Y_PADDING

## BACK BUTTON
INSERT_NEW_URL_BACK_BUTTON_DIMENSIONS = (STANDARD_BUTTON_DIMENSIONS[0], STANDARD_BUTTON_DIMENSIONS[1])
INSERT_NEW_URL_BACK_BUTTON_X_POSITION = (STANDARD_SIZE[0]/2)-(INSERT_NEW_URL_BACK_BUTTON_DIMENSIONS[0]/2)
INSERT_NEW_URL_BACK_BUTTON_Y_POSITION = INSERT_URL_BUTTON_Y_POSITION + INSERT_URL_BUTTON_DIMENSIONS[1] + STANDARD_Y_PADDING
##############################################################################################################################################
## INSERT NEW LOCAL PATH WINDOW SETTINGS
## LABEL
INSERT_NEW_LOCAL_PATH_WINDOW_LABEL_DIMENSIONS = (STANDARD_LABEL_DIMENSIONS[0], STANDARD_LABEL_DIMENSIONS[1])
INSERT_NEW_LOCAL_PATH_WINDOW_LABEL_X_POSITION = (STANDARD_SIZE[0]/2)-(INSERT_NEW_LOCAL_PATH_WINDOW_LABEL_DIMENSIONS[0]/2)
INSERT_NEW_LOCAL_PATH_WINDOW_LABEL_Y_POSITION = STANDARD_Y_PADDING

## FUNCTIONS
LOCAL_PATH_ENTRY_DIMENSIONS = (STANDARD_BUTTON_DIMENSIONS[0], STANDARD_BUTTON_DIMENSIONS[1])
INSERT_LOCAL_PATH_BUTTON_DIMENSIONS = (STANDARD_BUTTON_DIMENSIONS[0], STANDARD_BUTTON_DIMENSIONS[1])

LOCAL_PATH_ENTRY_X_POSITION = (STANDARD_SIZE[0]/2)-(LOCAL_PATH_ENTRY_DIMENSIONS[0]/2) ## THIS LINE CENTERS ALL THE BUTTONS HORIZONTALLY
LOCAL_PATH_ENTRY_Y_POSITION = STANDARD_Y_POSITION
INSERT_LOCAL_PATH_BUTTON_X_POSITION = LOCAL_PATH_ENTRY_X_POSITION
INSERT_LOCAL_PATH_BUTTON_Y_POSITION = LOCAL_PATH_ENTRY_Y_POSITION + LOCAL_PATH_ENTRY_DIMENSIONS[1] + STANDARD_Y_PADDING

## BROWSE BUTTON
BROWSE_BUTTON_DIMENSIONS = (STANDARD_BUTTON_DIMENSIONS[0], STANDARD_BUTTON_DIMENSIONS[1])
BROWSE_BUTTON_X_POSITION = (STANDARD_SIZE[0]/2)-(BROWSE_BUTTON_DIMENSIONS[0]/2)
BROWSE_BUTTON_Y_POSITION = INSERT_LOCAL_PATH_BUTTON_Y_POSITION + INSERT_LOCAL_PATH_BUTTON_DIMENSIONS[1] + STANDARD_Y_PADDING

## BACK BUTTON
INSERT_NEW_LOCAL_PATH_BACK_BUTTON_DIMENSIONS = (STANDARD_BUTTON_DIMENSIONS[0], STANDARD_BUTTON_DIMENSIONS[1])
INSERT_NEW_LOCAL_PATH_BACK_BUTTON_X_POSITION = (STANDARD_SIZE[0]/2)-(INSERT_NEW_LOCAL_PATH_BACK_BUTTON_DIMENSIONS[0]/2)
INSERT_NEW_LOCAL_PATH_BACK_BUTTON_Y_POSITION = BROWSE_BUTTON_Y_POSITION + BROWSE_BUTTON_DIMENSIONS[1] + STANDARD_Y_PADDING
##############################################################################################################################################
## DELETE URLS WINDOW SETTINGS
## LABEL
DELETE_URLS_WINDOW_LABEL_DIMENSIONS = (STANDARD_LABEL_DIMENSIONS[0], STANDARD_LABEL_DIMENSIONS[1])
DELETE_URLS_WINDOW_LABEL_X_POSITION = (STANDARD_SIZE[0]/2)-(DELETE_URLS_WINDOW_LABEL_DIMENSIONS[0]/2)
DELETE_URLS_WINDOW_LABEL_Y_POSITION = STANDARD_Y_PADDING

## FUNCTIONS
DELETE_URLS_OPTION_MENU_DIMENSIONS = (STANDARD_BUTTON_DIMENSIONS[0], STANDARD_BUTTON_DIMENSIONS[1])
DELETE_URLS_BUTTON_DIMENSIONS = (STANDARD_BUTTON_DIMENSIONS[0], STANDARD_BUTTON_DIMENSIONS[1])

DELETE_URL_OPTION_MENU_X_POSITION = (STANDARD_SIZE[0]/2)-(DELETE_URLS_OPTION_MENU_DIMENSIONS[0]/2) ## THIS LINE CENTERS ALL THE BUTTONS HORIZONTALLY
DELETE_URL_OPTION_MENU_Y_POSITION = STANDARD_Y_POSITION
DELETE_URL_BUTTON_X_POSITION = DELETE_URL_OPTION_MENU_X_POSITION
DELETE_URL_BUTTON_Y_POSITION = DELETE_URL_OPTION_MENU_Y_POSITION + DELETE_URLS_OPTION_MENU_DIMENSIONS[1] + STANDARD_Y_PADDING

## BACK BUTTON
DELETE_URLS_BACK_BUTTON_DIMENSIONS = (STANDARD_BUTTON_DIMENSIONS[0], STANDARD_BUTTON_DIMENSIONS[1])
DELETE_URLS_BACK_BUTTON_X_POSITION = (STANDARD_SIZE[0]/2)-(DELETE_URLS_BACK_BUTTON_DIMENSIONS[0]/2)
DELETE_URLS_BACK_BUTTON_Y_POSITION = DELETE_URL_OPTION_MENU_Y_POSITION + DELETE_URLS_BUTTON_DIMENSIONS[1] + STANDARD_Y_PADDING
##############################################################################################################################################
## DELETE LOCAL PATHS WINDOW SETTINGS
## LABEL
DELETE_LOCAL_PATHS_WINDOW_LABEL_DIMENSIONS = (STANDARD_LABEL_DIMENSIONS[0], STANDARD_LABEL_DIMENSIONS[1])
DELETE_LOCAL_PATHS_WINDOW_LABEL_X_POSITION = (STANDARD_SIZE[0]/2)-(DELETE_LOCAL_PATHS_WINDOW_LABEL_DIMENSIONS[0]/2)
DELETE_LOCAL_PATHS_WINDOW_LABEL_Y_POSITION = STANDARD_Y_PADDING

## FUNCTIONS
DELETE_LOCAL_PATHS_OPTION_MENU_DIMENSIONS = (STANDARD_BUTTON_DIMENSIONS[0], STANDARD_BUTTON_DIMENSIONS[1])
DELETE_LOCAL_PATHS_BUTTON_DIMENSIONS = (STANDARD_BUTTON_DIMENSIONS[0], STANDARD_BUTTON_DIMENSIONS[1])

DELETE_LOCAL_PATHS_OPTION_MENU_X_POSITION = (STANDARD_SIZE[0]/2)-(DELETE_LOCAL_PATHS_OPTION_MENU_DIMENSIONS[0]/2) ## THIS LINE CENTERS ALL THE BUTTONS HORIZONTALLY
DELETE_LOCAL_PATHS_OPTION_MENU_Y_POSITION = STANDARD_Y_POSITION
DELETE_LOCAL_PATHS_BUTTON_X_POSITION = DELETE_LOCAL_PATHS_OPTION_MENU_X_POSITION
DELETE_LOCAL_PATHS_BUTTON_Y_POSITION = DELETE_LOCAL_PATHS_OPTION_MENU_Y_POSITION + DELETE_LOCAL_PATHS_OPTION_MENU_DIMENSIONS[1] + STANDARD_Y_PADDING
##############################################################################################################################################
## POST DESCRIPTION FILE GENERATOR WINDOW SETTINGS
## LABELS
POST_DESCRIPTION_FILE_GENERATOR_WINDOW_LABEL_DIMENSIONS = (STANDARD_LABEL_DIMENSIONS[0]*1.3, STANDARD_LABEL_DIMENSIONS[1])
POST_DESCRIPTION_FILE_GENERATOR_WINDOW_LABEL_X_POSITION = (STANDARD_SIZE[0]/2)-(POST_DESCRIPTION_FILE_GENERATOR_WINDOW_LABEL_DIMENSIONS[0]/2)
POST_DESCRIPTION_FILE_GENERATOR_WINDOW_LABEL_Y_POSITION = STANDARD_Y_PADDING


## NUMBER OF POSTS LABEL
POST_DESCRIPTION_NUMBER_OF_POSTS_LABEL_DIMENSIONS = (STANDARD_LABEL_DIMENSIONS[0], STANDARD_LABEL_DIMENSIONS[1]*STANDARD_LABEL_HEIGHT_REDUCER)
POST_DESCRIPTION_NUMBER_OF_POSTS_LABEL_X_POSITION = (STANDARD_SIZE[0]/2)-(POST_DESCRIPTION_NUMBER_OF_POSTS_LABEL_DIMENSIONS[0]/2)
POST_DESCRIPTION_NUMBER_OF_POSTS_LABEL_Y_POSITION = POST_DESCRIPTION_FILE_GENERATOR_WINDOW_LABEL_Y_POSITION + POST_DESCRIPTION_FILE_GENERATOR_WINDOW_LABEL_DIMENSIONS[1] + STANDARD_Y_PADDING

## NUMBER OF POSTS ENTRY
NUMBER_OF_POSTS_ENTRY_DIMENSIONS = (STANDARD_BUTTON_DIMENSIONS[0], STANDARD_BUTTON_DIMENSIONS[1])
NUMBER_OF_POSTS_ENTRY_X_POSITION = (STANDARD_SIZE[0]/2)-(NUMBER_OF_POSTS_ENTRY_DIMENSIONS[0]/2)
NUMBER_OF_POSTS_ENTRY_Y_POSITION = POST_DESCRIPTION_NUMBER_OF_POSTS_LABEL_Y_POSITION + POST_DESCRIPTION_NUMBER_OF_POSTS_LABEL_DIMENSIONS[1] + STANDARD_Y_PADDING

## INITIAL POST NUMBER LABEL
POST_DESCRIPTION_INITIAL_POST_NUMBER_LABEL_DIMENSIONS = (STANDARD_LABEL_DIMENSIONS[0], STANDARD_LABEL_DIMENSIONS[1]*STANDARD_LABEL_HEIGHT_REDUCER)
POST_DESCRIPTION_INITIAL_POST_NUMBER_LABEL_X_POSITION = (STANDARD_SIZE[0]/2)-(POST_DESCRIPTION_INITIAL_POST_NUMBER_LABEL_DIMENSIONS[0]/2)
POST_DESCRIPTION_INITIAL_POST_NUMBER_LABEL_Y_POSITION = NUMBER_OF_POSTS_ENTRY_Y_POSITION + NUMBER_OF_POSTS_ENTRY_DIMENSIONS[1] + STANDARD_Y_PADDING

## INITIAL POST NUMBER ENTRY
INITIAL_POST_NUMBER_ENTRY_DIMENSIONS = (STANDARD_BUTTON_DIMENSIONS[0], STANDARD_BUTTON_DIMENSIONS[1])
INITIAL_POST_NUMBER_ENTRY_X_POSITION = (STANDARD_SIZE[0]/2)-(INITIAL_POST_NUMBER_ENTRY_DIMENSIONS[0]/2)
INITIAL_POST_NUMBER_ENTRY_Y_POSITION = POST_DESCRIPTION_INITIAL_POST_NUMBER_LABEL_Y_POSITION + POST_DESCRIPTION_INITIAL_POST_NUMBER_LABEL_DIMENSIONS[1] + STANDARD_Y_PADDING

## CREATE FILES BUTTON
CREATE_FILES_BUTTON_DIMENSIONS = (STANDARD_BUTTON_DIMENSIONS[0], STANDARD_BUTTON_DIMENSIONS[1])
CREATE_FILES_BUTTON_X_POSITION = (STANDARD_SIZE[0]/2)-(CREATE_FILES_BUTTON_DIMENSIONS[0]/2)
CREATE_FILES_BUTTON_Y_POSITION = INITIAL_POST_NUMBER_ENTRY_Y_POSITION + INITIAL_POST_NUMBER_ENTRY_DIMENSIONS[1] + STANDARD_Y_PADDING
##############################################################################################################################################

def center(root, WINDOW_SIZE):
    root.update_idletasks()  # Update "requested size" from geometry manager
    X, Y =  WINDOW_SIZE.split("x")
    x = ((root.winfo_screenwidth() - root.winfo_reqwidth()) / 2) - int(X)/2
    y = ((root.winfo_screenheight() - root.winfo_reqheight()) / 2) - int(Y)/2
    root.geometry("+%d+%d" % (x, y))
    
    root.deiconify()

##############################################################################################################
##############################################################################################################
class MainInterface:
    def __init__(self, master):
        WINDOW_SIZE = f"{STANDARD_SIZE[0]}x{STANDARD_SIZE[1]}"
        self.master = master
        master.title("Main Interface")
        master.geometry(WINDOW_SIZE)
        master.resizable(False, False)
        master.configure(background='#F0F8FF')

        ## OPENING WINDOW AT CENTER
        center(master, WINDOW_SIZE)

        ## STYLES
        self.style = ttk.Style(master)
        self.style.theme_use("xpnative")


        self.label = ttk.Label(master, anchor="center", text="INSTAGRAM AUTOMATION TOOL", justify=tk.RIGHT, background=MAIN_BG_COLOR, font=("Helvetica", 14))
        self.label.place(width=MAIN_WINDOW_LABEL_DIMENSIONS[0], height=MAIN_WINDOW_LABEL_DIMENSIONS[1], x=MAIN_WINDOW_LABEL_X_POSITION, y=MAIN_WINDOW_LABEL_Y_POSITION)

        self.open_tabs_button = ttk.Button(master, text="Open Tabs", command=self.open_tabs)
        self.open_tabs_button.place(width=OPEN_TABS_BUTTON_DIMENSIONS[0], height=OPEN_TABS_BUTTON_DIMENSIONS[1], x=OPEN_TABS_X_POSITION, y=OPEN_TABS_Y_POSITION)

        ## CREATE A BUTTON THAT OPENS A NEW WINDOW CALLED EDIT URLS
        self.edit_urls_button = ttk.Button(master, text="Edit URLs", command=self.edit_urls)
        self.edit_urls_button.place(width=EDIT_URLS_BUTTON_DIMENSIONS[0], height=EDIT_URLS_BUTTON_DIMENSIONS[1], x=EDIT_URLS_X_POSITION, y=EDIT_URLS_Y_POSITION)

        self.open_tabs_button = ttk.Button(master, text="Open Folders", command=self.open_folders)
        self.open_tabs_button.place(width=OPEN_FOLDERS_BUTTON_DIMENSIONS[0], height=OPEN_FOLDERS_BUTTON_DIMENSIONS[1], x=OPEN_FOLDERS_BUTTON_X_POSITION, y=OPEN_FOLDERS_BUTTON_Y_POSITION)


        ## CREATE A BUTTON THAT OPENS A NEW WINDOW CALLED EDIT LOCAL PATHS
        self.edit_local_paths_button = ttk.Button(master, text="Edit Local Paths", command=self.edit_local_paths)
        self.edit_local_paths_button.place(width=EDIT_LOCAL_PATHS_BUTTON_DIMENSIONS[0], height=EDIT_LOCAL_PATHS_BUTTON_DIMENSIONS[1], x=EDIT_LOCAL_PATHS_BUTTON_X_POSITION, y=EDIT_LOCAL_PATHS_BUTTON_Y_POSITION)


        self.open_post_description_file_generator_button = ttk.Button(master, text="Post Description File Generator", command=self.open_post_description_file_generator)
        self.open_post_description_file_generator_button.place(width=POST_DESCRIPTION_FILE_GENERATOR_BUTTON_DIMENSIONS[0], height=POST_DESCRIPTION_FILE_GENERATOR_BUTTON_DIMENSIONS[1], x=POST_DESCRIPTION_FILE_GENERATOR_BUTTON_X_POSITION, y=POST_DESCRIPTION_FILE_GENERATOR_BUTTON_Y_POSITION)
        

    def open_tabs(self):
        brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe %s"
        brave = webbrowser.get(brave_path)
        
        ## CREATE AN SQL QUERY THAT SELECTS THE TABLE urls_table AND FETCHES ALL THE URLS
        ## CREATE A FOR LOOP THAT OPENS ALL THE URLS IN THE TABLE urls_table

        conn, cursor = connect_to_sql()
        cursor.execute("SELECT * FROM urls_table")
        urls = cursor.fetchall()
        conn.close()

        
        brave.open("") ## THIS LINE OPENS A NEW BRAVE INSTANCE
        for url in urls:
            brave.open_new(url[1])


    def open_folders(self):
        ## CREATE AN SQL QUERY THAT SELECTS THE TABLE local_paths_table AND FETCHES ALL THE LOCAL PATHS
        ## CREATE A FOR LOOP THAT OPENS ALL THE LOCAL PATH FOLDERS
        conn, cursor = connect_to_sql()
        cursor.execute("SELECT * FROM local_paths_table")
        paths = cursor.fetchall()
        conn.close()

        for current_path in paths:
            path_parsed = os.path.realpath(current_path[1])
            try:
                os.startfile(path_parsed)
            except:
                messagebox.showerror("Error", "The path {} does not exist!".format(path_parsed))


    def edit_urls(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        self.app = EditUrls(self.newWindow)


    def edit_local_paths(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        self.app = EditLocalPaths(self.newWindow)


    def open_post_description_file_generator(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        self.app = PostDescriptionFileGenerator(self.newWindow)


##############################################################################################################
##############################################################################################################
class PostDescriptionFileGenerator:
    def __init__(self, master):
        WINDOW_SIZE = f"{STANDARD_SIZE[0]}x{STANDARD_SIZE[1]}"
        self.master = master
        master.title("Post Description File Generator")
        master.geometry(WINDOW_SIZE)
        master.resizable(False, False)
        master.configure(background='#F0F8FF')

        ## OPENING WINDOW AT CENTER
        center(master, WINDOW_SIZE)

        ## STYLES
        self.style = ttk.Style(master)
        self.style.theme_use("xpnative")

        self.window_label = ttk.Label(master, anchor="center", text="Post Description File Generator", justify=tk.RIGHT, background=MAIN_BG_COLOR, font=("Helvetica", 14))
        self.window_label.place(width=POST_DESCRIPTION_FILE_GENERATOR_WINDOW_LABEL_DIMENSIONS[0], height=POST_DESCRIPTION_FILE_GENERATOR_WINDOW_LABEL_DIMENSIONS[1], x=POST_DESCRIPTION_FILE_GENERATOR_WINDOW_LABEL_X_POSITION, y=POST_DESCRIPTION_FILE_GENERATOR_WINDOW_LABEL_Y_POSITION)

        self.lbl_number_of_posts = ttk.Label(master, anchor="center", text="Number of posts to be created", justify=tk.RIGHT, background=MAIN_BG_COLOR)
        self.lbl_number_of_posts.place(width=POST_DESCRIPTION_NUMBER_OF_POSTS_LABEL_DIMENSIONS[0], height=POST_DESCRIPTION_NUMBER_OF_POSTS_LABEL_DIMENSIONS[1], x=POST_DESCRIPTION_NUMBER_OF_POSTS_LABEL_X_POSITION, y=POST_DESCRIPTION_NUMBER_OF_POSTS_LABEL_Y_POSITION)

        self.entry_number_of_posts = ttk.Entry(master, width=10)
        self.entry_number_of_posts.place(width=NUMBER_OF_POSTS_ENTRY_DIMENSIONS[0], height=NUMBER_OF_POSTS_ENTRY_DIMENSIONS[1], x=NUMBER_OF_POSTS_ENTRY_X_POSITION, y=NUMBER_OF_POSTS_ENTRY_Y_POSITION)

        self.lbl_initial_post_number = ttk.Label(master, anchor="center", text="Initial post number", justify=tk.RIGHT, background=MAIN_BG_COLOR)
        self.lbl_initial_post_number.place(width=POST_DESCRIPTION_INITIAL_POST_NUMBER_LABEL_DIMENSIONS[0], height=POST_DESCRIPTION_INITIAL_POST_NUMBER_LABEL_DIMENSIONS[1], x=POST_DESCRIPTION_INITIAL_POST_NUMBER_LABEL_X_POSITION, y=POST_DESCRIPTION_INITIAL_POST_NUMBER_LABEL_Y_POSITION)

        self.entry_initial_post_number = ttk.Entry(master, width=10)
        self.entry_initial_post_number.place(width=INITIAL_POST_NUMBER_ENTRY_DIMENSIONS[0], height=INITIAL_POST_NUMBER_ENTRY_DIMENSIONS[1], x=INITIAL_POST_NUMBER_ENTRY_X_POSITION, y=INITIAL_POST_NUMBER_ENTRY_Y_POSITION)

        self.button_create_files = ttk.Button(master, text="Create files", command=self.clicked)
        self.button_create_files.place(width=CREATE_FILES_BUTTON_DIMENSIONS[0], height=CREATE_FILES_BUTTON_DIMENSIONS[1], x=CREATE_FILES_BUTTON_X_POSITION, y=CREATE_FILES_BUTTON_Y_POSITION)

        ## CREATE A BUTTON THAT GOES BACK TO THE MAIN INTERFACE
        self.button_back = ttk.Button(master, text="Back", command=self.back)
        self.button_back.place(width=CREATE_FILES_BUTTON_DIMENSIONS[0], height=CREATE_FILES_BUTTON_DIMENSIONS[1], x=CREATE_FILES_BUTTON_X_POSITION, y=CREATE_FILES_BUTTON_Y_POSITION + CREATE_FILES_BUTTON_DIMENSIONS[1] + STANDARD_Y_PADDING)


    def back(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        self.app = MainInterface(self.newWindow)

    def create_post_description_text_file(self, path, num_of_posts=1, initial_post_number=1):
        """
        Creates a text file with the description of the post
        :param path: path to the folder where the text file will be created
        :param num_of_posts: number of posts to be created
        :param initial_post_number: number of the first post
        :return: None
        """
        for i in range(num_of_posts):
            with open(path + "\post_{}.txt".format(initial_post_number + i), "a+", encoding='utf-8') as file:
                file.write("Texto da descrição do post {}".format(initial_post_number + i))

        print("Arquivos criados com sucesso")

    def clicked(self):
        try:
            num_of_posts = int(self.entry1.get())
            initial_post_number = int(self.entry2.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")
            return
        
        path = r"C:\Users\clib_\OneDrive\Desktop\SHAPER\MFCS\DESCRICAO_POSTS\DESCRICAO_POSTS_INSTAGRAM"

        self.create_post_description_text_file(path, num_of_posts, initial_post_number)
        messagebox.showinfo("Success", "Files created successfully!")


##############################################################################################################
##############################################################################################################
class EditUrls:
    def __init__(self, master):
        WINDOW_SIZE = f"{STANDARD_SIZE[0]}x{STANDARD_SIZE[1]}"
        self.master = master
        master.title("Edit URLs")
        master.geometry(WINDOW_SIZE)
        master.resizable(False, False)
        master.configure(background='#F0F8FF')

        ## OPENING WINDOW AT CENTER
        center(master, WINDOW_SIZE)

        ## STYLES
        self.style = ttk.Style(master)
        self.style.theme_use("xpnative")

        self.label = ttk.Label(master, anchor="center", text="Edit URLs", justify=tk.RIGHT, background=MAIN_BG_COLOR, font=("Helvetica", 14))
        self.label.place(width=EDIT_URLS_WINDOW_LABEL_DIMENSIONS[0], height=EDIT_URLS_WINDOW_LABEL_DIMENSIONS[1], x=EDIT_URLS_WINDOW_LABEL_X_POSITION, y=EDIT_URLS_WINDOW_LABEL_Y_POSITION)

        ## CREATE A BUTTON THAT OPENS A NEW WINDOW CALLED INSERT NEW URL
        self.insert_new_url_button = ttk.Button(master, text="Insert New URL", command=self.insert_new_url)
        self.insert_new_url_button.place(width=INSERT_NEW_URL_BUTTON_DIMENSIONS[0], height=INSERT_NEW_URL_BUTTON_DIMENSIONS[1], x=INSERT_NEW_URL_EDIT_BUTTON_X_POSITION, y=INSERT_NEW_URL_EDIT_BUTTON_Y_POSITION)

        self.delete_url_button = ttk.Button(master, text="Delete URLs", command=self.delete_urls)
        self.delete_url_button.place(width=DELETE_URL_EDIT_BUTTON_DIMENSIONS[0], height=DELETE_URL_EDIT_BUTTON_DIMENSIONS[1], x=DELETE_URL_EDIT_BUTTON_X_POSITION, y=DELETE_URL_EDIT_BUTTON_Y_POSITION)

        ## CREATE A BUTTON THAT GOES BACK TO THE MAIN INTERFACE
        self.button_back = ttk.Button(master, text="Back", command=self.back)
        self.button_back.place(width=EDIT_URLS_BACK_BUTTON_DIMENSIONS[0], height=EDIT_URLS_BACK_BUTTON_DIMENSIONS[1], x=EDIT_URLS_BACK_BUTTON_X_POSITION, y=EDIT_URLS_BACK_BUTTON_Y_POSITION)

    
    def insert_new_url(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        self.app = InsertNewUrl(self.newWindow)

    def delete_urls(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        self.app = DeleteUrls(self.newWindow)

    def back(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        self.app = MainInterface(self.newWindow)


##############################################################################################################
##############################################################################################################
class InsertNewUrl:
    def __init__(self, master):
        WINDOW_SIZE = f"{STANDARD_SIZE[0]}x{STANDARD_SIZE[1]}"
        self.master = master
        master.title("Insert New URL")
        master.geometry(WINDOW_SIZE)
        master.resizable(False, False)
        master.configure(background='#F0F8FF')

        ## OPENING WINDOW AT CENTER
        center(master, WINDOW_SIZE)

        ## STYLES
        self.style = ttk.Style(master)
        self.style.theme_use("xpnative")

        self.label = ttk.Label(master, anchor="center", text="Insert New URL", justify=tk.RIGHT, background=MAIN_BG_COLOR, font=("Helvetica", 14))
        self.label.place(width=INSERT_NEW_URL_WINDOW_LABEL_DIMENSIONS[0], height=INSERT_NEW_URL_WINDOW_LABEL_DIMENSIONS[1], x=INSERT_NEW_URL_WINDOW_LABEL_X_POSITION, y=INSERT_NEW_URL_WINDOW_LABEL_Y_POSITION)

        self.label1 = ttk.Label(master, anchor="center", text="URL", justify=tk.RIGHT, background=MAIN_BG_COLOR)
        self.label1.place(width=URL_ENTRY_DIMENSIONS[0], height=URL_ENTRY_DIMENSIONS[1], x=URL_ENTRY_X_POSITION, y=URL_ENTRY_Y_POSITION)

        self.entry1 = ttk.Entry(master, width=10)
        self.entry1.place(width=URL_ENTRY_DIMENSIONS[0], height=URL_ENTRY_DIMENSIONS[1], x=URL_ENTRY_X_POSITION, y=URL_ENTRY_Y_POSITION)

        self.button = ttk.Button(master, text="Insert", command=self.insert)
        self.button.place(width=INSERT_URL_BUTTON_DIMENSIONS[0], height=INSERT_URL_BUTTON_DIMENSIONS[1], x=INSERT_URL_BUTTON_X_POSITION, y=INSERT_URL_BUTTON_Y_POSITION)

        ## CREATE A BUTTON THAT GOES BACK TO THE MAIN INTERFACE
        self.button_back = ttk.Button(master, text="Back", command=self.back)
        self.button_back.place(width=INSERT_NEW_URL_BACK_BUTTON_DIMENSIONS[0], height=INSERT_NEW_URL_BACK_BUTTON_DIMENSIONS[1], x=INSERT_NEW_URL_BACK_BUTTON_X_POSITION, y=INSERT_NEW_URL_BACK_BUTTON_Y_POSITION)
        

    def back(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        self.app = EditUrls(self.newWindow)

    def insert(self):
        try:
            url = self.entry1.get()
            if url == "":
                messagebox.showerror("Error", "Please do not leave blank spaces!")
                return
        except ValueError:
            messagebox.showerror("Error", "Please do not leave blank spaces!")
            return

        ## CREATE AN SQL QUERY THAT INSERTS THE URL INTO THE TABLE urls_table

        conn, cursor = connect_to_sql()
        cursor.execute(f"INSERT INTO urls_table (url) VALUES ('{url}')")
        conn.commit()
        delete_duplicates_in_urls_table(conn, cursor)
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "URL inserted successfully!")


##############################################################################################################
##############################################################################################################
class DeleteUrls:
    def __init__(self, master):
        WINDOW_SIZE = f"{STANDARD_SIZE[0]}x{STANDARD_SIZE[1]}"
        self.master = master
        master.title("Delete URLs")
        master.geometry(WINDOW_SIZE)
        master.resizable(False, False)
        master.configure(background='#F0F8FF')

        ## OPENING WINDOW AT CENTER
        center(master, WINDOW_SIZE)

        ## STYLES
        self.style = ttk.Style(master)
        self.style.theme_use("xpnative")

        self.label = ttk.Label(master, anchor="center", text="Delete URLs", justify=tk.RIGHT, background=MAIN_BG_COLOR, font=("Helvetica", 14))
        self.label.place(width=DELETE_URLS_WINDOW_LABEL_DIMENSIONS[0], height=DELETE_URLS_WINDOW_LABEL_DIMENSIONS[1], x=DELETE_URLS_WINDOW_LABEL_X_POSITION, y=DELETE_URLS_WINDOW_LABEL_Y_POSITION)

        self.option_menu_variable = StringVar(master)
        self.options = self.set_dropdown()

        if self.options:
            self.option_menu = ttk.OptionMenu(master, self.option_menu_variable, *self.options)
        else:
            self.option_menu = ttk.OptionMenu(master, self.option_menu_variable, "No URLs to delete")
        self.option_menu.place(width=DELETE_URLS_OPTION_MENU_DIMENSIONS[0], height=DELETE_URLS_OPTION_MENU_DIMENSIONS[1], x=DELETE_URL_OPTION_MENU_X_POSITION, y=DELETE_URL_OPTION_MENU_Y_POSITION)

        self.button = ttk.Button(master, text="Delete", command=self.delete)
        self.button.place(width=DELETE_URLS_BUTTON_DIMENSIONS[0], height=DELETE_URLS_BUTTON_DIMENSIONS[1], x=DELETE_URL_BUTTON_X_POSITION, y=DELETE_URL_BUTTON_Y_POSITION)

        ## CREATE A BUTTON THAT GOES BACK TO THE MAIN INTERFACE
        self.button_back = ttk.Button(master, text="Back", command=self.back)
        self.button_back.place(width=DELETE_URLS_BUTTON_DIMENSIONS[0], height=DELETE_URLS_BUTTON_DIMENSIONS[1], x=DELETE_URL_BUTTON_X_POSITION, y=DELETE_URL_BUTTON_Y_POSITION + DELETE_URLS_BUTTON_DIMENSIONS[1] + STANDARD_Y_PADDING)


    def set_dropdown(self):
        ## SETTING THE DROPDOWN TO CHOSE FROM THE URLS IN THE TABLE urls_table
        self.options = fetch_urls_from_urls_table()
        try:
            self.option_menu_variable.set(self.options[0])
            return self.options
        except IndexError:
            messagebox.showerror("Error", "There are no more URLs to delete!")
            self.back()
            return

    def update_option_menu(self):
        menu = self.option_menu["menu"]
        menu.delete(0, "end")
        for string in self.options:
            menu.add_command(label=string, 
                             command=lambda value=string: self.option_menu_variable.set(value))

    def back(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        self.app = EditUrls(self.newWindow)

    def delete(self):
        try:
            url = self.option_menu_variable.get()
        except ValueError:
            messagebox.showerror("Error", "Please do not leave blank spaces!")
            return

        ## CREATE AN SQL QUERY THAT DELETES THE URL FROM THE TABLE urls_table

        conn, cursor = connect_to_sql()
        cursor.execute(f"DELETE FROM urls_table WHERE url = '{url}'")
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "URL deleted successfully!")

        self.options = self.set_dropdown()
        if self.options:
            self.update_option_menu()


##############################################################################################################
##############################################################################################################
class EditLocalPaths:
    def __init__(self, master):
        WINDOW_SIZE = f"{STANDARD_SIZE[0]}x{STANDARD_SIZE[1]}"
        self.master = master
        master.title("Edit Local Paths")
        master.geometry(WINDOW_SIZE)
        master.resizable(False, False)
        master.configure(background='#F0F8FF')

        ## OPENING WINDOW AT CENTER
        center(master, WINDOW_SIZE)

        ## STYLES
        self.style = ttk.Style(master)
        self.style.theme_use("xpnative")

        self.label = ttk.Label(master, anchor="center", text="Edit Local Paths", justify=tk.RIGHT, background=MAIN_BG_COLOR, font=("Helvetica", 14))
        self.label.place(width=EDIT_LOCAL_PATHS_WINDOW_LABEL_DIMENSIONS[0], height=EDIT_LOCAL_PATHS_WINDOW_LABEL_DIMENSIONS[1], x=EDIT_LOCAL_PATHS_WINDOW_LABEL_X_POSITION, y=EDIT_LOCAL_PATHS_WINDOW_LABEL_Y_POSITION)

        self.button = ttk.Button(master, text="Delete Local Paths", command=self.delete_local_paths)
        self.button.place(width=DELETE_LOCAL_PATHS_BUTTON_DIMENSIONS[0], height=DELETE_LOCAL_PATHS_BUTTON_DIMENSIONS[1], x=DELETE_LOCAL_PATH_EDIT_BUTTON_X_POSITION, y=DELETE_LOCAL_PATH_EDIT_BUTTON_Y_POSITION)

        ## CREATE A BUTTON THAT OPENS A NEW WINDOW CALLED INSERT NEW LOCAL PATH
        self.insert_new_local_path_button = ttk.Button(master, text="Insert New Local Path", command=self.insert_new_local_path)
        self.insert_new_local_path_button.place(width=INSERT_NEW_LOCAL_PATH_EDIT_BUTTON_DIMENSIONS[0], height=INSERT_NEW_LOCAL_PATH_EDIT_BUTTON_DIMENSIONS[1], x=INSERT_NEW_LOCAL_PATH_EDIT_BUTTON_X_POSITION, y=INSERT_NEW_LOCAL_PATH_EDIT_BUTTON_Y_POSITION)

        ## CREATE A BUTTON THAT GOES BACK TO THE MAIN INTERFACE
        self.button_back = ttk.Button(master, text="Back", command=self.back)
        self.button_back.place(width=EDIT_LOCAL_PATHS_BACK_BUTTON_DIMENSIONS[0], height=EDIT_LOCAL_PATHS_BACK_BUTTON_DIMENSIONS[1], x=EDIT_LOCAL_PATHS_BACK_BUTTON_X_POSITION, y=EDIT_LOCAL_PATHS_BACK_BUTTON_Y_POSITION)


    def insert_new_local_path(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        self.app = InsertNewLocalPath(self.newWindow)

    def delete_local_paths(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        self.app = DeleteLocalPaths(self.newWindow)

    def back(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        self.app = MainInterface(self.newWindow)


##############################################################################################################
##############################################################################################################
class InsertNewLocalPath:
    def __init__(self, master):
        WINDOW_SIZE = f"{STANDARD_SIZE[0]}x{STANDARD_SIZE[1]}"
        self.master = master
        master.title("Insert New Local Path")
        master.geometry(WINDOW_SIZE)
        master.resizable(False, False)
        master.configure(background='#F0F8FF')

        ## OPENING WINDOW AT CENTER
        center(master, WINDOW_SIZE)

        ## STYLES
        self.style = ttk.Style(master)
        self.style.theme_use("xpnative")

        self.label = ttk.Label(master, anchor="center", text="Insert New Local Path", justify=tk.RIGHT, background=MAIN_BG_COLOR, font=("Helvetica", 14))
        self.label.place(width=INSERT_NEW_LOCAL_PATH_WINDOW_LABEL_DIMENSIONS[0], height=INSERT_NEW_LOCAL_PATH_WINDOW_LABEL_DIMENSIONS[1], x=INSERT_NEW_LOCAL_PATH_WINDOW_LABEL_X_POSITION, y=INSERT_NEW_LOCAL_PATH_WINDOW_LABEL_Y_POSITION)

        self.label1 = ttk.Label(master, anchor="center", text="Local Path", justify=tk.RIGHT, background=MAIN_BG_COLOR)
        self.label1.place(width=LOCAL_PATH_ENTRY_DIMENSIONS[0], height=LOCAL_PATH_ENTRY_DIMENSIONS[1], x=LOCAL_PATH_ENTRY_X_POSITION, y=LOCAL_PATH_ENTRY_Y_POSITION)

        ## INSTEAD OF AN ENTRY, PLEASE ALLOW THE USER TO NAVIGATE ITS OWN PC AND SELECT A FOLDER
        ## THE SELECTED FOLDER WILL BE THE LOCAL PATH

        self.entry1 = ttk.Entry(master, width=10)
        self.entry1.place(width=LOCAL_PATH_ENTRY_DIMENSIONS[0], height=LOCAL_PATH_ENTRY_DIMENSIONS[1], x=LOCAL_PATH_ENTRY_X_POSITION, y=LOCAL_PATH_ENTRY_Y_POSITION)

        self.button = ttk.Button(master, text="Insert", command=self.insert)
        self.button.place(width=INSERT_LOCAL_PATH_BUTTON_DIMENSIONS[0], height=INSERT_LOCAL_PATH_BUTTON_DIMENSIONS[1], x=INSERT_LOCAL_PATH_BUTTON_X_POSITION, y=INSERT_LOCAL_PATH_BUTTON_Y_POSITION)

        self.browse_button = ttk.Button(master, text="Browse", command=self.browse_local_folders)
        self.browse_button.place(width=BROWSE_BUTTON_DIMENSIONS[0], height=BROWSE_BUTTON_DIMENSIONS[1], x=BROWSE_BUTTON_X_POSITION, y=BROWSE_BUTTON_Y_POSITION)

        ## CREATE A BUTTON THAT GOES BACK TO THE MAIN INTERFACE
        self.button_back = ttk.Button(master, text="Back", command=self.back)
        self.button_back.place(width=INSERT_NEW_LOCAL_PATH_BACK_BUTTON_DIMENSIONS[0], height=INSERT_NEW_LOCAL_PATH_BACK_BUTTON_DIMENSIONS[1], x=INSERT_NEW_LOCAL_PATH_BACK_BUTTON_X_POSITION, y=INSERT_NEW_LOCAL_PATH_BACK_BUTTON_Y_POSITION)

        

    def browse_local_folders(self):
        filename = filedialog.askdirectory()
        self.entry1.insert(END, filename)

    def insert(self):
        try:
            local_path = self.entry1.get()
            if local_path == "":
                messagebox.showerror("Error", "Please do not leave blank spaces!")
                return
        except ValueError:
            messagebox.showerror("Error", "Please do not leave blank spaces!")
            return

        ## CREATE AN SQL QUERY THAT INSERTS THE LOCAL PATH INTO THE TABLE local_paths_table

        conn, cursor = connect_to_sql()
        cursor.execute(f"INSERT INTO local_paths_table (local_path) VALUES ('{local_path}')")
        conn.commit()
        delete_duplicates_in_local_paths_table(conn, cursor)
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Local Path inserted successfully!")

    def back(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        self.app = EditLocalPaths(self.newWindow)


##############################################################################################################
##############################################################################################################
class DeleteLocalPaths:

    def __init__(self, master):
        WINDOW_SIZE = f"{STANDARD_SIZE[0]}x{STANDARD_SIZE[1]}"
        self.master = master
        master.title("Delete Local Paths")
        master.geometry(WINDOW_SIZE)
        master.resizable(False, False)
        master.configure(background='#F0F8FF')

        ## OPENING WINDOW AT CENTER
        center(master, WINDOW_SIZE)

        ## STYLES
        self.style = ttk.Style(master)
        self.style.theme_use("xpnative")

        self.label = ttk.Label(master, anchor="center", text="Delete Local Paths", justify=tk.RIGHT, background=MAIN_BG_COLOR, font=("Helvetica", 14))
        self.label.place(width=DELETE_LOCAL_PATHS_WINDOW_LABEL_DIMENSIONS[0], height=DELETE_LOCAL_PATHS_WINDOW_LABEL_DIMENSIONS[1], x=DELETE_LOCAL_PATHS_WINDOW_LABEL_X_POSITION, y=DELETE_LOCAL_PATHS_WINDOW_LABEL_Y_POSITION)

        self.option_menu_variable = StringVar(master)
        self.options = self.set_dropdown()

        if self.options:
            self.option_menu = ttk.OptionMenu(master, self.option_menu_variable, *self.options)
        else:
            self.option_menu = ttk.OptionMenu(master, self.option_menu_variable, "No Local Paths to delete")
        self.option_menu.place(width=DELETE_LOCAL_PATHS_OPTION_MENU_DIMENSIONS[0], height=DELETE_LOCAL_PATHS_OPTION_MENU_DIMENSIONS[1], x=DELETE_LOCAL_PATHS_OPTION_MENU_X_POSITION, y=DELETE_LOCAL_PATHS_OPTION_MENU_Y_POSITION)

        self.button = ttk.Button(master, text="Delete", command=self.delete)
        self.button.place(width=DELETE_LOCAL_PATHS_BUTTON_DIMENSIONS[0], height=DELETE_LOCAL_PATHS_BUTTON_DIMENSIONS[1], x=DELETE_LOCAL_PATHS_BUTTON_X_POSITION, y=DELETE_LOCAL_PATHS_BUTTON_Y_POSITION)

        ## CREATE A BUTTON THAT GOES BACK TO THE MAIN INTERFACE
        self.button_back = ttk.Button(master, text="Back", command=self.back)
        self.button_back.place(width=DELETE_LOCAL_PATHS_BUTTON_DIMENSIONS[0], height=DELETE_LOCAL_PATHS_BUTTON_DIMENSIONS[1], x=DELETE_LOCAL_PATHS_BUTTON_X_POSITION, y=DELETE_LOCAL_PATHS_BUTTON_Y_POSITION + DELETE_LOCAL_PATHS_BUTTON_DIMENSIONS[1] + STANDARD_Y_PADDING)

    def set_dropdown(self):
        ## SETTING THE DROPDOWN TO CHOSE FROM THE URLS IN THE TABLE local_paths_table
        self.options = fetch_local_paths_from_local_paths_table()
        try:
            self.option_menu_variable.set(self.options[0])
            return self.options
        except IndexError:
            messagebox.showerror("Error", "There are no Local Paths to delete!")
            self.back()
            return
        
    def update_option_menu(self):
        menu = self.option_menu["menu"]
        menu.delete(0, "end")
        for string in self.options:
            menu.add_command(label=string, 
                             command=lambda value=string: self.option_menu_variable.set(value))

    def back(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        self.app = EditLocalPaths(self.newWindow)

    def delete(self):
        try:
            local_path = self.option_menu_variable.get()
        except ValueError:
            messagebox.showerror("Error", "Please do not leave blank spaces!")
            return

        ## CREATE AN SQL QUERY THAT DELETES THE LOCAL PATH FROM THE TABLE local_paths_table

        conn, cursor = connect_to_sql()
        cursor.execute(f"DELETE FROM local_paths_table WHERE local_path = '{local_path}'")
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Local Path deleted successfully!")
        self.options = self.set_dropdown()
        if self.options:
            self.update_option_menu()


##############################################################################################################
##############################################################################################################
if __name__ == "__main__":
    ## CREATE THE DATABASE AND TABLES IF THEY DONT EXIST
    create_database()
    create_tables()
    root = ThemedTk() ## TKINTER WITH A LOT OF DIFFERENT THEMES
    root.withdraw()
    
    my_gui = MainInterface(root)
    root.mainloop()