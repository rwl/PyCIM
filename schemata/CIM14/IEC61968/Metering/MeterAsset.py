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

from CIM14.IEC61968.Metering.EndDeviceAsset import EndDeviceAsset

class MeterAsset(EndDeviceAsset):
    """Physical asset that performs the metering role of the ServiceDeliveryPoint. Used for measuring consumption and detection of events.
    """

    def __init__(self, kH=0.0, kR=0.0, formNumber='', MeterReplacementWorks=None, MeterServiceWorks=None, MeterReadings=None, VendingTransactions=None, **kw_args):
        """Initializes a new 'MeterAsset' instance.

        @param kH: Meter kh (watthour) constant. It is the number of watthours that must be applied to the meter to cause one disk revolution for an electromechanical meter or the number of watthours represented by one increment pulse for an electronic meter. 
        @param kR: Display multiplier used to produce a displayed value from a register value. 
        @param formNumber: Meter form designation per ANSI C12.10 or other applicable standard. An alphanumeric designation denoting the circuit arrangement for which the meter is applicable and its specific terminal arrangement. 
        @param MeterReplacementWorks: All works on replacement of this old meter asset.
        @param MeterServiceWorks: All non-replacement works on this meter asset.
        @param MeterReadings: All meter readings provided by this meter asset.
        @param VendingTransactions: All vending transactions on this meter asset.
        """
        #: Meter kh (watthour) constant. It is the number of watthours that must be applied to the meter to cause one disk revolution for an electromechanical meter or the number of watthours represented by one increment pulse for an electronic meter.
        self.kH = kH

        #: Display multiplier used to produce a displayed value from a register value.
        self.kR = kR

        #: Meter form designation per ANSI C12.10 or other applicable standard. An alphanumeric designation denoting the circuit arrangement for which the meter is applicable and its specific terminal arrangement.
        self.formNumber = formNumber

        self._MeterReplacementWorks = []
        self.MeterReplacementWorks = [] if MeterReplacementWorks is None else MeterReplacementWorks

        self._MeterServiceWorks = []
        self.MeterServiceWorks = [] if MeterServiceWorks is None else MeterServiceWorks

        self._MeterReadings = []
        self.MeterReadings = [] if MeterReadings is None else MeterReadings

        self._VendingTransactions = []
        self.VendingTransactions = [] if VendingTransactions is None else VendingTransactions

        super(MeterAsset, self).__init__(**kw_args)

    def getMeterReplacementWorks(self):
        """All works on replacement of this old meter asset.
        """
        return self._MeterReplacementWorks

    def setMeterReplacementWorks(self, value):
        for x in self._MeterReplacementWorks:
            x._OldMeterAsset = None
        for y in value:
            y._OldMeterAsset = self
        self._MeterReplacementWorks = value

    MeterReplacementWorks = property(getMeterReplacementWorks, setMeterReplacementWorks)

    def addMeterReplacementWorks(self, *MeterReplacementWorks):
        for obj in MeterReplacementWorks:
            obj._OldMeterAsset = self
            self._MeterReplacementWorks.append(obj)

    def removeMeterReplacementWorks(self, *MeterReplacementWorks):
        for obj in MeterReplacementWorks:
            obj._OldMeterAsset = None
            self._MeterReplacementWorks.remove(obj)

    def getMeterServiceWorks(self):
        """All non-replacement works on this meter asset.
        """
        return self._MeterServiceWorks

    def setMeterServiceWorks(self, value):
        for x in self._MeterServiceWorks:
            x._MeterAsset = None
        for y in value:
            y._MeterAsset = self
        self._MeterServiceWorks = value

    MeterServiceWorks = property(getMeterServiceWorks, setMeterServiceWorks)

    def addMeterServiceWorks(self, *MeterServiceWorks):
        for obj in MeterServiceWorks:
            obj._MeterAsset = self
            self._MeterServiceWorks.append(obj)

    def removeMeterServiceWorks(self, *MeterServiceWorks):
        for obj in MeterServiceWorks:
            obj._MeterAsset = None
            self._MeterServiceWorks.remove(obj)

    def getMeterReadings(self):
        """All meter readings provided by this meter asset.
        """
        return self._MeterReadings

    def setMeterReadings(self, value):
        for x in self._MeterReadings:
            x._MeterAsset = None
        for y in value:
            y._MeterAsset = self
        self._MeterReadings = value

    MeterReadings = property(getMeterReadings, setMeterReadings)

    def addMeterReadings(self, *MeterReadings):
        for obj in MeterReadings:
            obj._MeterAsset = self
            self._MeterReadings.append(obj)

    def removeMeterReadings(self, *MeterReadings):
        for obj in MeterReadings:
            obj._MeterAsset = None
            self._MeterReadings.remove(obj)

    def getVendingTransactions(self):
        """All vending transactions on this meter asset.
        """
        return self._VendingTransactions

    def setVendingTransactions(self, value):
        for x in self._VendingTransactions:
            x._MeterAsset = None
        for y in value:
            y._MeterAsset = self
        self._VendingTransactions = value

    VendingTransactions = property(getVendingTransactions, setVendingTransactions)

    def addVendingTransactions(self, *VendingTransactions):
        for obj in VendingTransactions:
            obj._MeterAsset = self
            self._VendingTransactions.append(obj)

    def removeVendingTransactions(self, *VendingTransactions):
        for obj in VendingTransactions:
            obj._MeterAsset = None
            self._VendingTransactions.remove(obj)

