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

class GmlFont(IdentifiedObject):
    """Identifies a font of a certain family, style, and size.Identifies a font of a certain family, style, and size.
    """

    def __init__(self, absoluteSize=False, size='', style='', family='', weight='', GmlTextSymbols=None, GmlSvgParameters=None, GmlColour=None, *args, **kw_args):
        """Initialises a new 'GmlFont' instance.

        @param absoluteSize: True if 'size' is expressed in absolute values. Default is false. 
        @param size: The size to use for the font in pixels. The default is defined to be 10 pixels, though various systems may have restrictions on what sizes are available. 
        @param style: The style to use for a font. The allowed values are 'normal', 'italic', and 'oblique'. 
        @param family: Family name of a font to use. Allowed values are system-dependent. Any number of font-family attributes may be given and they are assumed to be in preferred order. 
        @param weight: The amount of weight or boldness to use for a font. Allowed values are 'normal' and 'bold'. 
        @param GmlTextSymbols:
        @param GmlSvgParameters:
        @param GmlColour:
        """
        #: True if 'size' is expressed in absolute values. Default is false.
        self.absoluteSize = absoluteSize

        #: The size to use for the font in pixels. The default is defined to be 10 pixels, though various systems may have restrictions on what sizes are available.
        self.size = size

        #: The style to use for a font. The allowed values are 'normal', 'italic', and 'oblique'.
        self.style = style

        #: Family name of a font to use. Allowed values are system-dependent. Any number of font-family attributes may be given and they are assumed to be in preferred order.
        self.family = family

        #: The amount of weight or boldness to use for a font. Allowed values are 'normal' and 'bold'.
        self.weight = weight

        self._GmlTextSymbols = []
        self.GmlTextSymbols = [] if GmlTextSymbols is None else GmlTextSymbols

        self._GmlSvgParameters = []
        self.GmlSvgParameters = [] if GmlSvgParameters is None else GmlSvgParameters

        self._GmlColour = None
        self.GmlColour = GmlColour

        super(GmlFont, self).__init__(*args, **kw_args)

    _attrs = ["absoluteSize", "size", "style", "family", "weight"]
    _attr_types = {"absoluteSize": bool, "size": str, "style": str, "family": str, "weight": str}
    _defaults = {"absoluteSize": False, "size": '', "style": '', "family": '', "weight": ''}
    _enums = {}
    _refs = ["GmlTextSymbols", "GmlSvgParameters", "GmlColour"]
    _many_refs = ["GmlTextSymbols", "GmlSvgParameters"]

    def getGmlTextSymbols(self):
        
        return self._GmlTextSymbols

    def setGmlTextSymbols(self, value):
        for x in self._GmlTextSymbols:
            x.GmlFont = None
        for y in value:
            y._GmlFont = self
        self._GmlTextSymbols = value

    GmlTextSymbols = property(getGmlTextSymbols, setGmlTextSymbols)

    def addGmlTextSymbols(self, *GmlTextSymbols):
        for obj in GmlTextSymbols:
            obj.GmlFont = self

    def removeGmlTextSymbols(self, *GmlTextSymbols):
        for obj in GmlTextSymbols:
            obj.GmlFont = None

    def getGmlSvgParameters(self):
        
        return self._GmlSvgParameters

    def setGmlSvgParameters(self, value):
        for p in self._GmlSvgParameters:
            filtered = [q for q in p.GmlFonts if q != self]
            self._GmlSvgParameters._GmlFonts = filtered
        for r in value:
            if self not in r._GmlFonts:
                r._GmlFonts.append(self)
        self._GmlSvgParameters = value

    GmlSvgParameters = property(getGmlSvgParameters, setGmlSvgParameters)

    def addGmlSvgParameters(self, *GmlSvgParameters):
        for obj in GmlSvgParameters:
            if self not in obj._GmlFonts:
                obj._GmlFonts.append(self)
            self._GmlSvgParameters.append(obj)

    def removeGmlSvgParameters(self, *GmlSvgParameters):
        for obj in GmlSvgParameters:
            if self in obj._GmlFonts:
                obj._GmlFonts.remove(self)
            self._GmlSvgParameters.remove(obj)

    def getGmlColour(self):
        
        return self._GmlColour

    def setGmlColour(self, value):
        if self._GmlColour is not None:
            filtered = [x for x in self.GmlColour.GmlFonts if x != self]
            self._GmlColour._GmlFonts = filtered

        self._GmlColour = value
        if self._GmlColour is not None:
            if self not in self._GmlColour._GmlFonts:
                self._GmlColour._GmlFonts.append(self)

    GmlColour = property(getGmlColour, setGmlColour)

