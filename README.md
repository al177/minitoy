Dead-end personal project for a WiFi enabled FPGA board using the Lattice ICE40UP5K FPGA.

Features:

- Minimal-ish part count due to using the ESP8266 to configure the FPGA during power-up
- Intended to run Micropython
- Fast SPI channel between ICE40 and ES8266 can be used as a communications channel after boot

This project has been built as of the 0.1 revision of the PCB. There are numerous workarounds needed to get it running that are
rolled up into the v0.2 PCB committed here, though v0.2 has not been manufactured.

Possible improvements:

- ESP32 instead of ESP8266 for an additional serial port for a separate console, additional horsepower, and lower power modes.
- Reset button
- Combine both 3.3v LDOs since I don't think sequencing 1.2 before 3.3 is that critical for the ICE40
- Fix RGB LED pinout
- Fix reset circuit for ESP (in v0.2)
- 0 ohm resistor to take 5v power from FTDI cable
- LiFePO4 or LiPo power

Included are iceboot.py, a Micropython module that can boot an ICE40 bitstream, and boot.py which is a startup script to load a
bitstream on Micropython power-up.

