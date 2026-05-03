
---

# 📱 UPI QR Code Generator

A simple Python project that generates **scannable QR codes** for UPI payments across popular apps like **PhonePe, Paytm, and Google Pay**. This tool allows users to input their UPI ID and instantly create QR codes that can be saved or shared.

---

## 🚀 Features
- 🔑 Input your UPI ID and generate payment QR codes.
- 📷 Creates separate QR codes for **PhonePe, Paytm, and Google Pay**.
- 💾 Saves QR codes as PNG images for reuse.
- 🖼️ Displays QR codes directly using Pillow.
- ⚡ Lightweight and easy to run — no complex setup required.

---

## 🛠️ Tech Stack
- **Python 3.x**
- [qrcode](https://pypi.org/project/qrcode/) library
- [Pillow](https://pypi.org/project/Pillow/) for image display

---

## 📂 Project Structure
```
.
├── app.py              # Main script to generate QR codes
├── phonepe_qr.png      # Generated QR for PhonePe
├── paytm_qr.png        # Generated QR for Paytm
├── Google_pay_qr.png   # Generated QR for Google Pay
└── README.md           # Project documentation
```

---

## ⚙️ Installation & Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/upi-qr-generator.git
   cd upi-qr-generator
   ```

2. Install dependencies:
   ```bash
   pip install qrcode pillow
   ```

3. Run the script:
   ```bash
   python app.py
   ```

4. Enter your UPI ID when prompted.  
   Example: `aryan@upi`

5. The script will generate and save QR codes for **PhonePe, Paytm, and Google Pay**.

---

## 📸 Example Output
- `phonepe_qr.png` → QR code for PhonePe  
- `paytm_qr.png` → QR code for Paytm  
- `Google_pay_qr.png` → QR code for Google Pay  

Each QR can be scanned directly in the respective app to initiate payment.

---

## 🔮 Future Enhancements
- ✅ Add support for **amount, currency, and transaction notes** in the QR.
- ✅ Generate a **universal QR code** that works across all UPI apps.
- ✅ Build a **Tkinter GUI** for user-friendly input and QR preview.
- ✅ Extend to a **Flask web app** for online QR generation.

---

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to improve.

---

## 📜 License
This project is licensed under the MIT License — feel free to use and modify.

---
