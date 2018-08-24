from aster.aster import aster

config = {	# "COMPETITION" : "",
		  	# "DATASET": "",
		  	"_TARGET_COL" : "Survived", 
		  	"_ID_COL" : "PassengerId",
		  	# "_TAG" : "doc", # doc - text classification, num - binary classification 
			# "_TEXT_COL" :  "", # - name of the text classification
		  }
ast = aster(config)
ast._prepare()
# ast._push()

# Classification Problems - Numerical Data
## 1. titanic : ok | train, test, PassengerId, Survived
## 2. diabetes : ok | diabetes, outcome, ""
## 3. mushrooms : mushrooms, class, ""
## 4. iris : ok | Iris, Species, Id
# Classification Problems - Text Data
## 1. author : train 2, test 2, author, id 
## 2. author : ok  <<< Next Step
### standardization <<< Next Step
### Commit Aster <<< Next Step

### Image Classifiication
### Regression Problems
### readme -- 29 onwards 