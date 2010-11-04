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

class ServicePoint(IdentifiedObject):
    """Each ServicePoint is contained within (or on the boundary of) an ElectronicIinterchangeArea. ServicePoints are defined termination points of a transmission path (down to distribution level or to a customer - generation or consumption or both).
    """

    def __init__(self, CustomerConsumer=None, Declare_TiePoint=None, EnergyProducts=None, TransmissionProvider=None, HasAPOD_=None, HasAPOR_=None, MemberOf=None, GenerationProvider=None, **kw_args):
        """Initializes a new 'ServicePoint' instance.

        @param CustomerConsumer: A CustomerConsumer may have one or more ServicePoints.
        @param Declare_TiePoint: A tiepoint may be declared as a service point.
        @param EnergyProducts: An EnergyProduct injects energy into a service point.
        @param TransmissionProvider: A TransmissionProvider registers one or more ServicePoints.
        @param HasAPOD_: A transmission path has a 'point-of-delivery' service point
        @param HasAPOR_: A transmission path has a 'point-of-receipt' service point
        @param MemberOf: A transmission path's service point is part of an interchange area
        @param GenerationProvider: A GenerationProvider has one or more ServicePoints where energy is injected into the network.
        """
        self._CustomerConsumer = None
        self.CustomerConsumer = CustomerConsumer

        self._Declare_TiePoint = None
        self.Declare_TiePoint = Declare_TiePoint

        self._EnergyProducts = []
        self.EnergyProducts = [] if EnergyProducts is None else EnergyProducts

        self._TransmissionProvider = None
        self.TransmissionProvider = TransmissionProvider

        self._HasAPOD_ = []
        self.HasAPOD_ = [] if HasAPOD_ is None else HasAPOD_

        self._HasAPOR_ = []
        self.HasAPOR_ = [] if HasAPOR_ is None else HasAPOR_

        self._MemberOf = None
        self.MemberOf = MemberOf

        self._GenerationProvider = None
        self.GenerationProvider = GenerationProvider

        super(ServicePoint, self).__init__(**kw_args)

    def getCustomerConsumer(self):
        """A CustomerConsumer may have one or more ServicePoints.
        """
        return self._CustomerConsumer

    def setCustomerConsumer(self, value):
        if self._CustomerConsumer is not None:
            filtered = [x for x in self.CustomerConsumer.ServicePoint if x != self]
            self._CustomerConsumer._ServicePoint = filtered

        self._CustomerConsumer = value
        if self._CustomerConsumer is not None:
            self._CustomerConsumer._ServicePoint.append(self)

    CustomerConsumer = property(getCustomerConsumer, setCustomerConsumer)

    def getDeclare_TiePoint(self):
        """A tiepoint may be declared as a service point.
        """
        return self._Declare_TiePoint

    def setDeclare_TiePoint(self, value):
        if self._Declare_TiePoint is not None:
            self._Declare_TiePoint._Declared_ServicePoint = None

        self._Declare_TiePoint = value
        if self._Declare_TiePoint is not None:
            self._Declare_TiePoint._Declared_ServicePoint = self

    Declare_TiePoint = property(getDeclare_TiePoint, setDeclare_TiePoint)

    def getEnergyProducts(self):
        """An EnergyProduct injects energy into a service point.
        """
        return self._EnergyProducts

    def setEnergyProducts(self, value):
        for p in self._EnergyProducts:
            filtered = [q for q in p.ServicePoint if q != self]
            self._EnergyProducts._ServicePoint = filtered
        for r in value:
            if self not in r._ServicePoint:
                r._ServicePoint.append(self)
        self._EnergyProducts = value

    EnergyProducts = property(getEnergyProducts, setEnergyProducts)

    def addEnergyProducts(self, *EnergyProducts):
        for obj in EnergyProducts:
            if self not in obj._ServicePoint:
                obj._ServicePoint.append(self)
            self._EnergyProducts.append(obj)

    def removeEnergyProducts(self, *EnergyProducts):
        for obj in EnergyProducts:
            if self in obj._ServicePoint:
                obj._ServicePoint.remove(self)
            self._EnergyProducts.remove(obj)

    def getTransmissionProvider(self):
        """A TransmissionProvider registers one or more ServicePoints.
        """
        return self._TransmissionProvider

    def setTransmissionProvider(self, value):
        if self._TransmissionProvider is not None:
            filtered = [x for x in self.TransmissionProvider.ServicePoint if x != self]
            self._TransmissionProvider._ServicePoint = filtered

        self._TransmissionProvider = value
        if self._TransmissionProvider is not None:
            self._TransmissionProvider._ServicePoint.append(self)

    TransmissionProvider = property(getTransmissionProvider, setTransmissionProvider)

    def getHasAPOD_(self):
        """A transmission path has a 'point-of-delivery' service point
        """
        return self._HasAPOD_

    def setHasAPOD_(self, value):
        for x in self._HasAPOD_:
            x._DeliveryPointFor = None
        for y in value:
            y._DeliveryPointFor = self
        self._HasAPOD_ = value

    HasAPOD_ = property(getHasAPOD_, setHasAPOD_)

    def addHasAPOD_(self, *HasAPOD_):
        for obj in HasAPOD_:
            obj._DeliveryPointFor = self
            self._HasAPOD_.append(obj)

    def removeHasAPOD_(self, *HasAPOD_):
        for obj in HasAPOD_:
            obj._DeliveryPointFor = None
            self._HasAPOD_.remove(obj)

    def getHasAPOR_(self):
        """A transmission path has a 'point-of-receipt' service point
        """
        return self._HasAPOR_

    def setHasAPOR_(self, value):
        for x in self._HasAPOR_:
            x._PointOfReceiptFor = None
        for y in value:
            y._PointOfReceiptFor = self
        self._HasAPOR_ = value

    HasAPOR_ = property(getHasAPOR_, setHasAPOR_)

    def addHasAPOR_(self, *HasAPOR_):
        for obj in HasAPOR_:
            obj._PointOfReceiptFor = self
            self._HasAPOR_.append(obj)

    def removeHasAPOR_(self, *HasAPOR_):
        for obj in HasAPOR_:
            obj._PointOfReceiptFor = None
            self._HasAPOR_.remove(obj)

    def getMemberOf(self):
        """A transmission path's service point is part of an interchange area
        """
        return self._MemberOf

    def setMemberOf(self, value):
        if self._MemberOf is not None:
            filtered = [x for x in self.MemberOf.PartOf if x != self]
            self._MemberOf._PartOf = filtered

        self._MemberOf = value
        if self._MemberOf is not None:
            self._MemberOf._PartOf.append(self)

    MemberOf = property(getMemberOf, setMemberOf)

    def getGenerationProvider(self):
        """A GenerationProvider has one or more ServicePoints where energy is injected into the network.
        """
        return self._GenerationProvider

    def setGenerationProvider(self, value):
        if self._GenerationProvider is not None:
            filtered = [x for x in self.GenerationProvider.ServicePoint if x != self]
            self._GenerationProvider._ServicePoint = filtered

        self._GenerationProvider = value
        if self._GenerationProvider is not None:
            self._GenerationProvider._ServicePoint.append(self)

    GenerationProvider = property(getGenerationProvider, setGenerationProvider)

