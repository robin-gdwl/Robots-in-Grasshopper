# Robots in Grasshopper
🤖 + 🦗

A repository of plugins and Software that can be used to control industrial robots with Grasshopper in Rhino3D.
### Compiled by Robin Godwyll
Work in Progress [Raise an Issue](https://github.com/boundlessmaking/Robots-in-Grasshopper/issues) or pull request if a plugin is missing or information is incorrect.


# Overview

| NAME                  |COST                                                     | KUKA             |      ABB         | UR               | Fanuc            |other<br>robot<br>brands                              |Link                                                                                                                                                                                                |
| ----------                     |:-------------:                                 |:----------------:|:----------------:|:----------------:|:----------------:|:--:                                                  |---                                                                                                                                                                                                 |
|[Robots](#Robots)               | **Free** (open source)                         |:white_check_mark:|:white_check_mark:|:white_check_mark:|:x:               |Staubli                                                   |[github](https://github.com/visose/Robots)                                                                                                                                                      |
|[MACHINA](#Machina)             | **Free** (open source)                         |:white_check_mark:|:white_check_mark:|:white_check_mark:|:x:               |:x:                                                   |[Food4Rhino](https://www.food4rhino.com/app/machina)<br> [github](https://github.com/RobotExMachina)                                                                                                |
|[Furobot](#Furobot)             | **Free**                                       |:white_check_mark:|:white_check_mark:|:white_check_mark:|:x:               |:x:                                                   |[Food4Rhino](https://www.food4rhino.com/app/furobot)<br>[Website](http://www.fab-union.com/en/col.jsp?id=103)        |
|[HAL Robotics](#HAL)            | £800/yr<br>£60/yr (academic)<br>Free trial     |:white_check_mark:|:white_check_mark:|:white_check_mark:|:x:               |:x:                                                   |[Food4Rhino(old)](https://www.food4rhino.com/app/hal-robot-programming-control)<br> [Food4Rhino(new)](https://www.food4rhino.com/app/hal-robotics-framework)<br>[Website](https://hal-robotics.com/)|
|[KUKA PRC](#KukaPRC)            | Free (limited)<br> 450€/yr<br>95€/yr (Student) |:white_check_mark:|:x:               |:x:               |:x:               |:x:                                                   |[Food4Rhino](https://www.food4rhino.com/app/kukaprc-parametric-robot-control-grasshopper)<br> [Website](https://www.robotsinarchitecture.org/kuka-prc)                                              |
|[Scorpion](#Scorpion)           | **Free** (open source)                                    | :x:              |:x:               |:white_check_mark:|:x:               |:x:                                                   |[Food4Rhino](https://www.food4rhino.com/app/scorpion)<br>                                                                                                                                           |
|[Taco ABB](#Taco)               | **Free**                                       | :x:              |:white_check_mark:|:x:               |:x:               |:x:                                                   |[Food4Rhino](https://www.food4rhino.com/app/taco-abb)<br> [Website](http://blickfeld7.com/architecture/rhino/grasshopper/Taco/)                                                                     |
|[Robot Components](#RobotComp)  | **Free**  (open source)                        |:x:               |:white_check_mark:|:x:               |:x:               |:x:                                                   |[github](https://github.com/EDEK-UniKassel/RobotComponents)                         |
|[RoboDK](#RoboDK)               | Free trial<br>145€(Edu)<br>2995€(Pro)          |:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|many others<br>[see here](https://robodk.com/library) |[Food4Rhino](https://www.food4rhino.com/app/robodk)<br> [Website](https://robodk.com/)                                                                                                              |
|~~[Rapcam](#Rapcam)~~           | 150€/month<br>Free trial                       |:white_check_mark:|:white_check_mark:|:x:               |:white_check_mark:|:x:                                                   |~~[Food4Rhino](https://www.food4rhino.com/app/rapcam-gh)<br> [Website](https://www.rapcam.eu/)~~                                                                                                    |
|~~[ROBOTS IO](#RobotsIO)~~      | **Free**                                       |:white_check_mark:|:question:        |:question:        |:question:        |:question:                                            |[Website](https://www.robofold.com/make/software/IO)<br> [Forum](https://www.grasshopper3d.com/group/io)                                                                                            |

# Descriptions

<a name="Robots"></a>
## Robots

Developed by: [Vicente Soler](https://github.com/visose)   
Robot brands : **Kuka  ABB  UR  Staubli**

| offline programming |command streaming | Visualisation    |External axis support|
| ----------          |:-------------:   |:-------------:   |:-------------------:|
| :white_check_mark:  |:white_check_mark:|:white_check_mark:|:white_check_mark:   |


___
<a name="Machina"></a>
## MACHINA
Developed by: [Jose Luis Garcia del Castillo](https://github.com/garciadelcastillo)   
Robot brands : **Kuka** (no command streaming)  **ABB  UR**

| offline programming |command streaming | Visualisation |External axis support|    
| ----------          |:-------------:   |:-------------:|:-------------------:|
| :white_check_mark:  |:white_check_mark:|:x: **\***          |:white_check_mark:   |

**\* Visualisation:** can be done externally for ABB Robots with ABB Robot Studio

___
<a name="HAL"></a>
## HAL Robotics
Developed by: [HAL Robotics](https://hal-robotics.com/)   
Robot brands : **Kuka ABB  UR Staubli**

| offline programming |command streaming | Visualisation    |External axis support|
| ----------          |:-------------:   |:----------------:|:-------------------:|
| :white_check_mark:  |:white_check_mark:|:white_check_mark:|:question:           |


___
<a name="KukaPRC"></a>
## KUKA PRC
Developed by: [Robotsinarchitecture](https://www.robotsinarchitecture.org/kuka-prc)   
Robot brands : **Kuka**

| offline programming |command streaming | Visualisation    |External axis support|
| ----------          |:-------------:   |:----------------:|:-------------------:|
| :white_check_mark:  |:white_check_mark:|:white_check_mark:|:white_check_mark:   |

___
<a name="Scorpion"></a>
## Scorpion
Developed by: Khaled ElAshry - Vincent Huyghe - Ruairi Glynn  
Robot brands : **UR** (Visualisation only for UR10)

| offline programming |command streaming | Visualisation    |External axis support|
| ----------          |:-------------:   |:-------------:   |:-------------------:|
| :white_check_mark:  |:white_check_mark:|:white_check_mark:|:x:                  |

___
<a name="Taco"></a>
## Taco ABB
Developed by: [blickfeld7](http://blickfeld7.com/architecture/rhino/grasshopper/Taco/)   
Robot brands : **ABB**

| offline programming |command streaming | Visualisation    |External axis support|
| ----------          |:-------------:   |:----------------:|:-------------------:|
| :white_check_mark:  |:white_check_mark:|:white_check_mark:|:x:   |

___
<a name="RoboDK"></a>
## RoboDK
to be added

___
<a name="Furobot"></a>
## Furobot
Developed by: [Fab-Union](http://www.fab-union.com/en/col.jsp?id=101)   
Robot brands : **Kuka ABB UR**

|offline programming|command streaming | Visualisation    |External axis support|
|-------------------|:-------------:   |:----------------:|:-------------------:|
|:white_check_mark: |:white_check_mark:|:white_check_mark:|:white_check_mark:   |


___
<a name="RobotComp"></a>
## Robot Components
Developed by [EDEK-UniKassel](https://github.com/EDEK-UniKassel)  
Robot brands : **ABB**

| offline programming |command streaming | Visualisation    |External axis support|
| ----------          |:-------------:   |:-------------:   |:-------------------:|
| :white_check_mark:  |:white_check_mark:|:white_check_mark:|:x:                  |

___
<a name="Rapcam"></a>
## Rapcam
Rapcam appears to be discontinued by the developers.

___
<a name="RobotsIO"></a>
## ROBOTS IO
ROBOTS IO seems to be discontinued by the developer. The Website does not exist anymore [robots.io](http://www.robots.io/)
