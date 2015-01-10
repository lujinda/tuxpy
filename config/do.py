#!/usr/bin/env python
#coding:utf-8
from data import db
from admin.do import get_uuid

def create_new_sider(sider_name, sider_title, sider_description):
    db.sider.insert({'uuid': get_uuid(), 'sider_no': 0,
        'sider_name':sider_name, 'sider_title':sider_title,
        'sider_description':sider_description,
        'sider_show':1})

def update_sider_info(sider_name, **kwargs):
    db.sider.update({'sider_name': sider_name, '$nor':[{x:kwargs[x]} for x in kwargs]},
            {"$set": kwargs})

def remove_sider_info(sider_name):
    db.sider.remove({'sider_name': sider_name})

# 传入的是一个dict, 每个item 是sider name:sider_title
def update_sider(all_sider):
    old_sider_name_set = set([ x['sider_name'] for x in db.sider.find({}, {'sider_name':1})])
    new_sider_name_set = set(all_sider.keys())
    new_sider_name_list = new_sider_name_set - old_sider_name_set
    notexist_sider_name_list = old_sider_name_set - new_sider_name_set
    exist_sider_name_list = list(old_sider_name_set & new_sider_name_set)

    for sider_name in new_sider_name_list:
        sider_title, sider_description = all_sider[sider_name]
        create_new_sider(sider_name, sider_title, sider_description)

    # 把已经存在的做一次更新
    for sider_name in exist_sider_name_list:
        sider_title, sider_description = all_sider[sider_name]
        update_sider_info(sider_name, sider_title = sider_title, sider_description = sider_description)

    for sider_name in notexist_sider_name_list:
        remove_sider_info(sider_name)


        #if db.find_one({'sider_name': sider_name,
         #   'sider_title'})
    #print list(db.sider.find())
    
