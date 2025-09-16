# flatFileCopye
递归遍历源目录下的所有子目录，扁平化的将所有文件复制到目标路径

你这句话的意思是：

> “不复制文件夹” → **不在目标目录中创建任何子文件夹结构**  
> “只递归复制文件夹中的文件” → **把所有子目录中的文件，全部“拍平”复制到目标目录根目录下**

---

📌 **修改目标：**

- 递归遍历源目录下的所有子目录
- 找到所有文件（不管在几层目录下）
- **全部复制到目标目录的根目录下（不保留原目录结构）**
- 如果文件重名？→ **自动重命名避免覆盖**

---

✅ **修改后的脚本如下：**

```python
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
```

---

📌 **关键修改点说明：**

| 修改内容                             | 说明                                         |
| ------------------------------------ | -------------------------------------------- |
| 移除 `rel_path` 和 `target_dir` 计算 | 不再保留目录结构                             |
| 所有文件直接复制到 `dst_dir` 根目录  | 实现“拍平”效果                               |
| 添加重名检测和自动重命名             | 避免覆盖，例如 `photo.jpg` → `photo (1).jpg` |

---

✅ **使用方法：**

保存为 `copy_flatten.py`，然后运行：

```cmd
python copy_flatten.py "E:\笔记\图片" "E:\笔记\images"
```

> 💡 注意路径中的反斜杠和空格：建议用双引号包裹路径，避免解析错误。

---

🎯 **运行效果示例：**

源目录结构：

```
E:\笔记\图片
├── a.jpg
├── subdir1
│   ├── b.jpg
│   └── a.jpg          ← 重名！
└── subdir2
    └── c.png
```

目标目录结果：

```
E:\笔记\images
├── a.jpg
├── a (1).jpg
├── b.jpg
└── c.png
```

---

✅ 完美满足你的需求：**不复制文件夹，只递归复制所有文件到目标根目录，并自动处理重名。**

如需进一步定制（如只复制特定类型、跳过隐藏文件等），欢迎继续提问！
