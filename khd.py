'''客户端'''

import socket
import os
import json
import struct

filePath = 'F:/py/One/testfile/'
filenaem = 'F:/py/One/testfile/400.pcm'
#创建socket连接
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = '127.0.0.1'
port = 1025
s.connect((host,port))

#读取文件
def getFile(filename):
    with open(filenaem,'rb') as fp :
        return fp.read()

#发送文件
while True :
    print('开始')
    filesize = os.path.getsize(filenaem)
    data = getFile(filenaem)

    #发送文件表头
    print('发送文件表头')
    dirc = {
        filenaem :filenaem,
        filesize :filesize,
    }
    fileinfo = json.dumps(dirc)
    fileinfo_len = struct.pack('i',len(fileinfo))

    s.send(fileinfo_len)
    print(s.recv(1024))
    s.send(fileinfo.encode('utf-8'))
    print(s.recv(1024))

    #发送文件
    print('发送文件')
    s.sendall(data)

print('发送成功！')