# Copyright (C) 2010-2011 Richard Lincoln
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

from CIM15.IEC61970.Core.IdentifiedObject import IdentifiedObject

class GmlColour(IdentifiedObject):
    """The solid color that will be used. The color value is RGB-encoded using two hexadecimal digits per primary-color component, in the order Red, Green, Blue, prefixed with a hash (#) sign. The hexadecimal digits between A and F may be in either uppercase or lowercase. For example, full red is encoded as '#ff0000' (with no quotation marks). If the Stroke cssParameter element is absent, the default color is defined to be black ('#000000').The solid color that will be used. The color value is RGB-encoded using two hexadecimal digits per primary-color component, in the order Red, Green, Blue, prefixed with a hash (#) sign. The hexadecimal digits between A and F may be in either uppercase or lowercase. For example, full red is encoded as '#ff0000' (with no quotation marks). If the Stroke cssParameter element is absent, the default color is defined to be black ('#000000').
    """

    def __init__(self, red='', green='', blue='', GmlFills=None, GmlFonts=None, GmlStrokes=None, *args, **kw_args):
        """Initialises a new 'GmlColour' instance.

        @param red: The color value for RED (RGB-encoded using two hexadecimal digits per primary-color component, in the order Red, Green, Blue, prefixed with a hash (#) sign.) 
        @param green: The color value for GREEN (RGB-encoded using two hexadecimal digits per primary-color component, in the order Red, Green, Blue, prefixed with a hash (#) sign.) 
        @param blue: The color value for BLUE (RGB-encoded using two hexadecimal digits per primary-color component, in the order Red, Green, Blue, prefixed with a hash (#) sign.). 
        @param GmlFills:
        @param GmlFonts:
        @param GmlStrokes:
        """
        #: The color value for RED (RGB-encoded using two hexadecimal digits per primary-color component, in the order Red, Green, Blue, prefixed with a hash (#) sign.)
        self.red = red

        #: The color value for GREEN (RGB-encoded using two hexadecimal digits per primary-color component, in the order Red, Green, Blue, prefixed with a hash (#) sign.)
        self.green = green

        #: The color value for BLUE (RGB-encoded using two hexadecimal digits per primary-color component, in the order Red, Green, Blue, prefixed with a hash (#) sign.).
        self.blue = blue

        self._GmlFills = []
        self.GmlFills = [] if GmlFills is None else GmlFills

        self._GmlFonts = []
        self.GmlFonts = [] if GmlFonts is None else GmlFonts

        self._GmlStrokes = []
        self.GmlStrokes = [] if GmlStrokes is None else GmlStrokes

        super(GmlColour, self).__init__(*args, **kw_args)

    _attrs = ["red", "green", "blue"]
    _attr_types = {"red": str, "green": str, "blue": str}
    _defaults = {"red": '', "green": '', "blue": ''}
    _enums = {}
    _refs = ["GmlFills", "GmlFonts", "GmlStrokes"]
    _many_refs = ["GmlFills", "GmlFonts", "GmlStrokes"]

    def getGmlFills(self):
        
        return self._GmlFills

    def setGmlFills(self, value):
        for x in self._GmlFills:
            x.GmlColour = None
        for y in value:
            y._GmlColour = self
        self._GmlFills = value

    GmlFills = property(getGmlFills, setGmlFills)

    def addGmlFills(self, *GmlFills):
        for obj in GmlFills:
            obj.GmlColour = self

    def removeGmlFills(self, *GmlFills):
        for obj in GmlFills:
            obj.GmlColour = None

    def getGmlFonts(self):
        
        return self._GmlFonts

    def setGmlFonts(self, value):
        for x in self._GmlFonts:
            x.GmlColour = None
        for y in value:
            y._GmlColour = self
        self._GmlFonts = value

    GmlFonts = property(getGmlFonts, setGmlFonts)

    def addGmlFonts(self, *GmlFonts):
        for obj in GmlFonts:
            obj.GmlColour = self

    def removeGmlFonts(self, *GmlFonts):
        for obj in GmlFonts:
            obj.GmlColour = None

    def getGmlStrokes(self):
        
        return self._GmlStrokes

    def setGmlStrokes(self, value):
        for x in self._GmlStrokes:
            x.GmlColour = None
        for y in value:
            y._GmlColour = self
        self._GmlStrokes = value

    GmlStrokes = property(getGmlStrokes, setGmlStrokes)

    def addGmlStrokes(self, *GmlStrokes):
        for obj in GmlStrokes:
            obj.GmlColour = self

    def removeGmlStrokes(self, *GmlStrokes):
        for obj in GmlStrokes:
            obj.GmlColour = None

