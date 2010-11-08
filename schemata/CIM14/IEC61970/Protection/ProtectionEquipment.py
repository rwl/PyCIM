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

from CIM14.IEC61970.Core.Equipment import Equipment

class ProtectionEquipment(Equipment):
    """An electrical device designed to respond to input conditions in a prescribed manner and after specified conditions are met to cause contact operation or similar abrupt change in associated electric control circuits, or simply to display the detected condition. Protection equipment are associated with conducting equipment and usually operate circuit breakers.
    """

    def __init__(self, lowLimit=0.0, powerDirectionFlag=False, highLimit=0.0, relayDelayTime=0.0, ProtectedSwitches=None, Unit=None, ConductingEquipments=None, *args, **kw_args):
        """Initialises a new 'ProtectionEquipment' instance.

        @param lowLimit: The minimum allowable value. 
        @param powerDirectionFlag: Direction same as positive active power flow value. 
        @param highLimit: The maximum allowable value. 
        @param relayDelayTime: The time delay from detection of abnormal conditions to relay operation. 
        @param ProtectedSwitches: Protected switches operated by this ProtectionEquipment.
        @param Unit: The Unit for the Protection Equipment.
        @param ConductingEquipments: Protection equipment may be used to protect specific Conducting Equipment. Multiple equipment may be protected or monitored by multiple protection equipment.
        """
        #: The minimum allowable value.
        self.lowLimit = lowLimit

        #: Direction same as positive active power flow value.
        self.powerDirectionFlag = powerDirectionFlag

        #: The maximum allowable value.
        self.highLimit = highLimit

        #: The time delay from detection of abnormal conditions to relay operation.
        self.relayDelayTime = relayDelayTime

        self.ProtectedSwitches = [] if ProtectedSwitches is None else ProtectedSwitches

        self._Unit = None
        self.Unit = Unit

        self._ConductingEquipments = []
        self.ConductingEquipments = [] if ConductingEquipments is None else ConductingEquipments

        super(ProtectionEquipment, self).__init__(*args, **kw_args)

    _attrs = ["lowLimit", "powerDirectionFlag", "highLimit", "relayDelayTime"]
    _attr_types = {"lowLimit": float, "powerDirectionFlag": bool, "highLimit": float, "relayDelayTime": float}
    _defaults = {"lowLimit": 0.0, "powerDirectionFlag": False, "highLimit": 0.0, "relayDelayTime": 0.0}
    _enums = {}
    _refs = ["ProtectedSwitches", "Unit", "ConductingEquipments"]
    _many_refs = ["ProtectedSwitches", "ConductingEquipments"]

    def add_ProtectedSwitches(self, *ProtectedSwitches):
        for obj in ProtectedSwitches:
            self.ProtectedSwitches.append(obj)

    def remove_ProtectedSwitches(self, *ProtectedSwitches):
        for obj in ProtectedSwitches:
            self.ProtectedSwitches.remove(obj)

    def getUnit(self):
        """The Unit for the Protection Equipment.
        """
        return self._Unit

    def setUnit(self, value):
        if self._Unit is not None:
            filtered = [x for x in self.Unit.ProtectionEquipments if x != self]
            self._Unit._ProtectionEquipments = filtered

        self._Unit = value
        if self._Unit is not None:
            self._Unit._ProtectionEquipments.append(self)

    Unit = property(getUnit, setUnit)

    def getConductingEquipments(self):
        """Protection equipment may be used to protect specific Conducting Equipment. Multiple equipment may be protected or monitored by multiple protection equipment.
        """
        return self._ConductingEquipments

    def setConductingEquipments(self, value):
        for p in self._ConductingEquipments:
            filtered = [q for q in p.ProtectionEquipments if q != self]
            self._ConductingEquipments._ProtectionEquipments = filtered
        for r in value:
            if self not in r._ProtectionEquipments:
                r._ProtectionEquipments.append(self)
        self._ConductingEquipments = value

    ConductingEquipments = property(getConductingEquipments, setConductingEquipments)

    def addConductingEquipments(self, *ConductingEquipments):
        for obj in ConductingEquipments:
            if self not in obj._ProtectionEquipments:
                obj._ProtectionEquipments.append(self)
            self._ConductingEquipments.append(obj)

    def removeConductingEquipments(self, *ConductingEquipments):
        for obj in ConductingEquipments:
            if self in obj._ProtectionEquipments:
                obj._ProtectionEquipments.remove(self)
            self._ConductingEquipments.remove(obj)

