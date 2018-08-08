"""

Maggle : a kaggle bot to create baseline models for different category of kaggle competitions or datasets

__author__ == "shivam bansal"
__email__ == "shivam5992@gmail.com"

"""


""" make necessary imports """

import nbformat 

from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier


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
		code = """	## read dataset
					train_df = pd.read_csv('../input/train.csv')
					test_df = pd.read_csv("../input/test.csv")
					
					## get predictor and target variables
					_target = "Survived"
					_id = "PassengerId" 
					Y = train_df[_target]
					test_id = test_df[_id]

					## drop the target and id columns
					train_df = train_df.drop([_target, _id], axis=1)
					test_df = test_df.drop([_id], axis=1)

					## create the empty submission dataframe
					sub_df = pd.DataFrame({_id: test_id, _target : "??"})"""

		code = code.replace("\t","")		
		self.nb['cells'].append(nbformat.v4.new_code_cell(code))

		## add the intro text cell
		text = """	Lets look at the dataset snapshot and summary"""
		text = text.replace("\t","")
		self.nb['cells'].append(nbformat.v4.new_markdown_cell(text))

		## lets look at the data snapshot
		code = """	## snapshot of train and test
					train_df.head()"""
		code = code.replace("\t","")		
		self.nb['cells'].append(nbformat.v4.new_code_cell(code))

		## lets look at the data snapshot
		code = """	## snapshot of train and test
					train_df.describe()"""
		code = code.replace("\t","")		
		self.nb['cells'].append(nbformat.v4.new_code_cell(code))


	def _baseline_model(self):
		## add the intro text cell
		text = """	## Step 3 : Create baseline model
					### Step 3.1 : Logistic Regression"""
		text = text.replace("\t","")
		self.nb['cells'].append(nbformat.v4.new_markdown_cell(text))

		## lets look at the data snapshot
		code = """	model = LogisticRegression()
					model.fit(train_df, Y)
					pred = model.predict(test_df)"""
		code = code.replace("\t","")		
		self.nb['cells'].append(nbformat.v4.new_code_cell(code))


		## add the intro text cell
		text = """	### Step 3.2 : Random Forest Classifier"""
		text = text.replace("\t","")
		self.nb['cells'].append(nbformat.v4.new_markdown_cell(text))

		## lets look at the data snapshot
		code = """	model = RandomForestClassifier()
					model.fit(train_df, Y)
					pred = model.predict(test_df)"""
		code = code.replace("\t","")		
		self.nb['cells'].append(nbformat.v4.new_code_cell(code))


	def _ensembling(self):
		pass

	def _submission(self):
		# self.submission_doc[_target] = pred
		code = """	sub = pd.DataFrame()
					sub.to_csv("baseline_submission.csv", index=False)"""
		code = code.replace("\t","")		
		self.nb['cells'].append(nbformat.v4.new_code_cell(code))


	def _generate_notebook(self):
		self._prepare_environment()
		self._dataset_preparation()
		self._baseline_model()
		self._submission()
		nbformat.write(self.nb, 'test1.ipynb')

if __name__ == "__main__":
	config = { "filename" : "test.ipynb" }
	mg = maggle(config)
	mg._generate_notebook()


