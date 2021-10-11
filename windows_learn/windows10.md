##### 联想笔记本 bois 升级

```
官网下载地址
https://newsupport.lenovo.com.cn/driveList.html?fromsource=driveList&selname=%E6%8B%AF%E6%95%91%E8%80%85R7000%202020
```

##### windows 系统包管理工具

```
参考: https://www.jianshu.com/p/50993df76b1c
命令安装在: C:\Users\lg\scoop\apps

0. 打开windows powershell

1. 在 PowerShell 中输入下面内容，保证允许本地脚本的执行, 选择"全部"
set-executionpolicy remotesigned -scope currentuser

2. 执行下面的命令安装 Scoop：
iwr -useb get.scoop.sh | iex

3. 命令
scoop search firefox
    search 	搜索软件名
    update 	更新软件
    status 	查看软件状态
    uninstall 	卸载软件
    info 	查看软件详情
    home 	打开软件主页

scoop list                  显示已安装软件
scoop status                显示可更新的软件
scoop search <app>          查找软件
scoop info <app>            显示软件信息（含必要配置说明）
scoop cleanup *             清理所有旧版软件
scoop cleanup <app>         清理指定软件
scoop cleanup -k *  # 或 scoop cleanup --cache *     清理过期的安装包

# 更新scoop, 更新指定软件
scoop update
scoop update <app>
scoop update vscode-insiders -kf    # 更新 nightly 版本

4. scoop使用aria2进行多线程下载以加速下载：
scoop install aria2
aria2 配置文件路径: c：/user/xxx/.config/scoop/config.json
{
    "lastupdate":  "2020-06-16T23:58:19.3002510+08:00",
    "SCOOP_REPO":  "https://github.com/lukesampson/scoop",
    "SCOOP_BRANCH":  "master",
    "aria2-max-connection-per-server":  16,
    "aria2-split":  16,
    "aria2-min-split-size":  "2M"
}
配置命令
scoop config aria2-max-connection-per-server 16
scoop config aria2-split 16
scoop config aria2-min-split-size 1M

5. 添加仓库
scoop bucket add extras
# 第三方软件源bucket
scoop bucket add scoopbucket https://github.com/yuanying1199/scoopbucket
scoop bucket add versions

6. 常用软件
scoop install sudo
scoop install git 7zip openssh
scoop install aria2
scoop install ffmpeg
scoop install nodejs
scoop install python



***问题***
使用“1”个参数调用“DownloadString”时发生异常:“未能解析此远程名称: 'raw.githubusercontent.com'”
所在位置 行:1 字符: 1
+ iex (new-object net.webclient).downloadstring('https://get.scoop.sh')
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (:) [], MethodInvocationException
    + FullyQualifiedErrorId : WebException

***办法***
windows hosts 文件路径
    C:\Windows\System32\drivers\etc

在 hosts 文件里面添加
    151.101.76.133 raw.githubusercontent.com
```

##### 颜色管理工具

```
# 安装微软官方颜色工具
scoop install colortool

# 查看已安装主题
colortool -s

# 设置主题
colortool OneHalfDark
```

##### 安装字体

```
解决powershell乱码
https://github.com/powerline/fonts

进入目录以后执行
    .\install.ps1


符号字体官网
https://www.nerdfonts.com/

# 添加 nerd fonts 源
scoop bucket add 'nerd-fonts'
# 安装 nerd fonts
scoop install FantasqueSansMono-NF
sudo scoop install FantasqueSansMono-NF
```

#####  git 中文显示乱码

```
系统环境变量直接增加
LESSCHARSET=utf-8
```

##### pycharm 设置 terminal

```
tool -> shell path -> powershell.exe
```

##### mac type

```
字体美化
```

##### wox

```
教程 https://sspai.com/post/33460

1. 直接输入数字当做计算器使用
2. 安装插件
3. 剪切板历史插件
    安装 wpm install Clipboard History
    触发命令 cb
4. 弹出 USB 设备
    安装 wpm install Remove USB
    触发命令 reu
```

##### oh-my-posh

```
https://github.com/JanDeDobbeleer/oh-my-posh

1. 打开 PowerShell 安装

2. 安装 ConEmu
使用: choco install ConEmu
或使用: sudo scoop install conemu

2. 安装 posh-git 和 oh-my-posh 这两个模块
    Install-Module posh-git -Scope CurrentUser
    Install-Module oh-my-posh -Scope CurrentUser

3. 新增（或修改）你的 PowerShell 配置文件
    # 如果之前没有配置文件，就新建一个 PowerShell 配置文件
    if (!(Test-Path -Path $PROFILE )) { New-Item -Type File -Path $PROFILE -Force }
    # 用记事本打开配置文件
    notepad $PROFILE
    # 在其中添加下面的内容
    Import-Module posh-git
    Import-Module oh-my-posh
    Set-Theme Paradox
    # 如果后面日期乱码, 使用命令
    Set-Culture en-US

4. 生成配置文件目录, 可以通过命令查看
    $PROFILE

5. 使用命令设置主题
    Set-Theme paradox
        Agnoster
        Avit        (这个主题有两行)
        Darkblood
        Fish
        Honukai
        Paradox
        PowerLine
        robbyrussell
        Sorin
        tehrob

6. 安装Gow可以执行Linux命令
    choco install gow
```

