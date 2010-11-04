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

from CIM14v13.IEC61968.Informative.InfGMLSupport.GmlSymbol import GmlSymbol

class GmlPolygonSymbol(GmlSymbol):
    """Used to draw a polygon (or other area-type geometries), including filling its interior and stroking its border (outline).
    """

    def __init__(self, GmlFill=None, GmlDiagramObject=None, GmlStroke=None, **kw_args):
        """Initializes a new 'GmlPolygonSymbol' instance.

        @param GmlFill:
        @param GmlDiagramObject:
        @param GmlStroke:
        """
        self._GmlFill = None
        self.GmlFill = GmlFill

        self._GmlDiagramObject = None
        self.GmlDiagramObject = GmlDiagramObject

        self._GmlStroke = None
        self.GmlStroke = GmlStroke

        super(GmlPolygonSymbol, self).__init__(**kw_args)

    def getGmlFill(self):
        
        return self._GmlFill

    def setGmlFill(self, value):
        if self._GmlFill is not None:
            filtered = [x for x in self.GmlFill.GmlPolygonSymbols if x != self]
            self._GmlFill._GmlPolygonSymbols = filtered

        self._GmlFill = value
        if self._GmlFill is not None:
            self._GmlFill._GmlPolygonSymbols.append(self)

    GmlFill = property(getGmlFill, setGmlFill)

    def getGmlDiagramObject(self):
        
        return self._GmlDiagramObject

    def setGmlDiagramObject(self, value):
        if self._GmlDiagramObject is not None:
            filtered = [x for x in self.GmlDiagramObject.GmlPolygonSymbols if x != self]
            self._GmlDiagramObject._GmlPolygonSymbols = filtered

        self._GmlDiagramObject = value
        if self._GmlDiagramObject is not None:
            self._GmlDiagramObject._GmlPolygonSymbols.append(self)

    GmlDiagramObject = property(getGmlDiagramObject, setGmlDiagramObject)

    def getGmlStroke(self):
        
        return self._GmlStroke

    def setGmlStroke(self, value):
        if self._GmlStroke is not None:
            filtered = [x for x in self.GmlStroke.GmlPolygonSymbols if x != self]
            self._GmlStroke._GmlPolygonSymbols = filtered

        self._GmlStroke = value
        if self._GmlStroke is not None:
            self._GmlStroke._GmlPolygonSymbols.append(self)

    GmlStroke = property(getGmlStroke, setGmlStroke)

