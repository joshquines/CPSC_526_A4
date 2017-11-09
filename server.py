"""
CPSC 526 Assignment #4
Steven Leong 10129668 T01
Josh Quines 10138118 T03
"""
import socket
import socketserver
import sys
import os
import time
import traceback
import select
import string
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import random
import hashlib

#GLOBAL VARIABLES
BUFFER_SIZE = 4096
CIPHER = 0
BLOCK_SIZE = 0

def authentication(client, key, nonce):
    # https://codereview.stackexchange.com/questions/47529/creating-a-string-of-random-characters
    message = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length))

#def sendEncrypted(client, msg):
    	
#def recvEncrypted(client, msg):

# Use this to send msg to server
def encrypter(cipher, msg, nonce):

	return toSend

# Use this to receive msg from server
def decrypter(cipher,msg, nonce):
	if cipher == 'aes128':
		# Decrypt using aes128
		toReceive = resultOfEncryption
		pass
	elif cipher == 'aes256':
		# Decrypt using aes256
		toReceive = resultOfEncryption
		pass
	elif cipher == 'null':
		# Dest send msg
		toReceive = msg
		pass
	return toReceive

def read(client, filename):

def write(client, filename):

def setCipher(cCipher, key, nonce):
	IVMsg = b(key + nonce + "IV")
	SKMsg = b(key + nonce + "SK")
	backend = default_backend()

	if cipher == 'aes128':
		# Encrypt using aes128
		IV = hashlib.sha128(IVMsg).hexdigest()
		SK = hashlib.sha128(SKMsg).hexdigest()
		CIPHER = Cipher(algorithms.AES(SK), modes.CBC(IV), backend=backend)

	elif cipher == 'aes256':
		# Encrypt using aes256
		IV = hashlib.sha256(IVMsg).hexdigest()
		SK = hashlib.sha256(SKMsg).hexdigest()
		CIPHER = Cipher(algorithms.AES(SK), modes.CBC(IV), backend=backend)


"""Log client activity to standard output"""
def logging(msg):
    # get local time
    print(time.strftime("%a %b %d %H:%M:%S") + ": " + msg)
		

# Authentication
	# server → client: random challenge
	# client → server: compute and send back a reply that can only be computed if secret key is known
	# server → client: verify the reply, send success/failure message to client

# Request
	# client → server: operation, filename
	# server → client: response indicating whether operation can proceed

# Data Exchange
	# client → server: data chunk
	# server → client: data chunk
	# In case of any errors, the server should indicate so to the client and then disconnect.
		# server → client: optional error message


def clientHandler(client, cipher, nonce, key):
	""" What is this for
	# Acknowledge cipher + nonce to client but encrypted
	ackClient = "Cipher used: " + str(cipher) + "\nNonce: " + str(nonce)
	ackClientEncrypted = encrypter(cipher, ackClient)
 	client.sendall(ackClientEncrypted)


	# Authentication 
	# The key received from the client is encrypted using cipher<x>
	clientKeyEncrypted = client.recv(BUFFER_SIZE).decode("utf-8")
	clientKey = decrypter(cipher, clientKeyEncrypted)

	
	if(!authentication(client, key)):
    	logging("Error: wrong key")
		client.close()
		return True
	else: 
		return False
	"""

	
	if not authentication(client, key):
		logging("Error: wrong key")
		keyInvalid = 
		client.sendall(bytearray(, "utf -8"))
		client.close()
		return
	else:
		keyValid = encrypter(cipher, authCheck)
		client.sendall(keyValid)

	# Get method + filename
	clientFileRequestEncrypted = client.recv(BUFFER_SIZE).decode("utf-8")
	clientFileRequest = decrypter(cipher, clientFileRequestEncrypted)
	command = clientFileRequest.split(';')[0]
	filename = clientFileRequest.split(';')[1]

	# Check if server can do action
	# Temporarily calling this function doAction, still gotta define it and find out how to do it
	# doAction will return either True or False

	canDo = doAction()
	canDoEncrypt = encrypter(cipher, canDo)
	client.sendall(canDoEncrypt)

	# If canDo was true, should be able to either download from client, or give file to client
	# If canDo was not true, client closes connection



if __name__ == "__main__":

	# Arg check
	if len(sys.argv) == 3:
		PORT = sys.argv[1]
		KEY = sys.argv[2]
	else:
		print("\nIncorrect number of parameters: ")
		print("Usage: server.py <port> <key>")
		sys.exit()

	print("Listening on port " + str(PORT))
	print("Using secret key: " + str(KEY))

	serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	HOST = socket.gethostname
	serverSocket.bind((HOST, PORT))
	serverSocket.listen(5)

	while 1:
		client, addr = serverSocket.accept()
		# First message
		# client → server: cipher, nonce
		cipherNonceMsg = client.recv(BUFFER_SIZE).decode("utf-8").split(";")
		cCipher = cipherNonceMsg[0]
		nonce = cipherNonceMsg[1]

		logging("new connection from " + str(addr[0]) + " cipher = " + cCipher)
		logging("nonce = " + nonce)
		setCipher(cCipher, key, nonce)
		clientHandler(client, key, nonce) 
		# Final Success
		# server → client: final success
		logging("status: SUCCESS")

		client.close()

