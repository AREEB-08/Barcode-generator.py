
---

## 🎨✨ **BARCODE-GENERATOR**

🚀 This Python project **generates QR codes** from any text, URL, or data and **adds a custom label** below the QR code. The final QR code is saved as an **image file**.

🔹 **Perfect for:** 🎫 Business cards, 🌐 social media links, 🏷️ product packaging, and 💳 digital payments.

✨ **Key Features:**
✅ **Generate high-quality QR Codes** 📱  
✅ **Custom text labels** below the QR code 🏛️  
✅ **Customizable text color & font size** 🎨  
✅ **Save as PNG image** for easy sharing 🗂️  
✅ **High error correction** for better readability 🔍  

---

## 🛠 **Installation**

### 📺 **Required Libraries**

This project requires the following **Python libraries**:

| 📦 Library | 🔗 Installation Command   |
| ---------- | ------------------------- |
| `qrcode`   | `pip install qrcode[pil]` |
| `Pillow`   | `pip install pillow`      |

💡 **To install all dependencies at once using `requirements.txt`:**

```bash
pip install -r requirements.txt
```

---

## 🚀 **How to Use**

### 🏃 **Run the Script**

```bash
python qr_code_generator.py
```

### 🔹 **Follow These Steps**

1️⃣ **Enter the text or URL** to generate the QR code  
2️⃣ **Provide a custom text label** (e.g., "🔍 Scan Me!")  
3️⃣ **Choose a text color** (e.g., `black`, `#FF5733`)  
4️⃣ **Set a font size** for the text  
5️⃣ **Enter the filename** to save the QR code  

📌 **Example Input & Output:**

```plaintext
Enter the link you want to create a QR code for: https://github.com/AREEB-08
Enter the text you want to add below the QR code: Scan Me! 🔎
Enter the text color (e.g., 'black', '#FF5733'): black
Enter the font size you want for the text: 20
Enter the filename to save the QR code (without extension): my_qr_code
✅ QR code saved as 'my_qr_code.png' with the text below.
```

🎨 **Generated QR Code** (`my_qr_code.png`) is saved in your project directory.

---

## 📂 **Project Structure**

```
📦 QR-Code-Generator
 ┣ 📝 qr_code_generator.py  # Main script 🖥️
 ┣ 📝 README.md             # Documentation 📜
 ┗ 📝 requirements.txt      # Dependencies 📦
```

---

## 🎭 **Customization Options**

Modify these settings inside `qr_code_generator.py` to **customize QR code properties**:

| 🔧 Parameter | 🔹 Description      | ✏️ Default Value |
| ------------ | ------------------- | ---------------- |
| `box_size`   | Size of QR squares  | `8`              |
| `border`     | QR code border size | `3`              |
| `fill_color` | QR code color       | `"black"`        |
| `back_color` | Background color    | `"white"`        |
| `text_color` | Label text color    | User input       |
| `font_size`  | Label font size     | User input       |

🛡 **Change Font Style**  
To use a custom font, replace `"arial.ttf"` with your own `.ttf` font file.

---

## 🤝 **Contributing**

Want to improve this project? Follow these steps:

1. **Fork the repository** 🍴  
2. **Create a new branch** (`git checkout -b feature-branch`) 🌱  
3. **Commit your changes** (`git commit -m "✨ Added new feature"`) 📌  
4. **Push to the branch** (`git push origin feature-branch`) 🚀  
5. **Open a Pull Request** 🎉  

---

## 🔥 **GitHub Setup**

### 📌 **Steps to Push This Project to GitHub**

```bash
git init
git add .
git commit -m "🚀 Initial commit - QR Code Generator"
git branch -M main
git remote add origin https://github.com/AREEB-08/QR-Code-Generator.git
git push -u origin main
```

---

🎉 **Have  a nice day !** 🚀🔗

