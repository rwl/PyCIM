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

class MeterReading(IdentifiedObject):
    """Set of values obtained from the meter.Set of values obtained from the meter.
    """

    def __init__(self, ServiceDeliveryPoint=None, valuesInterval=None, EndDeviceEvents=None, Readings=None, CustomerAgreement=None, Meter=None, IntervalBlocks=None, *args, **kw_args):
        """Initialises a new 'MeterReading' instance.

        @param ServiceDeliveryPoint: Service delivery point from which this meter reading (set of values) has been obtained.
        @param valuesInterval: Date and time interval of the data items contained within this meter reading.
        @param EndDeviceEvents: All end device events associated with this set of measured values.
        @param Readings: All reading values contained within this meter reading.
        @param CustomerAgreement: (could be deprecated in the future) Customer agreement for this meter reading.
        @param Meter: Meter providing this reading.
        @param IntervalBlocks: All interval blocks contained in this meter reading.
        """
        self._ServiceDeliveryPoint = None
        self.ServiceDeliveryPoint = ServiceDeliveryPoint

        self.valuesInterval = valuesInterval

        self._EndDeviceEvents = []
        self.EndDeviceEvents = [] if EndDeviceEvents is None else EndDeviceEvents

        self._Readings = []
        self.Readings = [] if Readings is None else Readings

        self._CustomerAgreement = None
        self.CustomerAgreement = CustomerAgreement

        self._Meter = None
        self.Meter = Meter

        self._IntervalBlocks = []
        self.IntervalBlocks = [] if IntervalBlocks is None else IntervalBlocks

        super(MeterReading, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["ServiceDeliveryPoint", "valuesInterval", "EndDeviceEvents", "Readings", "CustomerAgreement", "Meter", "IntervalBlocks"]
    _many_refs = ["EndDeviceEvents", "Readings", "IntervalBlocks"]

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
            if self not in self._ServiceDeliveryPoint._MeterReadings:
                self._ServiceDeliveryPoint._MeterReadings.append(self)

    ServiceDeliveryPoint = property(getServiceDeliveryPoint, setServiceDeliveryPoint)

    # Date and time interval of the data items contained within this meter reading.
    valuesInterval = None

    def getEndDeviceEvents(self):
        """All end device events associated with this set of measured values.
        """
        return self._EndDeviceEvents

    def setEndDeviceEvents(self, value):
        for x in self._EndDeviceEvents:
            x.MeterReading = None
        for y in value:
            y._MeterReading = self
        self._EndDeviceEvents = value

    EndDeviceEvents = property(getEndDeviceEvents, setEndDeviceEvents)

    def addEndDeviceEvents(self, *EndDeviceEvents):
        for obj in EndDeviceEvents:
            obj.MeterReading = self

    def removeEndDeviceEvents(self, *EndDeviceEvents):
        for obj in EndDeviceEvents:
            obj.MeterReading = None

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
            if self not in self._CustomerAgreement._MeterReadings:
                self._CustomerAgreement._MeterReadings.append(self)

    CustomerAgreement = property(getCustomerAgreement, setCustomerAgreement)

    def getMeter(self):
        """Meter providing this reading.
        """
        return self._Meter

    def setMeter(self, value):
        if self._Meter is not None:
            filtered = [x for x in self.Meter.MeterReadings if x != self]
            self._Meter._MeterReadings = filtered

        self._Meter = value
        if self._Meter is not None:
            if self not in self._Meter._MeterReadings:
                self._Meter._MeterReadings.append(self)

    Meter = property(getMeter, setMeter)

    def getIntervalBlocks(self):
        """All interval blocks contained in this meter reading.
        """
        return self._IntervalBlocks

    def setIntervalBlocks(self, value):
        for x in self._IntervalBlocks:
            x.MeterReading = None
        for y in value:
            y._MeterReading = self
        self._IntervalBlocks = value

    IntervalBlocks = property(getIntervalBlocks, setIntervalBlocks)

    def addIntervalBlocks(self, *IntervalBlocks):
        for obj in IntervalBlocks:
            obj.MeterReading = self

    def removeIntervalBlocks(self, *IntervalBlocks):
        for obj in IntervalBlocks:
            obj.MeterReading = None

