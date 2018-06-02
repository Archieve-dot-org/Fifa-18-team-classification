import re,os,fnmatch,glob,shutil




with open('Fifa 18.txt','r') as f:
	output = f.read()
	group_name = ( (  (re.sub('".*?"', '', output)).replace(" ", "")  ).replace("=","") ).splitlines()
	del group_name[-1]

group_coun = re.findall(r'"(.*?)"', output.lower())
dictionary = dict(zip(group_name, group_coun))

def folder_create(dirs):
	if os.path.exists(dirs):
		shutil.rmtree(dirs)
	os.makedirs(dirs)

folder_create('result')
for sc, value in dictionary.iteritems():
	folder_create('result/'+sc)

	for scd in value.split(','):
		for file in glob.glob('svg/*'+scd+'*'):
			print file
			shutil.copy(file, 'result/'+sc)