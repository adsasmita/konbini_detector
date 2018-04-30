#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import shutil

# copy only pngs that have corresponding xml
def get_xml(src_dir="png/", dst_dir="png_f/"):
    """
    find PNGs in src_dir that are labeled with XMLS,
    then copy the files to dst_dir
    
    Args:
        src_dir (str): path to files
        dst_dir (str): path to destination directory
    """
    cdict = {}
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
        print(f"created directory: {dst_dir}")
    
    for keyword in os.listdir(src_dir):
        print(keyword)
        path = os.path.join(src_dir, keyword)
        count = 0
        for f in os.listdir(path):
            if os.path.splitext(f)[1] == '.xml':
                count += 1
                for ext in ['.xml','.png']:
                    src_path = os.path.join(path,os.path.splitext(f)[0]+ext)
                    shutil.copy2(src_path,dst_dir)

        cdict[keyword] = count
    print("done")
    for k,v in dict1.items():
        print(f"xml count for {k}:{v}")

if __name__ == "__main__":
    get_xml(src_dir="png/", dst_dir="png_f/")

