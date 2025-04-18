import pysftp
from urllib.parse import urlparse
import os


class Sftp:
    def __init__(self, hostname, username, password, port=22):
        self.connection = None
        self.hostname = hostname
        self.password = password
        self.username = username
        self.port = port

    def connect(self):
        try:
            self.connection = pysftp.Connection(
                host=self.hostname,
                username=self.username,
                password=self.password,
                port=self.port,
            )
            print(f"Connected to {self.hostname} as {self.username}")
        except Exception as er:
            raise Exception(er)

    def disconnect(self):
        self.connection.close()
        print(f"Disconnected from host {self.hostname}")

    def listdir(self, remote_path):
        for obj in self.connection.listdir(remote_path):
            yield obj

    def listdir_attr(self, remote_path):
        for attr in self.connection.listdir_attr(remote_path):
            yield attr

    def upload(self, source_local_path, remote_path):

        try:
            print(f"uploading to {self.hostname} as {self.username}")
            self.connection.put(source_local_path, remote_path)
            print("upload completed")
        except Exception as er:
            raise Exception(er)

    def download(self, remote_path, target_local_path):
        try:
            print(f"downloading from {self.hostname} as {self.username}")

            path, _ = os.path.split(target_local_path)
            if not os.path.isdir(path):
                try:
                    os.makedirs(path)
                except Exception as er:
                    raise Exception(er)

            self.connection.get(remote_path, target_local_path)
            print("download completed")

        except Exception as er:
            raise Exception(er)


if __name__ == "__main__":
    sftp = Sftp(hostname="192.168.0.204", username="CYP", password="whdwls212")
    sftp.connect()

    path = "/"

    print(f"List of files with attributes at location {path}:")
    for file in sftp.listdir_attr(path):
        print(file.filename, file.st_mode, file.st_size, file.st_atime, file.st_mtime)

    local_path = "C:/Users/main/workspace/20250331-python/library_class/lenna.png"
    remote_path = "/lenna.png"
    sftp.upload(local_path, remote_path)

    print(f"List of files at location {path}:")
    print([f for f in sftp.listdir(path)])

    sftp.download(remote_path, os.path.join(remote_path, local_path + ".backup"))

    sftp.disconnect()
