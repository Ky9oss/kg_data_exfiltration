import ftplib
import os
import socket
import win32file

def plain_ftp(filepath, server):
    ftp = ftplib.FTP(server)
    ftp.login("", "")

    # 定位目标目录
    ftp.cwd('/pub/')
    
    # 把文件写入目标目录
    ftp.storbinary("STOR " + os.path.basename(filepath), open(filepath, "rb"), 1024)

    ftp.quit()


def plain_ftp_windows(filepath):
    # 创建socket连接数据将要发送的主机的端口
    client = socket.socket()
    client.connect(("", ))

    # 使用win32file传送文件
    with open(filepath, 'rb') as t:
        win32file.TransmitFile(
                client,
                win32file._get_osfhandle(f.fileno()),
                0, 0, None, b'', b''
                )
