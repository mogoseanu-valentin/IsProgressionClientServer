import socket
import threading

from Progresie import Progresie


class Server:
    def __init__(self, host='127.0.0.1', port=8080):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Serverul asculta la adresa {self.host}:{self.port}")

    def start(self):
        try:
            while True:
                client_socket, client_address = self.server_socket.accept()
                print(f"Conexiune acceptata de la {client_address}")
                client_handler = ClientHandler(client_socket)
                client_handler.start()
        except KeyboardInterrupt:
            print("Server oprit manual.")


class ClientHandler(threading.Thread):
    def __init__(self, client_socket):
        threading.Thread.__init__(self)
        self.client_socket = client_socket

    def run(self):
        try:
            while True:
                # Primim datele de la client
                data = self.client_socket.recv(1024)
                if not data:
                    break  # Ieșim din bucla dacă nu primim date de la client

                # Convertim datele primite într-o listă de numere
                numbers = list(map(int, data.decode().split(',')))

                # Verificăm progresia și trimitem rezultatul la client
                progresie_obj = Progresie(numbers)
                result = progresie_obj.verificare_progresie()

                # Trimitem rezultatul la client
                self.client_socket.send(result.encode())

        except Exception as e:
            print(f"Eroare in gestionarea clientului: {str(e)}")
        finally:
            self.client_socket.close()
            print("Conexiune inchisa.")


# Exemplu de utilizare
if __name__ == "__main__":
    server = Server()
    server.start()
