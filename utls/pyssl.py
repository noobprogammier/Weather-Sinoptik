from ssl import create_default_context
def make_socket_ssl(socket:dict) -> dict:
	if type(socket) != dict:
		raise exc(error_tab["Argument"]%(type(socket)))
	cont_ = create_default_context()
	if "sock" not in socket and "host" not in socket:
		raise exc(error_tab["Missing"]%("sock or host"))
	return cont_.wrap_socket(socket["sock"], server_hostname=socket["host"])