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

class GmlGeometryStyle(IdentifiedObject):
    """The style for one geometry of a feature. Any number of geometry style descriptors can be assigned to one feature style. This is usually required for features with multiple geometry properties.The style for one geometry of a feature. Any number of geometry style descriptors can be assigned to one feature style. This is usually required for features with multiple geometry properties.
    """

    def __init__(self, geometryProperty='', geometryType='', symbol='', GmlFeatureStyle=None, GmlLabelStyle=None, *args, **kw_args):
        """Initialises a new 'GmlGeometryStyle' instance.

        @param geometryProperty: The name of the geometry property of a feature to which this GeometryStyle applies. 
        @param geometryType: It is necessary to specify the geometry type using this attribute as well since the application schema of the geometry property may allow different geometries as its value. 
        @param symbol: Graphical symbol used to render a geometry or a topology. A symbol is a description of graphical attributes of a graphical object without a particular, implicit meaning. It can be a description of a line, circle, polygon or more complex drawing. 
        @param GmlFeatureStyle:
        @param GmlLabelStyle:
        """
        #: The name of the geometry property of a feature to which this GeometryStyle applies.
        self.geometryProperty = geometryProperty

        #: It is necessary to specify the geometry type using this attribute as well since the application schema of the geometry property may allow different geometries as its value.
        self.geometryType = geometryType

        #: Graphical symbol used to render a geometry or a topology. A symbol is a description of graphical attributes of a graphical object without a particular, implicit meaning. It can be a description of a line, circle, polygon or more complex drawing.
        self.symbol = symbol

        self._GmlFeatureStyle = None
        self.GmlFeatureStyle = GmlFeatureStyle

        self._GmlLabelStyle = None
        self.GmlLabelStyle = GmlLabelStyle

        super(GmlGeometryStyle, self).__init__(*args, **kw_args)

    _attrs = ["geometryProperty", "geometryType", "symbol"]
    _attr_types = {"geometryProperty": str, "geometryType": str, "symbol": str}
    _defaults = {"geometryProperty": '', "geometryType": '', "symbol": ''}
    _enums = {}
    _refs = ["GmlFeatureStyle", "GmlLabelStyle"]
    _many_refs = []

    def getGmlFeatureStyle(self):
        
        return self._GmlFeatureStyle

    def setGmlFeatureStyle(self, value):
        if self._GmlFeatureStyle is not None:
            filtered = [x for x in self.GmlFeatureStyle.GmlGeometryStyles if x != self]
            self._GmlFeatureStyle._GmlGeometryStyles = filtered

        self._GmlFeatureStyle = value
        if self._GmlFeatureStyle is not None:
            if self not in self._GmlFeatureStyle._GmlGeometryStyles:
                self._GmlFeatureStyle._GmlGeometryStyles.append(self)

    GmlFeatureStyle = property(getGmlFeatureStyle, setGmlFeatureStyle)

    def getGmlLabelStyle(self):
        
        return self._GmlLabelStyle

    def setGmlLabelStyle(self, value):
        if self._GmlLabelStyle is not None:
            filtered = [x for x in self.GmlLabelStyle.GmlGeometryStyles if x != self]
            self._GmlLabelStyle._GmlGeometryStyles = filtered

        self._GmlLabelStyle = value
        if self._GmlLabelStyle is not None:
            if self not in self._GmlLabelStyle._GmlGeometryStyles:
                self._GmlLabelStyle._GmlGeometryStyles.append(self)

    GmlLabelStyle = property(getGmlLabelStyle, setGmlLabelStyle)

