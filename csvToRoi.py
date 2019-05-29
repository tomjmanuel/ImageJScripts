#libs for csv reading
import csv
import os
#libs nec for ROI handling
from ij.plugin.frame import RoiManager
from ij.gui import OvalRoi
RoiManager()
b = RoiManager.getInstance()
#x = OvalRoi(322, 144, 108, 104)
#b.addRoi(x)
print(os.getcwd())

fn = 'C:/Users/tomjm/Desktop/test.csv'

with open(fn) as csvfile:
	readCSV = csv.reader(csvfile,delimiter=',')
	for row in readCSV:
			if row[3].isdigit():
				print(row[3])
				x = OvalRoi(int(row[3]), int(row[4]), int(row[5]), int(row[6]))
				b.addRoi(x)