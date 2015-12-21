# cFEmdd
Model-driven Development for the NASA Core Flight Executive (cFE)

Quick-Start Developer's Guide
=============================

Setup Antlr4
------------
```bash
$ cd /usr/local/lib
$ sudo curl -O http://www.antlr.org/download/antlr-4.4-complete.jar
$ export CLASSPATH=".:/usr/local/lib/antlr-4.4-complete.jar:$CLASSPATH"
$ alias antlr4='java -jar /usr/local/lib/antlr-4.4-complete.jar'
$ alias grun='java org.antlr.v4.runtime.misc.TestRig'
```

Setup Cheetah Templating Engine
-------------------------------
1. Download from: https://pypi.python.org/pypi/Cheetah/2.4.4
2. Extract Cheetah-2.4.4.tar.gz
```bash
$ cd Cheetah-2.4.4
$ sudo python setup.py install
```

Quick-Start User's Guide
========================

Install Dependencies
--------------------
1. Cheetah Templating Engine

Start CFSEditor
---------------
```bash
$ cd cFEmdd/src
$ python editor.py
```

Open & Edit CFS Mission Models
-----------------------

![Alt text](https://github.com/pranav-srinivas-kumar/cFEmdd/blob/master/screenshots/open_models.png?raw=true "Open Mission Models")

Generate Mission Directory
--------------------------

![Alt text](https://github.com/pranav-srinivas-kumar/cFEmdd/blob/master/screenshots/generate_mission.png?raw=true "Generate Mission Directory")

Build and Execute Applications
------------------------------
```bash
$ cd <MISSION_HOME>
$ . ./setvars.sh
$ cd build/cpu1
$ make config
$ make
$ cd exe
$ sudo -s
$ ./core-linux.bin
```

For more details on cFE application development, refer to cfe-OSS-readme.txt in <MISSION_HOME>
