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

class GmlTextSymbol(GmlSymbol):
    """Used for styling text labels, i.e., for rendering them according to various graphical parameters.
    """

    def __init__(self, minFontSize=0, property='', fieldID='', label='', labelType='', GmlFont=None, GmlLabelPlacement=None, GmlFill=None, GmlHalo=None, GmlDiagramObject=None, *args, **kw_args):
        """Initializes a new 'GmlTextSymbol' instance.

        @param minFontSize: The minimum font size allowed. 
        @param property: Generic method for capturing all unspecified information pertaining to the TextSymbol. 
        @param fieldID: The name of the field of the class being annotated. Most objects will include name, description, and aliasName. Many objects may contain other fields such as comment, status, etc. 
        @param label: Text-label content. If the value is not provided, then no text will be rendered. 
        @param labelType: The type-classification of a label. 
        @param GmlFont:
        @param GmlLabelPlacement:
        @param GmlFill:
        @param GmlHalo:
        @param GmlDiagramObject:
        """
        #: The minimum font size allowed.
        self.minFontSize = minFontSize

        #: Generic method for capturing all unspecified information pertaining to the TextSymbol.
        self.property = property

        #: The name of the field of the class being annotated. Most objects will include name, description, and aliasName. Many objects may contain other fields such as comment, status, etc.
        self.fieldID = fieldID

        #: Text-label content. If the value is not provided, then no text will be rendered.
        self.label = label

        #: The type-classification of a label.
        self.labelType = labelType

        self._GmlFont = None
        self.GmlFont = GmlFont

        self._GmlLabelPlacement = None
        self.GmlLabelPlacement = GmlLabelPlacement

        self._GmlFill = None
        self.GmlFill = GmlFill

        self._GmlHalo = None
        self.GmlHalo = GmlHalo

        self._GmlDiagramObject = None
        self.GmlDiagramObject = GmlDiagramObject

        super(GmlTextSymbol, self).__init__(*args, **kw_args)

    def getGmlFont(self):
        
        return self._GmlFont

    def setGmlFont(self, value):
        if self._GmlFont is not None:
            filtered = [x for x in self.GmlFont.GmlTextSymbols if x != self]
            self._GmlFont._GmlTextSymbols = filtered

        self._GmlFont = value
        if self._GmlFont is not None:
            self._GmlFont._GmlTextSymbols.append(self)

    GmlFont = property(getGmlFont, setGmlFont)

    def getGmlLabelPlacement(self):
        
        return self._GmlLabelPlacement

    def setGmlLabelPlacement(self, value):
        if self._GmlLabelPlacement is not None:
            filtered = [x for x in self.GmlLabelPlacement.GmlTextSymbols if x != self]
            self._GmlLabelPlacement._GmlTextSymbols = filtered

        self._GmlLabelPlacement = value
        if self._GmlLabelPlacement is not None:
            self._GmlLabelPlacement._GmlTextSymbols.append(self)

    GmlLabelPlacement = property(getGmlLabelPlacement, setGmlLabelPlacement)

    def getGmlFill(self):
        
        return self._GmlFill

    def setGmlFill(self, value):
        if self._GmlFill is not None:
            filtered = [x for x in self.GmlFill.GmlTextSymbols if x != self]
            self._GmlFill._GmlTextSymbols = filtered

        self._GmlFill = value
        if self._GmlFill is not None:
            self._GmlFill._GmlTextSymbols.append(self)

    GmlFill = property(getGmlFill, setGmlFill)

    def getGmlHalo(self):
        
        return self._GmlHalo

    def setGmlHalo(self, value):
        if self._GmlHalo is not None:
            filtered = [x for x in self.GmlHalo.GmlTextSymbols if x != self]
            self._GmlHalo._GmlTextSymbols = filtered

        self._GmlHalo = value
        if self._GmlHalo is not None:
            self._GmlHalo._GmlTextSymbols.append(self)

    GmlHalo = property(getGmlHalo, setGmlHalo)

    def getGmlDiagramObject(self):
        
        return self._GmlDiagramObject

    def setGmlDiagramObject(self, value):
        if self._GmlDiagramObject is not None:
            filtered = [x for x in self.GmlDiagramObject.GmlTextSymbols if x != self]
            self._GmlDiagramObject._GmlTextSymbols = filtered

        self._GmlDiagramObject = value
        if self._GmlDiagramObject is not None:
            self._GmlDiagramObject._GmlTextSymbols.append(self)

    GmlDiagramObject = property(getGmlDiagramObject, setGmlDiagramObject)

