import re

f_input = open("/home/psycho/Desktop/igg.html", "r")
str = f_input.read()
pattern = "<li><a href=\"(.*)\" target=\"_blank\" rel=\"noopener noreferrer\">"

for m in re.finditer(pattern, str):
	print(m.group(1))
