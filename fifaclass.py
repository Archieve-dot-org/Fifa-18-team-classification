import re,os

with open('Fifa 18.txt','r') as f:
	output = f.read()
	group_name = ( (  (re.sub('".*?"', '', output)).replace(" ", "")  ).replace("=","") ).splitlines()
	del group_name[-1]

group_coun = re.findall(r'"(.*?)"', output.lower())
dictionary = dict(zip(group_name, group_coun))

for directory in dictionary:
	if not os.path.exists(directory):
		os.makedirs(directory)
