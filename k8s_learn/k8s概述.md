```
https://blog.csdn.net/zzq900503/article/details/80668686

https://zhuanlan.zhihu.com/p/96908130
https://www.cnblogs.com/wwchihiro/p/9261607.html
```

##### 是什么

```
Kubernetes 是用来管理容器集群的平台
```

##### 特点

```
1、可移植: 支持公有云，私有云，混合云，多重云（multi-cloud）
2、可扩展: 模块化, 插件化, 可挂载, 可组合
3、自动化: 自动部署，自动重启，自动复制，自动伸缩/扩展
4、快速部署应用，快速扩展应用
5、无缝对接新的应用功能
6、节省资源，优化硬件资源的使用
```

##### 架构图

![Kubernetes架构图](./image/Kubernetes架构图.png)

```
1. Master Node: 作为控制节点，对集群进行调度管理, 由API Server、Scheduler、Cluster State Store和Controller-Manger Server所组成
2. Worker Node: 作为真正的工作节点，运行业务应用的容器, 包含kubelet、kube proxy和Container Runtime；
3. kubectl: 用于对 Kubernetes 下命令, 它通过 APIServer 去调用各个进程来完成对 Node 的部署和控制
4. Add-on: 是对Kubernetes核心功能的扩展
5. repliceation: 用于伸缩副本数量
6. endpoint: 用于管理网络请求
7. scheduler: 调度器
```



## kubernetes 相关概念

```
每个 Kubernetes 集群都由一个 Master 负责管理和控制集群节点, 通过 Master 对每个节点 Node 发送命令
Node 可以是一台机器或者一台虚拟机。
在 Node 上面可以运行多个 Pod，
Pod 是 Kubernetes 管理的最小单位，
每个 Pod 可以包含多个容器（Docker）



```



##### Pod

```
Pod是最小部署单元，一个Pod由一个或多个容器组成，Pod中容器共享存储和网络，在同一台Docker主机上运行。
每个Pod都会包含一个 “根容器”，还会包含一个或者多个紧密相连的业务容器。 
```

##### 标签和选择器

```
Kubernetes 客户端将称为“标签”的键值对附加到系统中的任何API对象，如pod和节点。相应地，“标签选择器”是针对匹配对象的标签的查询。

标签和选择器是Kubernetes中的主要分组机制，用于确定操作适用的组件。

例如，如果应用程序的Pods具有系统的标签 tier ("front-end", "back-end", for example) 和一个 release_track ("canary", "production", for example)，那么对所有"back-end" 和 "canary" 节点的操作可以使用如下所示的标签选择器：
tier=back-end AND release_track=canary 
```

##### 控制器

```
控制器是将实际集群状态转移到所需集群状态的对帐循环。它通过管理一组pod来实现。一种控制器是一个“复制控制器”，它通过在集群中运行指定数量的pod副本来处理复制和缩放。如果基础节点出现故障，它还可以处理创建替换pod。

其它控制器，是核心Kubernetes系统的一部分包括一个“DaemonSet控制器”为每一台机器（或机器的一些子集）上运行的恰好一个pod，和一个“作业控制器”用于运行pod运行到完成，例如作为批处理作业的一部分。控制器管理的一组pod由作为控制器定义的一部分的标签选择器确定。
```

## 核心组件

