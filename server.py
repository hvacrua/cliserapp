import socket

# Определить сокет сервера
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Привязка адреса и порта localhost
server.bind(('127.0.0.1', 50000))
# Слушать до 5 соединений
server.listen(5)
print(f'\nChat is started!\n')
# accept получит запрошенный адрес, порт и вернет новый сокет,
# Если на сервере три клиентских соединения, т.е. четыре сокета, один из которых является только что созданным сокетом
conn, addr = server.accept()
# Запустим бесконечный цикл
while True:
    # Размер получаемой информации 1024 байта
    data = conn.recv(1024).decode('utf-8')
    # Условие, если получено "q", то выйдет из цикла и закроет сокет
    if data == 'q':
        break
    # Если нет, распечатает декодированную информацию
    print(f'\nMessage from client: {data}\n')
    # Введите то, что сервер хочет ответить
    reply = input(f'\nReply from server: \n')
    # Используйте соответствующий сокет для отправки этого ответного сообщения
    conn.send(reply.encode('utf-8'))
# Закройте первый сокет
server.close()
# Закрыть вновь созданный сокет
conn.close()
