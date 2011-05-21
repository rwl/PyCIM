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
            if self not in self._Unit._ProtectionEquipments:
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

