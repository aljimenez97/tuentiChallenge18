#!/usr/local/bin/python3
import socket
import time
from spliceMachine import  indexProvider, outputProvider, dnaAppend

# Setting up connection 
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ('52.49.91.111', 3241)
socket.connect(address)

# Some greeting 
resp = socket.recv(2048).decode('utf-8')
print(resp)
resp = socket.recv(2048).decode('utf-8')
print(resp)

# Can also enter TEST
socket.send(b'SUBMIT\n')
resp = socket.recv(2048).decode('utf-8')
print(resp)

# There are 20 questions
for i in range(20):
	resp = socket.recv(2048).decode('utf-8')
	print(resp)
	words = resp.replace('\n', '').split(' ', 18)	
	# Find DNA pieces that solve the challenge
	dna_pieces = dnaAppend(words)
	indexes = indexProvider(words, dna_pieces)
	# Preparing answer for requested format
	str_answer = outputProvider(indexes)
	socket.send(str_answer.encode())
	# Send answer
	resp = socket.recv(2048).decode('utf-8')
	print(resp)