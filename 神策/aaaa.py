import sensorsanalytics

# 初始化一个 Consumer，用于数据发送
# ConcurrentLoggingConsumer 是将数据写在日志文件中，再利用神策提供的 LogAgent 工具发送数据
consumer = sensorsanalytics.ConcurrentLoggingConsumer('/home/glfadd/Desktop/logs/a.log')
# 使用 Consumer 来构造 SensorsAnalytics 对象
sa = sensorsanalytics.SensorsAnalytics(consumer)

# 记录用户登录事件
distinct_id = 'ABCDEF123456789'
sa.track(distinct_id, 'UserLogin', is_login_id=True)

# 上报所有缓存数据，测试时可以调用调试数据，线上环境一般可以不调用
sa.flush()

sa.close()