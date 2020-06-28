import os

filePath = './text_gt/'
list_jpg = os.listdir(filePath)


if __name__ == '__main__':
    '''
    => 用于完成test.txt, 要在此文件目录下事先创建test.txt文件
    与后面完成train.txt分开单独使用时, 直接注释掉另一个
    '''
    # /=== ===> test.txt 写入pic_name & label <=== ===\
    name = []
    with open('test_gt.txt', 'w') as f:  # train.txt或者test.txt
        for i in list_jpg:
            name.append(i.split(".")[0])
            f.writelines(i.split(".")[0] + '\n')
    for i in range(len(name)):
        print(name[0])

    # \=== ===> test.txt 写入pic_name & label <=== ===/