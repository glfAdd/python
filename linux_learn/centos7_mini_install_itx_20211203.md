##### 解决无法上网问题

```
系统的内核不支持当前系统的网卡, 无法上网, 手动安装内核

1. 内核下载地址: https://elrepo.org/linux/kernel/el7/x86_64/RPMS/


2. 分别下载 3 个升级内核的 rpm
https://elrepo.org/linux/kernel/el7/x86_64/RPMS/kernel-ml-5.15.6-1.el7.elrepo.x86_64.rpm
https://elrepo.org/linux/kernel/el7/x86_64/RPMS/kernel-ml-devel-5.15.6-1.el7.elrepo.x86_64.rpm
https://elrepo.org/linux/kernel/el7/x86_64/RPMS/kernel-ml-headers-5.15.6-1.el7.elrepo.x86_64.rpm


3. 用硬盘拷贝到电脑上
fdisk -l
mount /dev/sda1 /mnt/


4. 安装内核
yum localinstall kernel-ml-5.15.6-1.el7.elrepo.x86_64.rpm
yum localinstall kernel-ml-devel-5.15.6-1.el7.elrepo.x86_64.rpm (这个安装失败了)
yum localinstall kernel-ml-headers-5.15.6-1.el7.elrepo.x86_64.rpm


5. nmtui 设置网卡
编辑连接 -> 添加 -> 以太网
Edis a connection -> add -> Ethernet -> 直接选择<OK> 
```

##### 设置阿里源

```bash
$ wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
$ yum clean all
$ yum makecache
$ yum update -y
```

##### 其他源

```bash
$ yum install epel-release
```

##### 升级内核

```bash
1. 首先导入public key
$ rpm --import https://www.elrepo.org/RPM-GPG-KEY-elrepo.org
$ rpm -Uvh http://www.elrepo.org/elrepo-release-7.0-2.el7.elrepo.noarch.rpm


2. ml 版本
$ yum --enablerepo=elrepo-kernel -y install kernel-ml
$ yum --enablerepo=elrepo-kernel install kernel-ml-{devel,headers}
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

##### wifi 无法使用

```
1. 安装 wifi 管理工具
$ yum install NetworkManager-wifi

2. 扫描可用于连接wifi
$ nmcli dev wifi 

3. shell ui
$ nmtui
```

##### 必备软件

```
$ yum install ntfs-3g wget htop vim net-tools



$ yum install dnf gcc-c++  mock cmake 
$ yum install devtoolset-8-gcc  devtoolset-8-gcc-c++
$ yum install yum-fastestmirror

$ yum install screenfetch
$ yum install ncurses-devel
$ yum install yum-utils
```

##### RPM 命令

```
# 安装rpm
yum localinstall xxxxx.rpm
rpm -Uvh mysql80-community-release-el6-n.noarch.rpm
# 查找所有的rpm
rpm -qa | grep -i crosso
# 卸载rpm
rpm -e --nodeps crossover-18.0.5-1.i386
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



##### 软件运行错误

- 错误描述

  ```
  /usr/lib/libstdc++.so.6: version `CXXABI_1.3.9' not found
  
  A JavaScript error occurred in the main process
  Uncaught Exception:
  Error: /lib64/libstdc++.so.6: version `CXXABI_1.3.8' not found (required by /opt/Typora-linux-x64/resources/app.asar.unpacked/main.node)
  ```
  
- 解决办法

  ```
  
   源码编译升级安装了gcc后，编译程序或运行其它程序时，有时会出现类似
  1. 检查动态库
  strings /usr/lib64/libstdc++.so.6 | grep GLIBC
  2. 查找编译gcc时生成的最新动态库
  find / -name "libstdc++.so*"
  3. 将上面的最新动态库libstdc++.so.6.0.21复制到/usr/lib64目录下
  cp /home/gladd/anaconda2/x86_64-conda_cos6-linux-gnu/sysroot/lib/libstdc++.so.6.0.25 /usr/lib64
  4. cd /usr/lib64
  5. 删除原来软连接
  rm -rf libstdc++.so.6
  6. 将默认库的软连接指向最新动态库
  ln -s libstdc++.so.6.0.21 libstdc++.so.6
  7. 重新运行以下命令检查动态库
  strings /usr/lib64/libstdc++.so.6 | grep GLIBC
  ```

  

## 优化

##### 查看开机时间

```
systemd-analyze blame|head
systemd-analyze blame
```



