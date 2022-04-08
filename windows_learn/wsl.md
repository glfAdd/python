##### 安装

```bash
# 1. 以管理员权限运行powershell，然后输入以下命令启用虚拟机平台：
Enable-WindowsOptionalFeature -Online -FeatureName VirtualMachinePlatform


# 2. 以管理员权限运行powershell，然后输入以下命令启用Linux子系统功能(WSL)：
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux


# 3. cmd 管理员运行
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart


# 4. 商店安装需要的Debian


# 5. 查看安装的linux是wsl还是wsl2
wsl -l -v
显示的结果
  NAME      STATE           VERSION
* Debian    Stopped         2


# wsl2 下载并安装
https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi


# 6. 将默认设置为wsl2
wsl --set-default-version 2
如果出现错误, 需要安装"适用于 x64 计算机的 WSL2 Linux 内核更新包"


# 7. 将Debian设置为 wsl2
wsl --set-default-version 2
```

##### 卸载

```
1. 查看已经安装的linux
wslconfig /l

2. 删除
wslconfig /u debian
```

##### 源

```
查看系统版本号
cat /etc/issue

清华源: https://mirrors.tuna.tsinghua.edu.cn/help/debian/

buster版
deb http://mirrors.163.com/debian/ buster main non-free contrib
deb http://mirrors.163.com/debian/ buster-updates main non-free contrib
deb http://mirrors.163.com/debian/ buster-backports main non-free contrib
deb http://mirrors.163.com/debian-security/ buster/updates main non-free contrib
deb-src http://mirrors.163.com/debian/ buster main non-free contrib
deb-src http://mirrors.163.com/debian/ buster-updates main non-free contrib
deb-src http://mirrors.163.com/debian/ buster-backports main non-free contrib
deb-src http://mirrors.163.com/debian-security/ buster/updates main non-free contrib
```

##### wsl 命令

```
wsl --shutdown          关闭
```

##### 常用

```
aptitude install net-tools
```

##### ssh

```
1. 必须先删除重新安装
aptitude remove openssh-server
aptitude install openssh-server

2.编辑sshd_config文件

sudo vim /etc/ssh/sshd_config

Port 22
PermitRootLogin yes
PasswordAuthentication yes

3. 重新启动
service ssh restart

4. 命令
service ssh status
/etc/init.d/ssh start
update-rc.d ssh enable              设为开机启动

```

##### 设置默认登录用户和root密码

```
1.查看当前系统安装的linux:
  PS C:\> wslconfig /l
  适用于 Linux 的 Windows 子系统:
  Ubuntu (默认)

2. 修改密码当wsl里的root密码忘了时，以管理员身份打开cmd或powershell：
  PS C:\> debian config --default-user root
  PS C:\> wsl
  root@universe:/mnt/c# passwd
  Enter new UNIX password:

3. 修改完以后将用户改为以前的用户
  PS C:\> debian config --default-user glfadd
```





