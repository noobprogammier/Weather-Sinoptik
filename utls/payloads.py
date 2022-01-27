def send_GET(sock:dict) -> dict:
	blob = [sock[bob] for bob in sock]
	sock = blob[2]
	headers_ = ("GET /%s HTTP/1.1\r\x0AHost: %s\r\x0AAccept: */*\r\x0AConnection: close\r\x0AUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36\r\x0A\r\x0A"%(blob[0], blob[1])).encode("utf-8")
	sock.send(headers_)
	data = b"".join(sock.recv(12482) for bob in range(45))
	return data