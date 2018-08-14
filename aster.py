"""

Maggle : a kaggle bot to create baseline models for different category of kaggle competitions or datasets

__author__ == "shivam bansal"
__email__ == "shivam5992@gmail.com"

"""


""" make necessary imports """
import nbformat 
import os

class maggle():

	## initialize the notebook parameters
	def __init__(self, config):
		self.nb = nbformat.v4.new_notebook()
		self.nb['cells'] = []
		self.config = config
		self.meta_path = "Meta/"

	## function to prepare and modify the base content
	def _prepare_meta(self, filename):
		content = open(self.meta_path+filename).read()
		for key,value in self.config.items():
			if key.startswith("_"):
				content = content.replace("<"+key+">", value)
		return content

	## function to cleanup the content of the cell
	def _cleanup(self, string):
		string = string.replace("<text>","").replace("</text>","")
		string = string.replace("<code>","").replace("</code>","")
		string = string.replace("<num>","").replace("</doc>","")
		return string.strip()

	## function to check if a given cell is valid with respect to the config
	def is_valid_cell(self, line, flag):
		valid = True
		if line.startswith(flag+"<num>") and self.config["_TAG"] != "num":
			valid = False
		if line.startswith(flag+"<doc>") and self.config["_TAG"] != "doc":
			valid = False
		return valid

	## function to generate a new kernel
	def _prepare(self):
		for x in sorted(os.listdir(self.meta_path)):
			if x.startswith("."):
				continue

			txt = ""
			cod = ""
			content = self._prepare_meta(x)
			for j, line in enumerate(content.split("\n")):
				
				## add markdown cells
				if line.startswith("<text>"):
					txt = ""
				if line.startswith("</text>") and self.is_valid_cell(line, "</text>"):
					txt = self._cleanup(txt)
					self.nb['cells'].append(nbformat.v4.new_markdown_cell(txt))
					txt = ""
				txt += "\n"
				txt += line 

				## add code cells
				if line.startswith("<code>"):
					cod = ""
				if line.startswith("</code>") and self.is_valid_cell(line, "</code>"):
					cod = self._cleanup(cod)
					self.nb['cells'].append(nbformat.v4.new_code_cell(cod))
					cod = ""
				cod += "\n"
				cod += line 

		nbformat.write(self.nb, "baseline_kernel.ipynb")


config = {	"_TAG" : "doc", 
			"_TRAIN_FILE" : "train 2", 
			"_TEST_FILE" : "test 2",
		  	"_TARGET_COL" : "author", 
		  	"_TEXT_COL" :  "text", 
		  	"_ID_COL" : "id"}
mg = maggle(config)
mg._prepare()


## todo - kernels api integration
## create readme



