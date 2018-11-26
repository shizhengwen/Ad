import uuid
import Ad.settings as settings
import os
from PIL import Image
import shutil

def article_dir_path(article,file):
    if file: 
        filename = file.name
        ext = filename.split('.')[-1]
        filename = '{}.{}'.format(uuid.uuid4().hex[:8], ext)
        title = str(uuid.uuid5(uuid.NAMESPACE_DNS,article.title))
        title = ''.join(title.split('-'))
        dirPath = os.path.join(settings.STATICFILES_DIRS[0],'article','img' ,title)
        dirPath = "".join(dirPath.split())
        if not os.path.isdir(dirPath):
            os.makedirs(dirPath)
        imgpath = os.path.join(dirPath, filename)
        img = Image.open(file)
        try:
            img.save(imgpath) #路径(绝对/相对)
        except:
            pass
    return "/{0}/{1}/{2}/{3}/{4}".format('static','article','img' ,title,  filename)

def defFile(filepath):
    '''
            删除filepath目录
    '''
    title = filepath.split('/')[-2]
    dirPath = os.path.join(settings.STATICFILES_DIRS[0],'article','img' ,title)
    if  os.path.isdir(dirPath):
        shutil.rmtree(dirPath)
        return True




