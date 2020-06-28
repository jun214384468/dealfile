import os

def RenameFile(path):
    # list_jpg = os.listdir(path)
    # for i in list_jpg:

    for roots, dirs, files in os.walk(path):
        n = 0
        for file in files:
            oldname = os.path.join(roots, file)
            newname = roots+"gt_img_"+file[4:]
            os.rename(oldname, newname)
            n += 1

path = './train_txt/'
RenameFile(path)