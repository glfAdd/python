## 安装

##### 设置阿里源

```
wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
yum clean all
yum makecache
yum update
```

##### 其他源

```bash
$ yum install epel-release
```

##### ssh

```bash
1. 重新安装
$ yum reinstall openssh-server


2. 编辑 /etc/ssh/sshd_config 文件修改为如下
Port 22
PermitRootLogin yes
PasswordAuthentication yes


3. 重启动服务
$ service sshd start
```

##### ibus

```bash
0. 主要需要安装如下包
  ibus， 这个包里有ibus-daemon这个平台服务器程序和ibus这个配置助手。
  ibus-libpinyin， 这个是ibus平台下具体的拼音输入法。
  ibus-gtk2/3，这个是ibus在GTK环境下的UI，托盘显示。
  im-chooser,这个是输入法平台选择助手程序。
  gtk2/3-immodule-xim，这个是输入法候选字显示UI


1. 安装
$ yum -y install ibus ibus-libpinyin ibus-gtk3 im-chooser gtk3-immodule-xim


2. 选择输入法平台和输入法
$ im-chooser


3. 启动设置
ibus-setup
```

##### 升级内核

```bash
1. 首先导入public key
$ rpm --import https://www.elrepo.org/RPM-GPG-KEY-elrepo.org
$ rpm -Uvh http://www.elrepo.org/elrepo-release-7.0-2.el7.elrepo.noarch.rpm


2. ml 版本
$ yum --enablerepo=elrepo-kernel -y install kernel-ml
$ yum --enablerepo=elrepo-kernel -y install kernel-ml-{devel,headers}
或 lt 版本
$ yum --enablerepo=elrepo-kernel install kernel-lt
$ yum --enablerepo=elrepo-kernel install kernel-lt-{devel,headers}


3. 设置以新的内核启动. 0 表示最新安装的内核，设置为 0 表示以新版本内核启动：
$ grub2-set-default 0


4. 生成grub配置文件并重启系统
$ grub2-mkconfig -o /boot/grub2/grub.cfg
$ reboot


5. 查看内核
$ rpm -qa | grep kernel


6. 删除内核
$ yum remove kernel-3.10.0-693.el7.x86_64
```

##### 必备软件

```
yum install net-tools dnf gcc-c++ terminator mock cmake ntfs-3g htop vim tree zsh
```

##### rpm 命令

```
# 安装rpm
yum localinstall xxxxx.rpm
rpm -Uvh mysql80-community-release-el6-n.noarch.rpm
# 查找所有的rpm
rpm -qa | grep -i crosso
# 卸载rpm
rpm -e --nodeps crossover-18.0.5-1.i386
```

##### xfce 安装

```
$ yum grouplist
$ yum groupinstall xfce
$ yum install xfce*

$ yum groupremove xfce
```

##### xfce 快捷键文件

```
~/.config/xfce4/xfconf/xfce-perchannel-xml
```

##### xfce 菜单快捷键

```
yum install xfce4-whiskermenu-plugin
```

##### xfce 设置默认应用程序

```
Settings -> MIME Type Editor
1. 如果能直接找到应用程序就直接选
2. 如果找不到应用程序可以使用 "Use a custom comand" 输入命令选择应用程序
```

##### xfce 快捷方式

```
存放目录
/usr/share/applications
```

##### xfce 美化

```
下载主题，图标样式：http://xfce-look.org/
将下载的主题，移动到桌面主题目录：/usr/share/themes
将下载的图标，移动到图标主题目录：/usr/share/icons
```

##### 蓝牙

```
bluedevil4 bluetooth blueman


bluez bluez-tools
```



##### gcc 9

```
yum install centos-release-scl scl-utils-build -y
yum install devtoolset-9-toolchain -y


查看 scl 安装的软件包
scl --list


临时启动启动环境
scl enable devtoolset-9 bash
gcc --version


永久环境
echo "source /opt/rh/devtoolset-9/enable" >>/etc/profile
```

##### 普通用户 sudo 命令

```
gladd is not in the sudoers file.  This incident will be reported

添加sudoers文件的写权限
/etc/sudoers文件默认是只读的
chmod u+w /etc/sudoers
vim /etc/sudoers

找到这行 root ALL=(ALL) ALL,在他下面添加xxx ALL=(ALL) ALL (这里的xxx是你的用户名)

撤销sudoers文件写权限,命令:
chmod u-w /etc/sudoers

切换用户免密码
## Same thing without a password
# %wheel        ALL=(ALL)       NOPASSWD: ALL
gong    ALL=(ALL)       NOPASSWD: ALL
```

