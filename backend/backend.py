from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Depends
import json
import os
import asyncio
from ftplib import FTP

app = FastAPI()

DATA_DIR = "chat_data"
FTP_HOST = "your.ftp.server"
FTP_USER = "your_ftp_user"
FTP_PASS = "your_ftp_password"

ios.makedirs(DATA_DIR, exist_ok=True)

connections = {}

def get_chat_file(channel: str):
    return os.path.join(DATA_DIR, f"{channel}.json")

def save_messages(channel: str, messages: list):
    with open(get_chat_file(channel), "w") as f:
        json.dump(messages, f)

def load_messages(channel: str):
    file_path = get_chat_file(channel)
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            return json.load(f)
    return []

def upload_to_ftp(channel: str):
    file_path = get_chat_file(channel)
    try:
        with FTP(FTP_HOST) as ftp:
            ftp.login(FTP_USER, FTP_PASS)
            with open(file_path, "rb") as f:
                ftp.storbinary(f"STOR {channel}.json", f)
    except Exception as e:
        print("FTP Upload Failed:", e)

def download_from_ftp(channel: str):
    file_path = get_chat_file(channel)
    try:
        with FTP(FTP_HOST) as ftp:
            ftp.login(FTP_USER, FTP_PASS)
            with open(file_path, "wb") as f:
                ftp.retrbinary(f"RETR {channel}.json", f.write)
    except Exception as e:
        print("FTP Download Failed:", e)

@app.websocket("/ws/{channel}/{user}")
async def chat_ws(websocket: WebSocket, channel: str, user: str):
    await websocket.accept()
    if channel not in connections:
        connections[channel] = []
    connections[channel].append(websocket)

    messages = load_messages(channel)
    await websocket.send_json(messages)

    try:
        while True:
            data = await websocket.receive_text()
            messages.append({"user": user, "message": data})
            save_messages(channel, messages)
            upload_to_ftp(channel)
            for connection in connections[channel]:
                await connection.send_json(messages)
    except WebSocketDisconnect:
        connections[channel].remove(websocket)
        if not connections[channel]:
            del connections[channel]
