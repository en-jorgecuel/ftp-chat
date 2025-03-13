# 🚀 FTP Chat (Architectural Joke Edition)

A **full-stack** chat application where messages are stored in JSON files and transferred via **FTP**—because why not? 😆 This project is both a **joke on bad architecture** and a fully functional chat system!

---

## 🛠️ Tech Stack
- **Backend:** FastAPI (Python)
- **Frontend:** React.js (Vite)
- **Storage:** JSON files (yes, seriously)
- **Data Transfer:** FTP (because REST or WebSockets were too mainstream)

---

## 📂 Project Structure
```
ftp-chat-project/
│── backend/     # FastAPI backend
│── frontend/    # React.js frontend
│── chat_data/   # JSON file storage (messages)
│── ftp_server/  # FTP storage simulation
```

---

## 🔧 Setup & Installation

### 🖥 Backend (FastAPI)
1. **Navigate to the backend directory:**
   ```sh
   cd backend
   ```
2. **Create a virtual environment (optional but recommended):**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: `venv\Scripts\activate`
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
   *(Make sure `requirements.txt` includes `fastapi`, `uvicorn`, `python-multipart`, `aiofiles`, and `ftplib`.)*
4. **Run the server:**
   ```sh
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

### 🌐 Frontend (React.js + Vite)
1. **Navigate to the frontend directory:**
   ```sh
   cd frontend
   ```
2. **Install dependencies:**
   ```sh
   npm install
   ```
3. **Run the development server:**
   ```sh
   npm run dev
   ```

---

## ⚙️ How It Works
- **Users connect** via WebSockets for real-time chat.
- **Messages are stored** in JSON files inside a local `chat_data/` directory.
- **JSON files are uploaded & downloaded** to an FTP server—because nothing screams "enterprise-grade" like FTP. 😂

---

## 📝 API Endpoints
| Method  | Endpoint                | Description             |
|---------|-------------------------|-------------------------|
| `WS`    | `/ws/{channel}/{user}`  | WebSocket chat stream  |

---

## 🔥 Features
✅ 1-on-1 and team chats  
✅ Messages stored in **JSON files** (because databases are overrated)  
✅ WebSockets for real-time updates  
✅ FTP-powered file transfers (don't ask why)  

---

## 📸 Screenshots
### 🚀 *Chat Interface Preview*
![Chatbox UI](https://github.com/en-jorgecuel/ftp-chat/blob/main/screenshots/chatbox.jpg?raw=true)

### 🔧 *Raw Chat JSON File*
![Chat JSON](https://github.com/en-jorgecuel/ftp-chat/blob/main/screenshots/json_file.jpg?raw=true)

---

## 🤣 Why This Exists
- To make **architects cry** 😭
- To **test WebSockets & FTP interactions** 🛜
- Because **I was bored** 😆

---

## 🏆 Future "Improvements"
- ~~Replace FTP with Blockchain~~ (please don’t 😅)
- Add **AI-powered emoji suggestions** 🤖
- Store messages in **DNS TXT records** (because why not? 😂)

---

## 📜 License
This project is open-source. Use it at your own risk, and *don’t blame me when your CTO yells at you!* 😆

