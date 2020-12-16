import os, sys

if len(sys.argv) < 2:
	print('Usage: combine_to_pdf.py <output_filename> -d <dpi>')
	print('dpi argument is optional, specifies output dpi of pdf. Defaults to 30. Use 0 for no compression')
	quit()
elif len(sys.argv) == 2:
	dpi = 30
elif len(sys.argv) == 4:
	if sys.argv[2] != '-d':
		print(f'Unknown argument: {sys.argv[2]}')
		quit()
	try:
		dpi = int(sys.argv[3])
	except ValueError:
		print('-d argument must be an integer')
		quit()
 
output = sys.argv[1]

files = []
i = 1
while True:
	if os.path.isfile(f'{i}.JPG'):
		files.append(f'{i}.JPG')
	elif os.path.isfile(f'{i}.jpeg'):
		files.append(f'{i}.jpeg')
	elif os.path.isfile(f'{i}.png'):
		files.append(f'{i}.png')
	else:
		break
	i += 1

for f in files:
	if 'png' not in f.lower():
		os.system(f"jpegoptim {f}")
	else:
		print(f'Skipping {f}, not jpg')

os.system(f"convert {' '.join(files)} output.pdf")
if dpi != 0:
	os.system(f"./shrinkpdf.sh output.pdf {output} {dpi}")
	d = (os.path.getsize('output.pdf')-os.path.getsize(output))/os.path.getsize('output.pdf')
	print(f'pdf compressed by {round(d*100, 2)}%')
else:
	os.system(f'cp output.pdf {output}')
print('Cleaning up...') 
os.system('rm output.pdf')
