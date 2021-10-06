import sensorsanalytics
import datetime


def test_1():
    # 1. 初始化 ConsoleConsumer, 有多种类型, 根据实际的需要选择
    consumer = sensorsanalytics.ConcurrentLoggingConsumer('/home/glfadd/Desktop/logs')
    # consumer = sensorsanalytics.DefaultConsumer(url_prefix='http://10.120.231.241:8106/log_agent', request_timeout=10)
    # consumer = sensorsanalytics.DebugConsumer(url_prefix='http://10.120.231.241:8106/log_agent', write_data=True, request_timeout=None)

    # 2. 使用 Consumer 来构造 SensorsAnalytics 对象
    sa = sensorsanalytics.SensorsAnalytics(consumer)

    # 设置
    distinct_id = '2'
    event_name = 'login'
    properties = {
        '$time': datetime.datetime.now(),
        'ProductId': '123457',
        'ProductCatalog': 'Laptop Computer',
        'IsAddedToFav': True,
    }

    # 跟踪一个用户的行为
    sa.track(distinct_id=distinct_id, event_name=event_name, properties=properties, is_login_id=False)

    event_name_list = ['login', 'home_page', 'item_detail', 'item_detail_update']
    for i in range(2):
        # for i in range(20, 50):
        distinct_id = str(i)
        for j in event_name_list:
            properties = {
                '$time': datetime.datetime.now() - datetime.timedelta(hours=i),
                'ProductId': '123457' + str(i),
                'ProductCatalog': 'Laptop Computer',
                'IsAddedToFav': True,
            }
            sa.track(distinct_id=distinct_id, event_name=j, properties=properties, is_login_id=False)


if __name__ == '__main__':
    test_1()
