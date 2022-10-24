from qiniu import Auth, put_file, etag
from swiper import config
from worker import call_by_worker
import os


def upload_to_qiniu(localfile, upload_name, expired=3600):
    """
    :param localfile: 要上传文件的本地路径
    :param upload_name: 上传后保存的文件名
    :param expired: 文件过期时间
    """
    # 构建鉴权对象cd
    q = Auth(config.QN_ACCESS_KEY, config.QN_SECRET_KEY)
    # 生成上传 Token，可以指定过期时间等
    token = q.upload_token(config.QN_BUCKET_NAME, upload_name, expired)
    ret, info = put_file(token, upload_name, localfile, version='v2')
    print(ret, info)
    assert ret['key'] == upload_name
    assert ret['hash'] == etag(localfile)
    if os.path.exists(localfile): os.remove(localfile)


# 呼async_upload_to_qiniu异步执行upload_to_qiniu函数
async_upload_to_qiniu = call_by_worker(upload_to_qiniu)

