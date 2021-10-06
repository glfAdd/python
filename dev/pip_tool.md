##### 安装

```
https://github.com/jazzband/pip-tools/
https://github.com/jazzband/pip-tools/

pip install pip-tools

python 包管理工具, 包含 pip-compile 和 pip-sync 两部分
```

##### pip-compile

- pip-compile 命令根据 requirements.in 或 setup.py 生成 requirements.txt 文件
- requirements.in 或 setup.py 需要手动创建
- 直接运行 pip-compile 会默认查找 requirements.in 或 setup.py 这两个文件, 也可以指定文件

#####  使用 setup.py 文件

```

```

##### 不使用 setup.py 文件

- 1. 手动创建 requirements.in 文件. 例如 Flask 项目写入一下内容

```
# requirements.in
# 可以指定版本
flask==1.0.1
```

- 2. 生成 requirements.txt 文件

```
$ pip-compile requirements.in

# 启动 hash 检测
$ pip-compile --generate-hashes requirements.in
```

- 3. 如果需要根据多个 *.in 文件生成 *.txt 文件时必须制定输出的文件, 否则报错

```
$ pip-compile requirements_test.in requirements.in --output-file aaa.txt
```

- 4. 更新包. 如果 requirements.txt 指定了版本则会被更新, 使用指定的版本

```
# 更新所有包
$ pip-compile --upgrade

# 更新指定包
$ pip-compile --upgrade-package flask

# 同时更新两个包
$ pip-compile --upgrade-package django --upgrade-package requests

# django 更新到最新, requests 更新到 2.0.0
$ pip-compile --upgrade-package django --upgrade-package requests==2.0.0
$ pip-compile --upgrade --upgrade-package 'requests<3.0'
$ pip-compile --upgrade-package 'django<1.0' --output-file requirements-django0x.txt
```

- CUSTOM_COMPILE_COMMAND

```


```

##### pip-sync

- pip-sync 根据 *.txt 文件安装包, 直接运行时默认使用 requirements.txt

```
$ pip-sync
$ pip-sync requirements.txt
$ pip-sync dev-requirements.txt
$ pip-sync dev-requirements.txt requirements.txt
```




