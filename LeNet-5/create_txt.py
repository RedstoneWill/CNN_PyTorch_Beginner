# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 14:24:12 2021

@author: Administrator
"""

# coding:utf-8
import os
'''
    为数据集生成对应的txt文件
'''

#path = 'F:/Code/Object Detection/data/LEDNUM/'
#src = os.path.join(os.path.abspath(path), item)

train_txt_path = os.path.join("data", "LEDNUM", "train.txt")
train_dir = os.path.join("data", "LEDNUM", "train_data")

valid_txt_path = os.path.join("data", "LEDNUM", "test.txt")
valid_dir = os.path.join("data", "LEDNUM", "test_data")


def gen_txt(txt_path, img_dir):
    f = open(txt_path, 'w')
    
    for root, s_dirs, _ in os.walk(img_dir, topdown=True):  # 获取 train文件下各文件夹名称
        for sub_dir in s_dirs:
            i_dir = os.path.join(root, sub_dir)             # 获取各类的文件夹 绝对路径
            img_list = os.listdir(i_dir)                    # 获取类别文件夹下所有png图片的路径
            for i in range(len(img_list)):
                if not img_list[i].endswith('jpg'):         # 若不是png文件，跳过
                    continue
                label = img_list[i].split('_')[0]
                img_path = os.path.join(i_dir, img_list[i])
                line = img_path + ' ' + label + '\n'
                f.write(line)
    f.close()


if __name__ == '__main__':
    gen_txt(train_txt_path, train_dir)
    gen_txt(valid_txt_path, valid_dir)