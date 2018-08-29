from aster.aster import aster

config = {	"COMPETITION" : "titanic",
		  	"_TARGET_COL" : "Survived", 
		  	"_ID_COL" : "PassengerId",
		 #  	"DATASET": "",
		 #  	"_TAG" : "doc", # doc - text classification, num - binary classification 
			# "_TEXT_COL" :  "", # - name of the text classification
		  }
ast = aster(config)
ast._prepare()
ast._push()