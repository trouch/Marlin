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
* Quick Commands Menu
    * Home (and Center Head)
    * Home/Preheat (PLA)
    * Home/Preheat (PETG)
    * Home & Level Bed
    * Extrude 100mm


# Variants
## Creality 1.1.x mainboard
These variants cover ATMega1284p based mainboards from Creality, including silent boards. Because of lack of available program memory, you'll have to choose variant according to your needs. SD card supports requires a lot program memory, then ABL with BL-Touch. If you need ABL, High-Quality features and filament change, your best take is to use Octoprint and a firwmare without SD card support.

| Variant                       | Lang | Extr. | ABL     | SD  | HQ  | Fil. Chg. | Menu  | EEPROM | Usage |
|-------------------------------|:----:|:-----:|:-------:|:---:|:---:|:---------:|:-----:|:------:|:-----:|
| tr300_noabl                   | EN   | Stock | NO      | YES | YES | YES       | YES   | YES    | 99.6% |
| tr300_bltouch_sd              | EN   | Stock | BLTouch | YES | NO  | NO        | NO    | YES    | 99.2% |
| tr300_bltouch_nosd            | EN   | Stock | BLTouch | NO  | YES | YES       | YES   | ALL    | 99.8% |
| tr300_touchmi_sd              | EN   | Stock | TouchMi | YES | NO  | NO        | NO    | YES    | 96.5% |
| tr300_touchmi_nosd            | EN   | Stock | TouchMi | NO  | YES | YES       | YES   | ALL    | 98.0% |
| tr300_noabl_bmg               | EN   | BMG   | NO      | YES | YES | YES       | YES   | YES    | 99.6% |
| tr300_bltouch_sd_bmg          | EN   | BMG   | BLTouch | YES | NO  | NO        | NO    | YES    | 99.2% |
| tr300_bltouch_nosd_bmg        | EN   | BMG   | BLTouch | NO  | YES | YES       | YES   | ALL    | 99.8% |
| tr300_touchmi_sd_bmg          | EN   | BMG   | TouchMi | YES | NO  | NO        | NO    | YES    | 96.5% |
| tr300_touchmi_nosd_bmg        | EN   | BMG   | TouchMi | NO  | YES | YES       | YES   | ALL    | 98.0% |
| tr300_noabl_fr                | FR   | Stock | NO      | YES | YES | YES       | NO    | YES    | 100%  |
| tr300_bltouch_sd_fr           | FR   | Stock | BLTouch | YES | NO  | NO        | NO    | MIN    | 100%  |
| tr300_bltouch_nosd_fr         | FR   | Stock | BLTouch | NO  | YES | YES       | NO    | YES    | 99.2% |
| tr300_touchmi_sd_fr           | FR   | Stock | TouchMi | YES | NO  | NO        | NO    | YES    | 97.8% |
| tr300_touchmi_nosd_fr         | FR   | Stock | TouchMi | NO  | YES | YES       | NO    | ALL    | 98.4% |
| tr300_noabl_bmg_fr            | FR   | BMG   | NO      | YES | YES | YES       | NO    | YES    | 100%  |
| tr300_bltouch_sd_bmg_fr       | FR   | BMG   | BLTouch | YES | NO  | NO        | NO    | MIN    | 100%  |
| tr300_bltouch_nosd_bmg_fr     | FR   | BMG   | BLTouch | NO  | YES | YES       | NO    | YES    | 99.2% |
| tr300_touchmi_sd_bmg_fr       | FR   | BMG   | TouchMi | YES | NO  | NO        | NO    | YES    | 97.8% |
| tr300_touchmi_nosd_bmg_fr     | FR   | BMG   | TouchMi | NO  | YES | YES       | NO    | ALL    | 98.4% |


## Fysetc Cheetah mainboard
These variants cover STM32F1 based mainboard from Fysetc who provides the very first direct drop-in replacement 32-bits based mainboard for the Ender series. Not only it has TMC2209 silent stepper drivers, it also has a much faster micro-controller with plenty of program memory available. No matter of ABL, you'll get all the features of Marlin you need !

| Variant                     | Lang | Extr. | ABL     | SD  | HQ  | Fil. Chg. | Menu  | EEPROM | 
|-----------------------------|:----:|:-----:|:-------:|:---:|:---:|:---------:|:-----:|:------:|
| tr300cheetah_noabl          | EN   | Stock | NO      | YES | YES | YES       | YES   | ALL    | 
| tr300cheetah_bltouch        | EN   | Stock | BLTouch | YES | YES | YES       | YES   | ALL    | 
| tr300cheetah_touchmi        | EN   | Stock | TouchMi | YES | YES | YES       | YES   | ALL    | 
| tr300cheetah_noabl_bmg      | EN   | BMG   | NO      | YES | YES | YES       | YES   | ALL    | 
| tr300cheetah_bltouch_bmg    | EN   | BMG   | BLTouch | YES | YES | YES       | YES   | ALL    | 
| tr300cheetah_touchmi_bmg    | EN   | BMG   | TouchMi | YES | YES | YES       | YES   | ALL    | 
| tr300cheetah_noabl_fr       | FR   | Stock | NO      | YES | YES | YES       | YES   | ALL    | 
| tr300cheetah_bltouch_fr     | FR   | Stock | BLTouch | YES | YES | YES       | YES   | ALL    | 
| tr300cheetah_btouchmi_fr    | FR   | Stock | TouchMi | YES | YES | YES       | YES   | ALL    | 
| tr300cheetah_noabl_bmg_fr   | FR   | BMG   | NO      | YES | YES | YES       | YES   | ALL    | 
| tr300cheetah_bltouch_bmg_fr | FR   | BMG   | BLTouch | YES | YES | YES       | YES   | ALL    | 
| tr300cheetah_touchmi_bmg_fr | FR   | BMG   | TouchMi | YES | YES | YES       | YES   | ALL    | 
