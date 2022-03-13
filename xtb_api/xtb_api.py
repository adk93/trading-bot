import socket
import ssl
import json
from dotenv import dotenv_values
from pathlib import Path

config = dotenv_values(Path().cwd() / '.env')

HOST = "xapi.xtb.com"
PORT = 5124 if int(config['DEMO']) else 5112
HOST_IP = socket.getaddrinfo(HOST, PORT)[0][4][0]


def connect_to_socket() -> socket.socket:
    s = socket.socket()
    s.connect((HOST, PORT))
    s = ssl.wrap_socket(s)
    return s


class XTBClient:
    """
    Client for XTB platform API

    xtb documentation: http://developers.xstore.pro/documentation/#getChartLastRequest

    args:

    userId - xtb platform user id
    password - xtb account password


    methods:
    login - performs a login operation to your account
    logout - performs a logout operation to your account
    make_call - performs an api call with given commands and arguments
    """
    def __init__(self, userId: str, password: str):
        self.userId = userId
        self.password = password
        self.s = connect_to_socket()

    @staticmethod
    def prepare_message(command: str, arguments: dict) -> json:
        message = {"command": command}
        if arguments is not None:
            message.update({"arguments": arguments})

        return json.dumps(message).encode("utf-8")

    def send_request(self, message: json) -> None:
        self.s.send(message)

    def read_response(self) -> json:
        full_response = ""
        while True:
            response = self.s.recv(8192).decode('utf-8')
            full_response += response
            try:
                json_response = json.loads(full_response)
                break
            except json.decoder.JSONDecodeError:
                continue

        return json_response

    def make_call(self, command: str, arguments: dict = None) -> dict:
        """Procedure of building request, sending and retrieving data"""

        # Prepare a message made of command and arguments
        message = self.prepare_message(command, arguments)

        # Send request to a server
        self.send_request(message)

        # Read response and return a dictionary
        response = self.read_response()

        return response

    def login(self):
        command = "login"
        arguments = {"userId": self.userId,
                     "password": self.password}

        return self.make_call(command, arguments)

    def logout(self):
        command = "logout"
        return self.make_call(command)
