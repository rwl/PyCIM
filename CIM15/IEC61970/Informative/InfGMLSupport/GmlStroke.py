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

class GmlStroke(IdentifiedObject):
    """The element encapsulating the graphical symbolization parameters for linear geometries.The element encapsulating the graphical symbolization parameters for linear geometries.
    """

    def __init__(self, lineCap='', width=0.0, linejoin='', dashArray='', lineStyle='', dashOffset='', opacity=0.0, GmlColour=None, GmlPolygonSymbols=None, GmlMarks=None, GmlSvgParameters=None, GmlLineSymbols=None, *args, **kw_args):
        """Initialises a new 'GmlStroke' instance.

        @param lineCap: Enumerated values telling how line strings should be capped (at the two ends of the line string). The values are represented as content strings.  The allowed values for line cap are 'butt', 'round', and 'square'. The default values are system-dependent. 
        @param width: The absolute width (thickness) of a stroke in pixels encoded as a float. The default is 1.0. Fractional numbers are allowed (with a system-dependent interpretation) but negative numbers are not. 
        @param linejoin: Enumerated values telling how line strings should be joined (between line segments). The values are represented as content strings.  The allowed values for line join are 'mitre', 'round', and 'bevel'. The default values are system-dependent. 
        @param dashArray: Encodes a dash pattern as a series of space separated floats. The first number gives the length in pixels of dash to draw, the second gives the amount of space to leave, and this pattern repeats. If an odd number of values is given, then the pattern is expanded by repeating it twice to give an even number of values. Decimal values have a system-dependent interpretation (usually depending on whether antialiasing is being used). The default is to draw an unbroken line. 
        @param lineStyle: The name of a defined line style. Usually will be an enumerated value and will be system-specific. 
        @param dashOffset: Specifies the distance as a float into the 'stroke-dasharray' pattern at which to start drawing. 
        @param opacity: Specifies the level of translucency to use when rendering the stroke. The value is encoded as a floating-point value between 0.0 and 1.0 with 0.0 representing completely transparent and 1.0 representing completely opaque, with a linear scale of translucency for intermediate values. The default value is 1.0 
        @param GmlColour:
        @param GmlPolygonSymbols:
        @param GmlMarks:
        @param GmlSvgParameters:
        @param GmlLineSymbols:
        """
        #: Enumerated values telling how line strings should be capped (at the two ends of the line string). The values are represented as content strings.  The allowed values for line cap are 'butt', 'round', and 'square'. The default values are system-dependent.
        self.lineCap = lineCap

        #: The absolute width (thickness) of a stroke in pixels encoded as a float. The default is 1.0. Fractional numbers are allowed (with a system-dependent interpretation) but negative numbers are not.
        self.width = width

        #: Enumerated values telling how line strings should be joined (between line segments). The values are represented as content strings.  The allowed values for line join are 'mitre', 'round', and 'bevel'. The default values are system-dependent.
        self.linejoin = linejoin

        #: Encodes a dash pattern as a series of space separated floats. The first number gives the length in pixels of dash to draw, the second gives the amount of space to leave, and this pattern repeats. If an odd number of values is given, then the pattern is expanded by repeating it twice to give an even number of values. Decimal values have a system-dependent interpretation (usually depending on whether antialiasing is being used). The default is to draw an unbroken line.
        self.dashArray = dashArray

        #: The name of a defined line style. Usually will be an enumerated value and will be system-specific.
        self.lineStyle = lineStyle

        #: Specifies the distance as a float into the 'stroke-dasharray' pattern at which to start drawing.
        self.dashOffset = dashOffset

        #: Specifies the level of translucency to use when rendering the stroke. The value is encoded as a floating-point value between 0.0 and 1.0 with 0.0 representing completely transparent and 1.0 representing completely opaque, with a linear scale of translucency for intermediate values. The default value is 1.0
        self.opacity = opacity

        self._GmlColour = None
        self.GmlColour = GmlColour

        self._GmlPolygonSymbols = []
        self.GmlPolygonSymbols = [] if GmlPolygonSymbols is None else GmlPolygonSymbols

        self._GmlMarks = []
        self.GmlMarks = [] if GmlMarks is None else GmlMarks

        self._GmlSvgParameters = []
        self.GmlSvgParameters = [] if GmlSvgParameters is None else GmlSvgParameters

        self._GmlLineSymbols = []
        self.GmlLineSymbols = [] if GmlLineSymbols is None else GmlLineSymbols

        super(GmlStroke, self).__init__(*args, **kw_args)

    _attrs = ["lineCap", "width", "linejoin", "dashArray", "lineStyle", "dashOffset", "opacity"]
    _attr_types = {"lineCap": str, "width": float, "linejoin": str, "dashArray": str, "lineStyle": str, "dashOffset": str, "opacity": float}
    _defaults = {"lineCap": '', "width": 0.0, "linejoin": '', "dashArray": '', "lineStyle": '', "dashOffset": '', "opacity": 0.0}
    _enums = {}
    _refs = ["GmlColour", "GmlPolygonSymbols", "GmlMarks", "GmlSvgParameters", "GmlLineSymbols"]
    _many_refs = ["GmlPolygonSymbols", "GmlMarks", "GmlSvgParameters", "GmlLineSymbols"]

    def getGmlColour(self):
        
        return self._GmlColour

    def setGmlColour(self, value):
        if self._GmlColour is not None:
            filtered = [x for x in self.GmlColour.GmlStrokes if x != self]
            self._GmlColour._GmlStrokes = filtered

        self._GmlColour = value
        if self._GmlColour is not None:
            if self not in self._GmlColour._GmlStrokes:
                self._GmlColour._GmlStrokes.append(self)

    GmlColour = property(getGmlColour, setGmlColour)

    def getGmlPolygonSymbols(self):
        
        return self._GmlPolygonSymbols

    def setGmlPolygonSymbols(self, value):
        for x in self._GmlPolygonSymbols:
            x.GmlStroke = None
        for y in value:
            y._GmlStroke = self
        self._GmlPolygonSymbols = value

    GmlPolygonSymbols = property(getGmlPolygonSymbols, setGmlPolygonSymbols)

    def addGmlPolygonSymbols(self, *GmlPolygonSymbols):
        for obj in GmlPolygonSymbols:
            obj.GmlStroke = self

    def removeGmlPolygonSymbols(self, *GmlPolygonSymbols):
        for obj in GmlPolygonSymbols:
            obj.GmlStroke = None

    def getGmlMarks(self):
        
        return self._GmlMarks

    def setGmlMarks(self, value):
        for p in self._GmlMarks:
            filtered = [q for q in p.GmlStrokes if q != self]
            self._GmlMarks._GmlStrokes = filtered
        for r in value:
            if self not in r._GmlStrokes:
                r._GmlStrokes.append(self)
        self._GmlMarks = value

    GmlMarks = property(getGmlMarks, setGmlMarks)

    def addGmlMarks(self, *GmlMarks):
        for obj in GmlMarks:
            if self not in obj._GmlStrokes:
                obj._GmlStrokes.append(self)
            self._GmlMarks.append(obj)

    def removeGmlMarks(self, *GmlMarks):
        for obj in GmlMarks:
            if self in obj._GmlStrokes:
                obj._GmlStrokes.remove(self)
            self._GmlMarks.remove(obj)

    def getGmlSvgParameters(self):
        
        return self._GmlSvgParameters

    def setGmlSvgParameters(self, value):
        for p in self._GmlSvgParameters:
            filtered = [q for q in p.GmlStokes if q != self]
            self._GmlSvgParameters._GmlStokes = filtered
        for r in value:
            if self not in r._GmlStokes:
                r._GmlStokes.append(self)
        self._GmlSvgParameters = value

    GmlSvgParameters = property(getGmlSvgParameters, setGmlSvgParameters)

    def addGmlSvgParameters(self, *GmlSvgParameters):
        for obj in GmlSvgParameters:
            if self not in obj._GmlStokes:
                obj._GmlStokes.append(self)
            self._GmlSvgParameters.append(obj)

    def removeGmlSvgParameters(self, *GmlSvgParameters):
        for obj in GmlSvgParameters:
            if self in obj._GmlStokes:
                obj._GmlStokes.remove(self)
            self._GmlSvgParameters.remove(obj)

    def getGmlLineSymbols(self):
        
        return self._GmlLineSymbols

    def setGmlLineSymbols(self, value):
        for x in self._GmlLineSymbols:
            x.GmlStroke = None
        for y in value:
            y._GmlStroke = self
        self._GmlLineSymbols = value

    GmlLineSymbols = property(getGmlLineSymbols, setGmlLineSymbols)

    def addGmlLineSymbols(self, *GmlLineSymbols):
        for obj in GmlLineSymbols:
            obj.GmlStroke = self

    def removeGmlLineSymbols(self, *GmlLineSymbols):
        for obj in GmlLineSymbols:
            obj.GmlStroke = None

