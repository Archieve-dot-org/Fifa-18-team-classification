import re,os,fnmatch,glob,shutil




with open('Fifa 18.txt','r') as f:
	output = f.read()
	group_name = ( (  (re.sub('".*?"', '', output)).replace(" ", "")  ).replace("=","") ).splitlines()
	del group_name[-1]

group_coun = re.findall(r'"(.*?)"', output.lower())
dictionary = dict(zip(group_name, group_coun))

for sc, value in dictionary.iteritems():
	#print dictionary[directory]
	
	if os.path.exists(sc):
		shutil.rmtree(sc)
		
	os.makedirs(sc)	


	for scd in value.split(','):
		for file in glob.glob('svg/*'+scd+'*'):
			print file
			shutil.copy(file, sc)