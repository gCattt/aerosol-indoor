# aerosol-indoor

Portable instrument for the measurement of indoor particulate matter in the 1-10 micron range, designed and developed for the Students Software House Project (2021), organized by the ITIS E.Fermi in collaboration with The Institute of Atmospheric Sciences and Climate (CNR -ISAC).

<hr>

Specifically, for this experiment two low cost sensors were used, the Sensirion SPS30 and the Omron B5W LD-0101, capable of carrying out extensive optical measurements of environmental particulate matter (from 0.5 μm to 10 μm) and obtaining the different mass concentrations.\
The two optical sensors have variable response characteristics, as their reliability can be compromised by external factors, such as high humidity, and for this particular reason, the BME280 sensor was added to the devices, which is capable of detecting values ​​of temperature, pressure and, indeed, humidity.\
Everything is coordinated by a script, written using the Arduino framework and loaded on the ESP32 microcontroller.
<p align="center"><img src="https://github.com/gCattt/aerosol-indoor/assets/78471254/4bf941d9-002f-4254-9bc5-83eeef25ca56" width=325></p>

<br>

The data flow occurs according to the following scheme:
<p align="center"><img src="https://github.com/gCattt/aerosol-indoor/assets/78471254/86c8b352-81bf-419d-b6bf-23e2058fc22e" width=800></p>

The same microcontroller interacts with an MQTT broker, publishing the measurements made on a given topic.\
The virtual machine within the server, once "registered" to the topic, is able to manage and publish the data using a Python script.
<br>

https://github.com/gCattt/aerosol-indoor/assets/78471254/1b51b7d1-a91b-427d-ad98-669352f237d0.mp4

<hr>

### Acknowledgements
- https://github.com/paulvha/sps30
