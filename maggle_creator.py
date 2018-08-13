"""

Maggle : a kaggle bot to create baseline models for different category of kaggle competitions or datasets

__author__ == "shivam bansal"
__email__ == "shivam5992@gmail.com"

"""


""" make necessary imports """

import nbformat 
import os

class maggle():
	def __init__(self, config):
		self.nb = nbformat.v4.new_notebook()
		self.nb['cells'] = []
		self.config = config
		self.meta_path = "Meta/"

	def _prepare_meta(self, filename):
		content = open(self.meta_path+filename).read()
		for key,value in self.config.items():
			if key.startswith("_"):
				content = content.replace("<"+key+">", value)
		return content

	def _prepare(self):
		for x in sorted(os.listdir(self.meta_path)):
			if x.startswith("."):
				continue


			txt = ""
			cod = ""
			content = self._prepare_meta(x)
			for j, line in enumerate(content.split("\n")):

				if line.startswith("<text>"):
					txt = ""
				if line.startswith("<code>"):
					cod = ""

				if line.startswith("</text>"):
					valid = True
					if line.startswith("</text><num>") and self.config["_TAG"] != "num":
						valid = False
					if line.startswith("</text><doc>") and self.config["_TAG"] != "doc":
						valid = False

					if valid:
						txt = txt.replace("<text>","").replace("</text>","").strip()
						txt = txt.replace("<num>","").replace("</doc>","").strip()
						self.nb['cells'].append(nbformat.v4.new_markdown_cell(txt))
						txt = ""

				if line.startswith("</code>"):
					valid = True
					if line.startswith("</code><num>") and self.config["_TAG"] != "num":
						valid = False
					if line.startswith("</code><doc>") and self.config["_TAG"] != "doc":
						valid = False

					if valid:
						cod = cod.replace("<code>","").replace("</code>","").strip()
						cod = cod.replace("<doc>","").replace("</doc>","").strip()
						self.nb['cells'].append(nbformat.v4.new_code_cell(cod))
						cod = ""

				txt += "\n"
				cod += "\n"

				txt += line 
				cod += line 

		nbformat.write(self.nb, "baseline_kernel.ipynb")


config = {"_TAG" : "num", "_TRAIN_FILE" : "train", "_TEST_FILE" : "test",
		  "_TARGET_COL" : "Survived", "_TEXT_COL" :  "text", "_ID_COL" : "PassengerId"}
mg = maggle(config)
mg._prepare()






