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

from CIM15.IEC61970.Core.Equipment import Equipment

class ProtectionEquipment(Equipment):
    """An electrical device designed to respond to input conditions in a prescribed manner and after specified conditions are met to cause contact operation or similar abrupt change in associated electric control circuits, or simply to display the detected condition. Protection equipment are associated with conducting equipment and usually operate circuit breakers.An electrical device designed to respond to input conditions in a prescribed manner and after specified conditions are met to cause contact operation or similar abrupt change in associated electric control circuits, or simply to display the detected condition. Protection equipment are associated with conducting equipment and usually operate circuit breakers.
    """

    def __init__(self, highLimit=0.0, powerDirectionFlag=False, lowLimit=0.0, unitSymbol="N", relayDelayTime=0.0, unitMultiplier="M", ConductingEquipments=None, ProtectedSwitches=None, *args, **kw_args):
        """Initialises a new 'ProtectionEquipment' instance.

        @param highLimit: The maximum allowable value. 
        @param powerDirectionFlag: Direction same as positive active power flow value. 
        @param lowLimit: The minimum allowable value. 
        @param unitSymbol: The unit of measure of the value. Values are: "N", "A", "rad", "VAh", "Pa", "J", "h", "Hz", "VArh", "ohm", "H", "m3", "deg", "V", "oC", "F", "Wh", "s", "g", "min", "S", "none", "W", "VAr", "m2", "m", "VA"
        @param relayDelayTime: The time delay from detection of abnormal conditions to relay operation. 
        @param unitMultiplier: The unit multiplier of the value. Values are: "M", "G", "d", "micro", "c", "p", "n", "T", "k", "m", "none"
        @param ConductingEquipments: Protection equipment may be used to protect specific Conducting Equipment. Multiple equipment may be protected or monitored by multiple protection equipment.
        @param ProtectedSwitches: Protected switches operated by this ProtectionEquipment.
        """
        #: The maximum allowable value.
        self.highLimit = highLimit

        #: Direction same as positive active power flow value.
        self.powerDirectionFlag = powerDirectionFlag

        #: The minimum allowable value.
        self.lowLimit = lowLimit

        #: The unit of measure of the value. Values are: "N", "A", "rad", "VAh", "Pa", "J", "h", "Hz", "VArh", "ohm", "H", "m3", "deg", "V", "oC", "F", "Wh", "s", "g", "min", "S", "none", "W", "VAr", "m2", "m", "VA"
        self.unitSymbol = unitSymbol

        #: The time delay from detection of abnormal conditions to relay operation.
        self.relayDelayTime = relayDelayTime

        #: The unit multiplier of the value. Values are: "M", "G", "d", "micro", "c", "p", "n", "T", "k", "m", "none"
        self.unitMultiplier = unitMultiplier

        self._ConductingEquipments = []
        self.ConductingEquipments = [] if ConductingEquipments is None else ConductingEquipments

        self._ProtectedSwitches = []
        self.ProtectedSwitches = [] if ProtectedSwitches is None else ProtectedSwitches

        super(ProtectionEquipment, self).__init__(*args, **kw_args)

    _attrs = ["highLimit", "powerDirectionFlag", "lowLimit", "unitSymbol", "relayDelayTime", "unitMultiplier"]
    _attr_types = {"highLimit": float, "powerDirectionFlag": bool, "lowLimit": float, "unitSymbol": str, "relayDelayTime": float, "unitMultiplier": str}
    _defaults = {"highLimit": 0.0, "powerDirectionFlag": False, "lowLimit": 0.0, "unitSymbol": "N", "relayDelayTime": 0.0, "unitMultiplier": "M"}
    _enums = {"unitSymbol": "UnitSymbol", "unitMultiplier": "UnitMultiplier"}
    _refs = ["ConductingEquipments", "ProtectedSwitches"]
    _many_refs = ["ConductingEquipments", "ProtectedSwitches"]

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

    def getProtectedSwitches(self):
        """Protected switches operated by this ProtectionEquipment.
        """
        return self._ProtectedSwitches

    def setProtectedSwitches(self, value):
        for p in self._ProtectedSwitches:
            filtered = [q for q in p.ProtectionEquipments if q != self]
            self._ProtectedSwitches._ProtectionEquipments = filtered
        for r in value:
            if self not in r._ProtectionEquipments:
                r._ProtectionEquipments.append(self)
        self._ProtectedSwitches = value

    ProtectedSwitches = property(getProtectedSwitches, setProtectedSwitches)

    def addProtectedSwitches(self, *ProtectedSwitches):
        for obj in ProtectedSwitches:
            if self not in obj._ProtectionEquipments:
                obj._ProtectionEquipments.append(self)
            self._ProtectedSwitches.append(obj)

    def removeProtectedSwitches(self, *ProtectedSwitches):
        for obj in ProtectedSwitches:
            if self in obj._ProtectionEquipments:
                obj._ProtectionEquipments.remove(self)
            self._ProtectedSwitches.remove(obj)

