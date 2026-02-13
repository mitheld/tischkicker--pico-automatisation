# 📍PIN-Belegung

## 1️⃣**Haupt-Pico/Torerkennung**

**🥅Tor-A**
- GoalA = machine.Pin(**2**, machine.Pin.OUT) 
- analog_value_goal_a = machine.ADC(**28**)

**🥅Tor-B**
- GoalB = machine.Pin(**3**, machine.Pin.OUT) 
- analog_value_goal_b = machine.ADC(**27**)
## 📝**Textform**
Für die Tor sind an dem Pico die PINS 
1. **GP28_A2** *Tor A*
   
und

2. **GP27_A1** *Tor B*

als Eingangspins deklariert worden.
Die Ausgangspins sind jeweiles **GP 2** und **GP 3**

## 2️⃣**Zweiter-Pico/Toranzeige**
Jeweils für die beiden Picos auf den Torseiten:
- PlayerAin_value = Pin(**0**, Pin.IN, Pin.PULL_DOWN) (Player A = Tor A
- PlayerBin_value = Pin(**1**, Pin.IN, Pin.PULL_DOWN) (Player B = Tor B)

# 📝**Textform**
Die Eingangspins sind 
1. **GP 0** *Tor A/PlayerA*
   
und

2. **GP 1** *Tor B/PlayerB*

deklariert worden.
