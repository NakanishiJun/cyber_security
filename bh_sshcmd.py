# -*- coding:utf-8 -*-

import threading 
import paramikio
import subprocess

def ssh_command(ip, user, passwd, command):
	client paramikio.SSHClient()
	#client.load_host_keys('/home/justin/.ssh/known_hosts')
	client.set_missing_host_key_oplicy(paramikio.AutoAddPolicy())
	client.connect(ip, username=user, password=passwd)
	ssh_session = client.get_transport().open_session()
	if ssh_session.active:
		ssh_session.exec_command(command)
		print ssh_session.recv(4096)
	return

ssh_command('192.168.223.136', 'justin', 'lovesthepython', 'id')