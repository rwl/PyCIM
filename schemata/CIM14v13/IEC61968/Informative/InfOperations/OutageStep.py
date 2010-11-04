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

from CIM14v13.IEC61970.Core.IdentifiedObject import IdentifiedObject

class OutageStep(IdentifiedObject):
    """Holds an outage start and end time for each supply point of an outage record. The supply point for a given step is the associated PowerSystemResource instance.
    """

    def __init__(self, jobPriority='', totalCml=0.0, estimatedRestoreDateTime='', averageCml=0.0, shockReported=False, specialCustomerCount=0, callerCount=0, damage=False, criticalCustomerCount=0, fatality=False, totalCustomerCount=0, injury=False, Crews=None, OutageCodes=None, OutageRecord=None, status=None, noPowerInterval=None, ConductingEquipmentRoles=None, *args, **kw_args):
        """Initializes a new 'OutageStep' instance.

        @param jobPriority: 
        @param totalCml: Total Customer Minutes Lost (CML) for this supply point for this outage. 
        @param estimatedRestoreDateTime: Estimated time of restoration. 
        @param averageCml: Average Customer Minutes Lost (CML) for this supply point for this outage. 
        @param shockReported: True if shocks reported by caller or engineer. 
        @param specialCustomerCount: Number of customers with high reliability required. 
        @param callerCount: Number of customers phoning in. 
        @param damage: True if damage reported by caller or engineer. 
        @param criticalCustomerCount: Number of customers with critical needs, e.g., with a dialysis machine. 
        @param fatality: True if fatalities reported by caller or engineer. 
        @param totalCustomerCount: Number of customers connected to the PowerSystemResource. 
        @param injury: True if injuries reported by caller or engineer. 
        @param Crews:
        @param OutageCodes: Multiple outage codes may apply to an outage step.
        @param OutageRecord:
        @param status:
        @param noPowerInterval: Date and time interval between loss and restoration of power.
        @param ConductingEquipmentRoles:
        """

        self.jobPriority = jobPriority

        #: Total Customer Minutes Lost (CML) for this supply point for this outage.
        self.totalCml = totalCml

        #: Estimated time of restoration.
        self.estimatedRestoreDateTime = estimatedRestoreDateTime

        #: Average Customer Minutes Lost (CML) for this supply point for this outage.
        self.averageCml = averageCml

        #: True if shocks reported by caller or engineer.
        self.shockReported = shockReported

        #: Number of customers with high reliability required.
        self.specialCustomerCount = specialCustomerCount

        #: Number of customers phoning in.
        self.callerCount = callerCount

        #: True if damage reported by caller or engineer.
        self.damage = damage

        #: Number of customers with critical needs, e.g., with a dialysis machine.
        self.criticalCustomerCount = criticalCustomerCount

        #: True if fatalities reported by caller or engineer.
        self.fatality = fatality

        #: Number of customers connected to the PowerSystemResource.
        self.totalCustomerCount = totalCustomerCount

        #: True if injuries reported by caller or engineer.
        self.injury = injury

        self._Crews = []
        self.Crews = [] if Crews is None else Crews

        self._OutageCodes = []
        self.OutageCodes = [] if OutageCodes is None else OutageCodes

        self._OutageRecord = None
        self.OutageRecord = OutageRecord

        self.status = status

        self.noPowerInterval = noPowerInterval

        self._ConductingEquipmentRoles = []
        self.ConductingEquipmentRoles = [] if ConductingEquipmentRoles is None else ConductingEquipmentRoles

        super(OutageStep, self).__init__(*args, **kw_args)

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

    def getOutageRecord(self):
        
        return self._OutageRecord

    def setOutageRecord(self, value):
        if self._OutageRecord is not None:
            filtered = [x for x in self.OutageRecord.OutageSteps if x != self]
            self._OutageRecord._OutageSteps = filtered

        self._OutageRecord = value
        if self._OutageRecord is not None:
            self._OutageRecord._OutageSteps.append(self)

    OutageRecord = property(getOutageRecord, setOutageRecord)

    status = None

    # Date and time interval between loss and restoration of power.
    noPowerInterval = None

    def getConductingEquipmentRoles(self):
        
        return self._ConductingEquipmentRoles

    def setConductingEquipmentRoles(self, value):
        for x in self._ConductingEquipmentRoles:
            x._OutageStep = None
        for y in value:
            y._OutageStep = self
        self._ConductingEquipmentRoles = value

    ConductingEquipmentRoles = property(getConductingEquipmentRoles, setConductingEquipmentRoles)

    def addConductingEquipmentRoles(self, *ConductingEquipmentRoles):
        for obj in ConductingEquipmentRoles:
            obj._OutageStep = self
            self._ConductingEquipmentRoles.append(obj)

    def removeConductingEquipmentRoles(self, *ConductingEquipmentRoles):
        for obj in ConductingEquipmentRoles:
            obj._OutageStep = None
            self._ConductingEquipmentRoles.remove(obj)

