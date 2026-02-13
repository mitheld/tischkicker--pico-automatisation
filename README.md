## Tischkick‑Automatisierung (Abi 2024)

## **Idee Hinter dem Projekt**


**Lichtschranke‑Torerkennung mit Raspberry Pi Pico**  
- Abi‑Fünftes Fach & Jugend forscht.  
- Hardware: RPi Pico 2W + Lichtschranke (Fotoresistor/LED) + 2x Unicorn pHAT Displays.  
- Kommunikation: GPIO zwischen Picos.  
- Bluetooth: WIP (funktioniert grundsätzlich).  

## **Hardware**
**Hardwarekomponeten**
- **Raspberry Pico 2W** x4
- **Pimoroni Pico Unicorn Pack** x2
- **Fotoresitoren**
- **Blaue LEDs**

**Hardwareaufbau**
- **Haupt‑Pico**: Lichtschranke (blaue LED + Fotoresistor Bridge).  
- **Toranzeigen**: 2x Pico + Unicorn pHAT (16x7 RGB Matrix).
- **BLE-Pico**: Für App-Komunniaktion

## Features
- Präzise Tor‑Detektion (Lichtunterbrechung).  
- Automatische Score‑Anzeige (RGB-LED‑Matrix).
- Geplante App-Communication
  

## Installation
1. Pico flashen: micropython.org (uf2‑File).  
2. Thonny: Code kopieren.  
3. GPIO verkabeln.  

## Code
- main(Torerkennung).px (Torerkkenung via Lichtschranken).
- main(Toranzeige).py (Toranzeige via der RGB Matrix).  
- font(Toranzeige).py (Schriftart für die RGB Matrix).

## Abi‑Arbeit


## Cybersecurity Lessons
- GPIO/IoT‑Security.  
- Sensor‑Detection.  
