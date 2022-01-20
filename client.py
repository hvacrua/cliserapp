import socket

# Создать сокет клиента
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(('127.0.0.1', 50000))

while True:
    # Введите контент, который вы хотите отправить
    msg = input(f"\nYou said: ")
    # Кодировать последние отправленные сообщения
    client.send(msg.encode('utf-8'))
    # Условие для выхода из беконечного цикла
    if msg == 'q':
        break
    # Декодировать полученное сообщение
    back_msg = client.recv(1024).decode('utf-8')
    # Распечатать полученное сообщение
    print(f'Reply from server: {back_msg}')
# Закрыть созданный сокет
client.close()
