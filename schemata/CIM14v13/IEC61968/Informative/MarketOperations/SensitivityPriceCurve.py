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

from CIM14v13.IEC61970.Core.Curve import Curve

class SensitivityPriceCurve(Curve):
    """Optionally, this curve expresses elasticity of the associated requirement.  For example, used to reduce requirements when clearing price exceeds reasonable values when the supply quantity becomes scarce.  For example, a single point value of $1000/MW for a spinning reserve will cause a reduction in the required spinning reserve.  X axis is constrained quantity (e.g., MW) Y1 axis is money per constrained quantity
    """

    def __init__(self, ReserveReq=None, **kw_args):
        """Initializes a new 'SensitivityPriceCurve' instance.

        @param ReserveReq:
        """
        self._ReserveReq = None
        self.ReserveReq = ReserveReq

        super(SensitivityPriceCurve, self).__init__(**kw_args)

    def getReserveReq(self):
        
        return self._ReserveReq

    def setReserveReq(self, value):
        if self._ReserveReq is not None:
            self._ReserveReq._SensitivityPriceCurve = None

        self._ReserveReq = value
        if self._ReserveReq is not None:
            self._ReserveReq._SensitivityPriceCurve = self

    ReserveReq = property(getReserveReq, setReserveReq)

