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

from CIM15.IEC61970.Informative.InfGMLSupport.GmlSymbol import GmlSymbol

class GmlTextSymbol(GmlSymbol):
    """Used for styling text labels, i.e., for rendering them according to various graphical parameters.Used for styling text labels, i.e., for rendering them according to various graphical parameters.
    """

    def __init__(self, label='', labelType='', fieldID='', minFontSize=0, property='', GmlFill=None, GmlLabelPlacement=None, GmlHalo=None, GmlFont=None, GmlDiagramObject=None, *args, **kw_args):
        """Initialises a new 'GmlTextSymbol' instance.

        @param label: Text-label content. If the value is not provided, then no text will be rendered. 
        @param labelType: The type-classification of a label. 
        @param fieldID: The name of the field of the class being annotated. Most objects will include name, description, and aliasName. Many objects may contain other fields such as comment, status, etc. 
        @param minFontSize: The minimum font size allowed. 
        @param property: Generic method for capturing all unspecified information pertaining to the TextSymbol. 
        @param GmlFill:
        @param GmlLabelPlacement:
        @param GmlHalo:
        @param GmlFont:
        @param GmlDiagramObject:
        """
        #: Text-label content. If the value is not provided, then no text will be rendered.
        self.label = label

        #: The type-classification of a label.
        self.labelType = labelType

        #: The name of the field of the class being annotated. Most objects will include name, description, and aliasName. Many objects may contain other fields such as comment, status, etc.
        self.fieldID = fieldID

        #: The minimum font size allowed.
        self.minFontSize = minFontSize

        #: Generic method for capturing all unspecified information pertaining to the TextSymbol.
        self.property = property

        self._GmlFill = None
        self.GmlFill = GmlFill

        self._GmlLabelPlacement = None
        self.GmlLabelPlacement = GmlLabelPlacement

        self._GmlHalo = None
        self.GmlHalo = GmlHalo

        self._GmlFont = None
        self.GmlFont = GmlFont

        self._GmlDiagramObject = None
        self.GmlDiagramObject = GmlDiagramObject

        super(GmlTextSymbol, self).__init__(*args, **kw_args)

    _attrs = ["label", "labelType", "fieldID", "minFontSize", "property"]
    _attr_types = {"label": str, "labelType": str, "fieldID": str, "minFontSize": int, "property": str}
    _defaults = {"label": '', "labelType": '', "fieldID": '', "minFontSize": 0, "property": ''}
    _enums = {}
    _refs = ["GmlFill", "GmlLabelPlacement", "GmlHalo", "GmlFont", "GmlDiagramObject"]
    _many_refs = []

    def getGmlFill(self):
        
        return self._GmlFill

    def setGmlFill(self, value):
        if self._GmlFill is not None:
            filtered = [x for x in self.GmlFill.GmlTextSymbols if x != self]
            self._GmlFill._GmlTextSymbols = filtered

        self._GmlFill = value
        if self._GmlFill is not None:
            if self not in self._GmlFill._GmlTextSymbols:
                self._GmlFill._GmlTextSymbols.append(self)

    GmlFill = property(getGmlFill, setGmlFill)

    def getGmlLabelPlacement(self):
        
        return self._GmlLabelPlacement

    def setGmlLabelPlacement(self, value):
        if self._GmlLabelPlacement is not None:
            filtered = [x for x in self.GmlLabelPlacement.GmlTextSymbols if x != self]
            self._GmlLabelPlacement._GmlTextSymbols = filtered

        self._GmlLabelPlacement = value
        if self._GmlLabelPlacement is not None:
            if self not in self._GmlLabelPlacement._GmlTextSymbols:
                self._GmlLabelPlacement._GmlTextSymbols.append(self)

    GmlLabelPlacement = property(getGmlLabelPlacement, setGmlLabelPlacement)

    def getGmlHalo(self):
        
        return self._GmlHalo

    def setGmlHalo(self, value):
        if self._GmlHalo is not None:
            filtered = [x for x in self.GmlHalo.GmlTextSymbols if x != self]
            self._GmlHalo._GmlTextSymbols = filtered

        self._GmlHalo = value
        if self._GmlHalo is not None:
            if self not in self._GmlHalo._GmlTextSymbols:
                self._GmlHalo._GmlTextSymbols.append(self)

    GmlHalo = property(getGmlHalo, setGmlHalo)

    def getGmlFont(self):
        
        return self._GmlFont

    def setGmlFont(self, value):
        if self._GmlFont is not None:
            filtered = [x for x in self.GmlFont.GmlTextSymbols if x != self]
            self._GmlFont._GmlTextSymbols = filtered

        self._GmlFont = value
        if self._GmlFont is not None:
            if self not in self._GmlFont._GmlTextSymbols:
                self._GmlFont._GmlTextSymbols.append(self)

    GmlFont = property(getGmlFont, setGmlFont)

    def getGmlDiagramObject(self):
        
        return self._GmlDiagramObject

    def setGmlDiagramObject(self, value):
        if self._GmlDiagramObject is not None:
            filtered = [x for x in self.GmlDiagramObject.GmlTextSymbols if x != self]
            self._GmlDiagramObject._GmlTextSymbols = filtered

        self._GmlDiagramObject = value
        if self._GmlDiagramObject is not None:
            if self not in self._GmlDiagramObject._GmlTextSymbols:
                self._GmlDiagramObject._GmlTextSymbols.append(self)

    GmlDiagramObject = property(getGmlDiagramObject, setGmlDiagramObject)