#####  删除win10预览版水印

```
Universal Watermark Disabler
```

##### Microsoft Stroe

```
quickLook              	空格浏览文件
EarTrumpet	系统和应用声音单独控制
Snipaste		截屏工具
TranslucentTB 汉化版 使任务栏透明
Fluent Terminal 终端
```

#####  visio 2019 激活方法

```
1.电脑新建一个记事本文件.txt（任何地方都可以）
2.复制下面代码到新建记事本文件.txt中，并保存
3.上述记事本文件.txt后缀成.bat 的Windows可执行脚本文件
4.直接右键使用【管理员权限身份】打开修改后的.bat文件
5.耐心等待一会，不要以为没有执行，等一会会有打印记录，激活成功。


@echo off
title Activate Microsoft Visio 2019&cls&echo ============================================================================&echo #Visio: Activating Microsoft software products for FREE without software&echo ============================================================================&echo.&echo #Supported products:&echo - Microsoft Visio Standard 2019&echo - Microsoft Visio Professional Plus 2019&echo.&echo.&(if exist "%ProgramFiles%\Microsoft Office\Office16\ospp.vbs" cd /d "%ProgramFiles%\Microsoft Office\Office16")&(if exist "%ProgramFiles(x86)%\Microsoft Office\Office16\ospp.vbs" cd /d "%ProgramFiles(x86)%\Microsoft Office\Office16")&cscript //nologo ospp.vbs /inslic:"..\root\Licenses16\pkeyconfig-office.xrm-ms" >nul&(for /f %%x in ('dir /b ..\root\Licenses16\client-issuance*.xrm-ms') do cscript ospp.vbs /inslic:"..\root\Licenses16\%%x" >nul)&(for /f %%x in ('dir /b ..\root\Licenses16\visioprovl_kms*.xrm-ms') do cscript ospp.vbs /inslic:"..\root\Licenses16\%%x" >nul)&(for /f %%x in ('dir /b ..\root\Licenses16\visiopro2019vl_kms*.xrm-ms') do cscript ospp.vbs /inslic:"..\root\Licenses16\%%x" >nul)&echo.&echo ============================================================================&echo 正在尝试激活...&cscript //nologo ospp.vbs /unpkey:7VCBB >nul&cscript //nologo ospp.vbs /inpkey:9BGNQ-K37YR-RQHF2-38RQ3-7VCBB >nul&set i=1
:server
if %i%==1 set KMS_Sev=kms8.MSGuides.com
if %i%==2 set KMS_Sev=kms9.MSGuides.com
if %i%==3 set KMS_Sev=kms7.MSGuides.com
if %i%==4 goto notsupported
cscript //nologo ospp.vbs /sethst:%KMS_Sev% >nul&echo ============================================================================&echo.&echo.
cscript //nologo ospp.vbs /act | find /i "successful" && (echo 已完成，按任意键退出) || (echo 连接KMS服务器失败! 试图连接到另一个… & echo 请等待... & echo. & echo. & set /a i+=1 & goto server)
pause >nul
exit
```

##### 系统美化

```

```

##### 删除VS2017右键菜单 在Visual Studio中打开

```
新建记事本 xxx.reg

Windows Registry Editor Version 5.00
[-HKEY_CLASSES_ROOT\Directory\Background\shell\AnyCode]
[-HKEY_CLASSES_ROOT\Directory\shell\AnyCode]
```

##### 完全卸载

```
1. 使用安装文件安装, 在选择的时候将所有的文件选择为 "uninstall"
2. 创建安.bat脚本删除其他的文件, DIRECTORY_NAME 设置成实际安装的目录

SET DIRECTORY_NAME="C:\cygwin64"
C:\windows\system32\TAKEOWN /f %DIRECTORY_NAME% /r /d y
C:\windows\system32\ICACLS %DIRECTORY_NAME% /grant administrators:F /t
PAUSE

```

## 效率软件

##### wox

```
快速启动

github: https://github.com/Wox-launcher/Wox/releases

使用: https://zhuanlan.zhihu.com/p/68383315/
```

##### LoveString

```
字符编码转换，在Text段输入文字，各种编码就都能看到了。各个编码框也可以输入，用来调试乱码问题很方便。比如你看到一段乱码 浣犲ソ锛屼笘鐣? ，把它拷到Text输入框，你发现Ansi段的编码不像GBK，倒像是utf-8，然后把Ansi里的内容拷出来粘到utf-8，马上就能发现这段乱码的错误原因。要是用python查这个乱码，还要写好几行呢，用LoveString，拷一拷，粘一粘，搞定   
```

##### rapidee

```
环境变量管理工具

官网: https://www.rapidee.com/en/about

RapidEEx64.zip
```

##### Procmon

```
监视Windows系统里程序的运行情况

官网: https://docs.microsoft.com/en-us/sysinternals/downloads/procmon

ProcessMonitor.zip
```

##### OpenedFilesView

```
列出所有被操作系统或是应用程序打开的文件

下载地址: 
https://www.nirsoft.net/
https://www.nirsoft.net/utils/opened_files_view.html

ofview-x64.zip
```

##### FastStoneImageViewer

```
图片查看工具

下载地址: https://faststone-image-viewer.en.softonic.com/
```

##### 浏览器插件

```
Website IP 
查看访问网页的ip
```

