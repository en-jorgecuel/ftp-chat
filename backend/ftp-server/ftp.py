from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

import os

# FTP Server Configuration
FTP_USER = "testuser"
FTP_PASS = "testpass"
FTP_DIR = "ftp_storage"
FTP_PORT = 2121

# Ensure the FTP directory exists
os.makedirs(FTP_DIR, exist_ok=True)

def start_ftp_server():
    authorizer = DummyAuthorizer()
    authorizer.add_user(FTP_USER, FTP_PASS, FTP_DIR, perm="elradfmw")
    
    handler = FTPHandler
    handler.authorizer = authorizer
    
    server = FTPServer(("0.0.0.0", FTP_PORT), handler)
    print(f"FTP Server running on port {FTP_PORT}...")
    server.serve_forever()

if __name__ == "__main__":
    start_ftp_server()