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

class TransmissionProduct(IdentifiedObject):

    def __init__(self, transmissionProductType=None, Offers=None, TransmissionProvider=None, LocationFor=None, **kw_args):
        """Initializes a new 'TransmissionProduct' instance.

        @param transmissionProductType: Type of the transmission product. This could be a transmission service class (firm, total transmission capability, or non-firm), transmission service period (on-peak, full-period, off-peak), transmission service increments (yearly extended, hourly fixed, monthly sliding, etc.), transmission service type (network, available transmission capability, or point-to-point, or a transmission service window (fixed hourly, sliding weekly, extended monthly, etc.). 
        @param Offers: A transmission product is offered as a transmission service along a transmission path.
        @param TransmissionProvider: A TransmissionProvider offers a TransmissionProduct.
        @param LocationFor: A transmission product is located on a transmission path.
        """
        #: Type of the transmission product. This could be a transmission service class (firm, total transmission capability, or non-firm), transmission service period (on-peak, full-period, off-peak), transmission service increments (yearly extended, hourly fixed, monthly sliding, etc.), transmission service type (network, available transmission capability, or point-to-point, or a transmission service window (fixed hourly, sliding weekly, extended monthly, etc.).
        self.transmissionProductType = transmissionProductType

        self._Offers = []
        self.Offers = [] if Offers is None else Offers

        self._TransmissionProvider = None
        self.TransmissionProvider = TransmissionProvider

        self._LocationFor = []
        self.LocationFor = [] if LocationFor is None else LocationFor

        super(TransmissionProduct, self).__init__(**kw_args)

    def getOffers(self):
        """A transmission product is offered as a transmission service along a transmission path.
        """
        return self._Offers

    def setOffers(self, value):
        for p in self._Offers:
            filtered = [q for q in p.OfferedAs if q != self]
            self._Offers._OfferedAs = filtered
        for r in value:
            if self not in r._OfferedAs:
                r._OfferedAs.append(self)
        self._Offers = value

    Offers = property(getOffers, setOffers)

    def addOffers(self, *Offers):
        for obj in Offers:
            if self not in obj._OfferedAs:
                obj._OfferedAs.append(self)
            self._Offers.append(obj)

    def removeOffers(self, *Offers):
        for obj in Offers:
            if self in obj._OfferedAs:
                obj._OfferedAs.remove(self)
            self._Offers.remove(obj)

    def getTransmissionProvider(self):
        """A TransmissionProvider offers a TransmissionProduct.
        """
        return self._TransmissionProvider

    def setTransmissionProvider(self, value):
        if self._TransmissionProvider is not None:
            filtered = [x for x in self.TransmissionProvider.TransmissionProducts if x != self]
            self._TransmissionProvider._TransmissionProducts = filtered

        self._TransmissionProvider = value
        if self._TransmissionProvider is not None:
            self._TransmissionProvider._TransmissionProducts.append(self)

    TransmissionProvider = property(getTransmissionProvider, setTransmissionProvider)

    def getLocationFor(self):
        """A transmission product is located on a transmission path.
        """
        return self._LocationFor

    def setLocationFor(self, value):
        for p in self._LocationFor:
            filtered = [q for q in p.LocatedOn if q != self]
            self._LocationFor._LocatedOn = filtered
        for r in value:
            if self not in r._LocatedOn:
                r._LocatedOn.append(self)
        self._LocationFor = value

    LocationFor = property(getLocationFor, setLocationFor)

    def addLocationFor(self, *LocationFor):
        for obj in LocationFor:
            if self not in obj._LocatedOn:
                obj._LocatedOn.append(self)
            self._LocationFor.append(obj)

    def removeLocationFor(self, *LocationFor):
        for obj in LocationFor:
            if self in obj._LocatedOn:
                obj._LocatedOn.remove(self)
            self._LocationFor.remove(obj)

