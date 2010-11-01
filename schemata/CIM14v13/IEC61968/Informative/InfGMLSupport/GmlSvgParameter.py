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

class GmlSvgParameter(IdentifiedObject):
    """Refers to an SVG/CSS graphical-formatting parameter. The parameter is identified using the 'name' attribute and the content of the element gives the SVG/CSS-coded value.
    """

    def __init__(self, value='', attribute='', GmlStokes=None, GmlFills=None, GmlFonts=None, *args, **kw_args):
        """Initializes a new 'GmlSvgParameter' instance.

        @param value: The SVG/CSS-coded value of the associated SvgAttribute. 
        @param attribute: The attribute of the GmlSvgParameter. E.g., for 'Stroke', the following SvgParameters may be used: 'stroke' (color), 'stroke-opacity', 'stroke-width', 'stroke-linejoin', 'stroke-linecap', 'stroke-dasharray', and 'stroke-dashoffset'. Others are not officially supported. 
        @param GmlStokes:
        @param GmlFills:
        @param GmlFonts:
        """
        #: The SVG/CSS-coded value of the associated SvgAttribute. 
        self.value = value

        #: The attribute of the GmlSvgParameter. E.g., for 'Stroke', the following SvgParameters may be used: 'stroke' (color), 'stroke-opacity', 'stroke-width', 'stroke-linejoin', 'stroke-linecap', 'stroke-dasharray', and 'stroke-dashoffset'. Others are not officially supported. 
        self.attribute = attribute

        self._GmlStokes = []
        self.GmlStokes = [] if GmlStokes is None else GmlStokes

        self._GmlFills = []
        self.GmlFills = [] if GmlFills is None else GmlFills

        self._GmlFonts = []
        self.GmlFonts = [] if GmlFonts is None else GmlFonts

        super(GmlSvgParameter, self).__init__(*args, **kw_args)

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

