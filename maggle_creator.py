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

	def _prepare_meta(self):
		pass

	def _prepare(self):
		for x in sorted(os.listdir(self.meta_path)):
			if x.startswith("."):
				continue

			txt = ""
			cod = ""
			content = open(self.meta_path+x).read()
			for j, line in enumerate(content.split("\n")):

				if line == "<text>":
					txt = ""
				if line == "<code>":
					cod = ""

				if line == "</text>":
					txt = txt.replace("<text>","").replace("</text>","").strip()
					self.nb['cells'].append(nbformat.v4.new_markdown_cell(txt))
					txt = ""

				if line == "</code>":
					cod = cod.replace("<code>","").replace("</code>","").strip()
					self.nb['cells'].append(nbformat.v4.new_code_cell(cod))
					cod = ""

				txt += "\n"
				cod += "\n"

				txt += line 
				cod += line 

		nbformat.write(self.nb, "baseline_kernel.ipynb")