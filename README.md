# Simple TCP SYN Port Scanner 🚀

A Python-based network utility built with the **Scapy** library to perform stealthy TCP "Half-Open" port scans. This tool identifies whether ports on a target host are **Open**, **Closed**, or **Filtered**.



## 🛠️ How It Works
This scanner implements a **TCP SYN Scan** (also known as a Half-Open scan). Instead of completing the full three-way handshake, it sends a `SYN` packet and waits for the response:

1. **Open Port:** The target sends a `SYN-ACK` ($0x12$). The scanner identifies this and identifies the port as open.
2. **Closed Port:** The target sends a `RST-ACK` ($0x14$).
3. **Filtered Port:** No response is received (Timeout), usually indicating a firewall is dropping the packets.

### Technical Logic
| Flag Received | Hex Code | Status |
| :--- | :--- | :--- |
| `SYN-ACK` | $0x12$ | **Open** |
| `RST-ACK` | $0x14$ | **Closed** |
| `None` | N/A | **Filtered** |

## 🚀 Features
* **Custom Target Input:** Scan any IP or Hostname.
* **Dynamic Port Selection:** Add ports one by one and type `stop` to begin.
* **Input Validation:** Ensures port numbers are within the valid range ($1$ - $65535$).
* **Raw Packet Crafting:** Uses Scapy's `sr()` (send/receive) function for Layer 3 packets.

## 📋 Prerequisites
* **Python 3.x**
* **Scapy Library:**
  ```bash
  pip install scapy
  ```

  
