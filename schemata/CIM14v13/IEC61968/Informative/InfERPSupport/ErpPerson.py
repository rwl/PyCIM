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

class ErpPerson(IdentifiedObject):
    """General purpose information for name and other information to contact people.
    """

    def __init__(self, prefix='', governmentID='', lastName='', category='', firstName='', suffix='', specialNeed='', mName='', ErpTelephoneNumbers=None, DocumentRoles=None, ElectronicAddresses=None, Crews=None, Appointments=None, LaborItems=None, MeasurementValues=None, CallBacks=None, ActivityRecords=None, ErpOrganisationRoles=None, Crafts=None, LocationRoles=None, Skills=None, CustomerData=None, ChangeItems=None, SwitchingStepRoles=None, ErpPersonnel=None, ErpCompetency=None, LandPropertyRoles=None, status=None, *args, **kw_args):
        """Initializes a new 'ErpPerson' instance.

        @param prefix: A prefix or title for the person's name, such as Miss, Mister, Doctor, etc. 
        @param governmentID: Unique identifier for person relative to its governing authority, for example a federal tax identifier (such as a Social Security number in the United States). 
        @param lastName: Person's last (family, sir) name. 
        @param category: Category of this person relative to utility operations, classified according to the utility's corporate standards and practices. Examples include employee, contractor, agent, not affiliated, etc. Note that this field is not used to indicate whether this person is a customer of the utility. Often an employee or contractor is also a customer. Customer information is gained with relationship to Organisation and CustomerData. In similar fashion, this field does not indicate the various roles this person may fill as part of utility operations. 
        @param firstName: Person's first name. 
        @param suffix: A suffix for the person's name, such as II, III, etc. 
        @param specialNeed: Special service needs for the person (contact) are described; examples include life support, etc. 
        @param mName: Middle name(s) or initial(s). 
        @param ErpTelephoneNumbers:
        @param DocumentRoles:
        @param ElectronicAddresses:
        @param Crews: All Crews to which this ErpPerson belongs.
        @param Appointments:
        @param LaborItems:
        @param MeasurementValues:
        @param CallBacks:
        @param ActivityRecords:
        @param ErpOrganisationRoles:
        @param Crafts:
        @param LocationRoles:
        @param Skills:
        @param CustomerData:
        @param ChangeItems:
        @param SwitchingStepRoles:
        @param ErpPersonnel:
        @param ErpCompetency:
        @param LandPropertyRoles:
        @param status:
        """
        #: A prefix or title for the person's name, such as Miss, Mister, Doctor, etc. 
        self.prefix = prefix

        #: Unique identifier for person relative to its governing authority, for example a federal tax identifier (such as a Social Security number in the United States). 
        self.governmentID = governmentID

        #: Person's last (family, sir) name. 
        self.lastName = lastName

        #: Category of this person relative to utility operations, classified according to the utility's corporate standards and practices. Examples include employee, contractor, agent, not affiliated, etc. Note that this field is not used to indicate whether this person is a customer of the utility. Often an employee or contractor is also a customer. Customer information is gained with relationship to Organisation and CustomerData. In similar fashion, this field does not indicate the various roles this person may fill as part of utility operations. 
        self.category = category

        #: Person's first name. 
        self.firstName = firstName

        #: A suffix for the person's name, such as II, III, etc. 
        self.suffix = suffix

        #: Special service needs for the person (contact) are described; examples include life support, etc. 
        self.specialNeed = specialNeed

        #: Middle name(s) or initial(s). 
        self.mName = mName

        self._ErpTelephoneNumbers = []
        self.ErpTelephoneNumbers = [] if ErpTelephoneNumbers is None else ErpTelephoneNumbers

        self._DocumentRoles = []
        self.DocumentRoles = [] if DocumentRoles is None else DocumentRoles

        self._ElectronicAddresses = []
        self.ElectronicAddresses = [] if ElectronicAddresses is None else ElectronicAddresses

        self._Crews = []
        self.Crews = [] if Crews is None else Crews

        self._Appointments = []
        self.Appointments = [] if Appointments is None else Appointments

        self._LaborItems = []
        self.LaborItems = [] if LaborItems is None else LaborItems

        self._MeasurementValues = []
        self.MeasurementValues = [] if MeasurementValues is None else MeasurementValues

        self._CallBacks = []
        self.CallBacks = [] if CallBacks is None else CallBacks

        self._ActivityRecords = []
        self.ActivityRecords = [] if ActivityRecords is None else ActivityRecords

        self._ErpOrganisationRoles = []
        self.ErpOrganisationRoles = [] if ErpOrganisationRoles is None else ErpOrganisationRoles

        self._Crafts = []
        self.Crafts = [] if Crafts is None else Crafts

        self._LocationRoles = []
        self.LocationRoles = [] if LocationRoles is None else LocationRoles

        self._Skills = []
        self.Skills = [] if Skills is None else Skills

        self._CustomerData = None
        self.CustomerData = CustomerData

        self._ChangeItems = []
        self.ChangeItems = [] if ChangeItems is None else ChangeItems

        self._SwitchingStepRoles = []
        self.SwitchingStepRoles = [] if SwitchingStepRoles is None else SwitchingStepRoles

        self._ErpPersonnel = None
        self.ErpPersonnel = ErpPersonnel

        self._ErpCompetency = None
        self.ErpCompetency = ErpCompetency

        self._LandPropertyRoles = []
        self.LandPropertyRoles = [] if LandPropertyRoles is None else LandPropertyRoles

        self.status = status

        super(ErpPerson, self).__init__(*args, **kw_args)

    def getErpTelephoneNumbers(self):
        
        return self._ErpTelephoneNumbers

    def setErpTelephoneNumbers(self, value):
        for p in self._ErpTelephoneNumbers:
            filtered = [q for q in p.ErpPersons if q != self]
            self._ErpTelephoneNumbers._ErpPersons = filtered
        for r in value:
            if self not in r._ErpPersons:
                r._ErpPersons.append(self)
        self._ErpTelephoneNumbers = value

    ErpTelephoneNumbers = property(getErpTelephoneNumbers, setErpTelephoneNumbers)

    def addErpTelephoneNumbers(self, *ErpTelephoneNumbers):
        for obj in ErpTelephoneNumbers:
            if self not in obj._ErpPersons:
                obj._ErpPersons.append(self)
            self._ErpTelephoneNumbers.append(obj)

    def removeErpTelephoneNumbers(self, *ErpTelephoneNumbers):
        for obj in ErpTelephoneNumbers:
            if self in obj._ErpPersons:
                obj._ErpPersons.remove(self)
            self._ErpTelephoneNumbers.remove(obj)

    def getDocumentRoles(self):
        
        return self._DocumentRoles

    def setDocumentRoles(self, value):
        for x in self._DocumentRoles:
            x._ErpPerson = None
        for y in value:
            y._ErpPerson = self
        self._DocumentRoles = value

    DocumentRoles = property(getDocumentRoles, setDocumentRoles)

    def addDocumentRoles(self, *DocumentRoles):
        for obj in DocumentRoles:
            obj._ErpPerson = self
            self._DocumentRoles.append(obj)

    def removeDocumentRoles(self, *DocumentRoles):
        for obj in DocumentRoles:
            obj._ErpPerson = None
            self._DocumentRoles.remove(obj)

    def getElectronicAddresses(self):
        
        return self._ElectronicAddresses

    def setElectronicAddresses(self, value):
        for x in self._ElectronicAddresses:
            x._ErpPerson = None
        for y in value:
            y._ErpPerson = self
        self._ElectronicAddresses = value

    ElectronicAddresses = property(getElectronicAddresses, setElectronicAddresses)

    def addElectronicAddresses(self, *ElectronicAddresses):
        for obj in ElectronicAddresses:
            obj._ErpPerson = self
            self._ElectronicAddresses.append(obj)

    def removeElectronicAddresses(self, *ElectronicAddresses):
        for obj in ElectronicAddresses:
            obj._ErpPerson = None
            self._ElectronicAddresses.remove(obj)

    def getCrews(self):
        """All Crews to which this ErpPerson belongs.
        """
        return self._Crews

    def setCrews(self, value):
        for p in self._Crews:
            filtered = [q for q in p.CrewMembers if q != self]
            self._Crews._CrewMembers = filtered
        for r in value:
            if self not in r._CrewMembers:
                r._CrewMembers.append(self)
        self._Crews = value

    Crews = property(getCrews, setCrews)

    def addCrews(self, *Crews):
        for obj in Crews:
            if self not in obj._CrewMembers:
                obj._CrewMembers.append(self)
            self._Crews.append(obj)

    def removeCrews(self, *Crews):
        for obj in Crews:
            if self in obj._CrewMembers:
                obj._CrewMembers.remove(self)
            self._Crews.remove(obj)

    def getAppointments(self):
        
        return self._Appointments

    def setAppointments(self, value):
        for p in self._Appointments:
            filtered = [q for q in p.ErpPersons if q != self]
            self._Appointments._ErpPersons = filtered
        for r in value:
            if self not in r._ErpPersons:
                r._ErpPersons.append(self)
        self._Appointments = value

    Appointments = property(getAppointments, setAppointments)

    def addAppointments(self, *Appointments):
        for obj in Appointments:
            if self not in obj._ErpPersons:
                obj._ErpPersons.append(self)
            self._Appointments.append(obj)

    def removeAppointments(self, *Appointments):
        for obj in Appointments:
            if self in obj._ErpPersons:
                obj._ErpPersons.remove(self)
            self._Appointments.remove(obj)

    def getLaborItems(self):
        
        return self._LaborItems

    def setLaborItems(self, value):
        for p in self._LaborItems:
            filtered = [q for q in p.ErpPersons if q != self]
            self._LaborItems._ErpPersons = filtered
        for r in value:
            if self not in r._ErpPersons:
                r._ErpPersons.append(self)
        self._LaborItems = value

    LaborItems = property(getLaborItems, setLaborItems)

    def addLaborItems(self, *LaborItems):
        for obj in LaborItems:
            if self not in obj._ErpPersons:
                obj._ErpPersons.append(self)
            self._LaborItems.append(obj)

    def removeLaborItems(self, *LaborItems):
        for obj in LaborItems:
            if self in obj._ErpPersons:
                obj._ErpPersons.remove(self)
            self._LaborItems.remove(obj)

    def getMeasurementValues(self):
        
        return self._MeasurementValues

    def setMeasurementValues(self, value):
        for x in self._MeasurementValues:
            x._ErpPerson = None
        for y in value:
            y._ErpPerson = self
        self._MeasurementValues = value

    MeasurementValues = property(getMeasurementValues, setMeasurementValues)

    def addMeasurementValues(self, *MeasurementValues):
        for obj in MeasurementValues:
            obj._ErpPerson = self
            self._MeasurementValues.append(obj)

    def removeMeasurementValues(self, *MeasurementValues):
        for obj in MeasurementValues:
            obj._ErpPerson = None
            self._MeasurementValues.remove(obj)

    def getCallBacks(self):
        
        return self._CallBacks

    def setCallBacks(self, value):
        for p in self._CallBacks:
            filtered = [q for q in p.ErpPersons if q != self]
            self._CallBacks._ErpPersons = filtered
        for r in value:
            if self not in r._ErpPersons:
                r._ErpPersons.append(self)
        self._CallBacks = value

    CallBacks = property(getCallBacks, setCallBacks)

    def addCallBacks(self, *CallBacks):
        for obj in CallBacks:
            if self not in obj._ErpPersons:
                obj._ErpPersons.append(self)
            self._CallBacks.append(obj)

    def removeCallBacks(self, *CallBacks):
        for obj in CallBacks:
            if self in obj._ErpPersons:
                obj._ErpPersons.remove(self)
            self._CallBacks.remove(obj)

    def getActivityRecords(self):
        
        return self._ActivityRecords

    def setActivityRecords(self, value):
        for p in self._ActivityRecords:
            filtered = [q for q in p.ErpPersons if q != self]
            self._ActivityRecords._ErpPersons = filtered
        for r in value:
            if self not in r._ErpPersons:
                r._ErpPersons.append(self)
        self._ActivityRecords = value

    ActivityRecords = property(getActivityRecords, setActivityRecords)

    def addActivityRecords(self, *ActivityRecords):
        for obj in ActivityRecords:
            if self not in obj._ErpPersons:
                obj._ErpPersons.append(self)
            self._ActivityRecords.append(obj)

    def removeActivityRecords(self, *ActivityRecords):
        for obj in ActivityRecords:
            if self in obj._ErpPersons:
                obj._ErpPersons.remove(self)
            self._ActivityRecords.remove(obj)

    def getErpOrganisationRoles(self):
        
        return self._ErpOrganisationRoles

    def setErpOrganisationRoles(self, value):
        for x in self._ErpOrganisationRoles:
            x._ErpPerson = None
        for y in value:
            y._ErpPerson = self
        self._ErpOrganisationRoles = value

    ErpOrganisationRoles = property(getErpOrganisationRoles, setErpOrganisationRoles)

    def addErpOrganisationRoles(self, *ErpOrganisationRoles):
        for obj in ErpOrganisationRoles:
            obj._ErpPerson = self
            self._ErpOrganisationRoles.append(obj)

    def removeErpOrganisationRoles(self, *ErpOrganisationRoles):
        for obj in ErpOrganisationRoles:
            obj._ErpPerson = None
            self._ErpOrganisationRoles.remove(obj)

    def getCrafts(self):
        
        return self._Crafts

    def setCrafts(self, value):
        for p in self._Crafts:
            filtered = [q for q in p.ErpPersons if q != self]
            self._Crafts._ErpPersons = filtered
        for r in value:
            if self not in r._ErpPersons:
                r._ErpPersons.append(self)
        self._Crafts = value

    Crafts = property(getCrafts, setCrafts)

    def addCrafts(self, *Crafts):
        for obj in Crafts:
            if self not in obj._ErpPersons:
                obj._ErpPersons.append(self)
            self._Crafts.append(obj)

    def removeCrafts(self, *Crafts):
        for obj in Crafts:
            if self in obj._ErpPersons:
                obj._ErpPersons.remove(self)
            self._Crafts.remove(obj)

    def getLocationRoles(self):
        
        return self._LocationRoles

    def setLocationRoles(self, value):
        for x in self._LocationRoles:
            x._ErpPerson = None
        for y in value:
            y._ErpPerson = self
        self._LocationRoles = value

    LocationRoles = property(getLocationRoles, setLocationRoles)

    def addLocationRoles(self, *LocationRoles):
        for obj in LocationRoles:
            obj._ErpPerson = self
            self._LocationRoles.append(obj)

    def removeLocationRoles(self, *LocationRoles):
        for obj in LocationRoles:
            obj._ErpPerson = None
            self._LocationRoles.remove(obj)

    def getSkills(self):
        
        return self._Skills

    def setSkills(self, value):
        for x in self._Skills:
            x._ErpPerson = None
        for y in value:
            y._ErpPerson = self
        self._Skills = value

    Skills = property(getSkills, setSkills)

    def addSkills(self, *Skills):
        for obj in Skills:
            obj._ErpPerson = self
            self._Skills.append(obj)

    def removeSkills(self, *Skills):
        for obj in Skills:
            obj._ErpPerson = None
            self._Skills.remove(obj)

    def getCustomerData(self):
        
        return self._CustomerData

    def setCustomerData(self, value):
        if self._CustomerData is not None:
            filtered = [x for x in self.CustomerData.ErpPersons if x != self]
            self._CustomerData._ErpPersons = filtered

        self._CustomerData = value
        if self._CustomerData is not None:
            self._CustomerData._ErpPersons.append(self)

    CustomerData = property(getCustomerData, setCustomerData)

    def getChangeItems(self):
        
        return self._ChangeItems

    def setChangeItems(self, value):
        for x in self._ChangeItems:
            x._ErpPerson = None
        for y in value:
            y._ErpPerson = self
        self._ChangeItems = value

    ChangeItems = property(getChangeItems, setChangeItems)

    def addChangeItems(self, *ChangeItems):
        for obj in ChangeItems:
            obj._ErpPerson = self
            self._ChangeItems.append(obj)

    def removeChangeItems(self, *ChangeItems):
        for obj in ChangeItems:
            obj._ErpPerson = None
            self._ChangeItems.remove(obj)

    def getSwitchingStepRoles(self):
        
        return self._SwitchingStepRoles

    def setSwitchingStepRoles(self, value):
        for x in self._SwitchingStepRoles:
            x._ErpPerson = None
        for y in value:
            y._ErpPerson = self
        self._SwitchingStepRoles = value

    SwitchingStepRoles = property(getSwitchingStepRoles, setSwitchingStepRoles)

    def addSwitchingStepRoles(self, *SwitchingStepRoles):
        for obj in SwitchingStepRoles:
            obj._ErpPerson = self
            self._SwitchingStepRoles.append(obj)

    def removeSwitchingStepRoles(self, *SwitchingStepRoles):
        for obj in SwitchingStepRoles:
            obj._ErpPerson = None
            self._SwitchingStepRoles.remove(obj)

    def getErpPersonnel(self):
        
        return self._ErpPersonnel

    def setErpPersonnel(self, value):
        if self._ErpPersonnel is not None:
            filtered = [x for x in self.ErpPersonnel.ErpPersons if x != self]
            self._ErpPersonnel._ErpPersons = filtered

        self._ErpPersonnel = value
        if self._ErpPersonnel is not None:
            self._ErpPersonnel._ErpPersons.append(self)

    ErpPersonnel = property(getErpPersonnel, setErpPersonnel)

    def getErpCompetency(self):
        
        return self._ErpCompetency

    def setErpCompetency(self, value):
        if self._ErpCompetency is not None:
            filtered = [x for x in self.ErpCompetency.ErpPersons if x != self]
            self._ErpCompetency._ErpPersons = filtered

        self._ErpCompetency = value
        if self._ErpCompetency is not None:
            self._ErpCompetency._ErpPersons.append(self)

    ErpCompetency = property(getErpCompetency, setErpCompetency)

    def getLandPropertyRoles(self):
        
        return self._LandPropertyRoles

    def setLandPropertyRoles(self, value):
        for x in self._LandPropertyRoles:
            x._ErpPerson = None
        for y in value:
            y._ErpPerson = self
        self._LandPropertyRoles = value

    LandPropertyRoles = property(getLandPropertyRoles, setLandPropertyRoles)

    def addLandPropertyRoles(self, *LandPropertyRoles):
        for obj in LandPropertyRoles:
            obj._ErpPerson = self
            self._LandPropertyRoles.append(obj)

    def removeLandPropertyRoles(self, *LandPropertyRoles):
        for obj in LandPropertyRoles:
            obj._ErpPerson = None
            self._LandPropertyRoles.remove(obj)

    status = None

