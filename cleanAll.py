import os
from ImageEnhance import clean

for filename in os.listdir("Project/test/"):
	clean(filename)
