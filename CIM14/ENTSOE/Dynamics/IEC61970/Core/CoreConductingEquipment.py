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

from CIM14.ENTSOE.Dynamics.IEC61970.Core.CoreEquipment import CoreEquipment

class CoreConductingEquipment(CoreEquipment):

    def __init__(self, phases="ABC", SvStatus=None, ClearanceTags=None, Terminals=None, ProtectionEquipments=None, BaseVoltage=None, *args, **kw_args):
        """Initialises a new 'CoreConductingEquipment' instance.

        @param phases: Values are: "ABC", "splitSecondary2N", "ABN", "CN", "ACN", "BC", "AN", "BN", "AB", "splitSecondary1N", "N", "C", "AC", "ABCN", "splitSecondary12N", "A", "B", "BCN"
        @param SvStatus:
        @param ClearanceTags:
        @param Terminals:
        @param ProtectionEquipments:
        @param BaseVoltage:
        """
        #: Values are: "ABC", "splitSecondary2N", "ABN", "CN", "ACN", "BC", "AN", "BN", "AB", "splitSecondary1N", "N", "C", "AC", "ABCN", "splitSecondary12N", "A", "B", "BCN"
        self.phases = phases

        self._SvStatus = None
        self.SvStatus = SvStatus

        self._ClearanceTags = []
        self.ClearanceTags = [] if ClearanceTags is None else ClearanceTags

        self._Terminals = []
        self.Terminals = [] if Terminals is None else Terminals

        self._ProtectionEquipments = []
        self.ProtectionEquipments = [] if ProtectionEquipments is None else ProtectionEquipments

        self._BaseVoltage = None
        self.BaseVoltage = BaseVoltage

        super(CoreConductingEquipment, self).__init__(*args, **kw_args)

    _attrs = ["phases"]
    _attr_types = {"phases": str}
    _defaults = {"phases": "ABC"}
    _enums = {"phases": "CorePhaseCode"}
    _refs = ["SvStatus", "ClearanceTags", "Terminals", "ProtectionEquipments", "BaseVoltage"]
    _many_refs = ["ClearanceTags", "Terminals", "ProtectionEquipments"]

    def getSvStatus(self):
        
        return self._SvStatus

    def setSvStatus(self, value):
        if self._SvStatus is not None:
            self._SvStatus._ConductingEquipment = None

        self._SvStatus = value
        if self._SvStatus is not None:
            self._SvStatus.ConductingEquipment = None
            self._SvStatus._ConductingEquipment = self

    SvStatus = property(getSvStatus, setSvStatus)

    def getClearanceTags(self):
        
        return self._ClearanceTags

    def setClearanceTags(self, value):
        for x in self._ClearanceTags:
            x.ConductingEquipment = None
        for y in value:
            y._ConductingEquipment = self
        self._ClearanceTags = value

    ClearanceTags = property(getClearanceTags, setClearanceTags)

    def addClearanceTags(self, *ClearanceTags):
        for obj in ClearanceTags:
            obj.ConductingEquipment = self

    def removeClearanceTags(self, *ClearanceTags):
        for obj in ClearanceTags:
            obj.ConductingEquipment = None

    def getTerminals(self):
        
        return self._Terminals

    def setTerminals(self, value):
        for x in self._Terminals:
            x.ConductingEquipment = None
        for y in value:
            y._ConductingEquipment = self
        self._Terminals = value

    Terminals = property(getTerminals, setTerminals)

    def addTerminals(self, *Terminals):
        for obj in Terminals:
            obj.ConductingEquipment = self

    def removeTerminals(self, *Terminals):
        for obj in Terminals:
            obj.ConductingEquipment = None

    def getProtectionEquipments(self):
        
        return self._ProtectionEquipments

    def setProtectionEquipments(self, value):
        for p in self._ProtectionEquipments:
            filtered = [q for q in p.ConductingEquipments if q != self]
            self._ProtectionEquipments._ConductingEquipments = filtered
        for r in value:
            if self not in r._ConductingEquipments:
                r._ConductingEquipments.append(self)
        self._ProtectionEquipments = value

    ProtectionEquipments = property(getProtectionEquipments, setProtectionEquipments)

    def addProtectionEquipments(self, *ProtectionEquipments):
        for obj in ProtectionEquipments:
            if self not in obj._ConductingEquipments:
                obj._ConductingEquipments.append(self)
            self._ProtectionEquipments.append(obj)

    def removeProtectionEquipments(self, *ProtectionEquipments):
        for obj in ProtectionEquipments:
            if self in obj._ConductingEquipments:
                obj._ConductingEquipments.remove(self)
            self._ProtectionEquipments.remove(obj)

    def getBaseVoltage(self):
        
        return self._BaseVoltage

    def setBaseVoltage(self, value):
        if self._BaseVoltage is not None:
            filtered = [x for x in self.BaseVoltage.ConductingEquipment if x != self]
            self._BaseVoltage._ConductingEquipment = filtered

        self._BaseVoltage = value
        if self._BaseVoltage is not None:
            if self not in self._BaseVoltage._ConductingEquipment:
                self._BaseVoltage._ConductingEquipment.append(self)

    BaseVoltage = property(getBaseVoltage, setBaseVoltage)

