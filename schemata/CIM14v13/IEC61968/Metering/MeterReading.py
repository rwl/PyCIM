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

class MeterReading(IdentifiedObject):
    """Set of values obtained from the meter.
    """

    def __init__(self, IntervalBlocks=None, CustomerAgreement=None, ServiceDeliveryPoint=None, MeterAsset=None, valuesInterval=None, Readings=None, EndDeviceEvents=None, **kw_args):
        """Initializes a new 'MeterReading' instance.

        @param IntervalBlocks: All interval blocks contained in this meter reading.
        @param CustomerAgreement: (could be deprecated in the future) Customer agreement for this meter reading.
        @param ServiceDeliveryPoint: Service delivery point from which this meter reading (set of values) has been obtained.
        @param MeterAsset: Meter asset providing this meter reading.
        @param valuesInterval: Date and time interval of the data items contained within this meter reading.
        @param Readings: All reading values contained within this meter reading.
        @param EndDeviceEvents: All end device events associated with this set of measured values.
        """
        self._IntervalBlocks = []
        self.IntervalBlocks = [] if IntervalBlocks is None else IntervalBlocks

        self._CustomerAgreement = None
        self.CustomerAgreement = CustomerAgreement

        self._ServiceDeliveryPoint = None
        self.ServiceDeliveryPoint = ServiceDeliveryPoint

        self._MeterAsset = None
        self.MeterAsset = MeterAsset

        self.valuesInterval = valuesInterval

        self._Readings = []
        self.Readings = [] if Readings is None else Readings

        self._EndDeviceEvents = []
        self.EndDeviceEvents = [] if EndDeviceEvents is None else EndDeviceEvents

        super(MeterReading, self).__init__(**kw_args)

    def getIntervalBlocks(self):
        """All interval blocks contained in this meter reading.
        """
        return self._IntervalBlocks

    def setIntervalBlocks(self, value):
        for x in self._IntervalBlocks:
            x._MeterReading = None
        for y in value:
            y._MeterReading = self
        self._IntervalBlocks = value

    IntervalBlocks = property(getIntervalBlocks, setIntervalBlocks)

    def addIntervalBlocks(self, *IntervalBlocks):
        for obj in IntervalBlocks:
            obj._MeterReading = self
            self._IntervalBlocks.append(obj)

    def removeIntervalBlocks(self, *IntervalBlocks):
        for obj in IntervalBlocks:
            obj._MeterReading = None
            self._IntervalBlocks.remove(obj)

    def getCustomerAgreement(self):
        """(could be deprecated in the future) Customer agreement for this meter reading.
        """
        return self._CustomerAgreement

    def setCustomerAgreement(self, value):
        if self._CustomerAgreement is not None:
            filtered = [x for x in self.CustomerAgreement.MeterReadings if x != self]
            self._CustomerAgreement._MeterReadings = filtered

        self._CustomerAgreement = value
        if self._CustomerAgreement is not None:
            self._CustomerAgreement._MeterReadings.append(self)

    CustomerAgreement = property(getCustomerAgreement, setCustomerAgreement)

    def getServiceDeliveryPoint(self):
        """Service delivery point from which this meter reading (set of values) has been obtained.
        """
        return self._ServiceDeliveryPoint

    def setServiceDeliveryPoint(self, value):
        if self._ServiceDeliveryPoint is not None:
            filtered = [x for x in self.ServiceDeliveryPoint.MeterReadings if x != self]
            self._ServiceDeliveryPoint._MeterReadings = filtered

        self._ServiceDeliveryPoint = value
        if self._ServiceDeliveryPoint is not None:
            self._ServiceDeliveryPoint._MeterReadings.append(self)

    ServiceDeliveryPoint = property(getServiceDeliveryPoint, setServiceDeliveryPoint)

    def getMeterAsset(self):
        """Meter asset providing this meter reading.
        """
        return self._MeterAsset

    def setMeterAsset(self, value):
        if self._MeterAsset is not None:
            filtered = [x for x in self.MeterAsset.MeterReadings if x != self]
            self._MeterAsset._MeterReadings = filtered

        self._MeterAsset = value
        if self._MeterAsset is not None:
            self._MeterAsset._MeterReadings.append(self)

    MeterAsset = property(getMeterAsset, setMeterAsset)

    # Date and time interval of the data items contained within this meter reading.
    valuesInterval = None

    def getReadings(self):
        """All reading values contained within this meter reading.
        """
        return self._Readings

    def setReadings(self, value):
        for p in self._Readings:
            filtered = [q for q in p.MeterReadings if q != self]
            self._Readings._MeterReadings = filtered
        for r in value:
            if self not in r._MeterReadings:
                r._MeterReadings.append(self)
        self._Readings = value

    Readings = property(getReadings, setReadings)

    def addReadings(self, *Readings):
        for obj in Readings:
            if self not in obj._MeterReadings:
                obj._MeterReadings.append(self)
            self._Readings.append(obj)

    def removeReadings(self, *Readings):
        for obj in Readings:
            if self in obj._MeterReadings:
                obj._MeterReadings.remove(self)
            self._Readings.remove(obj)

    def getEndDeviceEvents(self):
        """All end device events associated with this set of measured values.
        """
        return self._EndDeviceEvents

    def setEndDeviceEvents(self, value):
        for x in self._EndDeviceEvents:
            x._MeterReading = None
        for y in value:
            y._MeterReading = self
        self._EndDeviceEvents = value

    EndDeviceEvents = property(getEndDeviceEvents, setEndDeviceEvents)

    def addEndDeviceEvents(self, *EndDeviceEvents):
        for obj in EndDeviceEvents:
            obj._MeterReading = self
            self._EndDeviceEvents.append(obj)

    def removeEndDeviceEvents(self, *EndDeviceEvents):
        for obj in EndDeviceEvents:
            obj._MeterReading = None
            self._EndDeviceEvents.remove(obj)

