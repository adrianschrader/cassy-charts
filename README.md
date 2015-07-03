# cassy-charts
Python command line tool to convert .labx files from the proprietary Cassy Lab 2 to OpenDocument ODS spreadsheets. The tool can also display basic information about the retrieved measurements.

### Dependencies
``` bash
pip install lxml ezodf
```

## Usage
``` bash
python cassy-charts.py doc.labx measurements.ods
python cassy-charts.py doc.labx --details
python cassy-charts.py --help
```
