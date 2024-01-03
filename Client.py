import socket


class Client:
    def __init__(self, server_host='127.0.0.1', server_port=8080):
        self.server_host = server_host
        self.server_port = server_port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        try:
            self.client_socket.connect((self.server_host, self.server_port))
            print(f"Conexiune reusita la {self.server_host}:{self.server_port}")
        except Exception as e:
            print(f"Eroare la conectare: {str(e)}")

    def send_numbers(self):
        try:
            while True:
                numbers_str = input(
                    "Introduceti un sir de numere (minim 5, maxim 10) separate prin virgula (sir gol pentru a inchide): ")

                if not numbers_str:
                    # Daca se introduce un sir gol, inchidem conexiunea
                    break

                numbers = [int(num) for num in numbers_str.split(',')]

                if 5 <= len(numbers) <= 10:
                    numbers_data = ','.join(map(str, numbers))
                    self.client_socket.send(numbers_data.encode())
                    print("Numerele au fost trimise catre server.")

                    # Așteaptă rezultatul de la server
                    result = self.client_socket.recv(1024).decode()
                    print(f"Rezultat de la server: {result}")
                else:
                    print("Introduceti un numar corect de numere (minim 5, maxim 10).")

        except Exception as e:
            print(f"Eroare la trimiterea datelor: {str(e)}")
        finally:
            self.close()

    def close(self):
        print("Conexiune inchisa.")
        self.client_socket.close()


# Exemplu de utilizare
if __name__ == "__main__":
    client = Client()
    client.connect()
    client.send_numbers()
