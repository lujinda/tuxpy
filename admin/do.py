#!/usr/bin/env python
#coding:utf8
# Author          : tuxpy
# Email           : q8886888@qq.com
# Last modified   : 2014-12-24 15:50:03
# Filename        : admin/do.py
# Description     : 
from data import db
from page.do import deal_blog
import urllib
import time
from bson import binary
import re

def get_tag_list():
    return db.tag.find()

def get_sort_page_count(uuid):
    return db.blog.find({'sort': uuid}).count()


def get_sort_list():
    sort_list = []
    for sort in db.sort.find():
        del sort['_id']
        sort['count'] = get_sort_page_count(sort['uuid'])
        sort_list.append(sort)
    return sort_list

def get_uuid(): 
    import uuid
    import base64
    return base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes).replace('+', 'A')

def del_sort(uuid):
    db.sort.remove({'uuid':uuid})
    return '已成功执行删除操作'

# 用来判断类名或类别名有没有重复的
def sort_isexist(value):
    return db.sort.find_one({"$or":[{'name':value}, {'alias':value}]})

def add_sort(name, alias):
    if not (name and alias):
        return '请不要有空的信息'
    
    if not re.search(r'^\w+$', alias):
        return '别名只能由字母，数字，下划线组成'

    if sort_isexist(name) or sort_isexist(alias):
        return '分类名，别名不能与已存在的相同'

    db.sort.insert(dict(uuid=get_uuid(),
        name=name, alias=alias
        ))
    return u'%s 分类创建成功' % (name, )


def set_sort(uuid, value, t):
    if not value:
        return '内容不能为空'
    if sort_isexist(value):
        return '内容不能重复'
    db.sort.update({'uuid':uuid},
            {"$set":{t: value}}, False, True)
    return '更新成功'
    

def enc_password(password):
    import hashlib
    m = hashlib.md5()
    m.update(password)
    return m.hexdigest()

# 传入密码已经经过md5加密
def check_user_pass(user, pwd):
    if db.users.find_one({'username':user,
        'password':pwd}):
        return True
    return False

def change_user_pass(user, pwd):
    db.users.update({'uid':0},
            {"$set":{'username':user, 'password':pwd}})


def upload_file(filename, body):
    url_filename = time.strftime('%Y%m%d%H%M%s') + '_' + filename
    file_obj = dict(url_filename = url_filename,
        body = binary.Binary(body),
        upload_time = str(time.time()))
    db.files.insert(file_obj)

    return '/files/%s' % (url_filename,)


def write_tag(uuid, tag, old_tag): # tag是指用户传入的标签
    deleted_tag = list(set(old_tag) - set(tag)) # 算出有哪些标签，被删掉了
    for t in deleted_tag: # 在被去掉的标签中，删除日志uuid
        db.tag.update({'name':t},
                {"$pull":{"b_uuid":uuid}}
                )

    for t in list(set(tag) - set(old_tag)): # 那些没有改动的标签就不需要再添加它了
        if db.tag.find_one({'name':t}):
            db.tag.update({'name': t},
                {"$addToSet":{"b_uuid":uuid}})
        else:
            db.tag.insert({'name':t,'b_uuid':[uuid]})

def write_blog(**blog):
    old_tag = blog.pop('old_tag')
    if not blog['uuid']: # 如果没有uuid，则表示是新的
        blog['reply'] = []
        blog['view'] = 0
        blog['uuid'] = get_uuid()
        blog['date'] = str(time.time())
        blog['password'] = ''
        db.blog.insert(blog)
    else:
        db.blog.update({'uuid': blog['uuid']},
                {"$set": blog})
    
    write_tag(blog['uuid'], blog['tag'], old_tag)


def del_blog(blog_uuid):
    db.blog.remove({'uuid': blog_uuid})

def move_blog(blog_uuid, sort_uuid):
    db.blog.update({'uuid': blog_uuid}, 
            {"$set":{'sort':sort_uuid}})
    
def top_blog(blog_uuid):
    db.blog.update({'uuid': blog_uuid},
            {"$set":{'is_top': '1'}}
            )

def notop_blog(blog_uuid):
    db.blog.update({'uuid': blog_uuid},
            {"$set":{'is_top': ''}}
            )
       

def write_nav(No, name, url, uuid=''):
    if not (name and url):
        return 
    if not uuid:  # 当导航是添加，而不是编辑时
        db.nav.insert({'uuid':get_uuid(),
            'No':No, 'name':name, 'url': url,
            'is_display':1})
        
        return '添加成功'
        
def get_nav_list():
    return db.nav.find().sort([('No', 1)])
    
def del_nav(uuid):
    db.nav.remove({'uuid':uuid.replace(' ', '+')})

# 切换导航的显示状态
def switch_nav(uuid):
    db.nav.update({'uuid':uuid}, {"$set":{'is_display':
        abs(1 - db.nav.find_one({'uuid': uuid})['is_display'])
        }})

# 修改导航的序号
def order_nav(uuid, No):
    db.nav.update({'uuid':uuid}, {"$set":{'No':int(No)}})

