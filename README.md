# Robots in Grasshopper
🤖 + 🦗

A collection of plugins and software that can be used to control industrial robots with Grasshopper in Rhinoceros3D.
### Compiled by [Robin Godwyll](github.com/robin-gdwl)  
**Work in Progress**. [Raise an Issue](https://github.com/boundlessmaking/Robots-in-Grasshopper/issues) or pull request if a plugin is missing or information is incorrect.   
Not all Plugins have been tested by me. Use at your own Risk.   
The list tries to sort the plugins by accessibility (price, robot brands supported, open-source), It is not a ranking in functionality or quality. 


# Overview

| NAME                         |PRICE                                           | KUKA                                                                          |      ABB         | UR               |other<br>robot<br>brands                              | Operating systems*                                          |Link                                                                                                                                                                                                |
| ----------                   |:-------------:                                 |:----------------:                                                             |:----------------:|:----------------:|:--:                                                  |:------------:                                               |---                                                                                                                                                                                                 |
|[Robots](#Robots)             | **Free** (open source)                         |:white_check_mark:                                                             |:white_check_mark:|:white_check_mark:|Staubli                                               |Win  <br>MacOS                                               |[github](https://github.com/visose/Robots)                                                                                                                                                          |
|[MACHINA](#Machina)           | **Free** (open source)                         |:white_check_mark:                                                             |:white_check_mark:|:white_check_mark:|:x:                                                   |Win                                                          |[Food4Rhino](https://www.food4rhino.com/app/machina)<br> [github](https://github.com/RobotExMachina)                                                                                                |
|[Furobot](#Furobot)           | **Free**                                       |:white_check_mark:                                                             |:white_check_mark:|:white_check_mark:|[custom Robot creation inside gh](https://fabunion.github.io/Tutorial/CustRobot.html)    |Win                                                          |[Food4Rhino](https://www.food4rhino.com/app/furobot)<br>[Website](http://www.fab-union.com/en/col.jsp?id=103)                                                    |
|[HAL Robotics](#HAL)          | £800/yr<br>£60/yr (academic)<br>Free trial     |:white_check_mark:                                                             |:white_check_mark:|:white_check_mark:|:x:                                                   |Win                                                          |[Food4Rhino(old)](https://www.food4rhino.com/app/hal-robot-programming-control)<br> [Food4Rhino(new)](https://www.food4rhino.com/app/hal-robotics-framework)<br>[Website](https://hal-robotics.com/)|
|[Axis](#Axis)                 | **Free** (open source)                         |:question:                                                                     |:white_check_mark:|:x:               |[custom Robot creation inside gh](https://github.com/AxisArch/Axis/wiki/Custom-Robot)    |Win                  |[github](https://github.com/AxisArch/Axis)                                                                                                                                                               |
|[Robot Components](#RobotComp)| **Free**  (open source)                        |:x:                                                                            |:white_check_mark:|:x:               |:x:                                                   |Win                                                          |[github](https://github.com/EDEK-UniKassel/RobotComponents)<br> [Food4Rhino](https://www.food4rhino.com/app/robot-components#) <br> [Documentation](https://robotcomponents.github.io/RobotComponents-Documentation/) |
|[KUKA PRC](#KukaPRC)          | Free (limited)<br> 450€/yr<br>95€/yr (Student) |:white_check_mark:                                                             |:x:               |:x:               |:x:                                                   |Win                                                          |[Food4Rhino](https://www.food4rhino.com/app/kukaprc-parametric-robot-control-grasshopper)<br> [Website](https://www.robotsinarchitecture.org/kuka-prc)                                              |
|[Taco ABB](#TacoABB)          | **Free**                                       | :x:                                                                           |:white_check_mark:|:x:               |:x:                                                   |Win                                                          |[Food4Rhino](https://www.food4rhino.com/app/taco-abb)<br> [Website](http://blickfeld7.com/architecture/rhino/grasshopper/Taco/)                                                                     |
|[Taco HIWIN](#TacoHIWIN)      | **Free**                                       | :x:                                                                           |:x:               |:x:               |[**HIWIN**](https://www.hiwin.tw/products/mar/multi_axis_robot_list.aspx)                     |Win                  |[Food4Rhino](https://www.food4rhino.com/app/taco-hiwin)<br> [Facebook](https://www.facebook.com/rosocoop/)                                                                                          |
|[RoboDK](#RoboDK)             | Free trial<br>145€(Edu)<br>2995€(Pro)          |:white_check_mark:                                                             |:white_check_mark:|:white_check_mark:|many others<br>[see here](https://robodk.com/library) |Win + Others ([standalone App](https://robodk.com/download)) |[Food4Rhino](https://www.food4rhino.com/app/robodk)<br> [Website](https://robodk.com/)                                                                                                              |
|[Cobra (Easyrobot)](#Cobra)   | **Free** (open source)                         |[KR6-10R900](www.kuka.com/en-de/products/robot-systems/industrial-robots/kr-agilus) |:x:          |:x:               |:x:                                                   |Win                                                          |[Food4Rhino](https://www.food4rhino.com/app/cobra)<br>[github](https://github.com/richardgolee/EasyRobot)                                                                                           |
|[Robot Fabrication Design](#RFD)| **Free**                                     |[KR 120 R2500](www.google.com/search?q=KR+120+R2500+pro)                       |:x:               |:x:               |:x:                                                   |Win                                                          |[Food4Rhino](https://www.food4rhino.com/app/rfdrobotic-fabrication-design)<br>[Website](https://www.mxmarchitects.com/lab-mxm)                                                                      |
|[Scorpion](#Scorpion)         | **Free** (open source)                         | :x:                                                                           |:x:               |:white_check_mark:|:x:                                                   |Win                                                          |[Food4Rhino](https://www.food4rhino.com/app/scorpion)<br>                                                                                                                                           |
|[RHINOROBOT 4](#Rhinorobot4)  | 1800€ (commercial) <br> 1170€ (30 seat education lab license)|:white_check_mark:                                                |:white_check_mark:|:white_check_mark:|Staubli, Yaskawa, Fanuc, others                       |Win                                                          |[Food4Rhino](https://www.food4rhino.com/en/app/rhinorobot-4) [Website](https://www.kinematiq.net/fr/rhinorobot/)                                                                                        |
|~~[Rapcam](#Rapcam)~~         | 150€/month<br>Free trial                       |:white_check_mark:                                                             |:white_check_mark:|:x:               |Fanuc                                                 |Win                                                          |~~[Food4Rhino](https://www.food4rhino.com/app/rapcam-gh)<br> [Website](https://www.rapcam.eu/)~~                                                                                                    |
|~~[ROBOTS IO](#RobotsIO)~~    | £166 /yr (Edu) <br> £1999 /yr (Pro)            |:white_check_mark:                                                             |:white_check_mark:|:white_check_mark:|Fanuc                                                 |Win                                                          |[Developer Website](https://www.robofold.com/make/software/IO)<br> [Forum](https://www.grasshopper3d.com/group/io)<br>[Archived Website](https://web.archive.org/web/20170921144658/https://robots.io/wp/) |

\* information according to Food4Rhino.com, some plugins might also work in Rhino/Grasshopper for Mac. Let me know if you are using one of the plugins on a mac and it works. 

# Details

<a name="Robots"></a>
## Robots

Website:  [github.com/visose/Robots](https://github.com/visose/Robots)  
Download:  [via github](https://github.com/visose/Robots/wiki#installation)  
Price:  **Free** (Open source Plugin)
Developed by: [Vicente Soler](https://github.com/visose)   
Robot brands : **Kuka  ABB  UR  Staubli**  
  

| offline programming |command streaming | Visualisation    |External axis support|
| ----------          |:-------------:   |:-------------:   |:-------------------:|
| :white_check_mark:  |:white_check_mark:|:white_check_mark:|:white_check_mark:   |


___
<a name="Machina"></a>
## MACHINA
Website: [github.com/RobotExMachina](https://github.com/RobotExMachina)  
Download: [GH Plugin on Food4Rhino.com](https://www.food4rhino.com/app/machina#downloads_list)  
Research Publications:  [Machina.NET: A Library for Programming [...] Industrial Robots](http://doi.org/10.5334/jors.247)    
Price: **Free** (Open source) Framework written in **C#**  
Developed by: [Jose Luis Garcia del Castillo](https://github.com/garciadelcastillo)   
Robot brands : **Kuka** (no command streaming)  **ABB  UR** 

Description:  
Machina is a .NET library for action-based real-time control of mechanical actuators. Plugins for Grasshopper and Revit can be used with an app called Machina-Bridge to stream commands directly to a robot. 

"Or in more human terms, it allows you to talk to a robot and tell it what to do."

| offline programming |command streaming | Visualisation |External axis support|    
| ----------          |:-------------:   |:-------------:|:-------------------:|
| :white_check_mark:  |:white_check_mark:|:x: **\***     |:white_check_mark:   |

**\* Visualisation:** can be done externally for ABB Robots with ABB Robot Studio


___
<a name="Axis"></a>
## AxisArch - Axis
Website:  [github.com/AxisArch/Axis](https://github.com/AxisArch/Axis)  

Price: **Free** (Open source; written in C#)  

Developed by: [Ryan Hughes](https://github.com/rhughes42), [Povl Filip Sonne-Frederiksen](https://github.com/pfmephisto), [axisarch.tech](https://axisarch.tech/framework)  
Robot brands : **ABB** **Kuka** (not fully supported)     

Description:  
Axis is a plugin for Rhino/Grasshopper a 3D modeling and parametric design framework for designers and architects.
It offers the following components: 
- Main components such as Code Generator or Simulation.
- Connections and interactions with **live controllers**.
- Set Up which are secondary components to set settings such as speed and zone

| offline programming |command streaming | Visualisation    |External axis support|
| ----------          |:-------------:   |:----------------:|:-------------------:|
| :white_check_mark:  |:white_check_mark:|:white_check_mark:|:question:           |

___
<a name="HAL"></a>
## HAL Robotics
Website:  [hal-robotics.com](https://hal-robotics.com/)  

Price:    
    - Professional: £800+  /yr   
    - Academic ( non commerical use): £60+ /yr  

Developed by: [HAL Robotics](https://hal-robotics.com/)   
Robot brands : **Kuka ABB  UR Staubli**    

| offline programming |command streaming | Visualisation    |External axis support|
| ----------          |:-------------:   |:----------------:|:-------------------:|
| :white_check_mark:  |:white_check_mark:|:white_check_mark:|:question:           |


___
<a name="KukaPRC"></a>
## KUKA PRC
Website:   
    [Food4Rhino.com](https://www.food4rhino.com/app/kukaprc-parametric-robot-control-grasshopper)   
    [robotsinarchitecture.org](https://www.robotsinarchitecture.org/kuka-prc)   
Download:  [robotsinarchitecture.org](https://www.robotsinarchitecture.org/kuka-prc)  
Support/Tutorials: [Forum]([robotsinarchitecture.org](https://www.robotsinarchitecture.org/kuka-prc))  
Research Publications: [Adaptive Industrial Robot Control for Designers](https://www.researchgate.net/publication/319944935_Adaptive_Industrial_Robot_Control_for_Designers)   
Price:  
    - Academic/Lab: 350€  /yr   
    - Evaluation: **Free**  
Developed by: [Robotsinarchitecture](https://www.robotsinarchitecture.org/kuka-prc)   
Robot brands : **Kuka**   

| offline programming |command streaming | Visualisation    |External axis support|
| ----------          |:-------------:   |:----------------:|:-------------------:|
| :white_check_mark:  |:white_check_mark:|:white_check_mark:|:white_check_mark:   |

___
<a name="Scorpion"></a>
## Scorpion
Website:   
[Food4Rhino.com ](https://www.food4rhino.com/app/scorpion)  
~~[scorpion-robotics.org](http://scorpion-robotics.com/)~~  (offline, [Archived](https://web.archive.org/web/20170601033032/http://scorpion-robotics.com/))  
Download:  [Food4Rhino.com](https://www.food4rhino.com/app/scorpion#downloads_list)    
Research Publications:  [Automated Construction Using Adaptive Programing](https://www.researchgate.net/publication/300721200_An_Approach_to_Automated_Construction_Using_Adaptive_Programing)  
Price: **Free** (open source Grasshopper component)  
Developed by: [Khaled Elashry](https://www.researchgate.net/profile/Khaled_Elashry2) - [Vincent Huyghe](https://www.ucl.ac.uk/bartlett/architecture/vincent-huyghe) - [Ruairi Glynn  ](https://www.researchgate.net/profile/Ruairi_Glynn)  
Robot brands : **UR** (Visualisation only for UR10)   
Description:  
Scorpion is an open source robotic controller for Industrial Robots currently in beta.
Scorpion contains tools to control universal robots industrial robots, Including:  
Easy generation of robotic programs from paths,  
Inverse kinematic solver for universal robots,    
Direct upload to the robots through TCP/IP,  
End-effector Tools 

| offline programming |command streaming | Visualisation    |External axis support|
| ----------          |:-------------:   |:-------------:   |:-------------------:|
| :white_check_mark:  |:white_check_mark:|:white_check_mark:|:x:                  |

___
<a name="TacoABB"></a>
## Taco ABB
Website:  
[Food4Rhino.com](https://www.food4rhino.com/app/taco-abb)   
[blickfeld7.com](http://blickfeld7.com/architecture/rhino/grasshopper/Taco/)    
Download:  [blickfeld7.com](http://blickfeld7.com/downloads/installer/Taco.zip)      
Research Publications utilising this plugin:  
[Tool Path Generator for Artistic Drawing with Industrial Robot](https://www.researchgate.net/publication/338598379_Tool_Path_Generator_for_Artistic_Drawing_with_Industrial_Robot)  
[Robotic Formwork in the MARS Pavilion](http://papers.cumincad.org/data/works/att/acadia17_522.pdf)  
[Robotic Fabrication Workflows for Environmentally Driven Facades](https://vtechworks.lib.vt.edu/bitstream/handle/10919/92001/Cabrera_PM_T_2019.pdf?sequence=1)  
Price:  **Free**   
Developed by: [blickfeld7](http://blickfeld7.com/architecture/rhino/grasshopper/Taco/)   
Robot brands : **ABB**  
Description:  
TACO-ABB is a free and user-friendly programming plugin for the simulation and control of ABB industrial robots directly within Grasshopper. Taco offers users to program and visualize ABB robots with parametrics.  

| offline programming |command streaming | Visualisation    |External axis support|
| ----------          |:-------------:   |:----------------:|:-------------------:|
| :white_check_mark:  |:white_check_mark:|:white_check_mark:|:x:   |

___
<a name="TacoHIWIN"></a>
## Taco HIWIN
Developed by: [Shih-Yuan Wang](https://www.arch.nctu.edu.tw/en/people-2/shihyuanwang-2/), Yu-Ting Sheng, Florian Frank
__to be added__
___
<a name="RoboDK"></a>
## RoboDK 
Website: [RobotDK doc](https://robodk.com/doc/en/Plugin-Rhino.html)
Download: [Food4Rhino.com](https://www.food4rhino.com/app/robodk)
Research Publications:  
Price: [RobotDK prices](https://robodk.com/pricing)
Description:  

___
<a name="Cobra"></a>
## Cobra (EasyRobot)  
Developed by: [Richardgolee](https://github.com/richardgolee)  
Download: [Food4Rhino](https://www.food4rhino.com/en/app/cobra)  
Website: [github](https://github.com/richardgolee/EasyRobot)  
Description:  
Cobra(EasyRobot) is a very simple robotic controller, now only support KUKA KR6-10R900 Robot. It could provide solution to most tasks and generate src file.  
___
<a name="RFD"></a>
## Robotic Fabrication Design
Download: [Food4Rhino.com](https://www.food4rhino.com/app/rfdrobotic-fabrication-design)
Developed by: [MXM-Architects](https://www.mxmarchitects.com/lab-mxm)
__to be added__
___
<a name="Furobot"></a>
## Furobot

Website:  [fabunion.github.io](https://fabunion.github.io/)
Download:  [Food4Rhino](https://www.food4rhino.com/en/app/furobot)

Research Publications:  
Price:  **Free**
Developed by:   [Fab-Union](http://www.fab-union.com/en/col.jsp?id=101)   
Robot brands : **Kuka ABB UR**  
Description:  
FUROBOT is a robot programming platform developed by Fab-Union for the construction industry.
The purpose of FUROBOT is to program on robot more easily,and convert the design into real object with little effort by using some technique packages.  

|offline programming|command streaming | Visualisation    |External axis support|
|-------------------|:-------------:   |:----------------:|:-------------------:|
|:white_check_mark: |:white_check_mark:|:white_check_mark:|:white_check_mark:   |


___
<a name="RobotComp"></a>
## Robot Components
__to be added__   
Website:  
Download:  
Research Publications:  
Price:  
Developed by [EDEK-UniKassel](https://github.com/EDEK-UniKassel)  
Robot brands : **ABB**
Description:  

| offline programming |command streaming | Visualisation    |External axis support|
| ----------          |:-------------:   |:-------------:   |:-------------------:|
| :white_check_mark:  |:white_check_mark:|:white_check_mark:|:white_check_mark:   |

___

<a name="Rhinorobot4"></a>
## Rhinorobot 4

Website:  [www.kinematiq.net/fr/rhinorobot/](https://www.kinematiq.net/fr/rhinorobot/)  
Download/Buy:  [www.kinematiq.net/boutique/)](https://www.kinematiq.net/boutique/)  
Price:  1800€ (commercial), 1170€ (30 seat education lab license)  
Developed by: [Kinematiq SAS](https://www.kinematiq.net/)  
Robot brands : **Kuka  ABB  UR  Staubli Yaskawa**  
Description:  
RhinoRobot is a complete, affordable, and easy off-line programming and simulation plugin for Rhinoceros 3D, to handle all types of applications on industrial robots.  

___
<a name="Rapcam"></a>
## Rapcam
Website:  
~~[rapcam.eu](https://www.rapcam.eu/software/rapcam-for-grasshopper/)~~  (offline, [archived](https://web.archive.org/web/20190207201747/https://www.rapcam.eu/))  
~~[Food4Rhino.com](https://www.food4rhino.com/app/rapcam)~~  
[Developer Website: raptech.io](https://www.raptech.io/)  
 
The Grasshopper Plugin Rapcam appears to be discontinued by the developers.
Youtube videos describing its functionality can still be found [here](https://www.youtube.com/channel/UCGIOlbL0PD9FBO_yz02_8nQ).  
The [company](https://www.raptech.io/) now offers a standalone software for robotic 3D-printing with concrete which can be found [here](https://www.raptech.io/rapcam).


___
<a name="RobotsIO"></a>
## ROBOTS IO
Website:  
[Developer Website: robofold.com](https://www.robofold.com/make/software/IO)    
~~[robots.io](robots.io/wp)~~  (offline, [archived](https://web.archive.org/web/20170921144658/https://robots.io/wp/))  
  
Description:  

ROBOTS IO seems to be discontinued by the developer. The website at [robots.io](http://www.robots.io/) is offline. You can find an archived version of the website [here](https://web.archive.org/web/20190207201747/https://www.rapcam.eu/).
Documentation of the plugin can be found in this [PDF](https://st2.ning.com/topology/rest/1.0/file/get/2811285740?profile=original).
 
