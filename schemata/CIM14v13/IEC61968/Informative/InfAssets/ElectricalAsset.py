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

from CIM14v13.IEC61968.Assets.Asset import Asset

class ElectricalAsset(Asset):
    """An asset that has (or can have) a role in the electrical network.
    """

    def __init__(self, phaseCode='BC', isConnected=False, ElectricalInfos=None, ConductingEquipment=None, **kw_args):
        """Initializes a new 'ElectricalAsset' instance.

        @param phaseCode: If 'isConnected' is true, then this is the as-built phase(s) that the asset is associatied with. Values are: "BC", "AB", "B", "AC", "ABC", "splitSecondary1N", "ABN", "ABCN", "CN", "AN", "splitSecondary12N", "BCN", "splitSecondary2N", "ACN", "A", "C", "N", "BN"
        @param isConnected: True if the asset is physically connected to electrical network (as opposed to being in a warehouse, being refurbished, etc.). Note that this attribute is not intended to imply energization status and/or whether the asset is actually being used. 
        @param ElectricalInfos:
        @param ConductingEquipment:
        """
        #: If 'isConnected' is true, then this is the as-built phase(s) that the asset is associatied with.Values are: "BC", "AB", "B", "AC", "ABC", "splitSecondary1N", "ABN", "ABCN", "CN", "AN", "splitSecondary12N", "BCN", "splitSecondary2N", "ACN", "A", "C", "N", "BN"
        self.phaseCode = phaseCode

        #: True if the asset is physically connected to electrical network (as opposed to being in a warehouse, being refurbished, etc.). Note that this attribute is not intended to imply energization status and/or whether the asset is actually being used.
        self.isConnected = isConnected

        self._ElectricalInfos = []
        self.ElectricalInfos = [] if ElectricalInfos is None else ElectricalInfos

        self._ConductingEquipment = None
        self.ConductingEquipment = ConductingEquipment

        super(ElectricalAsset, self).__init__(**kw_args)

    def getElectricalInfos(self):
        
        return self._ElectricalInfos

    def setElectricalInfos(self, value):
        for p in self._ElectricalInfos:
            filtered = [q for q in p.ElectricalAssets if q != self]
            self._ElectricalInfos._ElectricalAssets = filtered
        for r in value:
            if self not in r._ElectricalAssets:
                r._ElectricalAssets.append(self)
        self._ElectricalInfos = value

    ElectricalInfos = property(getElectricalInfos, setElectricalInfos)

    def addElectricalInfos(self, *ElectricalInfos):
        for obj in ElectricalInfos:
            if self not in obj._ElectricalAssets:
                obj._ElectricalAssets.append(self)
            self._ElectricalInfos.append(obj)

    def removeElectricalInfos(self, *ElectricalInfos):
        for obj in ElectricalInfos:
            if self in obj._ElectricalAssets:
                obj._ElectricalAssets.remove(self)
            self._ElectricalInfos.remove(obj)

    def getConductingEquipment(self):
        
        return self._ConductingEquipment

    def setConductingEquipment(self, value):
        if self._ConductingEquipment is not None:
            filtered = [x for x in self.ConductingEquipment.ElectricalAssets if x != self]
            self._ConductingEquipment._ElectricalAssets = filtered

        self._ConductingEquipment = value
        if self._ConductingEquipment is not None:
            self._ConductingEquipment._ElectricalAssets.append(self)

    ConductingEquipment = property(getConductingEquipment, setConductingEquipment)

