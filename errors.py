#!/usr/bin/python
# coding: utf8
# Created by qyc on 2017/7/26


from __future__ import unicode_literals, absolute_import
import exceptions as exs


class FileNotFoundException(exs.Exception):
    """
    文件、目录没有找到异常
    """

    def __init__(self, filename):
        """
        构造函数
        :param filename: 引发异常的目录/文件名 
        """
        self.file = filename
        self.msg = '目录/文件: %s 没有找到' % filename


class NotDirectoryException(exs.Exception):
    """
    不是目录的异常
    """
    def __init__(self, filename):
        """
        构造函数
        :param filename: 引发异常的目录/文件名 
        """
        self.file = filename
        self.msg = '%s 不是目录' % filename
