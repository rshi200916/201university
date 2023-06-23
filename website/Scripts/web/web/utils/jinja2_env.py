from jinja2 import Environment
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
# 确保在模板中使用模板语言以{{urls('请求路径')}}， {{static（'静态文件路径'）}}
def environment(**options):
    env=Environment(**options)
    env.globals.update({
        'static':staticfiles_storage.url,
        'url':reverse,
    })
    return env