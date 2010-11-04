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

class GmlFont(IdentifiedObject):
    """Identifies a font of a certain family, style, and size.
    """

    def __init__(self, absoluteSize=False, style='', size='', family='', weight='', GmlTextSymbols=None, GmlColour=None, GmlSvgParameters=None, **kw_args):
        """Initializes a new 'GmlFont' instance.

        @param absoluteSize: True if 'size' is expressed in absolute values. Default is false. 
        @param style: The style to use for a font. The allowed values are 'normal', 'italic', and 'oblique'. 
        @param size: The size to use for the font in pixels. The default is defined to be 10 pixels, though various systems may have restrictions on what sizes are available. 
        @param family: Family name of a font to use. Allowed values are system-dependent. Any number of font-family attributes may be given and they are assumed to be in preferred order. 
        @param weight: The amount of weight or boldness to use for a font. Allowed values are 'normal' and 'bold'. 
        @param GmlTextSymbols:
        @param GmlColour:
        @param GmlSvgParameters:
        """
        #: True if 'size' is expressed in absolute values. Default is false.
        self.absoluteSize = absoluteSize

        #: The style to use for a font. The allowed values are 'normal', 'italic', and 'oblique'.
        self.style = style

        #: The size to use for the font in pixels. The default is defined to be 10 pixels, though various systems may have restrictions on what sizes are available.
        self.size = size

        #: Family name of a font to use. Allowed values are system-dependent. Any number of font-family attributes may be given and they are assumed to be in preferred order.
        self.family = family

        #: The amount of weight or boldness to use for a font. Allowed values are 'normal' and 'bold'.
        self.weight = weight

        self._GmlTextSymbols = []
        self.GmlTextSymbols = [] if GmlTextSymbols is None else GmlTextSymbols

        self._GmlColour = None
        self.GmlColour = GmlColour

        self._GmlSvgParameters = []
        self.GmlSvgParameters = [] if GmlSvgParameters is None else GmlSvgParameters

        super(GmlFont, self).__init__(**kw_args)

    def getGmlTextSymbols(self):
        
        return self._GmlTextSymbols

    def setGmlTextSymbols(self, value):
        for x in self._GmlTextSymbols:
            x._GmlFont = None
        for y in value:
            y._GmlFont = self
        self._GmlTextSymbols = value

    GmlTextSymbols = property(getGmlTextSymbols, setGmlTextSymbols)

    def addGmlTextSymbols(self, *GmlTextSymbols):
        for obj in GmlTextSymbols:
            obj._GmlFont = self
            self._GmlTextSymbols.append(obj)

    def removeGmlTextSymbols(self, *GmlTextSymbols):
        for obj in GmlTextSymbols:
            obj._GmlFont = None
            self._GmlTextSymbols.remove(obj)

    def getGmlColour(self):
        
        return self._GmlColour

    def setGmlColour(self, value):
        if self._GmlColour is not None:
            filtered = [x for x in self.GmlColour.GmlFonts if x != self]
            self._GmlColour._GmlFonts = filtered

        self._GmlColour = value
        if self._GmlColour is not None:
            self._GmlColour._GmlFonts.append(self)

    GmlColour = property(getGmlColour, setGmlColour)

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

