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

class AncillaryService(IdentifiedObject):
    """All of these services relate  to various aspects of insuring that the production of energy matches consumption of energy at any given time.  They are very critical to the security and reliability of the interconnected network. Some examples of AncillaryServices include Operating/Supplemental Reserve, Energy Imbalance Service, Operating/Spinning Reserve, Reactive Supply and Voltage Control, and Regulation and Frequency Response.
    """

    def __init__(self, TransmissionProviders=None, ControlAreaOperator=None, ReservedBy_ServiceReservation=None, OpenAccessProduct=None, **kw_args):
        """Initializes a new 'AncillaryService' instance.

        @param TransmissionProviders: A TransmissionProvider offers AncillaryServices. One type of AncillaryServices is a shipping and handling fee to manage the services purchased, another is the reactive power support used to control the voltage on the  transmission system.  This is the amount needed to support the path or amount necessary to maintain the proper voltage at a ServicePoint.
        @param ControlAreaOperator: Sale of ancillary services provided by ControlAreaOperators.
        @param ReservedBy_ServiceReservation: A ServiceReservation guarantees a certain AncillaryService.
        @param OpenAccessProduct: AncillaryServices are sold through a contract which offers a particular OpenAccessProduct.
        """
        self._TransmissionProviders = []
        self.TransmissionProviders = [] if TransmissionProviders is None else TransmissionProviders

        self._ControlAreaOperator = None
        self.ControlAreaOperator = ControlAreaOperator

        self._ReservedBy_ServiceReservation = None
        self.ReservedBy_ServiceReservation = ReservedBy_ServiceReservation

        self._OpenAccessProduct = None
        self.OpenAccessProduct = OpenAccessProduct

        super(AncillaryService, self).__init__(**kw_args)

    def getTransmissionProviders(self):
        """A TransmissionProvider offers AncillaryServices. One type of AncillaryServices is a shipping and handling fee to manage the services purchased, another is the reactive power support used to control the voltage on the  transmission system.  This is the amount needed to support the path or amount necessary to maintain the proper voltage at a ServicePoint.
        """
        return self._TransmissionProviders

    def setTransmissionProviders(self, value):
        for p in self._TransmissionProviders:
            filtered = [q for q in p.AncillaryServices if q != self]
            self._TransmissionProviders._AncillaryServices = filtered
        for r in value:
            if self not in r._AncillaryServices:
                r._AncillaryServices.append(self)
        self._TransmissionProviders = value

    TransmissionProviders = property(getTransmissionProviders, setTransmissionProviders)

    def addTransmissionProviders(self, *TransmissionProviders):
        for obj in TransmissionProviders:
            if self not in obj._AncillaryServices:
                obj._AncillaryServices.append(self)
            self._TransmissionProviders.append(obj)

    def removeTransmissionProviders(self, *TransmissionProviders):
        for obj in TransmissionProviders:
            if self in obj._AncillaryServices:
                obj._AncillaryServices.remove(self)
            self._TransmissionProviders.remove(obj)

    def getControlAreaOperator(self):
        """Sale of ancillary services provided by ControlAreaOperators.
        """
        return self._ControlAreaOperator

    def setControlAreaOperator(self, value):
        if self._ControlAreaOperator is not None:
            filtered = [x for x in self.ControlAreaOperator.AncillaryService if x != self]
            self._ControlAreaOperator._AncillaryService = filtered

        self._ControlAreaOperator = value
        if self._ControlAreaOperator is not None:
            self._ControlAreaOperator._AncillaryService.append(self)

    ControlAreaOperator = property(getControlAreaOperator, setControlAreaOperator)

    def getReservedBy_ServiceReservation(self):
        """A ServiceReservation guarantees a certain AncillaryService.
        """
        return self._ReservedBy_ServiceReservation

    def setReservedBy_ServiceReservation(self, value):
        if self._ReservedBy_ServiceReservation is not None:
            filtered = [x for x in self.ReservedBy_ServiceReservation.Reserves_AncillaryServices if x != self]
            self._ReservedBy_ServiceReservation._Reserves_AncillaryServices = filtered

        self._ReservedBy_ServiceReservation = value
        if self._ReservedBy_ServiceReservation is not None:
            self._ReservedBy_ServiceReservation._Reserves_AncillaryServices.append(self)

    ReservedBy_ServiceReservation = property(getReservedBy_ServiceReservation, setReservedBy_ServiceReservation)

    def getOpenAccessProduct(self):
        """AncillaryServices are sold through a contract which offers a particular OpenAccessProduct.
        """
        return self._OpenAccessProduct

    def setOpenAccessProduct(self, value):
        if self._OpenAccessProduct is not None:
            filtered = [x for x in self.OpenAccessProduct.AncillaryServices if x != self]
            self._OpenAccessProduct._AncillaryServices = filtered

        self._OpenAccessProduct = value
        if self._OpenAccessProduct is not None:
            self._OpenAccessProduct._AncillaryServices.append(self)

    OpenAccessProduct = property(getOpenAccessProduct, setOpenAccessProduct)

