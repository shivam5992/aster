"""

Maggle : a kaggle bot to create baseline models for different category of kaggle competitions or datasets

__author__ == "shivam bansal"
__email__ == "shivam5992@gmail.com"

"""


""" make necessary imports """

import nbformat 


class maggle():
	def __init__(self, config):

		# initialize important variables
		self.nb = nbformat.v4.new_notebook()
		self.nb['cells'] = []
		self.config = config

	def _prepare_environment(self):

		## add the intro text cell
		text = """	## Step 1: Prepare Environment
					Lets load the required libraries to be used"""
		text = text.replace("\t","")
		self.nb['cells'].append(nbformat.v4.new_markdown_cell(text))

		## add the code cell
		code = """	import pandas as pd
					import os"""
		code = code.replace("\t","")
		self.nb['cells'].append(nbformat.v4.new_code_cell(code))

	def _dataset_preparation(self):

		## add the intro text cell
		text = """	## Step 2: Dataset Preparation"""
		text = text.replace("\t","")
		self.nb['cells'].append(nbformat.v4.new_markdown_cell(text))

		## add the code cell
		code = """	train_df = pd.read_csv('../input/train.csv')
					test_df = pd.read_csv("../input/test.csv")
					target = "Survived"
					test_id = "PassengerId" """
		code = code.replace("\t","")		
		self.nb['cells'].append(nbformat.v4.new_code_cell(code))


	def _baseline_model(self):
		pass

	def _ensembling(self):
		pass

	def _generate_notebook(self):
		self._prepare_environment()
		self._dataset_preparation()
		nbformat.write(self.nb, 'test1.ipynb')

if __name__ == "__main__":
	config = { "filename" : "test.ipynb" }
	mg = maggle(config)
	mg._generate_notebook()


