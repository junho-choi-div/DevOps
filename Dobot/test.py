import socket
from _thread import *
from IMI import imi_run
from multiprocessing import Process,Queue
from cfg import config
import cv2
import numpy as np
import time

input_queue = Queue()
output_queue = Queue()



def threaded(client_socket, addr):
    global input_queue,output_queue
    origin_pos = (-640,-165) 
    w = 640-329
    h = 444-165
    z = 70
    scale_w = round(w/2448,3)
    scale_h = round(h/2048,3)
    cx_dir,cy_dir = 1, -1
    # move1 = b'-698,114,112.32,0;'
    move2 = b'-416.5,114,112.32,0;'
    # move3 = b'-503.9,-197.5,123.99,0;'

    now_state = "1"
    print('>> Connected by :', addr[0], ':', addr[1])

    ## process until client disconnect ##
    while True:
        print(now_state)
        try:
            ## send client if data recieved(echo) ##
            data = client_socket.recv(1024)

            if not data:
                print('>> Disconnected by ' + addr[0], ':', addr[1])
                break
            try:
                print('>> Received from ' + addr[0], ':', addr[1], data.decode())
            except:
                print('decode error')
            ## chat to client connecting client ##
            ## chat to client connecting client except person sending message ##
            if "1,2,3,4" in data.decode() :
                time.sleep(1)
                input_queue.put(True)
                image = output_queue.get()
                blr = cv2.GaussianBlur(image, (3, 3), 1.0)
                cv2.imwrite("ssss.jpg",blr)
                try:
                    circles = cv2.HoughCircles(blr, cv2.HOUGH_GRADIENT, 1, 50, param1=120, param2=70, minRadius=20, maxRadius=160)
                    if circles is not None:
                        for i in range(circles.shape[1]) :
                            cx, cy, radius = circles[0][i] 
                            break
                    pos_x, pos_y = origin_pos[0]+(scale_w*cx*cx_dir),origin_pos[1]+(scale_h*cy*cy_dir)
                    print(pos_x,pos_y)
                    msg= f"{pos_x},{pos_y},{z},0;"
                    move_pos = bytes(msg,encoding='utf-8')
                    print(move_pos)
                    client.send(move_pos)
                    print("sendcomplete~~")

                except:
                    print("no lens in image")

            for client in client_sockets:
                if client != client_socket:
                    client.send(data)
        
        except ConnectionResetError as e:
            print('>> Disconnected by ' + addr[0], ':', addr[1])
            break
    
    if client_socket in client_sockets:
        client_sockets.remove(client_socket)
        print('remove client list : ', len(client_sockets))

    client_socket.close()

if __name__=="__main__":
    camera_process = Process(
        target = imi_run,
        args=(output_queue,input_queue,config),
        daemon=True)
    camera_process.start()

    client_sockets = []

    HOST = socket.gethostbyname(socket.gethostname())
    PORT = 9999

    print('>> Server Start with ip :', HOST)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    try:
        while True:
            print('>> Wait')

            client_socket, addr = server_socket.accept()
            client_sockets.append(client_socket)
            start_new_thread(threaded, (client_socket, addr))
            print("참가자 수 : ", len(client_sockets))
    except Exception as e:
        print('에러 : ', e)

    finally:
        server_socket.close()