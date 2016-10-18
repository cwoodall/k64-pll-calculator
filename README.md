# K64 PLL Calculator : 
> Calculate your PLL Settings for the K64F12 Series of Processors in Style with Z3 and Python

[![Travis CI Build Status](https://travis-ci.org/cwoodall/k64-pll-calculator.svg)](https://travis-ci.org/cwoodall/k64-pll-calculator)

**Table of Contents**
<!-- TOC depthFrom:2 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [Overview](#overview)
- [Installing](#installing)
- [Usage](#usage)
	- [Web Api](#web-api)

<!-- /TOC -->

## Overview

This is a calculator for the PLL configuration values for VDIV, and PDIV
for the Freescale K64 processor. You put in your input frequency and Desired
output frequency and it returns the value of PDIV and VDIV. These values
are the numbers which are used in the equation:

```
f_{out} = VDIV * (f_{in} / PDIV)
```
where:

```
2MHz <= (f_{in} / PDIV ) <= 4 MHz
```

There are also constraints on VDIV and PDIV in terms of min and max
ranges.

To get the actual register values of PDIV and VDIV you can look up the
values in the [datasheet](http://cache.nxp.com/files/microcontrollers/doc/ref_manual/K64P144M120SF5RM.pdf)
on pages 589 and 590.

A simple calculator could have been used, but instead I decided to learn
a little about using <a href="https://z3.codeplex.com/">z3</a> which is a
high performance theorem prover. There is both a commandline interface and a web application.


## Installing

*Requires*: Python 2.7

All requirements are managemed by the setup.py file and the application can be installed by running:

```
$ setup.py install
```

To verified it is installed properly you can now run the unit tests:

```
$ setup.py test
```


This installs `pll_solver` and `pll_solver_web` which can be run from the command line. See the [usage section](#usage) for details.

## Usage

Getting help:

``` shell-session
$ pll_solver --help
Usage: pll_solver [OPTIONS]

  Simple program which takes an input frequency and an output
  frequency and returns the pdiv and vdiv necissary for the pll in
  the freescale k64 processors

Options:
  -i, --freq_in FLOAT   Input frequency value in Hz
  -o, --freq_out FLOAT  Output frequency value in Hz
  -v, --verbosity       Verbosity of output
  --version             Show the version and exit.
  --help                Show this message and exit.

```

Example of finding some values:

``` shell-session
pll_solver -i 24e6 -o 80e6
[d = 12, m = 40, f_out = 80000000, f_in = 24000000]
```

Example of a failure of the model to converge:

``` shell-session
$ pll_solver -i 1e6 -o 80e6
No results found.
```

### Web Api

A flask web application is also provided which can be run using:

``` shell-session
$ pll_solver_web
```

After you do this you can go to `localhost:5000` to get the web page. To make
API calls you can do the following:

```
$ curl localhost:5000/solve
{
  "payload": {
    "error": "float() argument must be a string or a number"
  },
  "status": "error"
}
```

The data is taken using a `GET` request with arguments `fin` and `fout`:

```
$ curl "localhost:5000/solve?fin=24e6&fout=80e6"
{
  "payload": {
    "d": "12",
    "f_in": "24000000",
    "f_out": "80000000",
    "m": "40"
  },
  "status": "success"
}
```

You can experiment with this [here](http://z3-pll-finder.herokuapp.com/), and use the the solve api at `http://z3-pll-finder.herokuapp.com/solve`. For example, we can repeat the above request:

```
$ curl "z3-pll-finder.herokuapp.com/solve?fin=24e6&fout=80e6"
{
  "payload": {
    "d": "12",
    "f_in": "24000000",
    "f_out": "80000000",
    "m": "40"
  },
  "status": "success"
}
```
For more information please see the [writeup](#)
