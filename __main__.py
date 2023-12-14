import fitz  # PyMuPDF
import os
import glob

class Tag:
	def __init__(self, name, cropLeft, cropTop, cropRight, cropBottom):
		self.name = name
		self.cropLeft = cropLeft
		self.cropTop = cropTop
		self.cropRight = cropRight
		self.cropBottom = cropBottom

def get_labels_dict():
	return {
		'correos': Tag("correos", 0, 0, 425, 283),
		'correos_int' : Tag("correos_int", 0, 0, 283, 411),
		'gls': Tag("gls", 0, 0, 250, 300),
		'inpost': Tag("inpost", 35, 20, 570, 350),
		'seur': Tag("seur", 0, 0, 200, 210),
		'seur_vinted': Tag("seur_vinted", 50, 20, 220, 250),
		'ups': Tag("ups", 10, 10, 325, 450)
	}

def get_pdf_files(folder_path):
	pdf_files = glob.glob(os.path.join('./labels/' + folder_path, '*.pdf'))
	return pdf_files

def crop_pdf(input_path, tag):
	
	global count
	count = 0
	for pdf_doc in get_pdf_files(folder_name):
		# Open the PDF file
		pdf_document = fitz.open(pdf_doc.replace('\\', '/'))
		# Get the page
		page = pdf_document[0]
		print(page.cropbox)

		page.set_cropbox(fitz.Rect(tag.cropTop, tag.cropLeft, tag.cropRight, tag.cropBottom))

		count = count + 1
		pdf_document.save('./resultado/' + folder_name + str(count) + '.pdf')
		pdf_document.close()
		print(pdf_doc + str(count))

labels_dict = get_labels_dict()
# Print the names of the subfolders
for folder_name in [f.name for f in os.scandir('./labels') if f.is_dir()]:
	crop_pdf(folder_name, labels_dict[folder_name])