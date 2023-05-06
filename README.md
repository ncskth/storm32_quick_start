[storm32 repo](https://github.com/olliw42/storm32bgc)

### Configuration tool
The configuration tool runs fine on linux using Wine. You might need to remap the COM-port to the linux equivalent in `wine regedit`. [link](https://wiki.winehq.org/index.php?title=Wine_User%27s_Guide&oldid=2519#Serial_and_Parallel_Ports)


With this tool you can configure and calibrate some parameters for the gimbal. I have created an example configuration, `config.cfg`, which you can load to get a decent setup for the gimbal. The PID parameters will depend on your camera so those might need to be updated. Set them to the lowest non-zero value possible and follow [this](http://www.olliw.eu/storm32bgc-wiki/Tuning_Recipe)


### Control
It can easily be controlled through its virtual serial port. See [Serial Communication](http://www.olliw.eu/storm32bgc-wiki/Serial_Communication) on the storm32 wiki. For a super basic implementation see `storm_example.py`


### Hardware
The gimbal has to be balanced by mounting a camera before you can use it. It doesn't have to be particularly precise but it should face mostly forward in its resting position.

The gimbal uses an old version of the hardware and therefore run the ancient V0.90 of the firmware. The difference to newer revisions is that the sensors use a complex NT bus instead of regular I2C.

On startup the gimbal will calibrate for ~20 seconds and then beep once it's ready to use.