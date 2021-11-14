##### 修改电脑名称

```
查看电脑名称
hostname

修改名称
hostnamectl set-hostname gong

重启电脑
```

##### 普通用户无法使用 sudo 

```
问题描述
gladd is not in the sudoers file.  This incident will be reported

添加sudoers文件的写权限
/etc/sudoers文件默认是只读的
chmod u+w /etc/sudoers
vim /etc/sudoers

找到这行 root ALL=(ALL) ALL,在他下面添加xxx ALL=(ALL) ALL (这里的xxx是你的用户名)

撤销sudoers文件写权限,命令:
chmod u-w /etc/sudoers
```

##### 启动 dnf fastest mirror

```
编辑 /etc/dnf/dnf.conf 并在结尾添加
fastestmirror=True
```

##### 常用命令

```
删除缓存的无用软件包
dnf clean all
dnf makecache
dnf update
dnf upgrade
删除无用孤立的软件包
dnf autoremove

查找包的版本
dnf list | grep vim
dnf list available |grep vim

查看已经安装的版本
rpm -qa | grep vim

# 列出已启用(enabled=1)、已禁用或所有已配置仓库
dnf repolist
dnf repolist --enabled
dnf repolist --disabled 
dnf repolist --all

# 查看某个或所有仓库的详细信息
dnf repolist -v
dnf repolist BaseOS -v
```

##### 必备代码库

```
dnf install epel-release
```

##### xfce(不好用)

```
查看是否有xfce组：
dnf grouplist

安装
dnf groupinstall xfce
dnf install xfce4* --skip-broken
```

##### 常用软件

```
dnf install -y htop ntfs-3g terminator zsh vim openvpn gcc gcc-c++ bzip2


# 硬盘 unknown filesystem type exfat 问题
dnf install http://download1.rpmfusion.org/free/el/updates/8/x86_64/f/fuse-exfat-1.3.0-3.el8.x86_64.rpm
dnf install http://download1.rpmfusion.org/free/el/updates/8/x86_64/e/exfat-utils-1.3.0-3.el8.x86_64.rpm
```

##### 查看发行版本

```
cat /etc/redhat-release
```

##### 升级内核

- 内核官网

  ```
  https://www.kernel.org/
  ```

- 内核版本

  ```
  mainline: 主线版本
  
  stable: 稳定版，由mainline在时机成熟时发布，稳定版也会在相应版本号的主线上提供bug修复和安全补丁，但内核社区人力有限，因此较老版本会停止维护，而标记为EOL(End of Life)的版本表示不再支持的版本。
  
  longterm(Long Term Support): 期支持版，长期支持版的内核不再支持时会标记EOL。
  
  linux-next，snapshot: 代码提交周期结束之前生成的快照 用于给Linux代码贡献者们做测试
  ```

- 内核软件包

  ```
  kernel: Linux 内核软件包，包含单、多核和多处理器系统的内核，是任何 Linux 操作系统的核心，单处理器的系统仅需安装内核包。内核处理操作系统的基本功能: 内存分配、进程分配、设备输入和输出等
  
  kernel-devel: 包含提供足够的针对内核软件包构建模块的内核头文件和 makefile 文件
  
  kernel-headers: 包含指定 Linux 内核、用户空间库文件和程序之间指定接口的 C 头文件。头文件定义了构建大多数标准程序所需的结构和常量，也是重建 glibc 软件包所必需的
  
  kernel-doc: 包含来自内核源代码的文档文件。各种关于 Linux 内核和设备以及驱动程序的信息都记录在这些文件当中
  
  kernel-firmware: 包含对于某些设备及其操作的固件信息文件
  
  kernel-debug: 包含许多对于内核 debug 诊断和调试的启用选项，只有当我们需要尝试收集额外的内核错误信息时才应该安装它。它是以牺牲性能为代价
  
  kernel-debug-devel: 包含内核 debug 诊断和调试的启用选项，以牺牲性能为代价
  ```

- 安装

  ```
  0. 查看系统中已安装的内核
  rpm -qa | grep kernel
  
  1. 首先导入public key
  rpm --import https://www.elrepo.org/RPM-GPG-KEY-elrepo.org
  yum install https://www.elrepo.org/elrepo-release-8.el8.elrepo.noarch.rpm
  
  2. 可用的系统内核安装包：
  yum --disablerepo="*" --enablerepo="elrepo-kernel" list available
  
  3. 安装最新版内核
  ml 版本
  sudo dnf --enablerepo=elrepo-kernel install kernel-ml
  sudo dnf --enablerepo=elrepo-kernel install kernel-ml-{devel,headers}
  或 lt 版本
  sudo dnf --enablerepo=elrepo-kernel install kernel-lt
  sudo dnf --enablerepo=elrepo-kernel install kernel-lt-{devel,headers}
  
  4. 设置以新的内核启动. 0 表示最新安装的内核，设置为 0 表示以新版本内核启动：
  grub2-set-default 0
  
  5. 生成grub配置文件并重启系统
  grub2-mkconfig -o /boot/grub2/grub.cfg
  reboot 
  
  6. 删除旧内核
  dnf remove (要删除的内核版本)
  ```

##### gcc （未使用）

