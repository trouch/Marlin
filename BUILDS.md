# TR-300 Firmware

An Ender-3 package with ready to use firmwares based on Marlin 2.

# Features

## Base Features
* THERMAL_PROTECTION_HOTENDS
* THERMAL_PROTECTION_BED
* PREVENT_COLD_EXTRUSION
* PIDTEMP
* PIDTEMPBED
* EEPROM_SETTINGS
    * MIN: CHITCHAT DISABLED, M503 DISABLED
    * YES: CHITCHAT ENABLED, M503 DISABLED
    * ALL: CHITCHAT ENABLED, M503 ENABLED

## Optional Features
* SD Card Support
* Automatic Bed Leveling (Bilinear)
    * BL-Touch
    * Touch-Mi
* HQ: High-Quality Features
    * S-Curve Acceleration
    * Linear Advance
* Filament Change / Load / Unload
* Extra **Menus**
    * PID Auto Tune
    * Software EndStop
    * Quick Commands
        * Home (and Center Head)
        * Home/Preheat (PLA)
        * Home/Preheat (PETG)
        * Home & Level Bed
        * Extrude 100mm


# Variants

Please download your firmware according to your need by choosing the right filename in the following tables.

All these variants are available in the [firmwares directory](./firmwares)

## Creality 1.1.x mainboard
These variants cover ATMega1284p based mainboards from Creality, including silent boards. Because of lack of available program memory, you'll have to choose variant according to your needs. SD card supports requires a lot program memory, then ABL with BL-Touch. If you need ABL, High-Quality features and filament change, your best take is to use Octoprint and a firwmare without SD card support.

| Filename                      | Lang | Extr. | ABL     | SD  | HQ  | Fil. Chg. | Menu  | EEPROM |
|-------------------------------|:----:|:-----:|:-------:|:---:|:---:|:---------:|:-----:|:------:|
| tr300_noabl                   | EN   | Stock | NO      | YES | YES | YES       | YES   | YES    |
| tr300_bltouch_sd              | EN   | Stock | BLTouch | YES | NO  | NO        | NO    | YES    |
| tr300_bltouch_nosd            | EN   | Stock | BLTouch | NO  | YES | YES       | YES   | YES    |
| tr300_touchmi_sd              | EN   | Stock | TouchMi | YES | NO  | NO        | NO    | YES    |
| tr300_touchmi_nosd            | EN   | Stock | TouchMi | NO  | YES | YES       | YES   | ALL    |
| tr300_noabl_bmg               | EN   | BMG   | NO      | YES | YES | YES       | YES   | YES    |
| tr300_bltouch_sd_bmg          | EN   | BMG   | BLTouch | YES | NO  | NO        | NO    | YES    |
| tr300_bltouch_nosd_bmg        | EN   | BMG   | BLTouch | NO  | YES | YES       | YES   | YES    |
| tr300_touchmi_sd_bmg          | EN   | BMG   | TouchMi | YES | NO  | NO        | NO    | YES    |
| tr300_touchmi_nosd_bmg        | EN   | BMG   | TouchMi | NO  | YES | YES       | YES   | ALL    |
| tr300_fr_noabl                | FR   | Stock | NO      | YES | YES | YES       | NO    | YES    |
| tr300_fr_bltouch_sd           | FR   | Stock | BLTouch | YES | NO  | NO        | NO    | MIN    |
| tr300_fr_bltouch_nosd         | FR   | Stock | BLTouch | NO  | YES | YES       | NO    | YES    |
| tr300_fr_touchmi_sd           | FR   | Stock | TouchMi | YES | NO  | NO        | NO    | YES    |
| tr300_fr_touchmi_nosd         | FR   | Stock | TouchMi | NO  | YES | YES       | NO    | ALL    |
| tr300_fr_noabl_bmg            | FR   | BMG   | NO      | YES | YES | YES       | NO    | YES    |
| tr300_fr_bltouch_sd_bmg       | FR   | BMG   | BLTouch | YES | NO  | NO        | NO    | MIN    |
| tr300_fr_bltouch_nosd_bmg     | FR   | BMG   | BLTouch | NO  | YES | YES       | NO    | YES    |
| tr300_fr_touchmi_sd_bmg       | FR   | BMG   | TouchMi | YES | NO  | NO        | NO    | YES    |
| tr300_fr_touchmi_nosd_bmg     | FR   | BMG   | TouchMi | NO  | YES | YES       | NO    | ALL    |


