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

from CIM14v13.IEC61970.Core.PowerSystemResource import PowerSystemResource

class Flowgate(PowerSystemResource):
    """A flowgate, is single or group of transmission elements intended to model MW flow impact relating to transmission limitations and transmission service usage.
    """

    def __init__(self, coordinatedFlag=False, counterFlowValue=0, reciprocalFlag=False, managingEntityFlag=False, AfcUseCode=None, outOfServiceDate='', coordinationStudyDate='', AtcFlag=False, inServiceDate='', IdcAssignedId=0, IdcOperationalName='', positiveImpactValue=0, IdcType=None, deletionDate='', SubControlArea=None, ViolationLimits=None, TransmissionProvider=None, TransmissionReliabilityMargin=None, PowerTransormers=None, Lines=None, CapacityBenefitMargin=None, FTRs=None, *args, **kw_args):
        """Initializes a new 'Flowgate' instance.

        @param coordinatedFlag: Flag to indicate if Flowgate qualified as coordinated Flowgate 
        @param counterFlowValue: Percentage of counterflow to remove/exclude from the AFC calculation.  Integer.  Must be 100 or less. 
        @param reciprocalFlag: Flag to indicate if Flowgate qualified as reciprocal Flowgate 
        @param managingEntityFlag: Standard Reliabilty Entity (e.g. in North America NERC) that has agreed per a reciprocal agreement to manage coordination on the Flowgate.  Will always be either True or False - if not a reciprocal Flowgate, will be false. 
        @param AfcUseCode: Used to indicate if FG should be used only for certain types of AFC Calculations.  Values are 'FIRM,'  'NONFIRM,' and 'BOTH.' 
        @param outOfServiceDate: Date at which point Flowgate becomes inactive. Used to insert outage condition. 
        @param coordinationStudyDate: Date upon which study of Flowgate to determine coordinated status was performed.  May be null is no study undertaken yet. 
        @param AtcFlag: Flag to indicate if Flowgate is utilized for coordination of ATC. 
        @param inServiceDate: Date at which point Flowgate becomes active.  Used to insert future Flowgates or Flowgates returning from an outage condition. 
        @param IdcAssignedId: The registered Flowgate ID Assigned by the IDC and/or Book of Flowgate. 
        @param IdcOperationalName: The Registered Name utilized in the IDC and/or Book of Flowgates 
        @param positiveImpactValue: Percentage of positive impact to include in the AFC calculation.  Integer.  Must be 100 or less. 
        @param IdcType: The type of Flowgate.  Values are 'PERMANENT' (in Book of Flowgates) or 'TEMPORARY'. 
        @param deletionDate: Date at which point Flowgate should be removed from the Interchange Distribution Calculatin (IDC). 
        @param SubControlArea: A control area may own 0 to n flowgates A flowgate must be owned by exactly 1 control area
        @param ViolationLimits:
        @param TransmissionProvider: A flowgate can be reciprocal flowgate for 0 to n transmission providers. A transmission provider may be a reciprocal entity for 0 to n flowgates.
        @param TransmissionReliabilityMargin: A fowgate may have 0 to 1 TRM
        @param PowerTransormers:
        @param Lines:
        @param CapacityBenefitMargin: A flowgate may have 0 to n CBM profile Each season may be a CBM which contains a set of profile data
        @param FTRs:
        """
        #: Flag to indicate if Flowgate qualified as coordinated Flowgate
        self.coordinatedFlag = coordinatedFlag

        #: Percentage of counterflow to remove/exclude from the AFC calculation.  Integer.  Must be 100 or less.
        self.counterFlowValue = counterFlowValue

        #: Flag to indicate if Flowgate qualified as reciprocal Flowgate
        self.reciprocalFlag = reciprocalFlag

        #: Standard Reliabilty Entity (e.g. in North America NERC) that has agreed per a reciprocal agreement to manage coordination on the Flowgate.  Will always be either True or False - if not a reciprocal Flowgate, will be false.
        self.managingEntityFlag = managingEntityFlag

        #: Used to indicate if FG should be used only for certain types of AFC Calculations.  Values are 'FIRM,'  'NONFIRM,' and 'BOTH.'
        self.AfcUseCode = AfcUseCode

        #: Date at which point Flowgate becomes inactive. Used to insert outage condition.
        self.outOfServiceDate = outOfServiceDate

        #: Date upon which study of Flowgate to determine coordinated status was performed.  May be null is no study undertaken yet.
        self.coordinationStudyDate = coordinationStudyDate

        #: Flag to indicate if Flowgate is utilized for coordination of ATC.
        self.AtcFlag = AtcFlag

        #: Date at which point Flowgate becomes active.  Used to insert future Flowgates or Flowgates returning from an outage condition.
        self.inServiceDate = inServiceDate

        #: The registered Flowgate ID Assigned by the IDC and/or Book of Flowgate.
        self.IdcAssignedId = IdcAssignedId

        #: The Registered Name utilized in the IDC and/or Book of Flowgates
        self.IdcOperationalName = IdcOperationalName

        #: Percentage of positive impact to include in the AFC calculation.  Integer.  Must be 100 or less.
        self.positiveImpactValue = positiveImpactValue

        #: The type of Flowgate.  Values are 'PERMANENT' (in Book of Flowgates) or 'TEMPORARY'.
        self.IdcType = IdcType

        #: Date at which point Flowgate should be removed from the Interchange Distribution Calculatin (IDC).
        self.deletionDate = deletionDate

        self._SubControlArea = None
        self.SubControlArea = SubControlArea

        self._ViolationLimits = []
        self.ViolationLimits = [] if ViolationLimits is None else ViolationLimits

        self._TransmissionProvider = []
        self.TransmissionProvider = [] if TransmissionProvider is None else TransmissionProvider

        self._TransmissionReliabilityMargin = None
        self.TransmissionReliabilityMargin = TransmissionReliabilityMargin

        self._PowerTransormers = []
        self.PowerTransormers = [] if PowerTransormers is None else PowerTransormers

        self._Lines = []
        self.Lines = [] if Lines is None else Lines

        self._CapacityBenefitMargin = []
        self.CapacityBenefitMargin = [] if CapacityBenefitMargin is None else CapacityBenefitMargin

        self._FTRs = []
        self.FTRs = [] if FTRs is None else FTRs

        super(Flowgate, self).__init__(*args, **kw_args)

    def getSubControlArea(self):
        """A control area may own 0 to n flowgates A flowgate must be owned by exactly 1 control area
        """
        return self._SubControlArea

    def setSubControlArea(self, value):
        if self._SubControlArea is not None:
            filtered = [x for x in self.SubControlArea.Flowgate if x != self]
            self._SubControlArea._Flowgate = filtered

        self._SubControlArea = value
        if self._SubControlArea is not None:
            self._SubControlArea._Flowgate.append(self)

    SubControlArea = property(getSubControlArea, setSubControlArea)

    def getViolationLimits(self):
        
        return self._ViolationLimits

    def setViolationLimits(self, value):
        for x in self._ViolationLimits:
            x._Flowgate = None
        for y in value:
            y._Flowgate = self
        self._ViolationLimits = value

    ViolationLimits = property(getViolationLimits, setViolationLimits)

    def addViolationLimits(self, *ViolationLimits):
        for obj in ViolationLimits:
            obj._Flowgate = self
            self._ViolationLimits.append(obj)

    def removeViolationLimits(self, *ViolationLimits):
        for obj in ViolationLimits:
            obj._Flowgate = None
            self._ViolationLimits.remove(obj)

    def getTransmissionProvider(self):
        """A flowgate can be reciprocal flowgate for 0 to n transmission providers. A transmission provider may be a reciprocal entity for 0 to n flowgates.
        """
        return self._TransmissionProvider

    def setTransmissionProvider(self, value):
        for p in self._TransmissionProvider:
            filtered = [q for q in p.Flowgate if q != self]
            self._TransmissionProvider._Flowgate = filtered
        for r in value:
            if self not in r._Flowgate:
                r._Flowgate.append(self)
        self._TransmissionProvider = value

    TransmissionProvider = property(getTransmissionProvider, setTransmissionProvider)

    def addTransmissionProvider(self, *TransmissionProvider):
        for obj in TransmissionProvider:
            if self not in obj._Flowgate:
                obj._Flowgate.append(self)
            self._TransmissionProvider.append(obj)

    def removeTransmissionProvider(self, *TransmissionProvider):
        for obj in TransmissionProvider:
            if self in obj._Flowgate:
                obj._Flowgate.remove(self)
            self._TransmissionProvider.remove(obj)

    def getTransmissionReliabilityMargin(self):
        """A fowgate may have 0 to 1 TRM
        """
        return self._TransmissionReliabilityMargin

    def setTransmissionReliabilityMargin(self, value):
        if self._TransmissionReliabilityMargin is not None:
            filtered = [x for x in self.TransmissionReliabilityMargin.Flowgate if x != self]
            self._TransmissionReliabilityMargin._Flowgate = filtered

        self._TransmissionReliabilityMargin = value
        if self._TransmissionReliabilityMargin is not None:
            self._TransmissionReliabilityMargin._Flowgate.append(self)

    TransmissionReliabilityMargin = property(getTransmissionReliabilityMargin, setTransmissionReliabilityMargin)

    def getPowerTransormers(self):
        
        return self._PowerTransormers

    def setPowerTransormers(self, value):
        for p in self._PowerTransormers:
            filtered = [q for q in p.Flowgates if q != self]
            self._PowerTransormers._Flowgates = filtered
        for r in value:
            if self not in r._Flowgates:
                r._Flowgates.append(self)
        self._PowerTransormers = value

    PowerTransormers = property(getPowerTransormers, setPowerTransormers)

    def addPowerTransormers(self, *PowerTransormers):
        for obj in PowerTransormers:
            if self not in obj._Flowgates:
                obj._Flowgates.append(self)
            self._PowerTransormers.append(obj)

    def removePowerTransormers(self, *PowerTransormers):
        for obj in PowerTransormers:
            if self in obj._Flowgates:
                obj._Flowgates.remove(self)
            self._PowerTransormers.remove(obj)

    def getLines(self):
        
        return self._Lines

    def setLines(self, value):
        for p in self._Lines:
            filtered = [q for q in p.Flowgates if q != self]
            self._Lines._Flowgates = filtered
        for r in value:
            if self not in r._Flowgates:
                r._Flowgates.append(self)
        self._Lines = value

    Lines = property(getLines, setLines)

    def addLines(self, *Lines):
        for obj in Lines:
            if self not in obj._Flowgates:
                obj._Flowgates.append(self)
            self._Lines.append(obj)

    def removeLines(self, *Lines):
        for obj in Lines:
            if self in obj._Flowgates:
                obj._Flowgates.remove(self)
            self._Lines.remove(obj)

    def getCapacityBenefitMargin(self):
        """A flowgate may have 0 to n CBM profile Each season may be a CBM which contains a set of profile data
        """
        return self._CapacityBenefitMargin

    def setCapacityBenefitMargin(self, value):
        for p in self._CapacityBenefitMargin:
            filtered = [q for q in p.Flowgate if q != self]
            self._CapacityBenefitMargin._Flowgate = filtered
        for r in value:
            if self not in r._Flowgate:
                r._Flowgate.append(self)
        self._CapacityBenefitMargin = value

    CapacityBenefitMargin = property(getCapacityBenefitMargin, setCapacityBenefitMargin)

    def addCapacityBenefitMargin(self, *CapacityBenefitMargin):
        for obj in CapacityBenefitMargin:
            if self not in obj._Flowgate:
                obj._Flowgate.append(self)
            self._CapacityBenefitMargin.append(obj)

    def removeCapacityBenefitMargin(self, *CapacityBenefitMargin):
        for obj in CapacityBenefitMargin:
            if self in obj._Flowgate:
                obj._Flowgate.remove(self)
            self._CapacityBenefitMargin.remove(obj)

    def getFTRs(self):
        
        return self._FTRs

    def setFTRs(self, value):
        for x in self._FTRs:
            x._Flowgate = None
        for y in value:
            y._Flowgate = self
        self._FTRs = value

    FTRs = property(getFTRs, setFTRs)

    def addFTRs(self, *FTRs):
        for obj in FTRs:
            obj._Flowgate = self
            self._FTRs.append(obj)

    def removeFTRs(self, *FTRs):
        for obj in FTRs:
            obj._Flowgate = None
            self._FTRs.remove(obj)