##### teamviewer

```
教程地址
https://blog.csdn.net/changgongzhao/article/details/52299314

用rpm 命令安装可能会出现缺少依赖，而导致安装失败
进入到rpm文件所在目录
yum install teamviewer_14.1.9025.x86_64.rpm

默认会安装到/opt/teamview里面，并且安装成功会默认启动
cd /opt/teamviewer/tv_bin/

teamviewer --setup console #设置启动方式为控制台启动
teamviewer --daemon restart  #重启teamview服务
teamviewer --info #查看teamview信息
teamviewer --passwd [PASSWD]   #设置密码
teamviewer --help  #查看帮助
```

##### vim 8

```bash
$ wget https://github.com/vim/vim/archive/master.zip
$ unzip master.zip
$ cd vim-master
$ cd src/
$ ./configure
$ make
$ sudo make install
```

##### chrome

```bash
1. 创建文件 /etc/yum.repos.d/google-chrome.repo 添加如下内容
[google-chrome]
name=google-chrome
baseurl=http://dl.google.com/linux/chrome/rpm/stable/$basearch
enabled=1
gpgcheck=1
gpgkey=https://dl-ssl.google.com/linux/linux_signing_key.pub


2. 安装
$ yum install google-chrome-stable --nogpgcheck


3. 插件
GNOME Shell integration
Chrono Download Manager
```

##### gnome创建快捷方式

```
vim pycharm.desktop

#!/usr/bin/env xdg-open
[Desktop Entry]
Version=1.0
Encoding=UTF-8
Name=eclipse
Type=Application
Terminal=false
Name[en_US]=eclipse
Exec=/home/gladd/eclipse/jee-oxygen/eclipse/eclipse
Comment[en_US]=Eclipse Mars.2
Comment=Eclipse Mars.2
GenericName[en_US]=
Icon=/home/gladd/eclipse/jee-oxygen/eclipse/icon.xpm

把快捷文件放在
/usr/share/applications
```

##### git 设置

```bash
$ git config --global user.name "gonglongfei"
$ git config --global user.email "2239660080@qq.com"
```

##### ssh 秘钥设置

```bash
$ ssh-keygen -t rsa -C "2239660080@qq.com"
```

##### docker

```bash
$ yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
$ yum install docker-ce
```

##### sublimt text3

```bash
$ rpm -v --import https://download.sublimetext.com/sublimehq-rpm-pub.gpg
$ yum-config-manager --add-repo https://download.sublimetext.com/rpm/stable/x86_64/sublime-text.repo
$ yum install sublime-text
```

##### vlc

```
yum install vlc
```

##### smplayer

```bash
$ yum install http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-release-0-5.el7.nux.noarch.rpm
$ yum install smplayer
```

##### 视频解码器

```
yum install libdvdcss gstreamer{,1}-plugins-ugly gstreamer-plugins-bad-nonfree gstreamer1-plugins-bad-freeworld libde265 x265
```

##### shadowsocks

```

vim /etc/yum.repos.d/shadowsocks-qt5.repo
[librehat-shadowsocks]
name=Copr repo for shadowsocks owned by librehat
baseurl=https://copr-be.cloud.fedoraproject.org/results/librehat/shadowsocks/epel-7-$basearch/
type=rpm-md
skip_if_unavailable=True
gpgcheck=1
gpgkey=https://copr-be.cloud.fedoraproject.org/results/librehat/shadowsocks/pubkey.gpg
repo_gpgcheck=0
enabled=1
enabled_metadata=1

yum install shadowsocks-qt5
```



##### openvpn

```

$ yum install openvpn
复制文件到/etc/openvpn
运行
openvpn glf.ovpn

设置配置文件保存用户名和密码
    1. 进行OPENVPN安装目录下config目录
    2. 打开并编辑你的配置文件XXXX.ovpn
    3. 在XXXX.ovpn最后增加配置 auth-user-pass pass.txt
    4. 在同目录下创建XXXX.ovpn的配置文件名 pass.txt将写入用户和密码
    (第一行用户名, 第二行密码)



```

##### charles

```
vim /etc/yum.repos.d/Charles.repo
[charlesproxy]
name=Charles Proxy Repository
baseurl=https://www.charlesproxy.com/packages/yum
gpgkey=https://www.charlesproxy.com/packages/yum/PublicKey

yum install charles-proxy
```

