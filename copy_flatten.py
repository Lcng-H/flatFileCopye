#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import shutil
import sys

def copy_files_flatten(src_dir, dst_dir):
    """
    递归复制 src_dir 下的所有文件到 dst_dir 根目录（拍平结构）。
    如遇重名文件，自动在文件名后加序号避免覆盖。
    """
    if not os.path.exists(src_dir):
        print(f"❌ 错误：源目录 '{src_dir}' 不存在。")
        return False

    # 创建目标目录（如果不存在）
    os.makedirs(dst_dir, exist_ok=True)

    copied_count = 0

    for root, dirs, files in os.walk(src_dir):
        for file in files:
            src_file = os.path.join(root, file)

            # 获取原始文件名和扩展名
            base_name, ext = os.path.splitext(file)
            dst_file = os.path.join(dst_dir, file)

            # 处理重名：如果目标已存在，则加序号 (1), (2)...
            counter = 1
            while os.path.exists(dst_file):
                new_name = f"{base_name} ({counter}){ext}"
                dst_file = os.path.join(dst_dir, new_name)
                counter += 1

            try:
                shutil.copy2(src_file, dst_file)
                print(f"✅ 已复制: {src_file} -> {dst_file}")
                copied_count += 1
            except Exception as e:
                print(f"❌ 复制失败: {src_file} -> {dst_file} | 错误: {e}")

    print(f"\n🎉 复制完成！共复制 {copied_count} 个文件到 '{dst_dir}'（已拍平结构）")
    return True


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("用法: python copy_flatten.py <源目录> <目标目录>")
        print("示例: python copy_flatten.py \"E:\\笔记\\图片\" \"E:\\笔记\\images\"")
        sys.exit(1)

    source_directory = sys.argv[1]
    destination_directory = sys.argv[2]

    copy_files_flatten(source_directory, destination_directory)