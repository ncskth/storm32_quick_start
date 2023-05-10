### STorM32 Gimbal
For more reading please see the STorM32's [github repo](https://github.com/olliw42/storm32bgc) and their [wiki](http://www.olliw.eu/storm32bgc-wiki/Getting_Started). This README is just mentions a few pitfalls.


### Configuration tool
The configuration tool runs fine on Linux using Wine. You might need to remap the COM-port to the Linux equivalent (/dev/ttyACM) in `wine regedit`. [link](https://wiki.winehq.org/index.php?title=Wine_User%27s_Guide&oldid=2519#Serial_and_Parallel_Ports).


With this tool you can configure and calibrate some parameters for the gimbal. I have created an example configuration, `config.cfg`, which you can load to get a decent first setup for the gimbal. The PID parameters will depend on your camera so those might need to be updated. Set them to the lowest non-zero value possible and follow [this](http://www.olliw.eu/storm32bgc-wiki/Tuning_Recipe).


### Control
It can easily be controlled through its virtual serial port. See [Serial Communication](http://www.olliw.eu/storm32bgc-wiki/Serial_Communication) on the storm32 wiki. For a super basic implementation see `storm_example.py`.


### Hardware
The gimbal has to be balanced by mounting a camera before you can use it. If it is too unbalanced it will not work at all.


The gimbal uses an old version of the hardware and therefore runs the ancient V0.90 of the firmware. The difference is that newer models use a complex NT bus instead of regular I2C.


On startup the gimbal will calibrate for ~20 seconds and then beep once it's ready to use.

It supports both the standing and hanging orientation as long as you configure it. `config.cfg` is for a standing mount.