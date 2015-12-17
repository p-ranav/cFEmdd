# cFEmdd
Model-driven Development for the Core Flight Executive (cFE)

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


