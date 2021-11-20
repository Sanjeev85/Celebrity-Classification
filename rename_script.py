import os


'''
    Make absolute path to image directory
'''


actual_path = 'Enter path here'
# path -> object to actual directory
path = os.chdir(actual_path)

cnt = 1
for file in os.listdir(path):
    newfile_name = "download{}.jpg".format(cnt)
    os.rename(file, newfile_name)
    cnt += 1
