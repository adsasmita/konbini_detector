#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Sample Usage:
from project root:
`python get_png_xml.py`
"""

import os
import shutil

# copy only pngs that have corresponding xml
def get_xml(src_dir="data/all_img", img_dst_dir="data/img", xml_dst_dir="data/xml"):
    """
    find PNGs in src_dir that are labeled with XML files,
    then copy the PNG files to img_dst_dir, and
    copy the XML files to xml_dst_dir
    
    Args:
        src_dir: path to files
        img_dst_dir: path to image destination
        xml_dst_dir: path to xml destination
    """
    cdict = {}
    if not os.path.exists(img_dst_dir):
        os.makedirs(img_dst_dir)
        print(f"created directory: {img_dst_dir}")

    if not os.path.exists(xml_dst_dir):
        os.makedirs(xml_dst_dir)
        print(f"created directory: {xml_dst_dir}")
    
    for keyword in os.listdir(src_dir):
        print(keyword)
        path = os.path.join(src_dir, keyword)
        count = 0
        for f in os.listdir(path):
            if os.path.splitext(f)[1] == '.xml':
                count += 1
                img_src_path = os.path.join(path,os.path.splitext(f)[0]+'.png')
                shutil.copy2(img_src_path,img_dst_dir)
                xml_src_path = os.path.join(path,os.path.splitext(f)[0]+'.xml')
                shutil.copy2(xml_src_path,xml_dst_dir)
        cdict[keyword] = count
        
    print("done")
    for k,v in cdict.items():
        print(f"xml count for {k}:{v}")

if __name__ == "__main__":
    get_xml(src_dir="data/all_img", img_dst_dir="data/img", xml_dst_dir="data/xml")

