# -*- coding:utf-8 -*- 

import socket
import os 

#リッスンするホストのIPアドレス
host = "192.168.0.100"

#rawソケットを作成し、パブリックなインターフェースにバインド
if os.name == "nt":
	socket_protocol = socket.IPPRONTO_IP
else:
	socket_protocol = socket.IPPRONTO_ICMP

sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)

sniffer.bind((host, 0))

#キャプチャー結果にIPヘッダーを含めるように指定
sniffer.setsockopt(socket.IPPRONTO_IP, socket.IP_HDRINCL, 1)

#Windowsの場合はioctlを使用して、プロミスキャスモードを有効化
if os.name == "nt":
	sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

#単一パケットの読み込み
print sniffer.recvfrom(65565)

#Windowsの場合はプロミスキャスモードを無効化
if os.name == "nt":
	sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
	