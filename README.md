# cassy-charts
Python command line tool to convert .labx files from the proprietary Cassy Lab 2 to OpenDocument ODS spreadsheets. The tool can also display basic information about the retrieved measurements.

## Installation & Dependencies
``` bash
pip install lxml ezodf
chmod +x cassy-charts.py

cd /usr/local/bin
ln -s ~/path/to/repository/cassy-charts.py
```

## Usage
``` bash
python cassy-charts.py -h
python cassy-charts.py --help
python cassy-charts.py doc.labx -d
python cassy-charts.py doc.labx --details
python cassy-charts.py doc.labx measurements.ods
python cassy-charts.py doc.labx measurements.ods -c 0 1 5
python cassy-charts.py doc.labx measurements.ods --channels 0 1 5
```

## Help
``` bash
usage: cassy-charts.py [-h] [--channels [CHANNELS [CHANNELS ...]]] [--details]
                       inputfile [outputfile]

Convert and interpret .labx-files from the proprietary Leybold CASSY software.

positional arguments:
  inputfile             path to the .labx file
  outputfile            path to the ods output file

optional arguments:
  -h, --help            show this help message and exit
  --channels [CHANNELS [CHANNELS ...]], -c [CHANNELS [CHANNELS ...]]
                        whitelist channels to export
  --details, -d         print details about the channels of the .labx file
```
