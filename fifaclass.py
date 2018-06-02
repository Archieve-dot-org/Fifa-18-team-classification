import re
with open('Fifa 18.txt','r') as f:
	output = f.read()
	group_name = ( (  (re.sub('".*?"', '', output)).replace(" ", "")  ).replace("=","") ).splitlines()
	del group_name[-1]

group_coun = re.findall(r'"(.*?)"', output)
dictionary = dict(zip(group_name, group_coun))
print dictionary
	