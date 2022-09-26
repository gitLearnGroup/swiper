# Broker settings.
broker_url = 'redis://127.0.0.1:6379/0'
broker_pool_limit = 1000
timezone = 'Asia/Shanghai'
accept_content = ['pickle', 'json']
task_serializer = 'pickle'

result_backend = 'redis://127.0.0.1:6379/0'
result_serializer = 'pickle'
result_cache_max = 10000  # 任務結果最大存儲量
result_expires = 3600  # 設置過期時長

worker_redirect_stdouts_level = 'INFO'
