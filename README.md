<div align="center">
<img width="894" height="413" alt="image" src="https://github.com/user-attachments/assets/7c5a6626-bb79-4d68-a58e-f7e8fee52eff" />

<div align="center">

  # 👯 FileTwin

  ### **The Digital DNA Test for Your Files.**
  
  <p>
    <img src="https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python" />
    <img src="https://img.shields.io/badge/Algorithm-SHA256-green?style=for-the-badge" />
    <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" />
  </p>

  <p>
    <a href="#-features">Features</a> •
    <a href="#-how-it-works">How It Works</a> •
    <a href="#-installation">Installation</a>
  </p>

</div>

---

## 🚀 Overview

**FileTwin** is a no-nonsense command-line tool designed to solve one problem: *Are these two files actually the same?* Windows or Mac might tell you two files have the same size, but that doesn't mean they have the same content. FileTwin uses cryptographic hashing to verify integrity, making it impossible for subtle corruption or hidden changes to slip by.

## ✨ Features

* **🔒 Cryptographic Accuracy:** Uses hashing to ensure byte-perfect comparison.
* **⚡ Chunked Reading:** Efficiently handles massive files (GBs or TBs) without eating up your RAM.
* **🧩 Binary Safe:** Works on images, videos, executables, and text files alike.
* **🚦 Instant Verdict:** Gives you a clear "IDENTICAL" or "NOT IDENTICAL" instantly.

---

## 🧠 How It Works

Comparing files by name or size isn't enough. FileTwin works by calculating the "Digital Fingerprint" of each file.

1.  **Block Reading:** It reads both files in small, manageable 4KB chunks (so your computer doesn't freeze).
2.  **Hashing:** As it reads, it feeds the data into a SHA-256 algorithm.
3.  **Comparison:**
    * If the final hash strings match → The files are **Identical**.
    * If even one bit is different → The files are **Different**.



---

## 🛠️ Installation

No complex dependencies required. Just clone and run.

```bash
git clone [https://github.com/YOUR_USERNAME/FileTwin.git](https://github.com/YOUR_USERNAME/FileTwin.git)
cd FileTwin
```
<div align="center"> <sub>Don't let data corruption fool you. Verify everything.</sub> </div>
