'''服务器端'''

import socket
import threading
import os
import json
import struct
from socketdata import sd

print('Server start to prepare ...')

host = '0.0.0.0'
port = 1025

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(5)

print('Server Open Successfully ...\nhost:%s\nport:%s'%(host,port))

'''
#data用于获得数据
data =None
filePath = 'F:/img/'
buffsize = 1024

#创建套接字
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#获得本地主机名
hostname = socket.gethostname()
host = '0.0.0.0'
port = 1025
s.bind((host, port))
#设置连接数，超过排队
s.listen(5)
print('本地主机为：'+host+'\n端口：'+'%s'%port)
print('服务器启动成功...')



#接收数据的函数
def tcps(sock, addr):
    #进入死循环，永不退出
    try:
        while True :
            #接收报头大小
            fileinfo_len = struct.unpack(s.recv(4))[0]
            s.send(fileinfo_len)
            fileinfo = s.recv(fileinfo_len)
            s.send(fileinfo)
            filename = filePath + filename
            filesize_b = fileinfo['filesize']
            print(fileinfo['filename'])
            print(fileinfo['filesize'])
            #接收文件
            recv_len = 0
            recv_mesg = b''
            f = open(filename, 'wb')
            while recv_len < filesize_b:
                percent = recv_len / filesize_b

                if filesize_b - recv_len > buffsize:

                    recv_mesg = s.recv(buffsize)
                    f.write(recv_mesg)
                    recv_len += len(recv_mesg)
                else:
                    recv_mesg = s.recv(filesize_b - recv_len)
                    recv_len += len(recv_mesg)
                    f.write(recv_mesg)

    except :
        print('%s异常退出！'%sock)
'''
def tcps(sock,addr):
    her = s.recv(1024)
    print(her.decode('utf-8'))

while True:
    sock, addr = s.accept()
    t = threading.Thread(target=tcps, args=(sock, addr))
    print('Open a new thread \n%s'%t)
    t.start()


