#!/usr/bin/python
# coding: utf8
# Created by qyc on 2017/7/26


from __future__ import unicode_literals, absolute_import
import os
import errors

class WalkMan(object):
    """
    用于目录、文件的扫描器
    """
    def __init__(self, entry):
        """
        构造函数
        :param entry: 扫描入口目录 
        """
        self.entry = entry
        if not os.access(self.entry, os.F_OK):
            raise errors.FileNotFoundException(self.entry)
        if not os.path.isdir(self.entry):
            raise errors.NotDirectoryException(self.entry)
        self.walk_man = os.walk(self.entry)

    def step(self):
        """
        取出目录下的父目录名、子目录、文件名列表
        :return: (父目录 str，子目录[]，文件[])
        """
        return self.walk_man.next()

    def rush(self):
        """
        取出目录下的所有目录名与文件名清单
        :return: (目录列表[], 文件列表[])
        """

