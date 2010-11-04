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

class GmlFill(IdentifiedObject):
    """Specifies how the area of the geometry will be filled.
    """

    def __init__(self, opacity=0.0, GmlColour=None, GmlPolygonSymbols=None, GmlSvgParameters=None, GmlMarks=None, GmlTextSymbols=None, *args, **kw_args):
        """Initializes a new 'GmlFill' instance.

        @param opacity: Specifies the level of translucency to use when rendering the Fill. The value is encoded as a floating-point value between 0.0 and 1.0 with 0.0 representing completely transparent and 1.0 representing completely opaque, with a linear scale of translucency for intermediate values. The default value is 1.0 
        @param GmlColour:
        @param GmlPolygonSymbols:
        @param GmlSvgParameters:
        @param GmlMarks:
        @param GmlTextSymbols:
        """
        #: Specifies the level of translucency to use when rendering the Fill. The value is encoded as a floating-point value between 0.0 and 1.0 with 0.0 representing completely transparent and 1.0 representing completely opaque, with a linear scale of translucency for intermediate values. The default value is 1.0
        self.opacity = opacity

        self._GmlColour = None
        self.GmlColour = GmlColour

        self._GmlPolygonSymbols = []
        self.GmlPolygonSymbols = [] if GmlPolygonSymbols is None else GmlPolygonSymbols

        self._GmlSvgParameters = []
        self.GmlSvgParameters = [] if GmlSvgParameters is None else GmlSvgParameters

        self._GmlMarks = []
        self.GmlMarks = [] if GmlMarks is None else GmlMarks

        self._GmlTextSymbols = []
        self.GmlTextSymbols = [] if GmlTextSymbols is None else GmlTextSymbols

        super(GmlFill, self).__init__(*args, **kw_args)

    def getGmlColour(self):
        
        return self._GmlColour

    def setGmlColour(self, value):
        if self._GmlColour is not None:
            filtered = [x for x in self.GmlColour.GmlFills if x != self]
            self._GmlColour._GmlFills = filtered

        self._GmlColour = value
        if self._GmlColour is not None:
            self._GmlColour._GmlFills.append(self)

    GmlColour = property(getGmlColour, setGmlColour)

    def getGmlPolygonSymbols(self):
        
        return self._GmlPolygonSymbols

    def setGmlPolygonSymbols(self, value):
        for x in self._GmlPolygonSymbols:
            x._GmlFill = None
        for y in value:
            y._GmlFill = self
        self._GmlPolygonSymbols = value

    GmlPolygonSymbols = property(getGmlPolygonSymbols, setGmlPolygonSymbols)

    def addGmlPolygonSymbols(self, *GmlPolygonSymbols):
        for obj in GmlPolygonSymbols:
            obj._GmlFill = self
            self._GmlPolygonSymbols.append(obj)

    def removeGmlPolygonSymbols(self, *GmlPolygonSymbols):
        for obj in GmlPolygonSymbols:
            obj._GmlFill = None
            self._GmlPolygonSymbols.remove(obj)

    def getGmlSvgParameters(self):
        
        return self._GmlSvgParameters

    def setGmlSvgParameters(self, value):
        for p in self._GmlSvgParameters:
            filtered = [q for q in p.GmlFills if q != self]
            self._GmlSvgParameters._GmlFills = filtered
        for r in value:
            if self not in r._GmlFills:
                r._GmlFills.append(self)
        self._GmlSvgParameters = value

    GmlSvgParameters = property(getGmlSvgParameters, setGmlSvgParameters)

    def addGmlSvgParameters(self, *GmlSvgParameters):
        for obj in GmlSvgParameters:
            if self not in obj._GmlFills:
                obj._GmlFills.append(self)
            self._GmlSvgParameters.append(obj)

    def removeGmlSvgParameters(self, *GmlSvgParameters):
        for obj in GmlSvgParameters:
            if self in obj._GmlFills:
                obj._GmlFills.remove(self)
            self._GmlSvgParameters.remove(obj)

    def getGmlMarks(self):
        
        return self._GmlMarks

    def setGmlMarks(self, value):
        for p in self._GmlMarks:
            filtered = [q for q in p.GmlFIlls if q != self]
            self._GmlMarks._GmlFIlls = filtered
        for r in value:
            if self not in r._GmlFIlls:
                r._GmlFIlls.append(self)
        self._GmlMarks = value

    GmlMarks = property(getGmlMarks, setGmlMarks)

    def addGmlMarks(self, *GmlMarks):
        for obj in GmlMarks:
            if self not in obj._GmlFIlls:
                obj._GmlFIlls.append(self)
            self._GmlMarks.append(obj)

    def removeGmlMarks(self, *GmlMarks):
        for obj in GmlMarks:
            if self in obj._GmlFIlls:
                obj._GmlFIlls.remove(self)
            self._GmlMarks.remove(obj)

    def getGmlTextSymbols(self):
        
        return self._GmlTextSymbols

    def setGmlTextSymbols(self, value):
        for x in self._GmlTextSymbols:
            x._GmlFill = None
        for y in value:
            y._GmlFill = self
        self._GmlTextSymbols = value

    GmlTextSymbols = property(getGmlTextSymbols, setGmlTextSymbols)

    def addGmlTextSymbols(self, *GmlTextSymbols):
        for obj in GmlTextSymbols:
            obj._GmlFill = self
            self._GmlTextSymbols.append(obj)

    def removeGmlTextSymbols(self, *GmlTextSymbols):
        for obj in GmlTextSymbols:
            obj._GmlFill = None
            self._GmlTextSymbols.remove(obj)

