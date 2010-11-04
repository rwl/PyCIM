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

class GmlPointSymbol(GmlSymbol):
    """Used to draw a 'graphic' at a point.
    """

    def __init__(self, GmlGraphic=None, GmlDiagramObject=None, **kw_args):
        """Initializes a new 'GmlPointSymbol' instance.

        @param GmlGraphic:
        @param GmlDiagramObject:
        """
        self._GmlGraphic = None
        self.GmlGraphic = GmlGraphic

        self._GmlDiagramObject = None
        self.GmlDiagramObject = GmlDiagramObject

        super(GmlPointSymbol, self).__init__(**kw_args)

    def getGmlGraphic(self):
        
        return self._GmlGraphic

    def setGmlGraphic(self, value):
        if self._GmlGraphic is not None:
            filtered = [x for x in self.GmlGraphic.GmlPointSymbols if x != self]
            self._GmlGraphic._GmlPointSymbols = filtered

        self._GmlGraphic = value
        if self._GmlGraphic is not None:
            self._GmlGraphic._GmlPointSymbols.append(self)

    GmlGraphic = property(getGmlGraphic, setGmlGraphic)

    def getGmlDiagramObject(self):
        
        return self._GmlDiagramObject

    def setGmlDiagramObject(self, value):
        if self._GmlDiagramObject is not None:
            filtered = [x for x in self.GmlDiagramObject.GmlPointSymbols if x != self]
            self._GmlDiagramObject._GmlPointSymbols = filtered

        self._GmlDiagramObject = value
        if self._GmlDiagramObject is not None:
            self._GmlDiagramObject._GmlPointSymbols.append(self)

    GmlDiagramObject = property(getGmlDiagramObject, setGmlDiagramObject)

