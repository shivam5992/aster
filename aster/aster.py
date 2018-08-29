"""

Aster : a kaggle bot to create baseline kernels for different category of kaggle competitions or datasets

__author__ == "shivam bansal"
__email__ == "shivam5992@gmail.com"
__kaggle__ == "https://www.kaggle.com/shivamb"

"""

import subprocess
import nbformat
import json, os
import random

class aster():

	## initialize the notebook parameters
	def __init__(self, config):
		self.nb = nbformat.v4.new_notebook()
		self.nb['cells'] = []
		self.config = config
		self.content_meta = "aster/templates/"
		self.hash = random.getrandbits(128)
		self.kernel_meta = {"id": "shivamb/"+str(self.hash), "title" : "Bot Generated Baseline Kernel :) (id: "+str(self.hash)[5:10] + ")", 
		"kernel_sources": [], "code_file": "baseline_kernel.ipynb", "language": "python", 
		"kernel_type": "notebook", "is_private": "true", "enable_gpu": "false", "enable_internet": "false", 
		"dataset_sources" : [], "competition_sources" : []}

		## setup default values for configs
		if self.config["DATASET"] != "":
			self.kernel_meta["dataset_sources"] = [self.config["DATASET"]]
		if self.config["COMPETITION"] != "":
			self.kernel_meta["competition_sources"] = [self.config["COMPETITION"]]
		if "_TRAIN_FILE" not in self.config:
			self.config["_TRAIN_FILE"] = "train"
		if "_TEST_FILE" not in self.config:
			self.config["_TEST_FILE"] = "test"
		if "_TAG" not in self.config:
			self.config["_TAG"] = "num"
		if "_TEXT_COL" not in self.config:
			self.config["_TEXT_COL"] = ""

		## create the folder for the kernel
		self.kernel_folder = "BaselineKernel"
		if not os.path.isdir(self.kernel_folder):
			os.makedirs(self.kernel_folder)

		## write the kernel-metadata.json
		fout = open(self.kernel_folder + "/kernel-metadata.json", "w")
		fout.write(json.dumps(self.kernel_meta))

	## function to prepare and modify the base content
	def _prepare_meta(self, filename):
		content = open(self.content_meta+filename).read()
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

	## function to push the generated kernel on kaggle
	def _push(self):
		command = "kaggle kernels push -p "+self.kernel_folder 
		subprocess.call(command.split())
		print ("Pushed")
		return None

	## function to generate a new kernel
	def _prepare(self):
		for x in sorted(os.listdir(self.content_meta)):
			if x.startswith("."):
				continue

			txt, cod = "", ""
			content = self._prepare_meta(x)
			for j, line in enumerate(content.split("\n")):
				## parse and append markdown cells
				if line.startswith("<text>"):
					txt = ""
				if line.startswith("</text>") and self.is_valid_cell(line, "</text>"):
					txt = self._cleanup(txt)
					self.nb['cells'].append(nbformat.v4.new_markdown_cell(txt))
					txt = ""
				txt += "\n"
				txt += line 
				## parse and append code cells
				if line.startswith("<code>"):
					cod = ""
				if line.startswith("</code>") and self.is_valid_cell(line, "</code>"):
					cod = self._cleanup(cod)
					self.nb['cells'].append(nbformat.v4.new_code_cell(cod))
					cod = ""
				cod += "\n"
				cod += line 

		nbformat.write(self.nb, self.kernel_folder + "/baseline_kernel.ipynb")
		print ("Generated")
		return None 