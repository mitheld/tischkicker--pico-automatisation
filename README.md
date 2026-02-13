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

> 📌 Hinweis: Für eine ausführliche Schritt‑für‑Schritt‑Installation inkl. Pins/Verkabelung (siehe unten „Schaltplan & Verkabelung“).

## 🔌 **Schaltplan & Verkabelung**
- 🧩 Schaltplan/Fotos der Verkabelung: **[schaltplan.png](https://github.com/mitheld/tischkicker--pico-automatisation/blob/cc84b4d476a509ef9cdfa26a50c255c8c1e5b9b7/documentation/Kompletter%20Schaltplan%20Tischkicker.png)** 
- 🧵 Pin‑Mapping (Toranzeigen ↔ Haupt‑Pico ↔ Sensor): **[PIN-Belegung.md](docs/pinout.md](https://github.com/mitheld/tischkicker--pico-automatisation/blob/3e12147f7516c3b7b3d17dfac8ad4ba78d0314ae/documentation/PIN-Belegung.md))**

## 📱 **App & PAPs**
- 📐 PAPs / Ablaufpläne:
  - PAP **Torerkennung** **[hier](https://github.com/mitheld/tischkicker--pico-automatisation/blob/cc84b4d476a509ef9cdfa26a50c255c8c1e5b9b7/documentation/Torerkennung%20PAP.pdf)**
  - PAP **Toranzeige** **[hier](https://github.com/mitheld/tischkicker--pico-automatisation/blob/cc84b4d476a509ef9cdfa26a50c255c8c1e5b9b7/documentation/PAP%20Toranzeige.pdf)**   
- 🎨 App‑Design Bilder: **[app/](https://github.com/mitheld/tischkicker--pico-automatisation/tree/84c3946407740578b0dcfe2722f7da696ce30cbe/app)** 

## 💻 **Code**
- `main_torerkennung.py` (Torerkennung via Lichtschranken).
  **([📥 Download Code](https://github.com/mitheld/tischkicker--pico-automatisation/blob/cc84b4d476a509ef9cdfa26a50c255c8c1e5b9b7/codes/main(Torerkennung).py))**
- `main_toranzeige.py` (Toranzeige via der RGB Matrix).
  **([📥 Download Code](https://github.com/mitheld/tischkicker--pico-automatisation/blob/cc84b4d476a509ef9cdfa26a50c255c8c1e5b9b7/codes/main(Toranzeige).py))**
- `font_toranzeige.py` (Schriftart für die RGB Matrix).
  **([📥 Download Code](https://github.com/mitheld/tischkicker--pico-automatisation/blob/cc84b4d476a509ef9cdfa26a50c255c8c1e5b9b7/codes/font(Toranzeige).py))**

## 📚 **Abi‑Arbeit**
**([📥 Download PDF](https://github.com/mitheld/tischkicker--pico-automatisation/blob/4ee2dc82677f77494fc8380a0d66b5e9431f0e39/Automatisierung%20eines%20Tischkickers%20Abi.pdf))**

> ⚠️ **Rechtshinweis**: Rechteinhaber ist mitheld. Schulische Arbeit – eigene Leistung, alle Rechte vorbehalten.

## 🛡️ **Cybersecurity Lessons**
- 🔌 GPIO/IoT‑Security.  
- 📡 Sensor‑Detection.

# **🔒 Urheberrechtshinweis**

**© 2026 mitheld. Alle Rechte vorbehalten.**

Alle in diesem Repository veröffentlichten Dateien und Inhalte sind urheberrechtlich geschützt. 
Sie dürfen ausschließlich zu privaten Zwecken gelesen bzw. angesehen werden.

Jegliche Vervielfältigung, Verbreitung, Veröffentlichung, Bearbeitung, Übersetzung oder sonstige Nutzung – ganz oder teilweise – ist ohne ausdrückliche schriftliche Genehmigung des Urhebers untersagt.

Die Rechte verbleiben vollständig beim Urheber.

## 📞 **Kontakt & Erreichbarkeit**

**Student** | Niedersachsen  
📧 **[ProtonMail](mailto:github@[deine-proton-domain].me)**  
🔗 **GitHub**: Dieses Profil  
🌐 **Portfolio**: [cyber-portfolio Repo](https://github.com/[username]/cyber-portfolio) **(folgt)** 

**Nachricht erwünscht**: Fragen zu Projekt, Code‑Review, Cybersecurity‑Collab.

