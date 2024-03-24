import socket
import os
import sys


# TCP/IPソケットを作成します。
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# サーバが待ち受けている特定の場所にソケットを接続します。
server_address = '/tmp/socket_file'
print('connecting to {}'.format(server_address))

message = input("サーバーに送る文字を入力してください").encode()

#サーバ接続
try:
    sock.connect(server_address)
except socket.error as err:
    print(err)

    sys.exit("サーバーに接続できません。")

#サーバーにメッセージ送信

try:
    sock.sendall(message)
    #2 wait session
    try:
        while True:
            data = str(sock.recv(32))
            if data:
                print("Server response: " + data)
            else:
                break
    
    except(TimeoutError):
        print("ソケットのタイムアウトです。")
finally:
    print("ソケットを終了します。")
    sock.close()

