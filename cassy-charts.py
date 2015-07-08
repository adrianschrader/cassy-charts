#!/usr/bin/python
import sys
import argparse
import xml.etree.ElementTree as ET
from ezodf import newdoc, Sheet

# Define Channel
class Channel:
    def __init__(self, node, index):
        self.node = node
        self.quantity   = node.find('quantity').text
        self.symbol     = node.find('symbol').text
        self.unit       = node.find('unit').text
        self.min        = node.find('range').get('min')
        self.max        = node.find('range').get('max')
        self.count      = node.find('values').get('count')
        self.index      = index

    def appendSheet(self, sheet, column):
        length = len(self.node.find('values'))

        if (length < 1):
            print('\r{1}{2} [{3}] {0}'.format('Skipped...', bold(repr(self.quantity)), ' '*(20-len(repr(self.quantity))), ' '*20)),
            return 0

        sheet.column(column)[0].set_value(self.quantity)
        sheet.column(column)[1].set_value(self.symbol + ' / ' + (self.unit or ''))
        update_progress(2 * 100 / length, self.quantity)

        row = 2;
        for value in self.node.find('values'):
            sheet.column(column)[row].set_value(float(value.text))
            update_progress(row * 100 / length, self.quantity)
            row += 1
        return 1

def bold(msg):
    return u'\033[1m%s\033[0m' % msg

def update_progress(progress, title):
    #sys.stdout.write("\r%d%%" % progress)
    print('\r{2}{3} [{0}] {1}%'.format('#'*(progress/5), progress, bold(repr(title)), ' '*(20-len(repr(title))))),
    sys.stdout.flush()

# Parse input arguments
parser = argparse.ArgumentParser(description='Convert and interpret .labx-files from the proprietary Leybold CASSY software. ')
parser.add_argument('inputpath', metavar='inputfile', type=str,
                   help='path to the .labx file')
parser.add_argument('outputpath', metavar='outputfile', nargs='?',
                   help='path to the ods output file')
parser.add_argument('--channels', '-c', nargs='*',
                   help='whitelist channels to export')
parser.add_argument('--details', '-d', action='store_true',
                  help='print details about the channels of the .labx file')

args = parser.parse_args()

# Load channels from xml-file
tree = ET.parse(args.inputpath)
root = tree.getroot()

channels = []
index = 0
for channel in root.iter('channel'):
    channels.append(Channel(channel, index))
    index += 1

if args.details:
    index = 0
    print('-------------------------------------------')
    for channel in channels:
        print('Index   : ' + str(channel.index))
        print('Quantity: ' + channel.quantity + '('+ channel.symbol + ')')
        print('Unit    : ' + (channel.unit or '--'))
        print('Range   : (' + str(round(float(channel.min), 3)) + ', ' + str(round(float(channel.max),3)) + ')')
        print('Count   : ' + channel.count)
        if index < len(channels):
            print('-------------------------------------------')
        index += 1
else:
    if len((args.outputpath or '')) < 1:
        print('No output path specified. Use -h for help')
        exit(1)
    # Construct a sheet from the channels
    length = channels[0].count

    spreadsheet = newdoc(doctype='ods', filename=args.outputpath)
    sheet = Sheet('Sheet 1', size=(int(length)+10, len(channels)))

    col = 0
    for channel in channels:
        if args.channels is not None:
            if str(channel.index) in args.channels:
                col += channel.appendSheet(sheet, col)
                print('')
        else:
            col += channel.appendSheet(sheet, col)
            print('')


    spreadsheet.sheets += sheet
    spreadsheet.save()

    print('\n-------------------------------------------')
    print('Saved ' + args.outputpath + ' successfully!')
    print('-------------------------------------------')
