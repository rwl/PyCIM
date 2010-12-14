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

    def __init__(self, kH=0.0, kR=0.0, formNumber='', MeterReplacementWorks=None, MeterServiceWorks=None, MeterReadings=None, VendingTransactions=None, *args, **kw_args):
        """Initialises a new 'MeterAsset' instance.

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

        super(MeterAsset, self).__init__(*args, **kw_args)

    _attrs = ["kH", "kR", "formNumber"]
    _attr_types = {"kH": float, "kR": float, "formNumber": str}
    _defaults = {"kH": 0.0, "kR": 0.0, "formNumber": ''}
    _enums = {}
    _refs = ["MeterReplacementWorks", "MeterServiceWorks", "MeterReadings", "VendingTransactions"]
    _many_refs = ["MeterReplacementWorks", "MeterServiceWorks", "MeterReadings", "VendingTransactions"]

    def getMeterReplacementWorks(self):
        """All works on replacement of this old meter asset.
        """
        return self._MeterReplacementWorks

    def setMeterReplacementWorks(self, value):
        for x in self._MeterReplacementWorks:
            x.OldMeterAsset = None
        for y in value:
            y._OldMeterAsset = self
        self._MeterReplacementWorks = value

    MeterReplacementWorks = property(getMeterReplacementWorks, setMeterReplacementWorks)

    def addMeterReplacementWorks(self, *MeterReplacementWorks):
        for obj in MeterReplacementWorks:
            obj.OldMeterAsset = self

    def removeMeterReplacementWorks(self, *MeterReplacementWorks):
        for obj in MeterReplacementWorks:
            obj.OldMeterAsset = None

    def getMeterServiceWorks(self):
        """All non-replacement works on this meter asset.
        """
        return self._MeterServiceWorks

    def setMeterServiceWorks(self, value):
        for x in self._MeterServiceWorks:
            x.MeterAsset = None
        for y in value:
            y._MeterAsset = self
        self._MeterServiceWorks = value

    MeterServiceWorks = property(getMeterServiceWorks, setMeterServiceWorks)

    def addMeterServiceWorks(self, *MeterServiceWorks):
        for obj in MeterServiceWorks:
            obj.MeterAsset = self

    def removeMeterServiceWorks(self, *MeterServiceWorks):
        for obj in MeterServiceWorks:
            obj.MeterAsset = None

    def getMeterReadings(self):
        """All meter readings provided by this meter asset.
        """
        return self._MeterReadings

    def setMeterReadings(self, value):
        for x in self._MeterReadings:
            x.MeterAsset = None
        for y in value:
            y._MeterAsset = self
        self._MeterReadings = value

    MeterReadings = property(getMeterReadings, setMeterReadings)

    def addMeterReadings(self, *MeterReadings):
        for obj in MeterReadings:
            obj.MeterAsset = self

    def removeMeterReadings(self, *MeterReadings):
        for obj in MeterReadings:
            obj.MeterAsset = None

    def getVendingTransactions(self):
        """All vending transactions on this meter asset.
        """
        return self._VendingTransactions

    def setVendingTransactions(self, value):
        for x in self._VendingTransactions:
            x.MeterAsset = None
        for y in value:
            y._MeterAsset = self
        self._VendingTransactions = value

    VendingTransactions = property(getVendingTransactions, setVendingTransactions)

    def addVendingTransactions(self, *VendingTransactions):
        for obj in VendingTransactions:
            obj.MeterAsset = self

    def removeVendingTransactions(self, *VendingTransactions):
        for obj in VendingTransactions:
            obj.MeterAsset = None

