# 🎯 Tischkick‑Automatisierung (Abi 2024)

## 📋 **Kurzüberblick was das Projekt kann**
Das Folgende Projekt dreht sich um die Automatisierung eines Kickers, um potenzielle Streitfragen, wie wann zählt ein Tor, war das ein Tor, wie viele Punkte gibt ein Tor usw. Aber auch Täuschung und Betrug, durch Manipulation der analogen Toranzeigen, vorzubeugen. Hierzu werden in dem Projekt mehrere Mikrocontroller benutzt, die jeweils andere Aufgaben haben. Eine dieser Aufgaben ist die Torerkennung, eine andere ist Darstellen der Tore auf einer Toranzeige.

## 💡 **Idee Hinter dem Projekt**
Die Idee für das folgende Projekt liegt in dem Gedanken, ein Kickerspiel fairer zu gestalten, indem man die Prozesse der Torerkennung und der Toranzeige automatisiert, da es oftmals zwischen den zwei Spielparteien aufgrund von Toren, deren Zählung und Bepunktung zu Streitigkeiten kommt. Außerdem, da es manchmal vorkommt, dass der Ball vom Tor reflektiert wird. Darüber hinaus kann es ebenfalls durch äußere Beeinflussung dazu kommen, dass die mechanische Toranzeige verrutscht und somit der Punktestand verfälscht wird.

**🏆 Restlichen Infos** 
- **Jugend‑Forsch**: 🥈 zweiter Platz (2024 Herford)
- **Abitur**: ⭐ Besondere Lernleistung am HVG (2024 Blomberg) 

## 🛠️ **Hardware**
**🔧 Hardwarekomponenten**
- **Raspberry Pi Pico 2W** x4
- **Pimoroni Pico Unicorn Pack** x2
- **Fotoresistoren**
- **Blaue LEDs**

**📐 Hardwareaufbau**
- **Haupt‑Pico**: Lichtschranke (blaue LED + Fotoresistor Bridge).  
- **Toranzeigen**: 2x Pico + Unicorn pHAT (16x7 RGB Matrix).
- **BLE‑Pico**: Für App‑Kommunikation

## ✨ **Features**
- ✅ Präzise Tor‑Detektion (Lichtunterbrechung).  
- ✅ Automatische Score‑Anzeige (RGB‑LED‑Matrix).
- 🔄 Geplante App‑Kommunikation

## 🚀 **Installation**
1. Pico flashen: [micropython.org](https://micropython.org) (uf2‑File).  
2. Thonny: Code kopieren.  
3. GPIO verkabeln.

> 📌 Hinweis: Eine ausführliche Schritt‑für‑Schritt‑Installation inkl. Pins/Verkabelung kommt (siehe unten „Schaltplan & Verkabelung“).

## 🔌 **Schaltplan & Verkabelung (kommt / wird verlinkt)**
- 🧩 Schaltplan/Fotos der Verkabelung: **[hardware/schaltplan.jpg](hardware/schaltplan.jpg)** (wird hochgeladen)
- 🧵 Pin‑Mapping (Haupt‑Pico ↔ Toranzeigen ↔ Sensor): **[docs/pinout.md](docs/pinout.md)** (wird hochgeladen)

## 🧾 **Platinen (kommt / wird verlinkt)**
- 🖨️ Platinenmuster/Layouts (druck/laser): **[hardware/pcb/](hardware/pcb/)** (Ordner wird hochgeladen)
  - z.B. Gerber/PNG/PDF je nachdem, was du hast

## 📱 **App & PAPs (kommt / wird verlinkt)**
- 📐 PAPs / Ablaufpläne: **[docs/paps/](docs/paps/)** (wird hochgeladen)
- 🎨 App‑Design Bilder/Wireframes: **[app_design/](app_design/)** (wird hochgeladen)

## 💻 **Code**
- `main_torerkennung.py` (Torerkennung via Lichtschranken).
  **([📥 Download Code**
- `main_toranzeige.py` (Toranzeige via der RGB Matrix).
  **([📥 Download Code]**
- `font_toranzeige.py` (Schriftart für die RGB Matrix).
  **([📥 Download Code]**

## 📚 **Abi‑Arbeit**
**([📥 Download PDF](https://github.com/mitheld/tischkicker--pico-automatisation/blob/4ee2dc82677f77494fc8380a0d66b5e9431f0e39/Automatisierung%20eines%20Tischkickers%20Abi.pdf))**

> ⚠️ **Rechtshinweis**: Rechteinhaber ist mitheld. Schulische Arbeit – eigene Leistung, alle Rechte vorbehalten.

## 🛡️ **Cybersecurity Lessons**
- 🔌 GPIO/IoT‑Security.  
- 📡 Sensor‑Detection.
