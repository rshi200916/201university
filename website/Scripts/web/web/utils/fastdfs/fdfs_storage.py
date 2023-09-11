import logging

from django.conf import settings
from django.core.files.storage import Storage
from django.utils.deconstruct import deconstructible
from fdfs_client.client import get_tracker_conf, Fdfs_client
import os

log = logging.getLogger('django')


@deconstructible
class FastDFSStorage(Storage):
    def __init__(self,base_url=None, client_conf= None):
        if base_url is None:
            base_url = settings.FDFS_URL
        self.base_url = base_url
        if client_conf is None:
            client_conf = settings.FDFS_CLIENT_CONF
        self.client_conf = client_conf

    def _open(self):
        pass

    def _save(self, name, content):
        conf_path = get_tracker_conf(self.client_conf)

        client = Fdfs_client(conf_path)
        # client = Fdfs_client(r'D:\马氏兵\Git\work\201university\website\Scripts\web\web\utils\fastdfs\client.conf')
        # imgdir = os.path.join(settings.BASE_DIR,"utils/fastdfs/picture.png")
        # if not os.path.exists(imgdir):
        #     os.makedirs(imgdir)
        # os.remove(imgdir)

        file_data = content.read()# 读取文件内容

        try:
            result = client.upload_by_buffer(filebuffer=file_data)
        except Exception as e:
            print(e)
            raise
        if result.get('Status') != 'Upload successed.':
            logging.error('上传文件到FastDFS失败')
            raise Exception('上传文件到FastDFS失败')
        filename = result.get('Remote file_id')

        return filename.decode()

    def url(self, name):

        return self.base_url + name

    def exists(self, name):

        return False
        """
        判断文件是否存在，FastDFS可以自行解决文件的重名问题
        所以此处返回False，告诉Django上传的都是新文件
        :param name:  文件名
        :return: False
        """
