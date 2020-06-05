<!---
#**============================================================================
#**
#**                Energy Harvesting Measurement Rig (ENHAMER)
#**                  THIS REPOSITORY IS PART OF THE ENHAMER
#**
#** TITLE:           ENHAMER (Python Main Program)
#**
#** AUTHOR:          Marcin J. Kraśny
#**
#**					 Advanced Biological Imaging Laboratory
#**                  School of Physics
#**                  College of Science and Engineering
#**                  National University of Ireland, Galway
#**
#** SOURCE URL       https://github.com/enhamer/enhamer
#** COPYRIGHT        © 2015-2020 M.J.Kraśny
#** LICENSE          MIT
#** CREDITS          NEMESIS - Novel Energy Materials, Engineering Science 
#**                  and Integrated Systems
#**                  Department of Mechanical Engineering
#**					 University of Bath, UK
#**
#**============================================================================
#**============================================================================
-->

# ENHAMER
**Energy Harvesting Measurement Rig (ENHAMER)**

[![License](https://img.shields.io/pypi/l/ansicolortags.svg)](https://img.shields.io/pypi/l/ansicolortags.svg)

Thank you for the interest in ENHAMER!

*"A System for Characterisation of Piezoelectric Materials and Associated Electronics for Vibration Powered Energy Harvesting Devices"*




## What is ENHAMER?

**ENHAMER** is a python-based, open-source tool for control over energy harvesting rig.

The design principles of ENHAMER are wide application scope, modularity, and easy extensibility!


<!---

## Who should use ENHAMER?
-->


## General Block Diagram
![General Rig Diagram](https://github.com/enhamer/enhamer/wiki/General/_img/Fig_01-Krasny-ENHAMER.png)

General block diagram of a vibration powered energy harvesting experimental setup
typically used for electrical characterisation and performance measurements of device under test (DUT).


## Important Links
<!---
Links to WIKI
-->
Software:
1. [User Guide / Documentation](https://github.com/enhamer/enhamer/wiki)
1. [Installation Guide](https://github.com/enhamer/enhamer/wiki/Installation/Install)
1. [Quick Start](https://github.com/enhamer/enhamer/wiki/Installation/Quick_Start)

Hardware:
1. Accelerometer: 
[ADXL316 PCB module](https://github.com/enhamer/ADXL316-module)
1. Ddraig Control Board:
[Ddraig](https://github.com/enhamer/DDRAIG_Ctrl-Board)
1. Accelerometer and sample holders: 
[Holders](https://github.com/enhamer/AccelerometerSample-holder)

![Ddraig Board top](https://github.com/enhamer/DDRAIG_Ctrl-Board/blob/master/_img/Ddraig_assembled_01small.jpg?raw=true)


## Dependencies
The ENHAMER scripts require Python >= 3.6 and use the libraries and packages specified below.


| Packages                                                      | Optional   | Note                         | License              |
| --------------                                                | ---------- | -----------------------------| ----------           |
| [**numpy**](https://numpy.org)                                |            | tested with `numpy-1.18.4`   |*BSD license*
| [**pandas**](https://pandas.pydata.org/)                      |            | tested with `pandas-0.25.3`  |*New BSD License*|
| [**pyvisa**](https://pyvisa.readthedocs.io/)                  |            | tested with `pyvisa-1.8`     |*MIT License*         |
| [**pathlib**](https://docs.python.org/3/library/pathlib.html) |            | tested with `pathlib-1.0.1`  | *Python Software Foundation License*
| [**matplotlib**](https://matplotlib.org/)                     | *Optional* |                              |*Matplotlib License*  |
| 



### Current Release
> The ENHAMER script has been successfully tested on Windows 10 with Python 3.8.3.

### Installation and Quick Start

Please clone this repository and install the [required dependencies](requirements.txt) as follows:

```bash
git clone https://github.com/enhamer/enhamer.git
cd enhamer
pip install -r requirements.txt
```

1. For detailed [**Installation Instruction**](https://github.com/enhamer/enhamer/wiki/Installation/Install)
 please go to [Project WIKI Page](https://github.com/enhamer/enhamer/wiki).
1. For [**Quick Start**](https://github.com/enhamer/enhamer/wiki/Installation/Quick_Start) guide please go to [Project WIKI Page](https://github.com/enhamer/enhamer/wiki).


<!---
# Citing ENHAMER
If you find ENHAMER useful, and you use any part of ENHAMER in your work please cite our work as the following paper:

#TODO: when paper available.
[![DOI](url to doi-icon)](url to published paper)   
-->

# License
```
Copyright © 2015-2020 Marcin J. Kraśny
```

This work is licensed under multiple licenses:

- The source code and the accompanying material is licensed under [MIT](LICENSE/MIT.txt)

- Hardware Design. Includes Schematic, BOM, Layout, CAD drawing is licensed under [CERN-OHL-P v2](LICENSE/cern_ohl_p_v2.txt); 
[CERN Open Hardware Licence version 2](https://cern.ch/cern-ohl)

- The data set and figures are licensed under [CC0-1.0](LICENSE/CC0-1.0.txt).

Please see the individual files and repositories descriptions for more accurate information.

*THE SOFTWARE AND HARDWARE ARE PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.*
