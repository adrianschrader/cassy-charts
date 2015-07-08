# cassy-charts
Python command line tool to convert .labx files from the proprietary Cassy Lab 2 to OpenDocument ODS spreadsheets. The tool can also display basic information about the retrieved measurements.

## Installation & Dependencies
Python 2.7 and the spreadheet libraries lxml and ezodf have to be installed locally. You can install the dependencies with pip.
``` bash
python --version
pip install lxml ezodf
```

To use the script natively from the terminal, you either have to add the repository in `$PATH` or create a symlink in a directory that is in the `$PATH` variable. If this doesn't work, determine the python directory with `where python` and put it in the header of `cassy-charts.py`.

```bash
chmod +x cassy-charts.py
cd /usr/local/bin
ln -s ~/path/to/repository/cassy-charts.py cassycharts
```

## Usage
Prints help text with usage instructions and the link to the guthub repository.
``` bash
python cassy-charts.py -h
python cassy-charts.py --help
```
Prints details about the different channels in the source file. It can also be used to determine the indices for the channel selection. This command doesn't start a file conversion.
``` bash
python cassy-charts.py doc.labx -d
python cassy-charts.py doc.labx --details
```
Converts the channels from CASSY's .labx file to a Open Document Spreadsheet (.ods). It requires the source file and a destination path. **WARNING: The output path will be overriden!**
``` bash
python cassy-charts.py doc.labx measurements.ods
```
Exports only certain channels specified with `-c` or `--channels`. The channel indices can be printed by the `--details` command.
``` bash
python cassy-charts.py doc.labx measurements.ods -c 0 1 5
python cassy-charts.py doc.labx measurements.ods --channels 0 1 5
```

## Help
```
usage: cassycharts [-h] [--channels [CHANNELS [CHANNELS ...]]] [--details]
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

For more instructions see https://github.com/adrianschrader/cassy-charts
```
