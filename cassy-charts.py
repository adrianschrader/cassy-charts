#!/usr/bin/python
import argparse
import xml.etree.ElementTree as ET
from ezodf import newdoc, Sheet

# Define Channel
class Channel:
    def __init__(self, node):
        self.node = node
        self.quantity   = node.find('quantity').text
        self.symbol     = node.find('symbol').text
        self.unit       = node.find('unit').text
        self.min        = node.find('range').get('min')
        self.max        = node.find('range').get('max')
        self.count      = node.find('values').get('count')

    def appendSheet(self, sheet, column):
        sheet.column(column)[0].set_value(self.quantity)
        sheet.column(column)[1].set_value(self.symbol + ' / ' + (self.unit or ''))

        row = 2;
        for value in self.node.find('values'):
            sheet.column(column)[row].set_value(float(value.text))
            row += 1

# Parse input arguments
parser = argparse.ArgumentParser(description='Convert and interpret .labx-files from the proprietary Leybold CASSY software. ')
parser.add_argument('inputpath', metavar='inputfile', type=str,
                   help='path to the .labx file')
parser.add_argument('outputpath', metavar='outputfile', nargs='?',
                   help='path to the ods output file')
parser.add_argument('--details', action='store_true',
                  help='print details about the channels of the .labx file')

args = parser.parse_args()

# Load channels from xml-file
tree = ET.parse(args.inputpath)
root = tree.getroot()

channels = []
for channel in root.iter('channel'):
    channels.append(Channel(channel))

if args.details:
    index = 0
    print('-------------------------------------------')
    for channel in channels:
        print('Index   : ' + str(index))
        print('Quantity: ' + channel.quantity + '('+ channel.symbol + ')')
        print('Unit    : ' + (channel.unit or '--'))
        print('Range   : (' + str(round(float(channel.min), 3)) + ', ' + str(round(float(channel.max),3)) + ')')
        print('Count   : ' + channel.count)
        if index < len(channels):
            print('-------------------------------------------')
        index += 1
else:
    # Construct a sheet from the channels
    length = channels[0].count

    spreadsheet = newdoc(doctype='ods', filename=args.outputpath)
    sheet = Sheet('Sheet 1', size=(int(length)+10, len(channels)))

    col = 0
    for channel in channels:
        channel.appendSheet(sheet, col)
        col += 1

    spreadsheet.sheets += sheet
    spreadsheet.save()

    print('-------------------------------------------')
    print('Saved ' + args.outputpath + ' successfully!')
    print('-------------------------------------------')
