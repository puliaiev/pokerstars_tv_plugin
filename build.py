# -*- coding: utf-8 -*-

import os
from xml.dom.minidom import parse
import re

pluginName = 'plugin.video.pokerstars.tv'

import zipfile

def zipdir(path, zip):
    for root, dirs, files in os.walk(path):
        for file in files:
            zip.write(os.path.join(root, file))

def makeZip(filename, dir):
    zip = zipfile.ZipFile(filename + '.zip', 'w')
    zipdir(dir + '/', zip)
    zip.close()

def incrementVersion():
    filename = pluginName + '/addon.xml'
    dom1 = parse(filename)
    addonTag = dom1.getElementsByTagName("addon")[0]
    version = addonTag.attributes['version'].value
    incr = re.compile('.([0-9]+)$').findall(version)[0]
    before = incr
    incr = str(int(incr) + 1)
    version = re.sub(before, incr, version)
    addonTag.attributes['version'] = version

    #write to file
    open(filename,"wb").write(dom1.toxml().encode("utf-8"))
    return version

def main():
    version = incrementVersion()
    makeZip(pluginName + '-' + version, pluginName)

if __name__ == '__main__':
    main()