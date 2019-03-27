# import os
#
# for root, dirs, files in os.walk("."):
#     for filename in files:
#         if "raw" in filename:
#             print(filename)
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir("C:\\OUTPUT") if isfile(join("C:\\OUTPUT", f))]
for i in onlyfiles:
    if "raw" in i:
        print(i)