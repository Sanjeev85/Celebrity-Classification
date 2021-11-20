import os


'''
    Make absolute path to image directory
'''


actual_path = "C:\\Users\\Sanjeev choubey\\Desktop\\CelebrityClassification\\modiji"
# path -> object to actual directory
path = os.chdir(actual_path)

cnt = 0
for file in os.listdir(path):
    newfile_name = "messi{}.jpg".format(cnt)
    os.rename(file, newfile_name)
    cnt += 1
