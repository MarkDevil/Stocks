# coding=utf-8
# coding = utf-8
# !/usr/bin/python


class FileParser(object):

    def __init__(self):
        pass

    """
        读取配置文件
        :type properties文件对应 p
              xml文件对应 xml
    """

    def readfile(self, type, inpath):
        # type: (object, object) -> object
        kv = {}
        with open(inpath, mode='rw') as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith('#') or line.startswith("\n"):
                    continue
                line.strip('\n')
                arrays = line.split("=")
                print(arrays)
                key = arrays[0]
                value = arrays[1]
                kv.__setitem__(key, value)
            print(kv)
            return kv

    """
        写出文件到指定位置
    """

    def writefile(self, outpath, contents):
        with open(outpath, mode='w') as out:
            for line in contents:
                out.write(str(line) + '=' + str(contents[line]))
                out.write('\n')

    """
        修改指定文件中的
    """
    def modifyvalue(self, inpath, kvs):
        confs = self.readfile('p', inpath)
        if kvs is not None or kvs is not '':
            for kv, val in kvs.iteritems():
                if confs.has_key(kv):
                    confs[kv] = val
            print(confs)
            self.writefile(inpath, confs)


if __name__ == '__main__':
    newDict = {'dubbo.registry.address': 'marktest', 'dubbo.consumer.check': 'true',
               'dubbo.registry.file': './hb_approval_dubbo.cache'}
    fp = FileParser()
    content = fp.readfile('p', '../resource/test.properties')
    fp.modifyvalue('../resource/test.properties', newDict)
