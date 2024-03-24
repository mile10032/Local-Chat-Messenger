import socket
import os
from faker import Faker

faker = Faker()
sock = socket.socket(socket.AF_UNIX,socket.SOCK_STREAM)

server_address = '/tmp/socket_file'


try:
    os.unlink(server_address)


except FileNotFoundError:
    pass

print('Starting up on {}'.format(server_address))


#ソケットに接続
sock.bind(server_address)

#1はソケットが同時に受け入れ可能な未処理の接続要求の数
sock.listen(1)

while True:
    # クライアントからの接続を受けとり。
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        while True:
            #データを読み込み
            # 16という数字は、一度に読み込むデータの最大バイト数
            data = connection.recv(16)

            # 受け取ったデータはバイナリ形式なので、それを文字列に変換
            data_str =  data.decode('utf-8')

            # 受け取ったデータを表示
            print('Received ' + data_str)
            ＃データをうけとったら
            if data:
                # 受け取ったメッセージを処理
                fake_message = faker.text(max_nb_chars=200)
                response = 'Fake Data: ' + fake_message

                # 処理したメッセージをクライアントに送る
                connection.sendall(response.encode())

            # クライアントからデータが送られてこなければ、終了
            else:
                print('no data from', client_address)
                break
    finally:
        print("Closing current connection")
        connection.close()
