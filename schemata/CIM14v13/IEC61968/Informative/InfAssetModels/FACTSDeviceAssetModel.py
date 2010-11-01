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

class FACTSDeviceAssetModel(ElectricalAssetModel):
    """A particular model of FACTS device provided from a manufacturer. A FACTS devices are used for the dynamic control of voltage, impedance and phase angle of high voltage AC transmission lines. FACTS device types include: - SVC = Static Var Compensator - STATCOM = Static Synchronous Compensator - TCPAR = Thyristor Controlled Phase-Angle Regulator - TCSC = Thyristor Controlled Series Capacitor - TCVL = Thyristor Controlled Voltage Limiter - TSBR = Thyristor Switched Braking Resistor - TSSC = Thyristor Switched Series Capacitor - UPFC = Unified Power Flow Controller
    """

    def __init__(self, FACTSDeviceAssets=None, FACTSDeviceTypeAsset=None, *args, **kw_args):
        """Initializes a new 'FACTSDeviceAssetModel' instance.

        @param FACTSDeviceAssets:
        @param FACTSDeviceTypeAsset:
        """
        self._FACTSDeviceAssets = []
        self.FACTSDeviceAssets = [] if FACTSDeviceAssets is None else FACTSDeviceAssets

        self._FACTSDeviceTypeAsset = None
        self.FACTSDeviceTypeAsset = FACTSDeviceTypeAsset

        super(FACTSDeviceAssetModel, self).__init__(*args, **kw_args)

    def getFACTSDeviceAssets(self):
        
        return self._FACTSDeviceAssets

    def setFACTSDeviceAssets(self, value):
        for x in self._FACTSDeviceAssets:
            x._FACTSDeviceAssetModel = None
        for y in value:
            y._FACTSDeviceAssetModel = self
        self._FACTSDeviceAssets = value

    FACTSDeviceAssets = property(getFACTSDeviceAssets, setFACTSDeviceAssets)

    def addFACTSDeviceAssets(self, *FACTSDeviceAssets):
        for obj in FACTSDeviceAssets:
            obj._FACTSDeviceAssetModel = self
            self._FACTSDeviceAssets.append(obj)

    def removeFACTSDeviceAssets(self, *FACTSDeviceAssets):
        for obj in FACTSDeviceAssets:
            obj._FACTSDeviceAssetModel = None
            self._FACTSDeviceAssets.remove(obj)

    def getFACTSDeviceTypeAsset(self):
        
        return self._FACTSDeviceTypeAsset

    def setFACTSDeviceTypeAsset(self, value):
        if self._FACTSDeviceTypeAsset is not None:
            filtered = [x for x in self.FACTSDeviceTypeAsset.FACTSDeviceAssetModels if x != self]
            self._FACTSDeviceTypeAsset._FACTSDeviceAssetModels = filtered

        self._FACTSDeviceTypeAsset = value
        if self._FACTSDeviceTypeAsset is not None:
            self._FACTSDeviceTypeAsset._FACTSDeviceAssetModels.append(self)

    FACTSDeviceTypeAsset = property(getFACTSDeviceTypeAsset, setFACTSDeviceTypeAsset)

