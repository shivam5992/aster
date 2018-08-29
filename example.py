from aster.aster import aster

config = {	"COMPETITION" : "spooky-author-identification",
		  	"_TARGET_COL" : "author", 
		  	"_ID_COL" : "id",
		  	"DATASET": "",
		  	# "_TRAIN_FILE" : "",
		  	# "_TEST_FILE" : "",
		  	# "_TAG" : "doc", # doc - text classification, num - binary classification 
			# "_TEXT_COL" :  "text", # - name of the text classification
		  }
ast = aster(config)
ast._prepare()
ast._push()