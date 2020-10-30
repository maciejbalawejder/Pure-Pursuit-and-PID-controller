# Pure-Pursuit-and-PID-controller

## Description: 
* Pure Pursuit 
- it based on look-ahead point and the fixed distance between the point and the center of the rear axle, it assumes no-slip conditions and ignores dynamic forces. To adjust it for higher speeds the look-ahead distance can be represented by constant Kdd and forward velocity vc (ld=Kdd*vc).

* PID 
- basic PID controller which is not accurately calibrated, so I would no suggest using a test value provided in a file.

* Soon I will make a video with an explanation in-depth about the mathematics background behind both controllers.

## Implementation: 
* The example of implementation can be found in file controller2d.py at line 120 where you can find initialization and further down at line 170(PID) and 184(Pure Pursuit).

* Classes(Controllers.py file):
- PID
- Pure_pursuit

## Requirements:
* Python 3.5 or 3.6 
* Libraries: 
- Pillow>=3.1.2
- numpy>=1.14.5
- protobuf>=3.6.0
- pygame>=1.9.4
- matplotlib>=2.2.2
- future>=0.16.0
- scipy>=0.17.0
* CarlaUE4


## To do: 
- autotuning PID controller such as PIDNN or implementing twiddle
- tuning Pure Pursuit controller to achive more smooth approach to the corners or try to implement Stanley
