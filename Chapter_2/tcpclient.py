import socket
target_host = "172.16.69.161"
target_port = 9996

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect((target_host,target_port))

#client.send("GET / HTTP/1.1\r\nHost:baidu.com\r\n\r\n".encode())
client.send("aaaaaacccc".encode())

response = client.recv(4096)

print(response)