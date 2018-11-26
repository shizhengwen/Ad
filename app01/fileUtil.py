import uuid
import Ad.settings as settings
import os
from PIL import Image
import shutil

def article_dir_path(article,file):
    '''
        保存上传的图片并返回图片url
    '''
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
        except Exception as e:
            print(e)
    return "/{0}/{1}/{2}/{3}/{4}".format('static','article','img' ,title,  filename)

def defFile(filepath):
    '''
            删除filepath目录
    '''
    try:
        title = filepath.split('/')[-2]
        dirPath = os.path.join(settings.STATICFILES_DIRS[0],'article','img' ,title)
        if  os.path.isdir(dirPath):
            shutil.rmtree(dirPath)
            return True
    except:
        pass

def editImg(host_url,article,file,oldimgurl):
    '''
        修改图片返回图片url
    '''
    title = str(uuid.uuid5(uuid.NAMESPACE_DNS,article.title))
    title = ''.join(title.split('-'))
    dirPath = os.path.join(settings.STATICFILES_DIRS[0],'article','img' ,title)
    if not os.path.isdir(dirPath):
        os.makedirs(dirPath)
    if file:
        if oldimgurl != '':
            filename = file.name
            ext = filename.split('.')[-1]
            filename = '{}.{}'.format(uuid.uuid4().hex[:8], ext)
            imgpath = os.path.join(dirPath, filename)
            img = Image.open(file)
            try:
                img.save(imgpath)
                oldimgurl = oldimgurl.replace(host_url,'')
                os.remove(oldimgurl)
            except Exception as e:
                print(e)
            filename = "/{0}/{1}/{2}/{3}/{4}".format('static','article','img' ,title,  filename)
        else:
            filename = article_dir_path(article,file)
        return filename
    else:
        return ''
        
    


