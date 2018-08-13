import nbformat 
import os

nb = nbformat.v4.new_notebook()
nb['cells'] = []

for x in sorted(os.listdir("Meta/")):
	if x.startswith("."):
		continue

	txt = ""
	cod = ""
	content = open("Meta/"+x).read()
	for j, line in enumerate(content.split("\n")):

		if line == "<text>":
			txt = ""
		if line == "</text>":
			nb['cells'].append(nbformat.v4.new_markdown_cell(txt.replace("<text>","").replace("</text>","").strip()))
			txt = ""

		if line == "<code>":
			cod = ""
		if line == "</code>":
			nb['cells'].append(nbformat.v4.new_code_cell(cod.replace("<code>","").replace("</code>","").strip()))
			cod = ""

		txt += "\n"
		txt += line 
		cod += "\n"
		cod += line 

nbformat.write(nb, 'new.ipynb')

