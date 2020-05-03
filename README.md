# Robots in Grasshopper
🤖 + 🦗

A repository of plugins and Software that can be used to control industrial robots with Grasshopper in Rhino3D.
### Compiled by Robin Godwyll
Work in Progress [Raise an Issue](https://github.com/boundlessmaking/Robots-in-Grasshopper/issues) or pull request if a plugin is missing or information is incorrect.


# Overview

| NAME                           |COST                                            | KUKA             |      ABB         | UR               |other<br>robot<br>brands                              | Operating systems*                                          |Link                                                                                                                                                                                                |
| ----------                     |:-------------:                                 |:----------------:|:----------------:|:----------------:|:--:                                                  |:----------------:                                           |---                                                                                                                                                                                                 |
|[Robots](#Robots)               | **Free** (open source)                         |:white_check_mark:|:white_check_mark:|:white_check_mark:|Staubli                                               |Win + MacOS                                                  |[github](https://github.com/visose/Robots)                                                                                                                                                          |
|[MACHINA](#Machina)             | **Free** (open source)                         |:white_check_mark:|:white_check_mark:|:white_check_mark:|:x:                                                   |Win                                                          |[Food4Rhino](https://www.food4rhino.com/app/machina)<br> [github](https://github.com/RobotExMachina)                                                                                                |
|[Furobot](#Furobot)             | **Free**                                       |:white_check_mark:|:white_check_mark:|:white_check_mark:|:x:                                                   |Win                                                          |[Food4Rhino](https://www.food4rhino.com/app/furobot)<br>[Website](http://www.fab-union.com/en/col.jsp?id=103)                                                                                       |
|[HAL Robotics](#HAL)            | £800/yr<br>£60/yr (academic)<br>Free trial     |:white_check_mark:|:white_check_mark:|:white_check_mark:|:x:                                                   |Win                                                          |[Food4Rhino(old)](https://www.food4rhino.com/app/hal-robot-programming-control)<br> [Food4Rhino(new)](https://www.food4rhino.com/app/hal-robotics-framework)<br>[Website](https://hal-robotics.com/)|
|[KUKA PRC](#KukaPRC)            | Free (limited)<br> 450€/yr<br>95€/yr (Student) |:white_check_mark:|:x:               |:x:               |:x:                                                   |Win                                                          |[Food4Rhino](https://www.food4rhino.com/app/kukaprc-parametric-robot-control-grasshopper)<br> [Website](https://www.robotsinarchitecture.org/kuka-prc)                                              |
|[Scorpion](#Scorpion)           | **Free** (open source)                         | :x:              |:x:               |:white_check_mark:|:x:                                                   |Win                                                          |[Food4Rhino](https://www.food4rhino.com/app/scorpion)<br>                                                                                                                                           |
|[Taco ABB](#Taco)               | **Free**                                       | :x:              |:white_check_mark:|:x:               |:x:                                                   |Win                                                          |[Food4Rhino](https://www.food4rhino.com/app/taco-abb)<br> [Website](http://blickfeld7.com/architecture/rhino/grasshopper/Taco/)                                                                     |
|[Robot Components](#RobotComp)  | **Free**  (open source)                        |:x:               |:white_check_mark:|:x:               |:x:                                                   |Win                                                          |[github](https://github.com/EDEK-UniKassel/RobotComponents)                                                                                                                                         |
|[RoboDK](#RoboDK)               | Free trial<br>145€(Edu)<br>2995€(Pro)          |:white_check_mark:|:white_check_mark:|:white_check_mark:|many others<br>[see here](https://robodk.com/library) |Win + Others ([standalone App](https://robodk.com/download)) |[Food4Rhino](https://www.food4rhino.com/app/robodk)<br> [Website](https://robodk.com/)                                                                                                              |
|~~[Rapcam](#Rapcam)~~           | 150€/month<br>Free trial                       |:white_check_mark:|:white_check_mark:|:x:               |Fanuc                                                 |Win                                                          |~~[Food4Rhino](https://www.food4rhino.com/app/rapcam-gh)<br> [Website](https://www.rapcam.eu/)~~                                                                                                    |
|~~[ROBOTS IO](#RobotsIO)~~      | **Free**                                       |:white_check_mark:|:question:        |:question:        |:question:                                            |Win                                                          |[Website](https://www.robofold.com/make/software/IO)<br> [Forum](https://www.grasshopper3d.com/group/io)                                                                                            |

\* information according to Food4Rhino.com, some plugins might also work in Rhino/Grasshopper for Mac

# Descriptions

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

Description: Machina is a .NET library for action-based real-time control of mechanical actuators. Plugins for Grasshopper and Revit can be used with an app called Machina-Bridge to stream commands directly to a robot. 

"Or in more human terms, it allows you to talk to a robot and tell it what to do."

| offline programming |command streaming | Visualisation |External axis support|    
| ----------          |:-------------:   |:-------------:|:-------------------:|
| :white_check_mark:  |:white_check_mark:|:x: **\***          |:white_check_mark:   |

**\* Visualisation:** can be done externally for ABB Robots with ABB Robot Studio

___
<a name="HAL"></a>
## HAL Robotics
Website:  [hal-robotics.com](https://hal-robotics.com/)  
Research Publications:  
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
    - Evaluation: Free  
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
~~[scorpion-robotics.org](http://scorpion-robotics.com/)~~  (offline)  
Download:  [Food4Rhino.com](https://www.food4rhino.com/app/scorpion#downloads_list)    
Research Publications:  [Automated Construction Using Adaptive Programing](https://www.researchgate.net/publication/300721200_An_Approach_to_Automated_Construction_Using_Adaptive_Programing)  
Price: Free   
Developed by: [Khaled Elashry](https://www.researchgate.net/profile/Khaled_Elashry2) - [Vincent Huyghe](https://www.ucl.ac.uk/bartlett/architecture/vincent-huyghe) - [Ruairi Glynn  ](https://www.researchgate.net/profile/Ruairi_Glynn)  
Robot brands : **UR** (Visualisation only for UR10)    

| offline programming |command streaming | Visualisation    |External axis support|
| ----------          |:-------------:   |:-------------:   |:-------------------:|
| :white_check_mark:  |:white_check_mark:|:white_check_mark:|:x:                  |

___
<a name="Taco"></a>
## Taco ABB
Website:
[Food4Rhino.com](https://www.food4rhino.com/app/taco-abb)   
[blickfeld7.com](http://blickfeld7.com/architecture/rhino/grasshopper/Taco/)    
Download:  [blickfeld7.com](http://blickfeld7.com/downloads/installer/Taco.zip)      
Research Publications utilising this plugin:  
[Tool Path Generator for Artistic Drawing with Industrial Robot](https://www.researchgate.net/publication/338598379_Tool_Path_Generator_for_Artistic_Drawing_with_Industrial_Robot)  
[Robotic Formwork in the MARS Pavilion](http://papers.cumincad.org/data/works/att/acadia17_522.pdf)  
[Robotic Fabrication Workflows for Environmentally Driven Facades](https://vtechworks.lib.vt.edu/bitstream/handle/10919/92001/Cabrera_PM_T_2019.pdf?sequence=1)  
Price:  Free   
Developed by: [blickfeld7](http://blickfeld7.com/architecture/rhino/grasshopper/Taco/)   
Robot brands : **ABB**  
Description:  TACO is a free and user-friendly programming plugin for the simulation and control of ABB industrial robots directly within Grasshopper. Taco offers users to program and visualize ABB robots with parametrics.  

| offline programming |command streaming | Visualisation    |External axis support|
| ----------          |:-------------:   |:----------------:|:-------------------:|
| :white_check_mark:  |:white_check_mark:|:white_check_mark:|:x:   |

___
<a name="RoboDK"></a>
## RoboDK
__to be added__  
Website:  
Download:  
Research Publications:  
Price:  
to be added  
Description:  

___
<a name="Furobot"></a>
## Furobot
Website:  
Download:  
Research Publications:  
Price:  
Developed by: [Fab-Union](http://www.fab-union.com/en/col.jsp?id=101)   
Robot brands : **Kuka ABB UR**
Description:  

|offline programming|command streaming | Visualisation    |External axis support|
|-------------------|:-------------:   |:----------------:|:-------------------:|
|:white_check_mark: |:white_check_mark:|:white_check_mark:|:white_check_mark:   |


___
<a name="RobotComp"></a>
## Robot Components
Website:  
Download:  
Research Publications:  
Price:  
Developed by [EDEK-UniKassel](https://github.com/EDEK-UniKassel)  
Robot brands : **ABB**
Description:  

| offline programming |command streaming | Visualisation    |External axis support|
| ----------          |:-------------:   |:-------------:   |:-------------------:|
| :white_check_mark:  |:white_check_mark:|:white_check_mark:|:x:                  |

___
<a name="Rapcam"></a>
## Rapcam
Website:  
Download:  
Research Publications:  
Price:  
Description:  
Rapcam appears to be discontinued by the developers.


___
<a name="RobotsIO"></a>
## ROBOTS IO
Website:  
Download:  
Research Publications:  
Price:  
Description:  
ROBOTS IO seems to be discontinued by the developer. The website does not exist anymore [robots.io](http://www.robots.io/). Documentation can still be found in this [PDF](https://st2.ning.com/topology/rest/1.0/file/get/2811285740?profile=original).
 
