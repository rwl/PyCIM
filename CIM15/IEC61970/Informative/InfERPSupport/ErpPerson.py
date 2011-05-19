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

class ErpPerson(IdentifiedObject):
    """General purpose information for name and other information to contact people.General purpose information for name and other information to contact people.
    """

    def __init__(self, category='', lastName='', firstName='', governmentID='', mName='', suffix='', specialNeed='', prefix='', ServiceLocation=None, ErpOrganisationRoles=None, Appointments=None, Crews=None, LaborItems=None, LandPropertyRoles=None, ActivityRecords=None, MeasurementValues=None, Skills=None, landlinePhone=None, mobilePhone=None, ChangeItems=None, status=None, DocumentRoles=None, ErpPersonnel=None, Crafts=None, CustomerData=None, CallBacks=None, SwitchingStepRoles=None, electronicAddress=None, ErpCompetency=None, *args, **kw_args):
        """Initialises a new 'ErpPerson' instance.

        @param category: Category of this person relative to utility operations, classified according to the utility's corporate standards and practices. Examples include employee, contractor, agent, not affiliated, etc. Note that this field is not used to indicate whether this person is a customer of the utility. Often an employee or contractor is also a customer. Customer information is gained with relationship to Organisation and CustomerData. In similar fashion, this field does not indicate the various roles this person may fill as part of utility operations. 
        @param lastName: Person's last (family, sir) name. 
        @param firstName: Person's first name. 
        @param governmentID: Unique identifier for person relative to its governing authority, for example a federal tax identifier (such as a Social Security number in the United States). 
        @param mName: Middle name(s) or initial(s). 
        @param suffix: A suffix for the person's name, such as II, III, etc. 
        @param specialNeed: Special service needs for the person (contact) are described; examples include life support, etc. 
        @param prefix: A prefix or title for the person's name, such as Miss, Mister, Doctor, etc. 
        @param ServiceLocation:
        @param ErpOrganisationRoles:
        @param Appointments:
        @param Crews: All Crews to which this ErpPerson belongs.
        @param LaborItems:
        @param LandPropertyRoles:
        @param ActivityRecords:
        @param MeasurementValues:
        @param Skills:
        @param landlinePhone: Landline phone number.
        @param mobilePhone: Mobile phone number.
        @param ChangeItems:
        @param status:
        @param DocumentRoles:
        @param ErpPersonnel:
        @param Crafts:
        @param CustomerData:
        @param CallBacks:
        @param SwitchingStepRoles:
        @param electronicAddress: Electronic address.
        @param ErpCompetency:
        """
        #: Category of this person relative to utility operations, classified according to the utility's corporate standards and practices. Examples include employee, contractor, agent, not affiliated, etc. Note that this field is not used to indicate whether this person is a customer of the utility. Often an employee or contractor is also a customer. Customer information is gained with relationship to Organisation and CustomerData. In similar fashion, this field does not indicate the various roles this person may fill as part of utility operations.
        self.category = category

        #: Person's last (family, sir) name.
        self.lastName = lastName

        #: Person's first name.
        self.firstName = firstName

        #: Unique identifier for person relative to its governing authority, for example a federal tax identifier (such as a Social Security number in the United States).
        self.governmentID = governmentID

        #: Middle name(s) or initial(s).
        self.mName = mName

        #: A suffix for the person's name, such as II, III, etc.
        self.suffix = suffix

        #: Special service needs for the person (contact) are described; examples include life support, etc.
        self.specialNeed = specialNeed

        #: A prefix or title for the person's name, such as Miss, Mister, Doctor, etc.
        self.prefix = prefix

        self._ServiceLocation = None
        self.ServiceLocation = ServiceLocation

        self._ErpOrganisationRoles = []
        self.ErpOrganisationRoles = [] if ErpOrganisationRoles is None else ErpOrganisationRoles

        self._Appointments = []
        self.Appointments = [] if Appointments is None else Appointments

        self._Crews = []
        self.Crews = [] if Crews is None else Crews

        self._LaborItems = []
        self.LaborItems = [] if LaborItems is None else LaborItems

        self._LandPropertyRoles = []
        self.LandPropertyRoles = [] if LandPropertyRoles is None else LandPropertyRoles

        self._ActivityRecords = []
        self.ActivityRecords = [] if ActivityRecords is None else ActivityRecords

        self._MeasurementValues = []
        self.MeasurementValues = [] if MeasurementValues is None else MeasurementValues

        self._Skills = []
        self.Skills = [] if Skills is None else Skills

        self.landlinePhone = landlinePhone

        self.mobilePhone = mobilePhone

        self._ChangeItems = []
        self.ChangeItems = [] if ChangeItems is None else ChangeItems

        self.status = status

        self._DocumentRoles = []
        self.DocumentRoles = [] if DocumentRoles is None else DocumentRoles

        self._ErpPersonnel = None
        self.ErpPersonnel = ErpPersonnel

        self._Crafts = []
        self.Crafts = [] if Crafts is None else Crafts

        self._CustomerData = None
        self.CustomerData = CustomerData

        self._CallBacks = []
        self.CallBacks = [] if CallBacks is None else CallBacks

        self._SwitchingStepRoles = []
        self.SwitchingStepRoles = [] if SwitchingStepRoles is None else SwitchingStepRoles

        self.electronicAddress = electronicAddress

        self._ErpCompetency = None
        self.ErpCompetency = ErpCompetency

        super(ErpPerson, self).__init__(*args, **kw_args)

    _attrs = ["category", "lastName", "firstName", "governmentID", "mName", "suffix", "specialNeed", "prefix"]
    _attr_types = {"category": str, "lastName": str, "firstName": str, "governmentID": str, "mName": str, "suffix": str, "specialNeed": str, "prefix": str}
    _defaults = {"category": '', "lastName": '', "firstName": '', "governmentID": '', "mName": '', "suffix": '', "specialNeed": '', "prefix": ''}
    _enums = {}
    _refs = ["ServiceLocation", "ErpOrganisationRoles", "Appointments", "Crews", "LaborItems", "LandPropertyRoles", "ActivityRecords", "MeasurementValues", "Skills", "landlinePhone", "mobilePhone", "ChangeItems", "status", "DocumentRoles", "ErpPersonnel", "Crafts", "CustomerData", "CallBacks", "SwitchingStepRoles", "electronicAddress", "ErpCompetency"]
    _many_refs = ["ErpOrganisationRoles", "Appointments", "Crews", "LaborItems", "LandPropertyRoles", "ActivityRecords", "MeasurementValues", "Skills", "ChangeItems", "DocumentRoles", "Crafts", "CallBacks", "SwitchingStepRoles"]

    def getServiceLocation(self):
        
        return self._ServiceLocation

    def setServiceLocation(self, value):
        if self._ServiceLocation is not None:
            filtered = [x for x in self.ServiceLocation.ErpPersons if x != self]
            self._ServiceLocation._ErpPersons = filtered

        self._ServiceLocation = value
        if self._ServiceLocation is not None:
            if self not in self._ServiceLocation._ErpPersons:
                self._ServiceLocation._ErpPersons.append(self)

    ServiceLocation = property(getServiceLocation, setServiceLocation)

    def getErpOrganisationRoles(self):
        
        return self._ErpOrganisationRoles

    def setErpOrganisationRoles(self, value):
        for x in self._ErpOrganisationRoles:
            x.ErpPerson = None
        for y in value:
            y._ErpPerson = self
        self._ErpOrganisationRoles = value

    ErpOrganisationRoles = property(getErpOrganisationRoles, setErpOrganisationRoles)

    def addErpOrganisationRoles(self, *ErpOrganisationRoles):
        for obj in ErpOrganisationRoles:
            obj.ErpPerson = self

    def removeErpOrganisationRoles(self, *ErpOrganisationRoles):
        for obj in ErpOrganisationRoles:
            obj.ErpPerson = None

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

    def getLandPropertyRoles(self):
        
        return self._LandPropertyRoles

    def setLandPropertyRoles(self, value):
        for x in self._LandPropertyRoles:
            x.ErpPerson = None
        for y in value:
            y._ErpPerson = self
        self._LandPropertyRoles = value

    LandPropertyRoles = property(getLandPropertyRoles, setLandPropertyRoles)

    def addLandPropertyRoles(self, *LandPropertyRoles):
        for obj in LandPropertyRoles:
            obj.ErpPerson = self

    def removeLandPropertyRoles(self, *LandPropertyRoles):
        for obj in LandPropertyRoles:
            obj.ErpPerson = None

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

    def getMeasurementValues(self):
        
        return self._MeasurementValues

    def setMeasurementValues(self, value):
        for x in self._MeasurementValues:
            x.ErpPerson = None
        for y in value:
            y._ErpPerson = self
        self._MeasurementValues = value

    MeasurementValues = property(getMeasurementValues, setMeasurementValues)

    def addMeasurementValues(self, *MeasurementValues):
        for obj in MeasurementValues:
            obj.ErpPerson = self

    def removeMeasurementValues(self, *MeasurementValues):
        for obj in MeasurementValues:
            obj.ErpPerson = None

    def getSkills(self):
        
        return self._Skills

    def setSkills(self, value):
        for x in self._Skills:
            x.ErpPerson = None
        for y in value:
            y._ErpPerson = self
        self._Skills = value

    Skills = property(getSkills, setSkills)

    def addSkills(self, *Skills):
        for obj in Skills:
            obj.ErpPerson = self

    def removeSkills(self, *Skills):
        for obj in Skills:
            obj.ErpPerson = None

    # Landline phone number.
    landlinePhone = None

    # Mobile phone number.
    mobilePhone = None

    def getChangeItems(self):
        
        return self._ChangeItems

    def setChangeItems(self, value):
        for x in self._ChangeItems:
            x.ErpPerson = None
        for y in value:
            y._ErpPerson = self
        self._ChangeItems = value

    ChangeItems = property(getChangeItems, setChangeItems)

    def addChangeItems(self, *ChangeItems):
        for obj in ChangeItems:
            obj.ErpPerson = self

    def removeChangeItems(self, *ChangeItems):
        for obj in ChangeItems:
            obj.ErpPerson = None

    status = None

    def getDocumentRoles(self):
        
        return self._DocumentRoles

    def setDocumentRoles(self, value):
        for x in self._DocumentRoles:
            x.ErpPerson = None
        for y in value:
            y._ErpPerson = self
        self._DocumentRoles = value

    DocumentRoles = property(getDocumentRoles, setDocumentRoles)

    def addDocumentRoles(self, *DocumentRoles):
        for obj in DocumentRoles:
            obj.ErpPerson = self

    def removeDocumentRoles(self, *DocumentRoles):
        for obj in DocumentRoles:
            obj.ErpPerson = None

    def getErpPersonnel(self):
        
        return self._ErpPersonnel

    def setErpPersonnel(self, value):
        if self._ErpPersonnel is not None:
            filtered = [x for x in self.ErpPersonnel.ErpPersons if x != self]
            self._ErpPersonnel._ErpPersons = filtered

        self._ErpPersonnel = value
        if self._ErpPersonnel is not None:
            if self not in self._ErpPersonnel._ErpPersons:
                self._ErpPersonnel._ErpPersons.append(self)

    ErpPersonnel = property(getErpPersonnel, setErpPersonnel)

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

    def getCustomerData(self):
        
        return self._CustomerData

    def setCustomerData(self, value):
        if self._CustomerData is not None:
            filtered = [x for x in self.CustomerData.ErpPersons if x != self]
            self._CustomerData._ErpPersons = filtered

        self._CustomerData = value
        if self._CustomerData is not None:
            if self not in self._CustomerData._ErpPersons:
                self._CustomerData._ErpPersons.append(self)

    CustomerData = property(getCustomerData, setCustomerData)

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

    def getSwitchingStepRoles(self):
        
        return self._SwitchingStepRoles

    def setSwitchingStepRoles(self, value):
        for x in self._SwitchingStepRoles:
            x.ErpPerson = None
        for y in value:
            y._ErpPerson = self
        self._SwitchingStepRoles = value

    SwitchingStepRoles = property(getSwitchingStepRoles, setSwitchingStepRoles)

    def addSwitchingStepRoles(self, *SwitchingStepRoles):
        for obj in SwitchingStepRoles:
            obj.ErpPerson = self

    def removeSwitchingStepRoles(self, *SwitchingStepRoles):
        for obj in SwitchingStepRoles:
            obj.ErpPerson = None

    # Electronic address.
    electronicAddress = None

    def getErpCompetency(self):
        
        return self._ErpCompetency

    def setErpCompetency(self, value):
        if self._ErpCompetency is not None:
            filtered = [x for x in self.ErpCompetency.ErpPersons if x != self]
            self._ErpCompetency._ErpPersons = filtered

        self._ErpCompetency = value
        if self._ErpCompetency is not None:
            if self not in self._ErpCompetency._ErpPersons:
                self._ErpCompetency._ErpPersons.append(self)

    ErpCompetency = property(getErpCompetency, setErpCompetency)

