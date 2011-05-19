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

from CIM15.IEC61970.Core.IdentifiedObject import IdentifiedObject

class OutageStep(IdentifiedObject):
    """Holds an outage start and end time for each supply point of an outage record. The supply point for a given step is the associated PowerSystemResource instance.Holds an outage start and end time for each supply point of an outage record. The supply point for a given step is the associated PowerSystemResource instance.
    """

    def __init__(self, averageCml=0.0, damage=False, specialCustomerCount=0, criticalCustomerCount=0, estimatedRestoreDateTime='', shockReported=False, callerCount=0, fatality=False, jobPriority='', totalCustomerCount=0, injury=False, totalCml=0.0, Crews=None, noPowerInterval=None, ConductingEquipmentRoles=None, status=None, OutageRecord=None, OutageCodes=None, *args, **kw_args):
        """Initialises a new 'OutageStep' instance.

        @param averageCml: Average Customer Minutes Lost (CML) for this supply point for this outage. 
        @param damage: True if damage reported by caller or engineer. 
        @param specialCustomerCount: Number of customers with high reliability required. 
        @param criticalCustomerCount: Number of customers with critical needs, e.g., with a dialysis machine. 
        @param estimatedRestoreDateTime: Estimated time of restoration. 
        @param shockReported: True if shocks reported by caller or engineer. 
        @param callerCount: Number of customers phoning in. 
        @param fatality: True if fatalities reported by caller or engineer. 
        @param jobPriority: 
        @param totalCustomerCount: Number of customers connected to the PowerSystemResource. 
        @param injury: True if injuries reported by caller or engineer. 
        @param totalCml: Total Customer Minutes Lost (CML) for this supply point for this outage. 
        @param Crews:
        @param noPowerInterval: Date and time interval between loss and restoration of power.
        @param ConductingEquipmentRoles:
        @param status:
        @param OutageRecord:
        @param OutageCodes: Multiple outage codes may apply to an outage step.
        """
        #: Average Customer Minutes Lost (CML) for this supply point for this outage.
        self.averageCml = averageCml

        #: True if damage reported by caller or engineer.
        self.damage = damage

        #: Number of customers with high reliability required.
        self.specialCustomerCount = specialCustomerCount

        #: Number of customers with critical needs, e.g., with a dialysis machine.
        self.criticalCustomerCount = criticalCustomerCount

        #: Estimated time of restoration.
        self.estimatedRestoreDateTime = estimatedRestoreDateTime

        #: True if shocks reported by caller or engineer.
        self.shockReported = shockReported

        #: Number of customers phoning in.
        self.callerCount = callerCount

        #: True if fatalities reported by caller or engineer.
        self.fatality = fatality


        self.jobPriority = jobPriority

        #: Number of customers connected to the PowerSystemResource.
        self.totalCustomerCount = totalCustomerCount

        #: True if injuries reported by caller or engineer.
        self.injury = injury

        #: Total Customer Minutes Lost (CML) for this supply point for this outage.
        self.totalCml = totalCml

        self._Crews = []
        self.Crews = [] if Crews is None else Crews

        self.noPowerInterval = noPowerInterval

        self._ConductingEquipmentRoles = []
        self.ConductingEquipmentRoles = [] if ConductingEquipmentRoles is None else ConductingEquipmentRoles

        self.status = status

        self._OutageRecord = None
        self.OutageRecord = OutageRecord

        self._OutageCodes = []
        self.OutageCodes = [] if OutageCodes is None else OutageCodes

        super(OutageStep, self).__init__(*args, **kw_args)

    _attrs = ["averageCml", "damage", "specialCustomerCount", "criticalCustomerCount", "estimatedRestoreDateTime", "shockReported", "callerCount", "fatality", "jobPriority", "totalCustomerCount", "injury", "totalCml"]
    _attr_types = {"averageCml": float, "damage": bool, "specialCustomerCount": int, "criticalCustomerCount": int, "estimatedRestoreDateTime": str, "shockReported": bool, "callerCount": int, "fatality": bool, "jobPriority": str, "totalCustomerCount": int, "injury": bool, "totalCml": float}
    _defaults = {"averageCml": 0.0, "damage": False, "specialCustomerCount": 0, "criticalCustomerCount": 0, "estimatedRestoreDateTime": '', "shockReported": False, "callerCount": 0, "fatality": False, "jobPriority": '', "totalCustomerCount": 0, "injury": False, "totalCml": 0.0}
    _enums = {}
    _refs = ["Crews", "noPowerInterval", "ConductingEquipmentRoles", "status", "OutageRecord", "OutageCodes"]
    _many_refs = ["Crews", "ConductingEquipmentRoles", "OutageCodes"]

    def getCrews(self):
        
        return self._Crews

    def setCrews(self, value):
        for p in self._Crews:
            filtered = [q for q in p.OutageSteps if q != self]
            self._Crews._OutageSteps = filtered
        for r in value:
            if self not in r._OutageSteps:
                r._OutageSteps.append(self)
        self._Crews = value

    Crews = property(getCrews, setCrews)

    def addCrews(self, *Crews):
        for obj in Crews:
            if self not in obj._OutageSteps:
                obj._OutageSteps.append(self)
            self._Crews.append(obj)

    def removeCrews(self, *Crews):
        for obj in Crews:
            if self in obj._OutageSteps:
                obj._OutageSteps.remove(self)
            self._Crews.remove(obj)

    # Date and time interval between loss and restoration of power.
    noPowerInterval = None

    def getConductingEquipmentRoles(self):
        
        return self._ConductingEquipmentRoles

    def setConductingEquipmentRoles(self, value):
        for x in self._ConductingEquipmentRoles:
            x.OutageStep = None
        for y in value:
            y._OutageStep = self
        self._ConductingEquipmentRoles = value

    ConductingEquipmentRoles = property(getConductingEquipmentRoles, setConductingEquipmentRoles)

    def addConductingEquipmentRoles(self, *ConductingEquipmentRoles):
        for obj in ConductingEquipmentRoles:
            obj.OutageStep = self

    def removeConductingEquipmentRoles(self, *ConductingEquipmentRoles):
        for obj in ConductingEquipmentRoles:
            obj.OutageStep = None

    status = None

    def getOutageRecord(self):
        
        return self._OutageRecord

    def setOutageRecord(self, value):
        if self._OutageRecord is not None:
            filtered = [x for x in self.OutageRecord.OutageSteps if x != self]
            self._OutageRecord._OutageSteps = filtered

        self._OutageRecord = value
        if self._OutageRecord is not None:
            if self not in self._OutageRecord._OutageSteps:
                self._OutageRecord._OutageSteps.append(self)

    OutageRecord = property(getOutageRecord, setOutageRecord)

    def getOutageCodes(self):
        """Multiple outage codes may apply to an outage step.
        """
        return self._OutageCodes

    def setOutageCodes(self, value):
        for p in self._OutageCodes:
            filtered = [q for q in p.OutageSteps if q != self]
            self._OutageCodes._OutageSteps = filtered
        for r in value:
            if self not in r._OutageSteps:
                r._OutageSteps.append(self)
        self._OutageCodes = value

    OutageCodes = property(getOutageCodes, setOutageCodes)

    def addOutageCodes(self, *OutageCodes):
        for obj in OutageCodes:
            if self not in obj._OutageSteps:
                obj._OutageSteps.append(self)
            self._OutageCodes.append(obj)

    def removeOutageCodes(self, *OutageCodes):
        for obj in OutageCodes:
            if self in obj._OutageSteps:
                obj._OutageSteps.remove(self)
            self._OutageCodes.remove(obj)

