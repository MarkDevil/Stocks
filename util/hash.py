# coding=utf-8

import hashlib


# 获取文件md5值
def get_file_md5(f):
    """
    :param f:
    :return: str
    """
    m = hashlib.md5()  # type: hashlib.md5
    assert isinstance(m, hashlib.md5)
    while True:
        data = f.read(1024)
        if not data:
            break
        m.update(data)
    return m.hexdigest()


def get_file_sha1(f):
    """
    :param f:
    :return: str
    """
    m = hashlib.sha1()  # type: hashlib.sha1
    assert isinstance(m, hashlib.sha1)
    while True:
        data = f.read(1024)
        if not data:
            break
        m.update(data)
    return m.hexdigest()


if __name__ == '__main__':
    with open('logutil.py') as f:
        print ("Orignal: \t" + get_file_sha1(f))
        print ("Orignal: \t" + get_file_md5(f))

    # with open('logutil.py', 'wb+') as f:
    #     f.write("mark")
    #     # print (get_file_md5(f))

    with open('logutil.py') as f:
        print ("New: \t" + get_file_sha1(f))
        print ("New: \t" + get_file_md5(f))
