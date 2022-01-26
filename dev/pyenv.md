```
查看系统 python 和 pip 命令的目录


$ which python
/usr/bin/python
$ which python3
/usr/bin/python3
$ which pip    
/usr/local/bin/pip
$ which pip3
/usr/local/bin/pip3
```

> [pyenv](https://github.com/pyenv/pyenv)
>
> [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)

## 安装

##### 依赖 - centos

```bash
$ dnf install gcc gcc-c++ glibc glibc-devel libffi-devel sqlite-devel bzip2-devel bzip2 readline-devel openssl-devel bzip2-devel sqlite-devel 

$ dnf install zlib zlib-devel
```

##### pyenv

> 用于安装多个版本 python
>
> shell 文件 .zshrc .bash_profile
>
> pip 包安装在虚拟环境的 ~/.pyenv/versions/p-3.9.2-learn/lib 目录下

- clone

  ```bash
  $ git clone https://github.com/pyenv/pyenv.git ~/.pyenv
  ```

- .zshrc 添加如下内容

  ```shell
  export PYENV_ROOT="$HOME/.pyenv"
  export PATH="$PYENV_ROOT/bin:$PATH"
  eval "$(pyenv init -)"
  eval "$(pyenv init --path)"
  ```

##### pyenv-virtualenv

> 用于创建 python 虚拟环境

- clone

  ```bash
  $ git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
  ```
  
- .zshrc 添加如下内容:

  ```bash
  eval "$(pyenv virtualenv-init -)"
  ```


##### 问题

- 描述

  ```
  切换环境成功, 但 python 和 pip 没有切换
  ```

- 原因

  ```
  .zshrc 环境变量问题
  ```

- 解决办法

  ```
  在 .zshrc 中添加
  eval "$(pyenv init --path)"
  ```

## 命令

```bash
pyenv help install
pyenv commands				# 所有可用的 pyenv 命令
pyenv version  				# 显示当前目录下采用的 python 版本
pyenv versions 				# 列出系统中安装的 python 版本
pyenv install --list		# 列出可安装版本
pyenv install <version>		# 安装对应版本 
pyenv install -v <version>	# 安装对应版本，若发生错误，可以显示详细的错误信息 
pyenv uninstall <version>	# 卸载 python 3.4.0
pyenv which python			# 显示当前python安装路径 
pyenv global <version>		# 全局设置, 整个系统生效 
pyenv local <version>		# 当前路径创建一个.python-version, 以后进入这个目录自动切换为该版本 
pyenv shell <version>		# 当前shell的session中启用某版本，优先级高于global 及 local
pyenv rehash 				# 安装完成之后需要对数据库进行更新



pyenv virtualenvs
pyenv virtualenv <version> <name> 	# 创建3.6.4版本的虚拟环境 
pyenv activate <name> 				# 激活 env-3.6.4 这个虚拟环境 
pyenv deactivate 					# 停用当前的虚拟环境 
pyenv uninstall env-3.6.4 			# 删除 env-3.6.4 这个虚拟环境
```

```
pyenv global 3.3.3 2.7.6
pyenv versions
  system
* 2.7.6 (set by /Users/yyuu/.pyenv/version)
* 3.3.3 (set by /Users/yyuu/.pyenv/version)
  venv27
python --version
Python 3.3.3
python2.7 --version
Python 2.7.6
python3.3 --version
Python 3.3.3
```

## 离线包安装python

```
创建目录放安装文件 ~/.pyenv/cache
使用pyenv install 2.7.16 查看下载文件的目录, 并用wget下载
安装 pyenv install 2.7.16
```

## pip

#####  pip 安装

- 在 Python2.x 中安装

  ```bash
  $ curl https://bootstrap.pypa.io/pip/2.7/get-pip.py -o get-pip2.py
  $ sudo python get-pip2.py
  $ pip --version
  $ pip install --upgrade pip
  ```

- 在 Python3.x 中安装

  ```bash
  $ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
  $ sudo python3 get-pip.py
  $ pip3 --version
  $ pip3 install --upgrade pip
  ```

##### 临时改变源

```bash
$ pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
```

##### 永久改变源 

```
创建并添加 ~/.pip/pip.conf

[global]
index-url = https://mirrors.aliyun.com/pypi/simple
[install]
trusted-host = https://mirrors.aliyun.com
```

## 问题

##### pyenv 安装 python 失败

- 原因

  ```
  缺少依赖
  ```

- 解决办法

  ```bash
  # 安装时使用 -v 查看详细信息, 缺少哪个依赖安装哪个
  $ pyenv install -v 3.9.2
  ```

##### 安装 psycopg2 失败

- centos

  ```bash
  $ yum install libjpeg libjpeg-devel zlib zlib-devel freetype freetype-devel lcms lcms-devel
  $ yum install postgresql-devel*
  $ yum install python-imaging
  ```

- man

  ```bash
  $ brew update
  $ brew install --force ossp-uuid
  $ brew install postgresql
  $ pip install psycopg
  ```

##### pyltp 安装失败

```
error: $MACOSX_DEPLOYMENT_TARGET mismatch: now "10.12" but "10.15" during configure

切换到虚拟环境
$ git clone https://github.com/HIT-SCIR/pyltp
$ cd pyltp
$ git submodule init
$ git submodule update
vim setup.py 修改文件121行
os.environ['MACOSX_DEPLOYMENT_TARGET'] = '10.12'
修改为后问题解决
os.environ['MACOSX_DEPLOYMENT_TARGET'] = '10.14' 
$ python setup.py install


$ MACOSX_DEPLOYMENT_TARGET=10.7 python setup.py install
```







