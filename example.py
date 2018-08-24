from aster.aster import aster

config = {	"COMPETITION" : "spooky-author-identification",
		  	"DATASET": "",
		  	"_TARGET_COL" : "author", 
		  	"_ID_COL" : "id",

		  	## only for text classification
		  	"_TAG" : "doc", # doc - text classification, num - binary classification 
			"_TEXT_COL" :  "", # - name of the text classification
		  }
ast = aster(config)
ast._prepare()
# ast._push()

### readme -- 29 onwards 
### regression 
### image classifiication