# import socket
# sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# sock.connect(("www.baidu.com",80))
# sock.send(b"GET / HTTP/1.1\r\nHOST:www.baidu.com\r\nConnection:close\r\n\r\n")
# buffer=[]
# while True:
#     content=sock.recv(1024)
#     if content:
#         buffer.append(content)
#     else:
#         break
# web_content=b"".join(buffer)
# print(web_content)
# http_header,http_content=web_content.split(b"\r\n\r\n",1)
# with open("baidu.html","wb")as f:
#     f.write(http_content)
# from urllib import request
# def fetch_baidu():
#     http_client=request.urlopen("http://www.baidu.com")
#     content=http_client.read()
#     print("HTTP Status: {}, {}",format(http_client.status,http_client.reason))
#     print("HTTP Resoponse headers:")
#     for k,v in http_client.getheaders():
#         print("{}:{}".format(k,v))
#     http_client.close()
#     return content.decode("utf-8")
# def save_page(content):
#     with open("baidu.html","w",encoding="utf-8")as f:
#         f.write(content)
# def main():
#     content=fetch_baidu()
#     save_page(content)
# if __name__=="__main__":
#     main()