## 32-bits Fysetc Cheetah mainboard
These variants cover STM32F1 based mainboard from Fysetc who provides the very first direct drop-in replacement 32-bits based mainboard for the Ender series. Not only it has TMC2208/TMC2209 silent stepper drivers, it also has a much faster micro-controller with plenty of program memory available. No matter of ABL, you'll get all the features of Marlin you need !

### Cheetah 1.1 (TMC2209)
| Filename             | Lang | Extr. | ABL     | SD  | HQ  | Fil. Chg. | Menu  | EEPROM | 
|----------------------|:----:|:-----:|:-------:|:---:|:---:|:---------:|:-----:|:------:|
| tr329_noabl          | EN   | Stock | NO      | YES | YES | YES       | YES   | ALL    | 
| tr329_bltouch        | EN   | Stock | BLTouch | YES | YES | YES       | YES   | ALL    | 
| tr329_touchmi        | EN   | Stock | TouchMi | YES | YES | YES       | YES   | ALL    | 
| tr329_noabl_bmg      | EN   | BMG   | NO      | YES | YES | YES       | YES   | ALL    | 
| tr329_bltouch_bmg    | EN   | BMG   | BLTouch | YES | YES | YES       | YES   | ALL    | 
| tr329_touchmi_bmg    | EN   | BMG   | TouchMi | YES | YES | YES       | YES   | ALL    | 
| tr329_fr_noabl       | FR   | Stock | NO      | YES | YES | YES       | YES   | ALL    | 
| tr329_fr_bltouch     | FR   | Stock | BLTouch | YES | YES | YES       | YES   | ALL    | 
| tr329_fr_touchmi     | FR   | Stock | TouchMi | YES | YES | YES       | YES   | ALL    | 
| tr329_fr_noabl_bmg   | FR   | BMG   | NO      | YES | YES | YES       | YES   | ALL    | 
| tr329_fr_bltouch_bmg | FR   | BMG   | BLTouch | YES | YES | YES       | YES   | ALL    | 
| tr329_fr_touchmi_bmg | FR   | BMG   | TouchMi | YES | YES | YES       | YES   | ALL    | 

### Cheetah 1.2 (TMC2208)
| Filename             | Lang | Extr. | ABL     | SD  | HQ  | Fil. Chg. | Menu  | EEPROM | 
|----------------------|:----:|:-----:|:-------:|:---:|:---:|:---------:|:-----:|:------:|
| tr328_noabl          | EN   | Stock | NO      | YES | YES | YES       | YES   | ALL    | 
| tr328_bltouch        | EN   | Stock | BLTouch | YES | YES | YES       | YES   | ALL    | 
| tr328_touchmi        | EN   | Stock | TouchMi | YES | YES | YES       | YES   | ALL    | 
| tr328_noabl_bmg      | EN   | BMG   | NO      | YES | YES | YES       | YES   | ALL    | 
| tr328_bltouch_bmg    | EN   | BMG   | BLTouch | YES | YES | YES       | YES   | ALL    | 
| tr328_touchmi_bmg    | EN   | BMG   | TouchMi | YES | YES | YES       | YES   | ALL    | 
| tr328_fr_noabl       | FR   | Stock | NO      | YES | YES | YES       | YES   | ALL    | 
| tr328_fr_bltouch     | FR   | Stock | BLTouch | YES | YES | YES       | YES   | ALL    | 
| tr328_fr_touchmi     | FR   | Stock | TouchMi | YES | YES | YES       | YES   | ALL    | 
| tr328_fr_noabl_bmg   | FR   | BMG   | NO      | YES | YES | YES       | YES   | ALL    | 
| tr328_fr_bltouch_bmg | FR   | BMG   | BLTouch | YES | YES | YES       | YES   | ALL    | 
| tr328_fr_touchmi_bmg | FR   | BMG   | TouchMi | YES | YES | YES       | YES   | ALL    | 
