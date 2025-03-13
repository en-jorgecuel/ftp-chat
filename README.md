# 🚀 FTP Chat (Architectural Joke Edition)

A **full-stack** chat application where messages are stored in JSON files and transferred via **FTP** (because why not? 😆). This project is a joke on bad architecture but is fully functional!

---

## 🛠️ Tech Stack
- **Backend:** FastAPI (Python)
- **Frontend:** React.js (Vite)
- **Storage:** JSON files (LOL)
- **Data Transfer:** FTP (because REST or WebSockets were too mainstream)

---

## 📂 Project Structure
```
ftp-chat-project/
│── backend/     # FastAPI backend
│── frontend/    # React.js frontend
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
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install dependencies:**
   ```sh
   pip install fastapi uvicorn python-multipart aiofiles ftplib
   ```
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
- **Users connect** via WebSockets to chat in 1-on-1 or team channels.
- **Messages are stored** in JSON files inside a local `chat_data/` directory.
- **JSON files are uploaded & downloaded** to an FTP server to simulate a "distributed system." 😂

---

## 📝 API Endpoints
| Method  | Endpoint                | Description             |
|---------|-------------------------|-------------------------|
| `WS`    | `/ws/{channel}/{user}`  | WebSocket chat stream  |

---

## 🔥 Features
✅ 1-on-1 and team chats  
✅ Messages stored in JSON (seriously...)  
✅ WebSockets for real-time updates  
✅ FTP-powered file transfers (because why not?)  

---

## 📸 Screenshots
**(Frontend UI preview)**

🚀 *Chat interface screenshot here* (add manually)

---

## 🤣 Why This Exists
- To make **architects cry** 😭
- To **test WebSockets & FTP interactions** 🛜
- Because **I was bored** 😆

---

## 🏆 Future "Improvements"
- ~~Replace FTP with Blockchain~~ (please don't 😅)
- Add **AI-powered emoji suggestions** 🤖
- Use **DNS TXT records to store messages** (😂)

---

## 📜 License
This project is open-source. Use it at your own risk and *don't blame me when your CTO yells at you!* 😆

