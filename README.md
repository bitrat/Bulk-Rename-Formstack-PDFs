# Bulk-Rename-Formstack-PDFs
Bulk rename Formstack Form PDFs based on the PDF data they contain.

When you export a zip file full of Formstack pdfs, which is submitted
form data, they are all named something like:
"Form_Submission_712305837.pdf", meaning, there is no indication of what
the PDF contains.

Renaming each file by hand is too manual, so we will be using the
**python** programming language and the **PyPDF2** library to rename the
files based on the content of each pdf, such as the Name of the Person
who filled the form out and the Date the form was filled out.

# Short List of commands - rename Formstack pdfs

Run **cmd**

\$ **cd** **C:\\Python\\python-venvs\\batchrename**

\$ **C:\\Python\\python-venvs\\batchrename\\Scripts\\activate.bat**

Export Formstack pdf zip file

Extract zip

Run the python script for the Form, in this case an Application form

\$ **python batchRenameApplication.py**

\$ **deactivate**

# Appendix A -- Setup

## Install Python

Download and install the python language for your operating system if
you don't already have it installed.

[Download Python \| Python.org](https://www.python.org/downloads/)

On Windows -- run the setup file - Tick \"Add Python to PATH\"

Select \"Custom\" - Untick \"tcl/thinker IDE\" (we will be using VSCode)

Create a folder for Python on your PC (if not wanting to use the default
Windows C:\\Users\\\<User\>\\Apps folder) -- I chose to create
**C:\\Python** you might want to add the version of Python to the folder
name, for example **C:\\Python3_9**

Open a command prompt and navigate into the Python directory (on
Windows):

Windows Key + S -- bring up the search field

**cmd**

Right-click "Command Prompt" -- Run as administrator

\$ **cd C:\\Python** (or whatever folder you setup)

## Setup the Virtual environment

Use the **venv** module (virtual env that comes with Python 3 by
default)

Source: <https://realpython.com/python-virtual-environments-a-primer/>

\$ **mkdir python-venvs && cd python-venvs**

Create a new virtual environment inside the directory:

\$ **python -m venv batchrename**

\$ **cd batchrename**

Activate the environment you created -- I used full path

\$ **C:\\Python\\python-venvs\\batchrename\\Scripts\\activate.bat**

## Install python modules and dependencies

We will use the **PyPDF2** module for this project.

### Update the package manager pip

\$ **python -m pip install -U pip**

### Install PyPDF2

\$ **pip install PyPDF2**

## Create the Batch Rename Python program

First, we want to find out what Info we can get out of the Formstack
pdfs, then we want to create a script that loops through a directory and
renames each pdf with the info from inside the pdf.

Adapted script from source:
<https://stackoverflow.com/questions/50116318/how-extract-extract-specific-text-from-pdf-file-python>

Create a **renameBatchApplication.py** python script file -- it will :

-   look for pdf files in the directory you specified

-   extract the "Given name or Names" and "Family Name" if those exist

-   Append the FormSubmission Time and Date

-   Rename the pdf file and loop to the next pdf file in the folder

## Formstack Advanced PDF settings

Export a zip file containing each pdf separately -- you need to set this
up in **Settings - Advanced PDF** -- turn on Exporting Multiple
Submissions "**One Submission Per PDF**"

We only want to extract Data from the first page of the pdf --make sure
you have multi-Page breaks unselected

## Export the Formstack submission PDFs

1.  In the Submissions section -- select all the pdfs you want to bulk export. 

2.  Then use the Export button to download a zip file containing the Submission pdfs.

3.  Extract the zip file -- you can extract in the **Downloads** folder
    -- remember to reference the Downloards folder path in your batchRenameApplication.py script

## Run your Python programs to rename the pdfs

Within the virtual environment, simply run:

## Deactivate the Virtual Environment

Once you are finished, to "exit" your virtual environment, you
deactivate it.

\$ **deactivate**

