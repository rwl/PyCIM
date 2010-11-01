# Copyright (C) 2010 Richard Lincoln
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA, USA

from CIM14v13.IEC61970.Core.IdentifiedObject import IdentifiedObject

class GmlColour(IdentifiedObject):
    """The solid color that will be used. The color value is RGB-encoded using two hexadecimal digits per primary-color component, in the order Red, Green, Blue, prefixed with a hash (#) sign. The hexadecimal digits between A and F may be in either uppercase or lowercase. For example, full red is encoded as '#ff0000' (with no quotation marks). If the Stroke cssParameter element is absent, the default color is defined to be black ('#000000').
    """

    def __init__(self, blue='', green='', red='', GmlFills=None, GmlFonts=None, GmlStrokes=None, *args, **kw_args):
        """Initializes a new 'GmlColour' instance.

        @param blue: The color value for BLUE (RGB-encoded using two hexadecimal digits per primary-color component, in the order Red, Green, Blue, prefixed with a hash (#) sign.). 
        @param green: The color value for GREEN (RGB-encoded using two hexadecimal digits per primary-color component, in the order Red, Green, Blue, prefixed with a hash (#) sign.) 
        @param red: The color value for RED (RGB-encoded using two hexadecimal digits per primary-color component, in the order Red, Green, Blue, prefixed with a hash (#) sign.) 
        @param GmlFills:
        @param GmlFonts:
        @param GmlStrokes:
        """
        #: The color value for BLUE (RGB-encoded using two hexadecimal digits per primary-color component, in the order Red, Green, Blue, prefixed with a hash (#) sign.). 
        self.blue = blue

        #: The color value for GREEN (RGB-encoded using two hexadecimal digits per primary-color component, in the order Red, Green, Blue, prefixed with a hash (#) sign.) 
        self.green = green

        #: The color value for RED (RGB-encoded using two hexadecimal digits per primary-color component, in the order Red, Green, Blue, prefixed with a hash (#) sign.) 
        self.red = red

        self._GmlFills = []
        self.GmlFills = [] if GmlFills is None else GmlFills

        self._GmlFonts = []
        self.GmlFonts = [] if GmlFonts is None else GmlFonts

        self._GmlStrokes = []
        self.GmlStrokes = [] if GmlStrokes is None else GmlStrokes

        super(GmlColour, self).__init__(*args, **kw_args)

    def getGmlFills(self):
        
        return self._GmlFills

    def setGmlFills(self, value):
        for x in self._GmlFills:
            x._GmlColour = None
        for y in value:
            y._GmlColour = self
        self._GmlFills = value

    GmlFills = property(getGmlFills, setGmlFills)

    def addGmlFills(self, *GmlFills):
        for obj in GmlFills:
            obj._GmlColour = self
            self._GmlFills.append(obj)

    def removeGmlFills(self, *GmlFills):
        for obj in GmlFills:
            obj._GmlColour = None
            self._GmlFills.remove(obj)

    def getGmlFonts(self):
        
        return self._GmlFonts

    def setGmlFonts(self, value):
        for x in self._GmlFonts:
            x._GmlColour = None
        for y in value:
            y._GmlColour = self
        self._GmlFonts = value

    GmlFonts = property(getGmlFonts, setGmlFonts)

    def addGmlFonts(self, *GmlFonts):
        for obj in GmlFonts:
            obj._GmlColour = self
            self._GmlFonts.append(obj)

    def removeGmlFonts(self, *GmlFonts):
        for obj in GmlFonts:
            obj._GmlColour = None
            self._GmlFonts.remove(obj)

    def getGmlStrokes(self):
        
        return self._GmlStrokes

    def setGmlStrokes(self, value):
        for x in self._GmlStrokes:
            x._GmlColour = None
        for y in value:
            y._GmlColour = self
        self._GmlStrokes = value

    GmlStrokes = property(getGmlStrokes, setGmlStrokes)

    def addGmlStrokes(self, *GmlStrokes):
        for obj in GmlStrokes:
            obj._GmlColour = self
            self._GmlStrokes.append(obj)

    def removeGmlStrokes(self, *GmlStrokes):
        for obj in GmlStrokes:
            obj._GmlColour = None
            self._GmlStrokes.remove(obj)

