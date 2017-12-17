#coding=utf-8
import sys
import socket
import getopt
import threading
import subprocess

listen = False
command = False
upload = False
execute = ""
target = ""
upload_desination = ""
port = 0

def main():
    global listen
    global port
    global execute
    global command
    global upload_desination
    global target
    if not len(sys.argv[1:]):
        print("no")
    try:
        opts,args=getopt.getopt(sys.argv[1:],"hle:t:p:cu",
                                ["help","listen","execute","target","port","command","upload"])
    except getopt.GetoptError as err:
        print str(err)
        print ("nono")

    for o,a in opts:
        if o in ("-h","--help"):
            print("hhh")
        elif o in ("-l","--listen"):
            listen = True
        elif o in ("-e","--excute"):
            execute=a
        elif o in ("-c","--command"):
            command =True
        elif o in ("-u","--upload"):
            upload_desination = a
        elif o in ("-t","--target"):
            target = a
        elif o in ("-p","--port"):
            port = int(8)
        else:
            assert False,"Unhandled Option"
    if not listen and len(target) and port>0:
        #从命令行读取内存数据
        buffer = sys.stdin.read()
        #发送数据
        client_sender(buffer)
        if listen:
            server_loop()
main()
def client_sender(buffer):
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
    # 连接到目标主机
        client.connect((target,port))
        if len(buffer):
            client_sender(buffer)
        while True:
            #现在等待数据回传
            recv_len=1
            response=""
            while recv_len:
                data = client.recv(4096)
                recv_len=len(data)
                response +=data;
                if recv_len<4096:
                    break
                print response,
                #等待更多输入
                buffer - raw_input()
                buffer+="\n"
                client.send(buffer)
    except:
        print "[*]Exception !"

    #关闭连接
    client.close()
def server_loop():
    global target
    #如果没有定义目标，那么我们监听所有的端口
    if not len(target):
        target="0.0.0.0"
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((target,port))
    server.listen(5)
    while True:
        client_socker , addr = server.accept()
        #分拆一个线程处理新的客户端
        client_theard = threading.Thread(target=client_handler,
                                         args=(client_socker,))
        client_theard.start()
def run_command(command):
    #换行
    command=command.rstrip()
    #运行命令并将输出返回
    try:
        output = subprocess.check_output(command,stderr=subprocess.STDOUT,
                                         shell=True)
    except:
        output = "Failed"
        #将输出发送
        return output

def client_handler(client_socket):
    global uploadl
    global execute
    global command
    #检测上传文件
    if len(upload_desination):
        #读取所有
        file_buffer=""
        #持续读取数据直到没有符合的数据
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            else:
                file_buffer = data
    #现在我们接收这些数据并将它们写出来：
    try:
        file_descriptor=open(upload_desination,"wb")
        file_descriptor.write(file_buffer)
        file_descriptor.close()

        #确认文件已经写出来了
        client_socket.send("Successflly ")
    except:
        client_socket.send("failed saved to "
                           "%s\r\n %upload_destination")
    #检查命令执行
    if len(execute):
        #运行命令
        output=run_command(execute)
        client_socket.send(output)
    #如果是第一个命令行shell，那么我们进入另一个循环
        if command:
            while True:
                #跳出一个窗口
                client_socket.send("<BHP:#>")
                #现在我们接收文件换行符（enter key）
                cmd_buffer=""
                while "\n" not in cmd_buffer:
                    cmd_buffer+=client_socket.recv(1024)
                    #返还命令输出
                    response = run_command(cmd_buffer)
                    #返回响应数据
                    client_socket.send(response)
