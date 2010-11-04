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

class SubscribePowerCurve(Curve):
    """Price curve for specifying the cost of energy (X) at points in time (y1) according to a prcing structure, which is based on a tariff.
    """

    def __init__(self, PricingStructure=None, **kw_args):
        """Initializes a new 'SubscribePowerCurve' instance.

        @param PricingStructure:
        """
        self._PricingStructure = None
        self.PricingStructure = PricingStructure

        super(SubscribePowerCurve, self).__init__(**kw_args)

    def getPricingStructure(self):
        
        return self._PricingStructure

    def setPricingStructure(self, value):
        if self._PricingStructure is not None:
            self._PricingStructure._SubscribePowerCurve = None

        self._PricingStructure = value
        if self._PricingStructure is not None:
            self._PricingStructure._SubscribePowerCurve = self

    PricingStructure = property(getPricingStructure, setPricingStructure)

