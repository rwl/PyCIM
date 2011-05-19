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

class GmlLabelStyle(IdentifiedObject):
    """The style for the text that is to be displayed along with the graphical representation of a feature. The content of the label is not necessarily defined in the GML data set. More precisely, the content can be static text specified in the style itself and the text from the GML data set. Label style has two elements: gml:style that specifies the style and gml:label that is used to compose the label content.The style for the text that is to be displayed along with the graphical representation of a feature. The content of the label is not necessarily defined in the GML data set. More precisely, the content can be static text specified in the style itself and the text from the GML data set. Label style has two elements: gml:style that specifies the style and gml:label that is used to compose the label content.
    """

    def __init__(self, transform='', labelExpression='', style='', GmlTopologyStyles=None, GmlGeometryStyles=None, GmlFeatureStyle=None, *args, **kw_args):
        """Initialises a new 'GmlLabelStyle' instance.

        @param transform: Allows us to specify a transformation expression that will be applied to the symbol in the rendering phase. Its type is xsd:string and the value is specified in the SVG specification (transform attribute). 
        @param labelExpression: Allows both text content and unbounded number of gml:LabelExpression elements. The value of gml:LabelExpression element is an XPath expression that selects the value of some property of the feature. 
        @param style: Used to specify the style of the rendered text. The CSS2 styling expressions grammar should be used to express graphic properties. 
        @param GmlTopologyStyles:
        @param GmlGeometryStyles:
        @param GmlFeatureStyle:
        """
        #: Allows us to specify a transformation expression that will be applied to the symbol in the rendering phase. Its type is xsd:string and the value is specified in the SVG specification (transform attribute).
        self.transform = transform

        #: Allows both text content and unbounded number of gml:LabelExpression elements. The value of gml:LabelExpression element is an XPath expression that selects the value of some property of the feature.
        self.labelExpression = labelExpression

        #: Used to specify the style of the rendered text. The CSS2 styling expressions grammar should be used to express graphic properties.
        self.style = style

        self._GmlTopologyStyles = []
        self.GmlTopologyStyles = [] if GmlTopologyStyles is None else GmlTopologyStyles

        self._GmlGeometryStyles = []
        self.GmlGeometryStyles = [] if GmlGeometryStyles is None else GmlGeometryStyles

        self._GmlFeatureStyle = None
        self.GmlFeatureStyle = GmlFeatureStyle

        super(GmlLabelStyle, self).__init__(*args, **kw_args)

    _attrs = ["transform", "labelExpression", "style"]
    _attr_types = {"transform": str, "labelExpression": str, "style": str}
    _defaults = {"transform": '', "labelExpression": '', "style": ''}
    _enums = {}
    _refs = ["GmlTopologyStyles", "GmlGeometryStyles", "GmlFeatureStyle"]
    _many_refs = ["GmlTopologyStyles", "GmlGeometryStyles"]

    def getGmlTopologyStyles(self):
        
        return self._GmlTopologyStyles

    def setGmlTopologyStyles(self, value):
        for x in self._GmlTopologyStyles:
            x.GmlLableStyle = None
        for y in value:
            y._GmlLableStyle = self
        self._GmlTopologyStyles = value

    GmlTopologyStyles = property(getGmlTopologyStyles, setGmlTopologyStyles)

    def addGmlTopologyStyles(self, *GmlTopologyStyles):
        for obj in GmlTopologyStyles:
            obj.GmlLableStyle = self

    def removeGmlTopologyStyles(self, *GmlTopologyStyles):
        for obj in GmlTopologyStyles:
            obj.GmlLableStyle = None

    def getGmlGeometryStyles(self):
        
        return self._GmlGeometryStyles

    def setGmlGeometryStyles(self, value):
        for x in self._GmlGeometryStyles:
            x.GmlLabelStyle = None
        for y in value:
            y._GmlLabelStyle = self
        self._GmlGeometryStyles = value

    GmlGeometryStyles = property(getGmlGeometryStyles, setGmlGeometryStyles)

    def addGmlGeometryStyles(self, *GmlGeometryStyles):
        for obj in GmlGeometryStyles:
            obj.GmlLabelStyle = self

    def removeGmlGeometryStyles(self, *GmlGeometryStyles):
        for obj in GmlGeometryStyles:
            obj.GmlLabelStyle = None

    def getGmlFeatureStyle(self):
        
        return self._GmlFeatureStyle

    def setGmlFeatureStyle(self, value):
        if self._GmlFeatureStyle is not None:
            filtered = [x for x in self.GmlFeatureStyle.GmlLabelStyles if x != self]
            self._GmlFeatureStyle._GmlLabelStyles = filtered

        self._GmlFeatureStyle = value
        if self._GmlFeatureStyle is not None:
            if self not in self._GmlFeatureStyle._GmlLabelStyles:
                self._GmlFeatureStyle._GmlLabelStyles.append(self)

    GmlFeatureStyle = property(getGmlFeatureStyle, setGmlFeatureStyle)