```
gcc Developer Toolset 7 地址
https://www.softwarecollections.org/en/scls/rhscl/devtoolset-7/

GCC rpm 下载地址
http://www.rpmfind.net/linux/rpm2html/search.php?query=gcc(x86-64)
http://rpm.pbone.net/index.php3?stat=3&search=gcc&srodzaj=3


(这种方式安装的是 centos 默认内核的版本)
gcc 包的地址, 看看不用下载
https://centos.pkgs.org/8-stream/centos-appstream-x86_64/gcc-toolset-10-toolchain-10.1-0.el8.x86_64.rpm.html

安装
dnf install gcc-toolset-10-gcc


(编译安装最新内核gcc)
0. 源代码下载地址
http://mirror.hust.edu.cn/gnu/gcc/
https://mirrors.aliyun.com/gnu/gcc/
gcc-10.3.0.tar.gz

1. 创建安装的目录
/usr/lib/gcc/x86_64-redhat-linux/10.3.0

2. 安装依赖
$ yum install -y gcc gcc-c++ bzip2


3. 进入gcc源码目录, 保证其确实是将 gmp、mpfr、mpc 等依赖包成功下载下
$ ./contrib/download_prerequisites

4. 配置 GCC 支持编译 C 和 C++ 语言
$ ./configure --prefix=/usr/lib/gcc/x86_64-redhat-linux/10.3.0/ --enable-checking=release --enable-languages=c,c++ --disable-multilib

5. 
$ make

6. 
$ make install

 
7. 查看系统当前的gcc版本
$ gcc --version

8. 配置多本本 gcc 
$ mv /usr/bin/gcc /usr/bin/gcc-8.4.1
$ mv /usr/bin/g++ /usr/bin/g++-8.4.1
$ alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-8.4.1 80 --slave /usr/bin/g++ g++ /usr/bin/g++-8.4.1
$ alternatives --install /usr/bin/gcc gcc /usr/lib/gcc/x86_64-redhat-linux/10.3.0/bin/x86_64-pc-linux-gnu-gcc 99 --slave /usr/bin/g++ g++ /usr/lib/gcc/x86_64-redhat-linux/10.3.0/bin/x86_64-pc-linux-gnu-g++

9. 切换 gcc 版本
$ alternatives --config gcc

10. 查看版本
gcc -v
g++ -v
```

##### docker ce

```
yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
yum install docker-ce
# 尝试在命令行中添加 '--allowerasing' 来替换冲突的软件包
dnf install docker-ce allowerasing

systemctl start docker
systemctl enable docker
systemctl restart docker
systemctl status docker

# 普通用户使用 docker
```

##### 美化

```
扩展工具安装在文件下
/home/gladd/.local/share/gnome-shell/extensions

dnf install gnome-tweaks

浏览器安装插件, 点击开关可以安装

# 把主题放置在user/share/themes
User Themes
# 应用窗口的菜单项放置在了桌面顶部栏中
Gnome Global Application Menu
# 任务栏
dash-to-panel
# 屏幕截图工具
Screenshot Tool 
# 在顶栏显示应用图标
TopIcons Plus
# 在顶栏显示移动盘图标
Removable Drive Menu
# 最近查看过的文件
Recent Items
# 顶栏显示应用图标，输入法切换的时候特别有用
TopIcons Plus 
# 顶栏显示网速
Netspeed
# 在顶栏显示当前工作区号
WorkSpace indicator
# 剪切版
Clipboard Indicator
```

##### ibus-rime （未完成）

```
使用系统的 ibus

ibus-rime 装不上, 暂时不用
```

##### typora

```
https://www.typora.io/

wget https://typora.io/li	nux/Typora-linux-x64.tar.gz

1. 下载源代码

2. 移动到 /opt 目录下

3. 运行(需要图形页面的用户才能执行)

4. 配置环境变量(没有实验)
export PATH=$PATH:/opt/Typora-linux-x64

5. 运行软件
Typora

```

##### sublime-text

```
sudo rpm -v --import https://download.sublimetext.com/sublimehq-rpm-pub.gpg
sudo dnf config-manager --add-repo https://download.sublimetext.com/rpm/stable/x86_64/sublime-text.repo
sudo dnf install sublime-text
```

##### vlc

```
yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
yum install https://download1.rpmfusion.org/free/el/rpmfusion-free-release-8.noarch.rpm
dnf install vlc
```

##### smplayer

```
官网: https://www.smplayer.info/zh/downloads
github 地址: https://github.com/smplayer-dev/smplayer

依赖:
dnf install subversion rpm-build


git clone https://github.com/smplayer-dev/smplayer.git
```

##### vmware

```
```



##### google chrome

```
vim /etc/yum.repos.d/google-chrome.repo
[google-chrome]
name=google-chrome
baseurl=http://dl.google.com/linux/chrome/rpm/stable/$basearch
enabled=1
gpgcheck=1
gpgkey=https://dl-ssl.google.com/linux/linux_signing_key.pub


dnf install google-chrome-stable
```

##### flash plugin(未使用)

```
dnf install http://linuxdownload.adobe.com/adobe-release/adobe-release-x86_64-1.0-1.noarch.rpm
dnf install libcurl flash-plugin alsa-plugins-pulseaudio
```

##### vscode

```
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo sh -c 'echo -e "[code]\nname=Visual Studio Code\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\nenabled=1\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc" > /etc/yum.repos.d/vscode.repo'
sudo dnf check-update
sudo dnf install code
```

##### oh my zsh

- 安装

  ```
  sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
  ```

- 错误

  ```
  描述
  curl: (7) Failed to connect to raw.github.com port 443: No route to host
  
  
  解决办法
  1. 打开 https://www.ipaddress.com/ 输入需要访问的域名，查到该域名 ip 地址
  
  2. 查询 raw.githubusercontent.com 对应的IP 地址
  
  3. 修改 hosts 添加
  185.199.108.133 raw.githubusercontent.com
  ```

  

```
https://www.ipaddress.com/








```

##### 错误 1

```
描述
This system is not registered to Red Hat Subscription Management. You can use subscription-manager to register.


解决办法: 
1. 禁用注册插件. 修改 /etc/yum/pluginconf.d/subscription-manager.conf 的 enabled
enabled=0
2. 重新安装
dnf install install yum-utils
```

