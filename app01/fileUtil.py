import uuid
import Ad.settings as settings
import os
from PIL import Image

def article_dir_path(article,file):
    if file: 
        filename = file.name
        ext = filename.split('.')[-1]
        filename = '{}.{}'.format(uuid.uuid4().hex[:8], ext)
        dirPath = os.path.join(settings.STATICFILES_DIRS[0],'article','img' ,article.title)
        dirPath = "".join(dirPath.split())
        if not os.path.isdir(dirPath):
            os.makedirs(dirPath)
        imgpath = os.path.join(dirPath, filename)
        img = Image.open(file)
        try:
            img.save(imgpath) #路径(绝对/相对)
            print('保存了图片')
        except:
            pass
    return "/{0}/{1}/{2}/{3}/{4}".format('static','article','img' ,"".join(article.title.split()),  filename)



