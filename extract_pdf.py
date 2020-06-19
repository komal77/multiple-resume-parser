# python -m spacy download en_core_web_sm

import spacy
import json
from pyresparser import ResumeParser
import glob
import os
import sys

docfile , docxfile = glob.glob('*.doc'), glob.glob('*.docx')
for doc in docfile+docxfile:
    command = "lowriter --convert-to pdf "+doc
    os.system(command)

filenames = glob.glob('*.pdf')
print(filenames)

for f in filenames:
# pdffile = convert('resume/docresume1.docx')
    data = ResumeParser(f).get_extracted_data()
    print(json.dumps(data))