""" ============================ 复制
如果主从服务器之间的网络带宽不足, 或者主服务器没有足够的内存来创建子进程和创建记录写命令的缓冲区，那么Redis 处理命令请求的效率就会受到影响。
最好还是让主服务器只使用50%~ 65%的内存，留下30%~ 45%的内存用于执行BGSAVE命令和创建记录写命令的缓冲区。
从服务器在与主服务器进行初始连接时，数据库中原有的所有数据都将丢失，并被替换成主服务器发来的数据。
同时使用复制和AOF持久化将数据持久化到多台机器上面

从服务器连接主服务器步骤
  步骤     主服务器操作                                                                  从服务器操作
  1       (等待命令进入)                                                                连接主服务器, 发送SYNC命令
  2       开始执行bgsave, 并使用缓冲区记录bgsave之后执行的所有命令                          根据配置选项决定是否继续使用现有的数据处理客户端的命令请求, 还是想发送请求的客户端返回错误
  3       bgsave执行完毕向从服务器发送快照文件, 期间继续使用缓冲区记录被执行的写命令           丢弃所有旧数据, 载入主服务器发来的快照文件
  4       快照文件发送完毕, 开始向从服务器发送存储的缓冲区里的写命令                          完成快照文件解释操作, 并开始接收命令请求
  5       缓冲区存储的写命令发送完毕, 从现在开始每执行一个写命令就向从服务器发送相同的命令       执行主服务器发来的所有缓冲区里面的写命令. 从现在开始接收并执行主服务器传来的每个写命令

主从链
  - 从服务器也可以有从服务器
  - 从服务器对从服务器复制和从服务器对主服务器复制唯一区别在于, 如果从服务器X拥有从服务器Y, 那么当从服务器X在执行表步骤4时，它将断开与从服务器Y的连接，导致从服务器Y需要重新连接并重新同步
"""

""" ============================ Redis 有哪些架构模式
单机版: 内存容量有限, 处理能力有限, 无法高可用
主从复制
"""

""" ============================ 短结构
短结构, 分片结构, 打包存储二进制和字节
"""

""" ============================ 命令 字符串
set k v
get k
del k

incr k                  值自增1
decr k                  值自减1
incrby k n              值加n
decrbu k n              值减n
incrbyfloat k n         值加浮点n

append k v              值末尾追加字符串
getrange k start end    获取start和end之间字符
setrange k start v      从start开始替换为v
getbit
setbit
bitcount
bitop

* 对不存在的值进行自增/自减, 会将这个值当0处理
* 对无法解释为整数/浮点的字符串自增/自减返回错误
"""

""" ============================ 命令 列表
lpush k v1 v2           左边添加多个元素
rpush k v1 v2           右边添加多个元素
lpop k
rpop k
lindex k v              获取指定位置上一个元素
lrange k start end      获取指定范围所有元素
ltrim k start end       只保留start和end及之间的元素  

blpop k timeout         从第一个非空列表中弹出最左边元素, 或timeout内等待可弹出的元素出现                   
brpop                                        右
rpoplpush k1 k2         弹出k1最右边, 推入k2最左, 并获取这个元素
brpoplpush k1 k2 timeout弹出k1最右边, 推入k2最左, 并获取这个元素, 如果k1位空则阻塞timeout直到元素出现
"""

""" ============================ 命令 集合
sadd k v1 v2            添加1个/多个元素, 获取不存在新增加的个数        
srem k v1 v2            删除1个/多个元素, 获取删除的个数
scard k                 获取元素个数
smembers k              获取所有元素
sismember k v           是否包含元素v
srandmember k count     随机获取count个元素, 当count为正数时元素不重复, 负数时可以重复
spop k                  随机移除一个元素并获取元素
smove k1 k2 v           如果k1有元素v则移动到k2则
"""

""" ============================ 命令 散列
hset k1 k2 v
hget k1 k2
hdel k1 k2
hgetall k1              获取所有键值对
hmget K k1 k2           获取1个/多个键的值
hmset K k1 v1 k2 v2     添加1个/多个值
hdel K k1 k2            获取成功删除的数量
hlen K                  获取键值对的数量
hexists K k             查看k是否存在
hkeys K k               删除
hvals K                 获取所有值
hgetall K               获取所有键值对
hincrby K k count       值加上count
hincrbyfloat K k count  值加上count 浮zrange点
"""

""" ============================ 命令 有序集合
有序集合
zadd k s1 v1 s2 v2      将分数s1 s2和元素添加到集合
zrem k v1 v2            移除元素, 并获取成功的数量            
zcard k                 获取元素数量
zincrby k count v       v的分数增加count
zcount k s1 s2          获取分数s1和s2之间元素数量
zrank k v               获取元素的排名
zscore k v              获取元素的分值
zrange k start stop [withscores]    返回排名start和stop之间的成员, 如果有withscores则一起返回分数
"""
