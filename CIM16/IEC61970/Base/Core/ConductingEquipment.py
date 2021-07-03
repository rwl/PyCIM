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

from CIM16.IEC61970.Core.Equipment import Equipment

class ConductingEquipment(Equipment):
    """The parts of the power system that are designed to carry current or that are conductively connected therewith. ConductingEquipment is contained within an EquipmentContainer that may be a Substation, or a VoltageLevel or a Bay within a Substation.The parts of the power system that are designed to carry current or that are conductively connected therewith. ConductingEquipment is contained within an EquipmentContainer that may be a Substation, or a VoltageLevel or a Bay within a Substation.
    """

    def __init__(self, BaseVoltage=None, ClearanceTags=None, ProtectionEquipments=None, Terminals=None, OutageStepRoles=None, SvStatus=None, *args, **kw_args):
        """Initialises a new 'ConductingEquipment' instance.

        @param BaseVoltage: Use association to ConductingEquipment only when there is no VoltageLevel container used.
        @param ClearanceTags: Conducting equipment may have multiple clearance tags for authorized field work
        @param ProtectionEquipments: Protection equipment may be used to protect specific Conducting Equipment. Multiple equipment may be protected or monitored by multiple protection equipment.
        @param Terminals: ConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodes
        @param OutageStepRoles:
        @param SvStatus: The status state associated with the conducting equipment.
        """
        self._BaseVoltage = None
        self.BaseVoltage = BaseVoltage

        self._ClearanceTags = []
        self.ClearanceTags = [] if ClearanceTags is None else ClearanceTags

        self._ProtectionEquipments = []
        self.ProtectionEquipments = [] if ProtectionEquipments is None else ProtectionEquipments

        self._Terminals = []
        self.Terminals = [] if Terminals is None else Terminals

        self._OutageStepRoles = []
        self.OutageStepRoles = [] if OutageStepRoles is None else OutageStepRoles

        self._SvStatus = None
        self.SvStatus = SvStatus

        super(ConductingEquipment, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["BaseVoltage", "ClearanceTags", "ProtectionEquipments", "Terminals", "OutageStepRoles", "SvStatus"]
    _many_refs = ["ClearanceTags", "ProtectionEquipments", "Terminals", "OutageStepRoles"]

    def getBaseVoltage(self):
        """Use association to ConductingEquipment only when there is no VoltageLevel container used.
        """
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

    def getClearanceTags(self):
        """Conducting equipment may have multiple clearance tags for authorized field work
        """
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

    def getProtectionEquipments(self):
        """Protection equipment may be used to protect specific Conducting Equipment. Multiple equipment may be protected or monitored by multiple protection equipment.
        """
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

    def getTerminals(self):
        """ConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodes
        """
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

    def getOutageStepRoles(self):
        
        return self._OutageStepRoles

    def setOutageStepRoles(self, value):
        for x in self._OutageStepRoles:
            x.ConductingEquipment = None
        for y in value:
            y._ConductingEquipment = self
        self._OutageStepRoles = value

    OutageStepRoles = property(getOutageStepRoles, setOutageStepRoles)

    def addOutageStepRoles(self, *OutageStepRoles):
        for obj in OutageStepRoles:
            obj.ConductingEquipment = self

    def removeOutageStepRoles(self, *OutageStepRoles):
        for obj in OutageStepRoles:
            obj.ConductingEquipment = None

    def getSvStatus(self):
        """The status state associated with the conducting equipment.
        """
        return self._SvStatus

    def setSvStatus(self, value):
        if self._SvStatus is not None:
            self._SvStatus._ConductingEquipment = None

        self._SvStatus = value
        if self._SvStatus is not None:
            self._SvStatus.ConductingEquipment = None
            self._SvStatus._ConductingEquipment = self

    SvStatus = property(getSvStatus, setSvStatus)

