"""
拼写的 shell 命令字符串的换行和 # 是否在行首会影响发送的命令能否被正常解析
"""
import os
import random
import time

command = """
cat <<EOF | curl --data-binary @- http://localhost:9091/metrics/job/redis_custom/instance/check_key
    # HELP redis_key_101 监控 redis key 的长度
    # TYPE redis_key_101 gauge
    redis_key_101 %s
    # HELP redis_key_102 监控 redis key 的长度
    # TYPE redis_key_102 gauge
    redis_key_102 %s
EOF
"""
for i in range(3000000):
    a = random.randint(10, 320)
    b = random.randint(200, 220)
    cc = os.system(command % (a, b))
    print(i)
    print(cc)
    time.sleep(3)
