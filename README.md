# flatFileCopye
递归遍历源目录下的所有子目录，扁平化的将所有文件复制到目标路径
📌 **目标说明：**

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

python copy_flatten.py "./tmp/src/path" "./tmp/targetPath"
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
