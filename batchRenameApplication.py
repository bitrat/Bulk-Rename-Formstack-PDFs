# Adjust the path where the FormStack pdfs live

import os
import PyPDF2
import itertools
from datetime import datetime

path = r'DRIVE:\<FOLDER WHERE THE PDFS YOU WANT TO RENAME ARE>'

def renameFileToPDFTitle(path, fileName,pdfName):
    fullName = os.path.join(path, fileName)
    # Extract pdf title from pdf file
    newName = pdfName+".pdf"
    newFullName = os.path.join(path, newName)
    os.rename(fullName, newFullName)
    
def extractTextList(self):
    text_list = []
    content = self["/Contents"].getObject()
    if not isinstance(content, ContentStream):
        content = ContentStream(content, self.pdf)

    for operands, operator in content.operations:
        if operator == b_("Tj"):
            _text = operands[0]
            if isinstance(_text, TextStringObject) and len(_text.strip()):
                text_list.append(_text.strip())
        elif operator == b_("T*"):
            pass
        elif operator == b_("'"):
            pass
            _text = operands[0]
            if isinstance(_text, TextStringObject) and len(operands[0]):
                text_list.append(operands[0])
        elif operator == b_('"'):
            _text = operands[2]
            if isinstance(_text, TextStringObject) and len(_text):
                text_list.append(_text)
        elif operator == b_("TJ"):
            for i in operands[0]:
                if isinstance(i, TextStringObject) and len(i):
                    text_list.append(i)
    return text_list

from PyPDF2.pdf import PageObject, u_, ContentStream, b_, TextStringObject
PageObject.extractTextList = extractTextList

def between(text_elements, drop_while, take_while):    
    return list(itertools.takewhile(take_while, itertools.dropwhile(drop_while, text_elements)))[1:]    

for fileName in os.listdir(path):
    # Rename only pdf files
    fullName = os.path.join(path, fileName)
    if (not os.path.isfile(fullName) or fileName[-4:] != '.pdf'):
        continue
    # Extract the PDF Text
    pdfFileObj = open(fullName, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    page0 = pdfReader.getPage(0)
    text_elements = page0.extractTextList()
    #print(text_elements)

    lines = between(text_elements, lambda x: x != 'Form Name:', lambda x: 'Birthdate' not in x)
    #print('\n'.join(lines))

    #Concatenate the new pdf name
    # Name of Form
    print("--------------------")
    nameOfForm = lines[0]
    #print(nameOfForm)
    #print(type(nameOfForm))

    pdfName = nameOfForm

    if "Given Name or Names" in lines:
        indexFNTitle = lines.index("Given Name or Names")
        indexFN = indexFNTitle+1
        personFN = lines[indexFN]
        #print(personFN)
        #print(type(personFN))
        pdfName = pdfName+"_"+personFN
        #print(pdfName)

    if "Family Name" in lines:
        indexLNTitle = lines.index("Family Name")
        indexLN = indexLNTitle+1
        personLN = lines[indexLN]
        #print(personLN)
        #print(type(personLN))
        pdfName = pdfName+" "+personLN
        #print(pdfName)

    if "Submission Time:" in lines:
        indexDateTitle = lines.index("Submission Time:")
        indexDate = indexDateTitle+1
        submissionDate = lines[indexDate]
        #print(lines[indexDate])
        #print(type(lines[indexDate]))
        removePuctuation =  lines[indexDate].replace(',', '')
        #Convert Submission date and time into usable Date format
        timeSubmitted = datetime.strptime(removePuctuation, '%B %d %Y %I:%M %p').time()
        #print(timeSubmitted)
        timeToConcat = timeSubmitted.strftime('%H%M%S')
        dateSubmitted = datetime.strptime(removePuctuation, '%B %d %Y %I:%M %p').date()
        dateToConcat = dateSubmitted.strftime('%Y-%m-%d')
        #print(dateToConcat)
        #print(type(dateToConcat))
        pdfName = pdfName+"_"+timeToConcat+"_"+dateToConcat
        #print(pdfName)
    print(pdfName)
    print("--------------------")
    pdfFileObj.close()

    try:
        renameFileToPDFTitle(path, fileName, pdfName)
    except Exception:
        print("Could not rename file")
        pass