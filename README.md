# filter_unused_string
过滤Xcode项目中Localizable.strings未使用的字符串

#使用
命令：
```bash
python [脚本文件路径] [工程目录路径] [Localizable.strings路径]
```

例如： 
```bash
python filter_unused_string.py ~/Desktop/DemoProject ~/Desktop/DemoProject/Base.lproj/Localizable.strings
````

当前目录输出过滤后的`Localizable.strings`文件：`outputLocalizable.strings`
