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

from CIM15.IEC61968.Metering.EndDevice import EndDevice

class Meter(EndDevice):
    """Physical asset that performs the metering role of the ServiceDeliveryPoint. Used for measuring consumption and detection of events.Physical asset that performs the metering role of the ServiceDeliveryPoint. Used for measuring consumption and detection of events.
    """

    def __init__(self, kR=0.0, kH=0.0, formNumber='', MeterReplacementWorks=None, MeterReadings=None, MeterServiceWorks=None, VendingTransactions=None, *args, **kw_args):
        """Initialises a new 'Meter' instance.

        @param kR: Display multiplier used to produce a displayed value from a register value. 
        @param kH: Meter kh (watthour) constant. It is the number of watthours that must be applied to the meter to cause one disk revolution for an electromechanical meter or the number of watthours represented by one increment pulse for an electronic meter. 
        @param formNumber: Meter form designation per ANSI C12.10 or other applicable standard. An alphanumeric designation denoting the circuit arrangement for which the meter is applicable and its specific terminal arrangement. 
        @param MeterReplacementWorks: All works on replacement of this old meter.
        @param MeterReadings: All meter readings provided by this meter.
        @param MeterServiceWorks: All non-replacement works on this meter.
        @param VendingTransactions: All vending transactions on this meter.
        """
        #: Display multiplier used to produce a displayed value from a register value.
        self.kR = kR

        #: Meter kh (watthour) constant. It is the number of watthours that must be applied to the meter to cause one disk revolution for an electromechanical meter or the number of watthours represented by one increment pulse for an electronic meter.
        self.kH = kH

        #: Meter form designation per ANSI C12.10 or other applicable standard. An alphanumeric designation denoting the circuit arrangement for which the meter is applicable and its specific terminal arrangement.
        self.formNumber = formNumber

        self._MeterReplacementWorks = []
        self.MeterReplacementWorks = [] if MeterReplacementWorks is None else MeterReplacementWorks

        self._MeterReadings = []
        self.MeterReadings = [] if MeterReadings is None else MeterReadings

        self._MeterServiceWorks = []
        self.MeterServiceWorks = [] if MeterServiceWorks is None else MeterServiceWorks

        self._VendingTransactions = []
        self.VendingTransactions = [] if VendingTransactions is None else VendingTransactions

        super(Meter, self).__init__(*args, **kw_args)

    _attrs = ["kR", "kH", "formNumber"]
    _attr_types = {"kR": float, "kH": float, "formNumber": str}
    _defaults = {"kR": 0.0, "kH": 0.0, "formNumber": ''}
    _enums = {}
    _refs = ["MeterReplacementWorks", "MeterReadings", "MeterServiceWorks", "VendingTransactions"]
    _many_refs = ["MeterReplacementWorks", "MeterReadings", "MeterServiceWorks", "VendingTransactions"]

    def getMeterReplacementWorks(self):
        """All works on replacement of this old meter.
        """
        return self._MeterReplacementWorks

    def setMeterReplacementWorks(self, value):
        for x in self._MeterReplacementWorks:
            x.OldMeter = None
        for y in value:
            y._OldMeter = self
        self._MeterReplacementWorks = value

    MeterReplacementWorks = property(getMeterReplacementWorks, setMeterReplacementWorks)

    def addMeterReplacementWorks(self, *MeterReplacementWorks):
        for obj in MeterReplacementWorks:
            obj.OldMeter = self

    def removeMeterReplacementWorks(self, *MeterReplacementWorks):
        for obj in MeterReplacementWorks:
            obj.OldMeter = None

    def getMeterReadings(self):
        """All meter readings provided by this meter.
        """
        return self._MeterReadings

    def setMeterReadings(self, value):
        for x in self._MeterReadings:
            x.Meter = None
        for y in value:
            y._Meter = self
        self._MeterReadings = value

    MeterReadings = property(getMeterReadings, setMeterReadings)

    def addMeterReadings(self, *MeterReadings):
        for obj in MeterReadings:
            obj.Meter = self

    def removeMeterReadings(self, *MeterReadings):
        for obj in MeterReadings:
            obj.Meter = None

    def getMeterServiceWorks(self):
        """All non-replacement works on this meter.
        """
        return self._MeterServiceWorks

    def setMeterServiceWorks(self, value):
        for x in self._MeterServiceWorks:
            x.Meter = None
        for y in value:
            y._Meter = self
        self._MeterServiceWorks = value

    MeterServiceWorks = property(getMeterServiceWorks, setMeterServiceWorks)

    def addMeterServiceWorks(self, *MeterServiceWorks):
        for obj in MeterServiceWorks:
            obj.Meter = self

    def removeMeterServiceWorks(self, *MeterServiceWorks):
        for obj in MeterServiceWorks:
            obj.Meter = None

    def getVendingTransactions(self):
        """All vending transactions on this meter.
        """
        return self._VendingTransactions

    def setVendingTransactions(self, value):
        for x in self._VendingTransactions:
            x.Meter = None
        for y in value:
            y._Meter = self
        self._VendingTransactions = value

    VendingTransactions = property(getVendingTransactions, setVendingTransactions)

    def addVendingTransactions(self, *VendingTransactions):
        for obj in VendingTransactions:
            obj.Meter = self

    def removeVendingTransactions(self, *VendingTransactions):
        for obj in VendingTransactions:
            obj.Meter = None

