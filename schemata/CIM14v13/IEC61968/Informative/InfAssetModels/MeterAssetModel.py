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

from CIM14v13.IEC61968.Informative.InfAssetModels.ElectricalAssetModel import ElectricalAssetModel

class MeterAssetModel(ElectricalAssetModel):
    """Documentation for a type of a meter asset of a particular product model made by a manufacturer.
    """

    def __init__(self, kVAhMeter=False, intervalDataMeter=False, maxRegisterCount=0, wireCount=0, kH=0.0, timeOfUseMeter=False, form='', registerRatio=0.0, demandMeter=False, reactiveMeter=False, loadProfileMeter=False, kwhMeter=False, qMeter=False, MeterTypeAsset=None, MeterAssets=None, **kw_args):
        """Initializes a new 'MeterAssetModel' instance.

        @param kVAhMeter: True when the meter is capable of metering apparent energy in kVAh. 
        @param intervalDataMeter: True when the meter or the installed AMR option is capable of capturing interval data for a user selectable measurement (kWh, Volts, or some other billing or engineering quantity). 
        @param maxRegisterCount: Maximum number of registers this meter model can support. The actual number in use is based on the number of Registers associated with a given MeterAsset. 
        @param wireCount: Number of wires. 
        @param kH: Meter kh (watthour) constant. This constant is the number of watthours that must be applied to the meter to cause one disk revolution for an electromechanical meter or the number of watthours represented by one increment pulse for an electronic meter. 
        @param timeOfUseMeter: True when the meter or meter+AMR module are capable of offering TOU data. 
        @param form: Meter form number. 
        @param registerRatio: Meter register ratio. 
        @param demandMeter: True when the meter or installed AMR option is capable of capturing demand data. 
        @param reactiveMeter: True when the meter is capable of metering reactive energy in kVArh. 
        @param loadProfileMeter: True when the meter or the installed AMR option is capable of capturing kWh interval data. 
        @param kwhMeter: True when the meter is capable of metering real energy in kWh. 
        @param qMeter: True when the meter is capable of metering reactive energy in kQh. 
        @param MeterTypeAsset:
        @param MeterAssets:
        """
        #: True when the meter is capable of metering apparent energy in kVAh.
        self.kVAhMeter = kVAhMeter

        #: True when the meter or the installed AMR option is capable of capturing interval data for a user selectable measurement (kWh, Volts, or some other billing or engineering quantity).
        self.intervalDataMeter = intervalDataMeter

        #: Maximum number of registers this meter model can support. The actual number in use is based on the number of Registers associated with a given MeterAsset.
        self.maxRegisterCount = maxRegisterCount

        #: Number of wires.
        self.wireCount = wireCount

        #: Meter kh (watthour) constant. This constant is the number of watthours that must be applied to the meter to cause one disk revolution for an electromechanical meter or the number of watthours represented by one increment pulse for an electronic meter.
        self.kH = kH

        #: True when the meter or meter+AMR module are capable of offering TOU data.
        self.timeOfUseMeter = timeOfUseMeter

        #: Meter form number.
        self.form = form

        #: Meter register ratio.
        self.registerRatio = registerRatio

        #: True when the meter or installed AMR option is capable of capturing demand data.
        self.demandMeter = demandMeter

        #: True when the meter is capable of metering reactive energy in kVArh.
        self.reactiveMeter = reactiveMeter

        #: True when the meter or the installed AMR option is capable of capturing kWh interval data.
        self.loadProfileMeter = loadProfileMeter

        #: True when the meter is capable of metering real energy in kWh.
        self.kwhMeter = kwhMeter

        #: True when the meter is capable of metering reactive energy in kQh.
        self.qMeter = qMeter

        self._MeterTypeAsset = None
        self.MeterTypeAsset = MeterTypeAsset

        self._MeterAssets = []
        self.MeterAssets = [] if MeterAssets is None else MeterAssets

        super(MeterAssetModel, self).__init__(**kw_args)

    def getMeterTypeAsset(self):
        
        return self._MeterTypeAsset

    def setMeterTypeAsset(self, value):
        if self._MeterTypeAsset is not None:
            filtered = [x for x in self.MeterTypeAsset.MeterAssetModels if x != self]
            self._MeterTypeAsset._MeterAssetModels = filtered

        self._MeterTypeAsset = value
        if self._MeterTypeAsset is not None:
            self._MeterTypeAsset._MeterAssetModels.append(self)

    MeterTypeAsset = property(getMeterTypeAsset, setMeterTypeAsset)

    def getMeterAssets(self):
        
        return self._MeterAssets

    def setMeterAssets(self, value):
        for x in self._MeterAssets:
            x._MeterAssetModel = None
        for y in value:
            y._MeterAssetModel = self
        self._MeterAssets = value

    MeterAssets = property(getMeterAssets, setMeterAssets)

    def addMeterAssets(self, *MeterAssets):
        for obj in MeterAssets:
            obj._MeterAssetModel = self
            self._MeterAssets.append(obj)

    def removeMeterAssets(self, *MeterAssets):
        for obj in MeterAssets:
            obj._MeterAssetModel = None
            self._MeterAssets.remove(obj)

