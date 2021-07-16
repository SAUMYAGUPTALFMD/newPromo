print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('')
print("Initializing Dependencies...")

import PyPDF2
import colorama
import glob
import os
colorama.init()

list_of_files = glob.glob('C:\\Users\\anand59\\Desktop\\Journals\\*.pdf') # * means all if need specific format then *.csv
latest_file = max(list_of_files, key=os.path.getctime)
print(colorama.Fore.LIGHTYELLOW_EX + 'Path of journal to be used: ' + latest_file)

pdfFileObject = open(str(latest_file), 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
count = pdfReader.numPages
company = open("C:\\Users\\anand59\\Desktop\\Promo\\Journal\\company.txt","a+")
lis =[]

print(colorama.Fore.LIGHTGREEN_EX + 'Reading PDF (may take upto 1 min) \n')

for i in range(count):
	page = pdfReader.getPage(i)
	content = page.extractText()
	l=content.split('\n')
	for i in l:
		# print(i)
		if ("trading" in i) or ("PVT" in i):
			i=i.replace("trading as ;", "") 
			# i=i.replace("trading as", "") 
			# print(i + '\n')
			lis.append(i+'\n')
			# lis = list(set(lis)
			# company.writelines(l)
# lis = list(set(lis)

print(colorama.Fore.LIGHTRED_EX + 'Removing Duplicates... \n')
res = []
[res.append(x) for x in lis if x not in res]
company.writelines(res)

print(colorama.Fore.YELLOW + 'Names Written in ', end='')
print(colorama.Fore.WHITE + 'company.txt \n')

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(colorama.Fore.RED + 'Completed Names: \n')

for i in res:
	print(colorama.Fore.LIGHTBLUE_EX + i)	

print(colorama.Fore.LIGHTGREEN_EX + 'Please manually remove the bad or incorrect company names from company.txt \n')

print(colorama.Fore.RED+'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

		# 	if '' and 'INCLUDED' and 'Goods' and 'CLASS' and 'INCLUDED' and 'EGGS' not in i:
		# 		file1.writelines(i)
		# 		print(i + '\n')

		# elif ("PVT" in i) or ("PRIVATE" in i) or ("INC" in i) or ("M/S" in i) or ("Healthcare" in i) or ("Remedies" in i) or ("Lifecare" in i) or ("Enterprises" in i) or ("Lifesciences" in i):
		# 	print(i)
		# 	file1.writelines(i + '\n')
		# 	if ',' and 'Goods' and 'CLASS' and 'INCLUDED' and 'EGGS' not in i:
		# 		file1.writelines(i)
		# 		print(i + '\n')
		#  or ("Remedies" in i)