##### Adobe Flash Player

```
wget http://linuxdownload.adobe.com/adobe-release/adobe-release-x86_64-1.0-1.noarch.rpm
rpm -ivh adobe-release-x86_64-1.0-1.noarch.rpm
rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-adobe-linux
yum install firefox.x86_64 flash-plugin
```

##### crossover

```
官网下载
chmod 755 crossover.bin
./crossover.bin

安装以后用root权限执行
```

##### 常用软件

```

**************************************************
navicat

https://www.navicat.com.cn/download/navicat-premium
**************************************************
postman

https://www.getpostman.com/downloads/
**************************************************
Typora

https://www.typora.io/#download
**************************************************
flashplayer

https://get.adobe.com/cn/flashplayer/
```

## 问题

##### yum 安装软件时错误

- 错误描述

  ```
  Loaded plugins: fastestmirror, langpacks
  Existing lock /var/run/yum.pid: another copy is running as pid 3646.
  Another app is currently holding the yum lock; waiting for it to exit...
    The other application is: PackageKit
      Memory :  38 M RSS (455 MB VSZ)
      Started: Fri Aug 20 11:44:29 2021 - 02:46 ago
      State  : Sleeping, pid: 3646
  ```

- 原因

  ```
  yum只能支持一个进程运行，如果有一个进程已经在运行，其他的必须等待该进程退出释放lock
  ```

- 解决办法

  ```bash
  $ rm -rf /var/run/yum.pid
  ```

##### pycahrm不能输入中文

```
在pycharm.sh脚本的如下行（大约在201行）：

# ---------------------------------------------------------------------
# Run the IDE.
# ---------------------------------------------------------------------
 IFS="$(printf '\n\t')"
前增加以下三行配置即可
：

export GTK_IM_MODULE=ibus
export QT_IM_MODULE=ibus
export XMODIFIERS=@im=ibus
```

##### libstdc++.so.6

- 错误描述

  ```
  Uncaught Exception:
  Error: /lib64/libstdc++.so.6: version `CXXABI_1.3.8' not found
  ```
  
- 原因

  ```
  升级 gcc 后 libstdc++.so.6 没有更新, 还是就版本
  ```
  
- 解决办法

  ```
  省级 libstdc++.so.6 版本
  ```

- 步骤

  ```
  1. 确认自己的动态库是否支持CXXABI_1.3.8
  [root@gong ~]# strings /usr/lib64/libstdc++.so.6|grep CXXABI
  CXXABI_1.3
  CXXABI_1.3.1
  CXXABI_1.3.2
  CXXABI_1.3.3
  CXXABI_1.3.4
  CXXABI_1.3.5
  CXXABI_1.3.6
  CXXABI_1.3.7
  CXXABI_TM_1
  
  2. 查看 libstdc++.so.6 的版本
  [root@gong lib64]# ls /usr/lib64|grep libstdc++
  libstdc++.so.6
  libstdc++.so.6.0.19
  
  3. 下载 libstdc++.so.6
  （如果没有可以安装 miniconda， 将这里面新版本的复制到 /usr/lib64）
  
  4. 删除旧的链接
  rm -rf libstdc++.so.6.0.26
  
  5. 生成软软链接
  ln -s libstdc++.so.6.0.26 libstdc++.so.6
  ```

  

## 优化

##### 查看开机时间

```
systemd-analyze blame|head
systemd-analyze blame
```

##### 显示桌面快捷键

```
Hide all normal windows
```

##### gnome美化

```

扩展工具安装在文件下
/home/gladd/.local/share/gnome-shell/extensions

yum install gnome-shell
yum install gnome-shell-extension*

浏览器安装插件
https://extensions.gnome.org/
firefox点击Click here to install browser extension安装插件
chrome需要chrome-gnome-shell
点击开关可以安装

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
。。。	。。。	。。。	。。。
主题网站
https://www.gnome-look.org/

主题工具 OCS-Store
https://www.opendesktop.org/p/1175480/
下载运行AppImage文件
chmod a+x *.AppImage
普通用户：主题安装在/home/gladd/.themes
root用户：主题安装在/root/.themes

隐藏底部任务栏
cd /usr/share/gnome-shell/extensions/
mv window-list@gnome-shell-extensions.gcampax.github.com/ window-list@gnome-shell-extensions.gcampax.github.com.backup
```

