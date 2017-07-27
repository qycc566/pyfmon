#!/usr/bin/python
# coding: utf8
# Created by qyc on 2017/7/26


from __future__ import unicode_literals, absolute_import
import os
from hashlib import md5


class node(object):
    """
    节点描述
    """
    # 父节点，当为根节点时parent的值为None
    parent = None
    # 子节点
    children = []

    def __init__(self, name):
        """
        构造函数
        :param name: 节点名称 
        """
        self.name = name

    def getPath(self, path_sp='/'):
        """
        获得路径
        :param path_sp:路径分割符 
        :return: 路径
        """
        if not isinstance(path_sp, str) and  not isinstance(path_sp, unicode):
            raise TypeError(message="path_sp必须为字符串类型")
        n = self.parent
        l = []
        l.append(self.name)
        while n is not None:
            l.append(n.name)
            n = n.parent
        l.reverse()
        p = path_sp.join(l)

    def new_child(self, child_name):
        """
        添加一个子节点
        :param child_name: 子节点名称 
        :return: None
        """
        c = node(child_name)
        c.parent = self
        self.children.append(c)

    def isdir(self, path_sp='/'):
        """
        判断节点是否是一个目录
        :param path_sp: 路径分割符 
        :return: boolean
        """
        p = self.getPath(path_sp=path_sp)
        return os.path.isdir(p)

    def isfile(self, path_sp='/'):
        """
        判断节点是否是一个文件
        :param path_sp: 路径分割符 
        :return: boolean
        """
        p = self.getPath(path_sp=path_sp)
        return os.path.isfile(p)

    def get_hash(self, path_sp='/'):
        mp = md5(self.getPath(path_sp=path_sp)).hexdigest()
        if self.isdir(path_sp=path_sp):
            """是目录，返回路径的MD5"""
            return mp, None
        elif self.isfile(path_sp=path_sp):
            """是文件"""
            if os.access(self.getPath(path_sp), os.F_OK):
                with open(self.getPath(path_sp)) as fp:
                    m = md5(fp.read()).hexdigest()
                    fp.close()
                return mp, m








