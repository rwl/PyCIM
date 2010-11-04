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

class Crew(IdentifiedObject):
    """A crew is a group of people (ErpPersons) with specific skills, tools, and vehicles.
    """

    def __init__(self, category='', Capabilities=None, WorkTasks=None, Vehicles=None, CrewMembers=None, Assignments=None, Tools=None, Route=None, OutageSteps=None, WorkEquipmentAssets=None, Locations=None, ShiftPatterns=None, SwitchingSchedules=None, Organisations=None, *args, **kw_args):
        """Initializes a new 'Crew' instance.

        @param category: Category by utility's work management standards and practices. 
        @param Capabilities:
        @param WorkTasks: All WorkTasks this Crew participates in.
        @param Vehicles:
        @param CrewMembers: All ErpPersons that are members of this Crew.
        @param Assignments: All Assignments for this Crew.
        @param Tools:
        @param Route:
        @param OutageSteps:
        @param WorkEquipmentAssets:
        @param Locations:
        @param ShiftPatterns:
        @param SwitchingSchedules: All SwitchingSchedules executed by this Crew.
        @param Organisations:
        """
        #: Category by utility's work management standards and practices.
        self.category = category

        self._Capabilities = []
        self.Capabilities = [] if Capabilities is None else Capabilities

        self._WorkTasks = []
        self.WorkTasks = [] if WorkTasks is None else WorkTasks

        self._Vehicles = []
        self.Vehicles = [] if Vehicles is None else Vehicles

        self._CrewMembers = []
        self.CrewMembers = [] if CrewMembers is None else CrewMembers

        self._Assignments = []
        self.Assignments = [] if Assignments is None else Assignments

        self._Tools = []
        self.Tools = [] if Tools is None else Tools

        self._Route = None
        self.Route = Route

        self._OutageSteps = []
        self.OutageSteps = [] if OutageSteps is None else OutageSteps

        self._WorkEquipmentAssets = []
        self.WorkEquipmentAssets = [] if WorkEquipmentAssets is None else WorkEquipmentAssets

        self._Locations = []
        self.Locations = [] if Locations is None else Locations

        self._ShiftPatterns = []
        self.ShiftPatterns = [] if ShiftPatterns is None else ShiftPatterns

        self._SwitchingSchedules = []
        self.SwitchingSchedules = [] if SwitchingSchedules is None else SwitchingSchedules

        self._Organisations = []
        self.Organisations = [] if Organisations is None else Organisations

        super(Crew, self).__init__(*args, **kw_args)

    def getCapabilities(self):
        
        return self._Capabilities

    def setCapabilities(self, value):
        for x in self._Capabilities:
            x._Crew = None
        for y in value:
            y._Crew = self
        self._Capabilities = value

    Capabilities = property(getCapabilities, setCapabilities)

    def addCapabilities(self, *Capabilities):
        for obj in Capabilities:
            obj._Crew = self
            self._Capabilities.append(obj)

    def removeCapabilities(self, *Capabilities):
        for obj in Capabilities:
            obj._Crew = None
            self._Capabilities.remove(obj)

    def getWorkTasks(self):
        """All WorkTasks this Crew participates in.
        """
        return self._WorkTasks

    def setWorkTasks(self, value):
        for p in self._WorkTasks:
            filtered = [q for q in p.Crews if q != self]
            self._WorkTasks._Crews = filtered
        for r in value:
            if self not in r._Crews:
                r._Crews.append(self)
        self._WorkTasks = value

    WorkTasks = property(getWorkTasks, setWorkTasks)

    def addWorkTasks(self, *WorkTasks):
        for obj in WorkTasks:
            if self not in obj._Crews:
                obj._Crews.append(self)
            self._WorkTasks.append(obj)

    def removeWorkTasks(self, *WorkTasks):
        for obj in WorkTasks:
            if self in obj._Crews:
                obj._Crews.remove(self)
            self._WorkTasks.remove(obj)

    def getVehicles(self):
        
        return self._Vehicles

    def setVehicles(self, value):
        for x in self._Vehicles:
            x._Crew = None
        for y in value:
            y._Crew = self
        self._Vehicles = value

    Vehicles = property(getVehicles, setVehicles)

    def addVehicles(self, *Vehicles):
        for obj in Vehicles:
            obj._Crew = self
            self._Vehicles.append(obj)

    def removeVehicles(self, *Vehicles):
        for obj in Vehicles:
            obj._Crew = None
            self._Vehicles.remove(obj)

    def getCrewMembers(self):
        """All ErpPersons that are members of this Crew.
        """
        return self._CrewMembers

    def setCrewMembers(self, value):
        for p in self._CrewMembers:
            filtered = [q for q in p.Crews if q != self]
            self._CrewMembers._Crews = filtered
        for r in value:
            if self not in r._Crews:
                r._Crews.append(self)
        self._CrewMembers = value

    CrewMembers = property(getCrewMembers, setCrewMembers)

    def addCrewMembers(self, *CrewMembers):
        for obj in CrewMembers:
            if self not in obj._Crews:
                obj._Crews.append(self)
            self._CrewMembers.append(obj)

    def removeCrewMembers(self, *CrewMembers):
        for obj in CrewMembers:
            if self in obj._Crews:
                obj._Crews.remove(self)
            self._CrewMembers.remove(obj)

    def getAssignments(self):
        """All Assignments for this Crew.
        """
        return self._Assignments

    def setAssignments(self, value):
        for p in self._Assignments:
            filtered = [q for q in p.Crews if q != self]
            self._Assignments._Crews = filtered
        for r in value:
            if self not in r._Crews:
                r._Crews.append(self)
        self._Assignments = value

    Assignments = property(getAssignments, setAssignments)

    def addAssignments(self, *Assignments):
        for obj in Assignments:
            if self not in obj._Crews:
                obj._Crews.append(self)
            self._Assignments.append(obj)

    def removeAssignments(self, *Assignments):
        for obj in Assignments:
            if self in obj._Crews:
                obj._Crews.remove(self)
            self._Assignments.remove(obj)

    def getTools(self):
        
        return self._Tools

    def setTools(self, value):
        for x in self._Tools:
            x._Crew = None
        for y in value:
            y._Crew = self
        self._Tools = value

    Tools = property(getTools, setTools)

    def addTools(self, *Tools):
        for obj in Tools:
            obj._Crew = self
            self._Tools.append(obj)

    def removeTools(self, *Tools):
        for obj in Tools:
            obj._Crew = None
            self._Tools.remove(obj)

    def getRoute(self):
        
        return self._Route

    def setRoute(self, value):
        if self._Route is not None:
            filtered = [x for x in self.Route.Crews if x != self]
            self._Route._Crews = filtered

        self._Route = value
        if self._Route is not None:
            self._Route._Crews.append(self)

    Route = property(getRoute, setRoute)

    def getOutageSteps(self):
        
        return self._OutageSteps

    def setOutageSteps(self, value):
        for p in self._OutageSteps:
            filtered = [q for q in p.Crews if q != self]
            self._OutageSteps._Crews = filtered
        for r in value:
            if self not in r._Crews:
                r._Crews.append(self)
        self._OutageSteps = value

    OutageSteps = property(getOutageSteps, setOutageSteps)

    def addOutageSteps(self, *OutageSteps):
        for obj in OutageSteps:
            if self not in obj._Crews:
                obj._Crews.append(self)
            self._OutageSteps.append(obj)

    def removeOutageSteps(self, *OutageSteps):
        for obj in OutageSteps:
            if self in obj._Crews:
                obj._Crews.remove(self)
            self._OutageSteps.remove(obj)

    def getWorkEquipmentAssets(self):
        
        return self._WorkEquipmentAssets

    def setWorkEquipmentAssets(self, value):
        for x in self._WorkEquipmentAssets:
            x._Crew = None
        for y in value:
            y._Crew = self
        self._WorkEquipmentAssets = value

    WorkEquipmentAssets = property(getWorkEquipmentAssets, setWorkEquipmentAssets)

    def addWorkEquipmentAssets(self, *WorkEquipmentAssets):
        for obj in WorkEquipmentAssets:
            obj._Crew = self
            self._WorkEquipmentAssets.append(obj)

    def removeWorkEquipmentAssets(self, *WorkEquipmentAssets):
        for obj in WorkEquipmentAssets:
            obj._Crew = None
            self._WorkEquipmentAssets.remove(obj)

    def getLocations(self):
        
        return self._Locations

    def setLocations(self, value):
        for p in self._Locations:
            filtered = [q for q in p.Crews if q != self]
            self._Locations._Crews = filtered
        for r in value:
            if self not in r._Crews:
                r._Crews.append(self)
        self._Locations = value

    Locations = property(getLocations, setLocations)

    def addLocations(self, *Locations):
        for obj in Locations:
            if self not in obj._Crews:
                obj._Crews.append(self)
            self._Locations.append(obj)

    def removeLocations(self, *Locations):
        for obj in Locations:
            if self in obj._Crews:
                obj._Crews.remove(self)
            self._Locations.remove(obj)

    def getShiftPatterns(self):
        
        return self._ShiftPatterns

    def setShiftPatterns(self, value):
        for p in self._ShiftPatterns:
            filtered = [q for q in p.Crews if q != self]
            self._ShiftPatterns._Crews = filtered
        for r in value:
            if self not in r._Crews:
                r._Crews.append(self)
        self._ShiftPatterns = value

    ShiftPatterns = property(getShiftPatterns, setShiftPatterns)

    def addShiftPatterns(self, *ShiftPatterns):
        for obj in ShiftPatterns:
            if self not in obj._Crews:
                obj._Crews.append(self)
            self._ShiftPatterns.append(obj)

    def removeShiftPatterns(self, *ShiftPatterns):
        for obj in ShiftPatterns:
            if self in obj._Crews:
                obj._Crews.remove(self)
            self._ShiftPatterns.remove(obj)

    def getSwitchingSchedules(self):
        """All SwitchingSchedules executed by this Crew.
        """
        return self._SwitchingSchedules

    def setSwitchingSchedules(self, value):
        for p in self._SwitchingSchedules:
            filtered = [q for q in p.Crews if q != self]
            self._SwitchingSchedules._Crews = filtered
        for r in value:
            if self not in r._Crews:
                r._Crews.append(self)
        self._SwitchingSchedules = value

    SwitchingSchedules = property(getSwitchingSchedules, setSwitchingSchedules)

    def addSwitchingSchedules(self, *SwitchingSchedules):
        for obj in SwitchingSchedules:
            if self not in obj._Crews:
                obj._Crews.append(self)
            self._SwitchingSchedules.append(obj)

    def removeSwitchingSchedules(self, *SwitchingSchedules):
        for obj in SwitchingSchedules:
            if self in obj._Crews:
                obj._Crews.remove(self)
            self._SwitchingSchedules.remove(obj)

    def getOrganisations(self):
        
        return self._Organisations

    def setOrganisations(self, value):
        for p in self._Organisations:
            filtered = [q for q in p.Crews if q != self]
            self._Organisations._Crews = filtered
        for r in value:
            if self not in r._Crews:
                r._Crews.append(self)
        self._Organisations = value

    Organisations = property(getOrganisations, setOrganisations)

    def addOrganisations(self, *Organisations):
        for obj in Organisations:
            if self not in obj._Crews:
                obj._Crews.append(self)
            self._Organisations.append(obj)

    def removeOrganisations(self, *Organisations):
        for obj in Organisations:
            if self in obj._Crews:
                obj._Crews.remove(self)
            self._Organisations.remove(obj)

