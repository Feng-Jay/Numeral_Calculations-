#coding:utf-8
from websocket_server import WebsocketServer 
import xlrd
import os
import logging

count = 1
data = xlrd.open_workbook(os.path.join('C:/Users/DELL/Desktop/', 'pop.xls'))
table = data.sheets()[0]

def startWebsocketServer():
    def new_client(client, server):
        # server.send_message_to_all("Hey all, a new client has joined us")
        return 

    def mysend(client,server,msg):
        global count
        print(msg)
        shuju =' '
        shuju1 = table.row_values(count)
        # del shuju1[1:2]
        # print(shuju1)
        shuju += str(shuju1[0])+ ','
        shuju += str(shuju1[1])
        server.send_message(client,shuju+',118,30')
        count += 1
        if(msg == "_end"):         #如果收到了_end 消息，那么断开连接
            server.server_close()

    server = WebsocketServer(port = 5005, host='127.0.0.1', loglevel=logging.INFO)
    server.set_fn_new_client(new_client)
    server.set_fn_message_received(mysend)
    server.run_forever()
    server.server_close()

if __name__ == "__main__":
    startWebsocketServer()