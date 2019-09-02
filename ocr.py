# export GOOGLE_APPLICATION_CREDENTIALS=kyourcredentials.json
import io
import os
import sys
import re

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client


def parse_text():
	original = open("Read.txt","r")
	contents = original.readlines()
	original.close()
	file = open("OCR.txt","w")

	for line in contents:

		if ("publicclass" in line):
			line = line.replace("publicclass", "public class ")
		if("publicstaticvoidmain" in line):
			line = line.replace("publicstaticvoidmain", "public static void main")
		if("psvm" in line):
			line = line.replace("psvm", "public static void main(String[] args)")
		if("psum" in line):
			line = line.replace("psum", "public static void main(String[] args)")
		if("sout" in line):
			line = line.replace("sout", "System.out.println")
		if("Sout" in line):
			line = line.replace("Sout", "System.out.println")
		if("BEOL" in line):
			line = line.replace("BEOL","}\n")
		if("3EOL" in line):
			line = line.replace("3EOL","}\n")
		if("JEOL" in line):
			line = line.replace("JEOL","}\n")
		if("]EOL" in line):
			line = line.replace("]EOL","}\n")

		if("int" in line):
			line = line.replace("int","int ")
		if("double" in line):
			line = line.replace("double","double ")
		if("float" in line):
			line = line.replace("float", "float ")
		if("String" in line):
			line = line.replace("String", "String ")
		if("char" in line):
			line = line.replace("char", "char ")
		if("print ln" in line):
			line = line.replace("print ln","println")

		file.write(line+"\n")
	file.close()


def detect_document(path):


    """Detects document features in an image."""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.document_text_detection(image=image)

    for page in response.full_text_annotation.pages:
        for block in page.blocks:
            print('\nBlock confidence: {}\n'.format(block.confidence))

            for paragraph in block.paragraphs:
                print('Paragraph confidence: {}'.format(
                    paragraph.confidence))

                for word in paragraph.words:
                    word_text = ''.join([
                        symbol.text for symbol in word.symbols
                    ])
                    print('Word text: {} (confidence: {})'.format(
                        word_text, word.confidence))
                    arrValues.append(word_text)

                    for symbol in word.symbols:
                        print('\tSymbol: {} (confidence: {})'.format(
                            symbol.text, symbol.confidence))
# When everything done, release the capture

arrValues = []
myPath = sys.argv[1]
myNewPath = os.path.dirname(os.path.realpath(__file__))
myNewPath = myNewPath+'/'+myPath

detect_document(myNewPath)
file = open("Read.txt","w")

end_of_line = "EOL"
flagged = False
sentence = ""
quoteString = ""

for item in arrValues:
	if(item == "Eol"):
		item = "EOL"
	
	if (item=="\""):
		if (flagged):
			flagged = False
			quoteString+=str(item)
			sentence+=quoteString
			quoteString=""
		else:
			flagged = True
			quoteString+="\""

	elif (flagged):
		quoteString+=str(item)+" "

	elif (item==end_of_line):
		sentence+=quoteString
		quoteString=""
		file.write(sentence+"\n")
		sentence = ""

	else:
		sentence+=str(item)

file.write(sentence)
file.close()


parse_text()





# for item in arrValues:
# 	if (item==end_of_line):
# 		file.write(sentence+"\n")
# 		sentence = ""
# 	else:
# 		sentence+=str(item)
# 		sentence+=" "
# file.write(sentence)
# file.close()
