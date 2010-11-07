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

from CIM14.Element import Element

class CurveData(Element):
    """Multi-purpose data points for defining a curve.
    """

    def __init__(self, y3value=0.0, xvalue=0.0, y2value=0.0, y1value=0.0, Curve=None, **kw_args):
        """Initializes a new 'CurveData' instance.

        @param y3value: The data value of the third Y-axis variable (if present), depending on the Y-axis units 
        @param xvalue: The data value of the X-axis variable,  depending on the X-axis units 
        @param y2value: The data value of the second Y-axis variable (if present), depending on the Y-axis units 
        @param y1value: The data value of the  first Y-axis variable, depending on the Y-axis units 
        @param Curve: The Curve defined by this CurveData.
        """
        #: The data value of the third Y-axis variable (if present), depending on the Y-axis units
        self.y3value = y3value

        #: The data value of the X-axis variable,  depending on the X-axis units
        self.xvalue = xvalue

        #: The data value of the second Y-axis variable (if present), depending on the Y-axis units
        self.y2value = y2value

        #: The data value of the  first Y-axis variable, depending on the Y-axis units
        self.y1value = y1value

        self._Curve = None
        self.Curve = Curve

        super(CurveData, self).__init__(**kw_args)

    def getCurve(self):
        """The Curve defined by this CurveData.
        """
        return self._Curve

    def setCurve(self, value):
        if self._Curve is not None:
            filtered = [x for x in self.Curve.CurveDatas if x != self]
            self._Curve._CurveDatas = filtered

        self._Curve = value
        if self._Curve is not None:
            self._Curve._CurveDatas.append(self)

    Curve = property(getCurve, setCurve)

