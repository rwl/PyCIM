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

from CIM14v13.IEC61968.Informative.InfERPSupport.ErpOrganisation import ErpOrganisation

class TransmissionProvider(ErpOrganisation):
    """Provider of the transmission capacity (interconnecting wires between Generation and Consumption) required to fulfill and Energy Transaction's energy exchange. Posts information for transmission paths and AvailableTransmissionCapacities on a reservation node. Buys and sells its products and services on the same reservation node.
    """

    def __init__(self, TransmissionProducts=None, Flowgate=None, ServicePoint=None, AncillaryServices=None, For=None, OfferedBy=None, SoldBy=None, **kw_args):
        """Initializes a new 'TransmissionProvider' instance.

        @param TransmissionProducts: A TransmissionProvider offers a TransmissionProduct.
        @param Flowgate: A flowgate can be reciprocal flowgate for 0 to n transmission providers. A transmission provider may be a reciprocal entity for 0 to n flowgates.
        @param ServicePoint: A TransmissionProvider registers one or more ServicePoints.
        @param AncillaryServices: A TransmissionProvider offers AncillaryServices. One type of AncillaryServices is a shipping and handling fee to manage the services purchased, another is the reactive power support used to control the voltage on the  transmission system.  This is the amount needed to support the path or amount necessary to maintain the proper voltage at a ServicePoint.
        @param For: Part of the LossProfile for an EnergyTransaction may be a loss for a TransmissionProvider.
        @param OfferedBy: The combination of a TransmissionProduct on a TransmissionPath is a TransmissionService, for which the TransmissionProvider must post one or two ATC's (AvailableTransmissionCapacity - Amount of possible flow by  direction).
        @param SoldBy: A TransmissionProvider sells the right to transmit energy across the wires in a ServiceReservation.
        """
        self._TransmissionProducts = []
        self.TransmissionProducts = [] if TransmissionProducts is None else TransmissionProducts

        self._Flowgate = []
        self.Flowgate = [] if Flowgate is None else Flowgate

        self._ServicePoint = []
        self.ServicePoint = [] if ServicePoint is None else ServicePoint

        self._AncillaryServices = []
        self.AncillaryServices = [] if AncillaryServices is None else AncillaryServices

        self._For = []
        self.For = [] if For is None else For

        self._OfferedBy = []
        self.OfferedBy = [] if OfferedBy is None else OfferedBy

        self._SoldBy = []
        self.SoldBy = [] if SoldBy is None else SoldBy

        super(TransmissionProvider, self).__init__(**kw_args)

    def getTransmissionProducts(self):
        """A TransmissionProvider offers a TransmissionProduct.
        """
        return self._TransmissionProducts

    def setTransmissionProducts(self, value):
        for x in self._TransmissionProducts:
            x._TransmissionProvider = None
        for y in value:
            y._TransmissionProvider = self
        self._TransmissionProducts = value

    TransmissionProducts = property(getTransmissionProducts, setTransmissionProducts)

    def addTransmissionProducts(self, *TransmissionProducts):
        for obj in TransmissionProducts:
            obj._TransmissionProvider = self
            self._TransmissionProducts.append(obj)

    def removeTransmissionProducts(self, *TransmissionProducts):
        for obj in TransmissionProducts:
            obj._TransmissionProvider = None
            self._TransmissionProducts.remove(obj)

    def getFlowgate(self):
        """A flowgate can be reciprocal flowgate for 0 to n transmission providers. A transmission provider may be a reciprocal entity for 0 to n flowgates.
        """
        return self._Flowgate

    def setFlowgate(self, value):
        for p in self._Flowgate:
            filtered = [q for q in p.TransmissionProvider if q != self]
            self._Flowgate._TransmissionProvider = filtered
        for r in value:
            if self not in r._TransmissionProvider:
                r._TransmissionProvider.append(self)
        self._Flowgate = value

    Flowgate = property(getFlowgate, setFlowgate)

    def addFlowgate(self, *Flowgate):
        for obj in Flowgate:
            if self not in obj._TransmissionProvider:
                obj._TransmissionProvider.append(self)
            self._Flowgate.append(obj)

    def removeFlowgate(self, *Flowgate):
        for obj in Flowgate:
            if self in obj._TransmissionProvider:
                obj._TransmissionProvider.remove(self)
            self._Flowgate.remove(obj)

    def getServicePoint(self):
        """A TransmissionProvider registers one or more ServicePoints.
        """
        return self._ServicePoint

    def setServicePoint(self, value):
        for x in self._ServicePoint:
            x._TransmissionProvider = None
        for y in value:
            y._TransmissionProvider = self
        self._ServicePoint = value

    ServicePoint = property(getServicePoint, setServicePoint)

    def addServicePoint(self, *ServicePoint):
        for obj in ServicePoint:
            obj._TransmissionProvider = self
            self._ServicePoint.append(obj)

    def removeServicePoint(self, *ServicePoint):
        for obj in ServicePoint:
            obj._TransmissionProvider = None
            self._ServicePoint.remove(obj)

    def getAncillaryServices(self):
        """A TransmissionProvider offers AncillaryServices. One type of AncillaryServices is a shipping and handling fee to manage the services purchased, another is the reactive power support used to control the voltage on the  transmission system.  This is the amount needed to support the path or amount necessary to maintain the proper voltage at a ServicePoint.
        """
        return self._AncillaryServices

    def setAncillaryServices(self, value):
        for p in self._AncillaryServices:
            filtered = [q for q in p.TransmissionProviders if q != self]
            self._AncillaryServices._TransmissionProviders = filtered
        for r in value:
            if self not in r._TransmissionProviders:
                r._TransmissionProviders.append(self)
        self._AncillaryServices = value

    AncillaryServices = property(getAncillaryServices, setAncillaryServices)

    def addAncillaryServices(self, *AncillaryServices):
        for obj in AncillaryServices:
            if self not in obj._TransmissionProviders:
                obj._TransmissionProviders.append(self)
            self._AncillaryServices.append(obj)

    def removeAncillaryServices(self, *AncillaryServices):
        for obj in AncillaryServices:
            if self in obj._TransmissionProviders:
                obj._TransmissionProviders.remove(self)
            self._AncillaryServices.remove(obj)

    def getFor(self):
        """Part of the LossProfile for an EnergyTransaction may be a loss for a TransmissionProvider.
        """
        return self._For

    def setFor(self, value):
        for x in self._For:
            x._HasLoss_ = None
        for y in value:
            y._HasLoss_ = self
        self._For = value

    For = property(getFor, setFor)

    def addFor(self, *For):
        for obj in For:
            obj._HasLoss_ = self
            self._For.append(obj)

    def removeFor(self, *For):
        for obj in For:
            obj._HasLoss_ = None
            self._For.remove(obj)

    def getOfferedBy(self):
        """The combination of a TransmissionProduct on a TransmissionPath is a TransmissionService, for which the TransmissionProvider must post one or two ATC's (AvailableTransmissionCapacity - Amount of possible flow by  direction).
        """
        return self._OfferedBy

    def setOfferedBy(self, value):
        for x in self._OfferedBy:
            x._Offers = None
        for y in value:
            y._Offers = self
        self._OfferedBy = value

    OfferedBy = property(getOfferedBy, setOfferedBy)

    def addOfferedBy(self, *OfferedBy):
        for obj in OfferedBy:
            obj._Offers = self
            self._OfferedBy.append(obj)

    def removeOfferedBy(self, *OfferedBy):
        for obj in OfferedBy:
            obj._Offers = None
            self._OfferedBy.remove(obj)

    def getSoldBy(self):
        """A TransmissionProvider sells the right to transmit energy across the wires in a ServiceReservation.
        """
        return self._SoldBy

    def setSoldBy(self, value):
        for x in self._SoldBy:
            x._Sells = None
        for y in value:
            y._Sells = self
        self._SoldBy = value

    SoldBy = property(getSoldBy, setSoldBy)

    def addSoldBy(self, *SoldBy):
        for obj in SoldBy:
            obj._Sells = self
            self._SoldBy.append(obj)

    def removeSoldBy(self, *SoldBy):
        for obj in SoldBy:
            obj._Sells = None
            self._SoldBy.remove(obj)

