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

class GmlLineSymbol(GmlSymbol):
    """Used to style a 'stroke' along a linear geometry type, such as a string of line segments.
    """

    def __init__(self, sourceSide='', GmlDiagramObject=None, GmlStroke=None, *args, **kw_args):
        """Initializes a new 'GmlLineSymbol' instance.

        @param sourceSide: For dynamic network update (i.e. colouring) purposes 
        @param GmlDiagramObject:
        @param GmlStroke:
        """
        #: For dynamic network update (i.e. colouring) purposes
        self.sourceSide = sourceSide

        self._GmlDiagramObject = None
        self.GmlDiagramObject = GmlDiagramObject

        self._GmlStroke = None
        self.GmlStroke = GmlStroke

        super(GmlLineSymbol, self).__init__(*args, **kw_args)

    def getGmlDiagramObject(self):
        
        return self._GmlDiagramObject

    def setGmlDiagramObject(self, value):
        if self._GmlDiagramObject is not None:
            filtered = [x for x in self.GmlDiagramObject.GmlLineSymbols if x != self]
            self._GmlDiagramObject._GmlLineSymbols = filtered

        self._GmlDiagramObject = value
        if self._GmlDiagramObject is not None:
            self._GmlDiagramObject._GmlLineSymbols.append(self)

    GmlDiagramObject = property(getGmlDiagramObject, setGmlDiagramObject)

    def getGmlStroke(self):
        
        return self._GmlStroke

    def setGmlStroke(self, value):
        if self._GmlStroke is not None:
            filtered = [x for x in self.GmlStroke.GmlLineSymbols if x != self]
            self._GmlStroke._GmlLineSymbols = filtered

        self._GmlStroke = value
        if self._GmlStroke is not None:
            self._GmlStroke._GmlLineSymbols.append(self)

    GmlStroke = property(getGmlStroke, setGmlStroke)

