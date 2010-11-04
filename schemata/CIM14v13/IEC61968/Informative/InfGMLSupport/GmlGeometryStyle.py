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

class GmlGeometryStyle(IdentifiedObject):
    """The style for one geometry of a feature. Any number of geometry style descriptors can be assigned to one feature style. This is usually required for features with multiple geometry properties.
    """

    def __init__(self, symbol='', geometryType='', geometryProperty='', GmlFeatureStyle=None, GmlLabelStyle=None, *args, **kw_args):
        """Initializes a new 'GmlGeometryStyle' instance.

        @param symbol: Graphical symbol used to render a geometry or a topology. A symbol is a description of graphical attributes of a graphical object without a particular, implicit meaning. It can be a description of a line, circle, polygon or more complex drawing. 
        @param geometryType: It is necessary to specify the geometry type using this attribute as well since the application schema of the geometry property may allow different geometries as its value. 
        @param geometryProperty: The name of the geometry property of a feature to which this GeometryStyle applies. 
        @param GmlFeatureStyle:
        @param GmlLabelStyle:
        """
        #: Graphical symbol used to render a geometry or a topology. A symbol is a description of graphical attributes of a graphical object without a particular, implicit meaning. It can be a description of a line, circle, polygon or more complex drawing.
        self.symbol = symbol

        #: It is necessary to specify the geometry type using this attribute as well since the application schema of the geometry property may allow different geometries as its value.
        self.geometryType = geometryType

        #: The name of the geometry property of a feature to which this GeometryStyle applies.
        self.geometryProperty = geometryProperty

        self._GmlFeatureStyle = None
        self.GmlFeatureStyle = GmlFeatureStyle

        self._GmlLabelStyle = None
        self.GmlLabelStyle = GmlLabelStyle

        super(GmlGeometryStyle, self).__init__(*args, **kw_args)

    def getGmlFeatureStyle(self):
        
        return self._GmlFeatureStyle

    def setGmlFeatureStyle(self, value):
        if self._GmlFeatureStyle is not None:
            filtered = [x for x in self.GmlFeatureStyle.GmlGeometryStyles if x != self]
            self._GmlFeatureStyle._GmlGeometryStyles = filtered

        self._GmlFeatureStyle = value
        if self._GmlFeatureStyle is not None:
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
            self._GmlLabelStyle._GmlGeometryStyles.append(self)

    GmlLabelStyle = property(getGmlLabelStyle, setGmlLabelStyle)

