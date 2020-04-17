import sys
import os
from PIL import Image

# garb the path from command prompt
jpg_path = sys.argv[1]
png_path = sys.argv[2]

# if new path does not exist, create new folder
if os.path.exists(png_path) == False:
	os.mkdir(png_path)

for filename in os.listdir(jpg_path):
	img = Image.open(f'{jpg_path}{filename}')
	clean_name = os.path.splitext(filename)[0]
	if not os.path.exists(f'{clean_name}.png'):
		img.save(f'{png_path}{clean_name}.png', 'png')

		
print('All done!!')