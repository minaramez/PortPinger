## **🛡️ PortPinger - A Lightweight Port Scanning Tool**
**⚠️ Note: This tool is intended for legitimate security testing and network auditing. Unauthorized scanning of networks without permission may be illegal. Use responsibly.**

### **📖 Overview**
**PortPinger** is a Python-based **port scanner** that allows users to scan a range of **ports (0-1000)** on a given **domain or IPv4 address**. It helps identify **open, closed, or filtered** ports on a target system.

### **🚀 Features**
✅ **Scans a range of ports on a target domain/IP**  
✅ **Provides real-time status (open/closed)**  
✅ **Uses a simple and interactive interface**  
✅ **Color-coded output for easy readability**  
✅ **Input validation to prevent invalid domain/port entries**  
✅ **Error handling for better user experience**  

---

## **⚙️ How It Works**
1️⃣ **User provides a domain or IP address**  
2️⃣ **User specifies a port range (0-1000)**  
3️⃣ **The script scans each port and reports if it is open or closed**  
4️⃣ **Color-coded output helps quickly identify results**  
5️⃣ **Users can access help (`--help`) and version (`--version`) options**  

---

## **📜 Installation & Usage**
### **🔹 Prerequisites**
- Python 3  
- Internet connection (if scanning external domains)

### **🔹 Clone the Repository**
```bash
git clone https://github.com/minaramez/PortPinger.git
cd PortPinger
```

### **🔹 Running the Port Scanner**
```bash
python3 portpinger.py
```

### **🔹 Example Usage**
```
Welcome to PortPinger.
Type '--help or --h' for help, or '--version or --v' for version.

Enter your domain/IPv4: example.com
Enter a starting port between 0 and 1000: 22
Enter an ending port between 22 and 1000: 80

Scanning ports...

example.com Port 22: open
example.com Port 23: closed
example.com Port 80: open
```

### **🔹 Command Line Options**
| Command | Description |
|---------|------------|
| `--help` or `--h` | Displays usage instructions |
| `--version` or `--v` | Shows the current version |

---

## **📝 How the Code Works**
### **1️⃣ Input Validation**
- **Domains/IPs are checked** to ensure a valid format.
- **Ports must be numeric (0-1000).**
- **End port must be ≥ start port.**

### **2️⃣ Port Scanning Logic**
- A **TCP connection** attempt is made using `socket.socket()`.
- If the port is **open**, it prints in **green** (`\033[92m`).
- If the port is **closed**, it prints in **red** (`\033[91m`).
- Any **unexpected errors** are displayed in **yellow** (`\033[93m`).

### **3️⃣ Error Handling**
- Detects **invalid domains/IPs**.
- Prevents **scanning out-of-range ports**.
- Handles **connection timeouts** to avoid freezing.

### License
This script is released under the **MIT License**, which allows modification, distribution, and use with minimal restrictions.