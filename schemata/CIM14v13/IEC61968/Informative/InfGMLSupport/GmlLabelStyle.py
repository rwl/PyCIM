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

class GmlLabelStyle(IdentifiedObject):
    """The style for the text that is to be displayed along with the graphical representation of a feature. The content of the label is not necessarily defined in the GML data set. More precisely, the content can be static text specified in the style itself and the text from the GML data set. Label style has two elements: gml:style that specifies the style and gml:label that is used to compose the label content.
    """

    def __init__(self, transform='', style='', labelExpression='', GmlGeometryStyles=None, GmlFeatureStyle=None, GmlTopologyStyles=None, *args, **kw_args):
        """Initializes a new 'GmlLabelStyle' instance.

        @param transform: Allows us to specify a transformation expression that will be applied to the symbol in the rendering phase. Its type is xsd:string and the value is specified in the SVG specification (transform attribute). 
        @param style: Used to specify the style of the rendered text. The CSS2 styling expressions grammar should be used to express graphic properties. 
        @param labelExpression: Allows both text content and unbounded number of gml:LabelExpression elements. The value of gml:LabelExpression element is an XPath expression that selects the value of some property of the feature. 
        @param GmlGeometryStyles:
        @param GmlFeatureStyle:
        @param GmlTopologyStyles:
        """
        #: Allows us to specify a transformation expression that will be applied to the symbol in the rendering phase. Its type is xsd:string and the value is specified in the SVG specification (transform attribute).
        self.transform = transform

        #: Used to specify the style of the rendered text. The CSS2 styling expressions grammar should be used to express graphic properties.
        self.style = style

        #: Allows both text content and unbounded number of gml:LabelExpression elements. The value of gml:LabelExpression element is an XPath expression that selects the value of some property of the feature.
        self.labelExpression = labelExpression

        self._GmlGeometryStyles = []
        self.GmlGeometryStyles = [] if GmlGeometryStyles is None else GmlGeometryStyles

        self._GmlFeatureStyle = None
        self.GmlFeatureStyle = GmlFeatureStyle

        self._GmlTopologyStyles = []
        self.GmlTopologyStyles = [] if GmlTopologyStyles is None else GmlTopologyStyles

        super(GmlLabelStyle, self).__init__(*args, **kw_args)

    def getGmlGeometryStyles(self):
        
        return self._GmlGeometryStyles

    def setGmlGeometryStyles(self, value):
        for x in self._GmlGeometryStyles:
            x._GmlLabelStyle = None
        for y in value:
            y._GmlLabelStyle = self
        self._GmlGeometryStyles = value

    GmlGeometryStyles = property(getGmlGeometryStyles, setGmlGeometryStyles)

    def addGmlGeometryStyles(self, *GmlGeometryStyles):
        for obj in GmlGeometryStyles:
            obj._GmlLabelStyle = self
            self._GmlGeometryStyles.append(obj)

    def removeGmlGeometryStyles(self, *GmlGeometryStyles):
        for obj in GmlGeometryStyles:
            obj._GmlLabelStyle = None
            self._GmlGeometryStyles.remove(obj)

    def getGmlFeatureStyle(self):
        
        return self._GmlFeatureStyle

    def setGmlFeatureStyle(self, value):
        if self._GmlFeatureStyle is not None:
            filtered = [x for x in self.GmlFeatureStyle.GmlLabelStyles if x != self]
            self._GmlFeatureStyle._GmlLabelStyles = filtered

        self._GmlFeatureStyle = value
        if self._GmlFeatureStyle is not None:
            self._GmlFeatureStyle._GmlLabelStyles.append(self)

    GmlFeatureStyle = property(getGmlFeatureStyle, setGmlFeatureStyle)

    def getGmlTopologyStyles(self):
        
        return self._GmlTopologyStyles

    def setGmlTopologyStyles(self, value):
        for x in self._GmlTopologyStyles:
            x._GmlLableStyle = None
        for y in value:
            y._GmlLableStyle = self
        self._GmlTopologyStyles = value

    GmlTopologyStyles = property(getGmlTopologyStyles, setGmlTopologyStyles)

    def addGmlTopologyStyles(self, *GmlTopologyStyles):
        for obj in GmlTopologyStyles:
            obj._GmlLableStyle = self
            self._GmlTopologyStyles.append(obj)

    def removeGmlTopologyStyles(self, *GmlTopologyStyles):
        for obj in GmlTopologyStyles:
            obj._GmlLableStyle = None
            self._GmlTopologyStyles.remove(obj)

