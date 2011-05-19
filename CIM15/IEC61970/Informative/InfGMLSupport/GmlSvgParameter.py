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

class GmlSvgParameter(IdentifiedObject):
    """Refers to an SVG/CSS graphical-formatting parameter. The parameter is identified using the 'name' attribute and the content of the element gives the SVG/CSS-coded value.Refers to an SVG/CSS graphical-formatting parameter. The parameter is identified using the 'name' attribute and the content of the element gives the SVG/CSS-coded value.
    """

    def __init__(self, attribute='', value='', GmlStokes=None, GmlFonts=None, GmlFills=None, *args, **kw_args):
        """Initialises a new 'GmlSvgParameter' instance.

        @param attribute: The attribute of the GmlSvgParameter. E.g., for 'Stroke', the following SvgParameters may be used: 'stroke' (color), 'stroke-opacity', 'stroke-width', 'stroke-linejoin', 'stroke-linecap', 'stroke-dasharray', and 'stroke-dashoffset'. Others are not officially supported. 
        @param value: The SVG/CSS-coded value of the associated SvgAttribute. 
        @param GmlStokes:
        @param GmlFonts:
        @param GmlFills:
        """
        #: The attribute of the GmlSvgParameter. E.g., for 'Stroke', the following SvgParameters may be used: 'stroke' (color), 'stroke-opacity', 'stroke-width', 'stroke-linejoin', 'stroke-linecap', 'stroke-dasharray', and 'stroke-dashoffset'. Others are not officially supported.
        self.attribute = attribute

        #: The SVG/CSS-coded value of the associated SvgAttribute.
        self.value = value

        self._GmlStokes = []
        self.GmlStokes = [] if GmlStokes is None else GmlStokes

        self._GmlFonts = []
        self.GmlFonts = [] if GmlFonts is None else GmlFonts

        self._GmlFills = []
        self.GmlFills = [] if GmlFills is None else GmlFills

        super(GmlSvgParameter, self).__init__(*args, **kw_args)

    _attrs = ["attribute", "value"]
    _attr_types = {"attribute": str, "value": str}
    _defaults = {"attribute": '', "value": ''}
    _enums = {}
    _refs = ["GmlStokes", "GmlFonts", "GmlFills"]
    _many_refs = ["GmlStokes", "GmlFonts", "GmlFills"]

    def getGmlStokes(self):
        
        return self._GmlStokes

    def setGmlStokes(self, value):
        for p in self._GmlStokes:
            filtered = [q for q in p.GmlSvgParameters if q != self]
            self._GmlStokes._GmlSvgParameters = filtered
        for r in value:
            if self not in r._GmlSvgParameters:
                r._GmlSvgParameters.append(self)
        self._GmlStokes = value

    GmlStokes = property(getGmlStokes, setGmlStokes)

    def addGmlStokes(self, *GmlStokes):
        for obj in GmlStokes:
            if self not in obj._GmlSvgParameters:
                obj._GmlSvgParameters.append(self)
            self._GmlStokes.append(obj)

    def removeGmlStokes(self, *GmlStokes):
        for obj in GmlStokes:
            if self in obj._GmlSvgParameters:
                obj._GmlSvgParameters.remove(self)
            self._GmlStokes.remove(obj)

    def getGmlFonts(self):
        
        return self._GmlFonts

    def setGmlFonts(self, value):
        for p in self._GmlFonts:
            filtered = [q for q in p.GmlSvgParameters if q != self]
            self._GmlFonts._GmlSvgParameters = filtered
        for r in value:
            if self not in r._GmlSvgParameters:
                r._GmlSvgParameters.append(self)
        self._GmlFonts = value

    GmlFonts = property(getGmlFonts, setGmlFonts)

    def addGmlFonts(self, *GmlFonts):
        for obj in GmlFonts:
            if self not in obj._GmlSvgParameters:
                obj._GmlSvgParameters.append(self)
            self._GmlFonts.append(obj)

    def removeGmlFonts(self, *GmlFonts):
        for obj in GmlFonts:
            if self in obj._GmlSvgParameters:
                obj._GmlSvgParameters.remove(self)
            self._GmlFonts.remove(obj)

    def getGmlFills(self):
        
        return self._GmlFills

    def setGmlFills(self, value):
        for p in self._GmlFills:
            filtered = [q for q in p.GmlSvgParameters if q != self]
            self._GmlFills._GmlSvgParameters = filtered
        for r in value:
            if self not in r._GmlSvgParameters:
                r._GmlSvgParameters.append(self)
        self._GmlFills = value

    GmlFills = property(getGmlFills, setGmlFills)

    def addGmlFills(self, *GmlFills):
        for obj in GmlFills:
            if self not in obj._GmlSvgParameters:
                obj._GmlSvgParameters.append(self)
            self._GmlFills.append(obj)

    def removeGmlFills(self, *GmlFills):
        for obj in GmlFills:
            if self in obj._GmlSvgParameters:
                obj._GmlSvgParameters.remove(self)
            self._GmlFills.remove(obj)

