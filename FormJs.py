lines = open("new.js").readlines()[0].split(";")
indent = 0
formatted = []
for line in lines:
	newline = []
	for char in line:
		newline.append(char)
		if char=='{':
			indent+=1
			newline.append("\n")
			newline.append("\t"*indent)
		if char=="}":
			indent-=1
			newline.append("\n")
			newline.append("\t"*indent)
	formatted.append("\t"*indent+"".join(newline))
open("formated.js","w").writelines(";\n".join(formatted))
