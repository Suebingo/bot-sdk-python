#!/usr/bin/env python3
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/1/5

"""
    desc:pass
"""


class Utils:

    @staticmethod
    def checkKeyInDict(dicts, key):
        '''
        校验字典中是否存在指定的key
        :param dicts:
        :param key:
        :return:
        '''
        if isinstance(dicts, dict):
            return key in dicts
        return False

    @staticmethod
    def checkKeysInDict(dicts, keys):

        if isinstance(dicts, dict):
            for key in keys:
                if key in dicts:
                    dicts = dicts[key]
                    continue
                return False

    @staticmethod
    def getDictDataByKey(dicts, key):
        tmp = dicts
        for k, v in tmp.items():
            if k == key:
                return v
            else:
                if isinstance(v, dict):
                    ret = Utils.getDictDataByKey(v, key)
                    if isinstance(ret, str):
                        return ret
        pass

    @staticmethod
    def getDictDataByKeys(dicts, keys):
        if isinstance(dicts, dict):
            for key in keys:
                if key in dicts:
                    v = dicts[key]
                    if isinstance(v, dict):
                        dicts = v
                        continue
                    elif isinstance(v, str):
                        return v


if __name__ == '__main__':
    dicttest = {"result": {"code": "110002", "msg": "设备设备序列号或验证码错误"}}
    ret = Utils.getDictDataByKey(dicttest, 'msg2')
    print(ret)

    print(Utils.getDictDataByKeys(dicttest, ['result', 'code', ]))
    pass