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

from CIM14v13.IEC61968.Common.Document import Document

class WorkTask(Document):
    """A set of tasks is required to implement a design.
    """

    def __init__(self, schedOverride='', priority='', ContractorItems=None, Crews=None, WorkCostDetails=None, Usages=None, QualificationRequirements=None, Work=None, WorkFlowStep=None, LaborItems=None, MaterialItems=None, EquipmentItems=None, DesignLocationCUs=None, OverheadCost=None, Assets=None, Capabilities=None, MiscCostItems=None, SwitchingSchedules=None, Design=None, *args, **kw_args):
        """Initializes a new 'WorkTask' instance.

        @param schedOverride: If specified, override schedule and perform this task in accordance with instructions specified here. 
        @param priority: The priority of this work task. 
        @param ContractorItems:
        @param Crews: All Crews participating in this WorkTask.
        @param WorkCostDetails:
        @param Usages:
        @param QualificationRequirements:
        @param Work:
        @param WorkFlowStep:
        @param LaborItems:
        @param MaterialItems:
        @param EquipmentItems:
        @param DesignLocationCUs:
        @param OverheadCost:
        @param Assets:
        @param Capabilities:
        @param MiscCostItems:
        @param SwitchingSchedules:
        @param Design:
        """
        #: If specified, override schedule and perform this task in accordance with instructions specified here. 
        self.schedOverride = schedOverride

        #: The priority of this work task. 
        self.priority = priority

        self._ContractorItems = []
        self.ContractorItems = [] if ContractorItems is None else ContractorItems

        self._Crews = []
        self.Crews = [] if Crews is None else Crews

        self._WorkCostDetails = []
        self.WorkCostDetails = [] if WorkCostDetails is None else WorkCostDetails

        self._Usages = []
        self.Usages = [] if Usages is None else Usages

        self._QualificationRequirements = []
        self.QualificationRequirements = [] if QualificationRequirements is None else QualificationRequirements

        self._Work = None
        self.Work = Work

        self._WorkFlowStep = None
        self.WorkFlowStep = WorkFlowStep

        self._LaborItems = []
        self.LaborItems = [] if LaborItems is None else LaborItems

        self._MaterialItems = []
        self.MaterialItems = [] if MaterialItems is None else MaterialItems

        self._EquipmentItems = []
        self.EquipmentItems = [] if EquipmentItems is None else EquipmentItems

        self._DesignLocationCUs = []
        self.DesignLocationCUs = [] if DesignLocationCUs is None else DesignLocationCUs

        self._OverheadCost = None
        self.OverheadCost = OverheadCost

        self._Assets = []
        self.Assets = [] if Assets is None else Assets

        self._Capabilities = []
        self.Capabilities = [] if Capabilities is None else Capabilities

        self._MiscCostItems = []
        self.MiscCostItems = [] if MiscCostItems is None else MiscCostItems

        self._SwitchingSchedules = []
        self.SwitchingSchedules = [] if SwitchingSchedules is None else SwitchingSchedules

        self._Design = None
        self.Design = Design

        super(WorkTask, self).__init__(*args, **kw_args)

    def getContractorItems(self):
        
        return self._ContractorItems

    def setContractorItems(self, value):
        for x in self._ContractorItems:
            x._WorkTask = None
        for y in value:
            y._WorkTask = self
        self._ContractorItems = value

    ContractorItems = property(getContractorItems, setContractorItems)

    def addContractorItems(self, *ContractorItems):
        for obj in ContractorItems:
            obj._WorkTask = self
            self._ContractorItems.append(obj)

    def removeContractorItems(self, *ContractorItems):
        for obj in ContractorItems:
            obj._WorkTask = None
            self._ContractorItems.remove(obj)

    def getCrews(self):
        """All Crews participating in this WorkTask.
        """
        return self._Crews

    def setCrews(self, value):
        for p in self._Crews:
            filtered = [q for q in p.WorkTasks if q != self]
            self._Crews._WorkTasks = filtered
        for r in value:
            if self not in r._WorkTasks:
                r._WorkTasks.append(self)
        self._Crews = value

    Crews = property(getCrews, setCrews)

    def addCrews(self, *Crews):
        for obj in Crews:
            if self not in obj._WorkTasks:
                obj._WorkTasks.append(self)
            self._Crews.append(obj)

    def removeCrews(self, *Crews):
        for obj in Crews:
            if self in obj._WorkTasks:
                obj._WorkTasks.remove(self)
            self._Crews.remove(obj)

    def getWorkCostDetails(self):
        
        return self._WorkCostDetails

    def setWorkCostDetails(self, value):
        for x in self._WorkCostDetails:
            x._WorkTask = None
        for y in value:
            y._WorkTask = self
        self._WorkCostDetails = value

    WorkCostDetails = property(getWorkCostDetails, setWorkCostDetails)

    def addWorkCostDetails(self, *WorkCostDetails):
        for obj in WorkCostDetails:
            obj._WorkTask = self
            self._WorkCostDetails.append(obj)

    def removeWorkCostDetails(self, *WorkCostDetails):
        for obj in WorkCostDetails:
            obj._WorkTask = None
            self._WorkCostDetails.remove(obj)

    def getUsages(self):
        
        return self._Usages

    def setUsages(self, value):
        for x in self._Usages:
            x._WorkTask = None
        for y in value:
            y._WorkTask = self
        self._Usages = value

    Usages = property(getUsages, setUsages)

    def addUsages(self, *Usages):
        for obj in Usages:
            obj._WorkTask = self
            self._Usages.append(obj)

    def removeUsages(self, *Usages):
        for obj in Usages:
            obj._WorkTask = None
            self._Usages.remove(obj)

    def getQualificationRequirements(self):
        
        return self._QualificationRequirements

    def setQualificationRequirements(self, value):
        for p in self._QualificationRequirements:
            filtered = [q for q in p.WorkTasks if q != self]
            self._QualificationRequirements._WorkTasks = filtered
        for r in value:
            if self not in r._WorkTasks:
                r._WorkTasks.append(self)
        self._QualificationRequirements = value

    QualificationRequirements = property(getQualificationRequirements, setQualificationRequirements)

    def addQualificationRequirements(self, *QualificationRequirements):
        for obj in QualificationRequirements:
            if self not in obj._WorkTasks:
                obj._WorkTasks.append(self)
            self._QualificationRequirements.append(obj)

    def removeQualificationRequirements(self, *QualificationRequirements):
        for obj in QualificationRequirements:
            if self in obj._WorkTasks:
                obj._WorkTasks.remove(self)
            self._QualificationRequirements.remove(obj)

    def getWork(self):
        
        return self._Work

    def setWork(self, value):
        if self._Work is not None:
            filtered = [x for x in self.Work.WorkTasks if x != self]
            self._Work._WorkTasks = filtered

        self._Work = value
        if self._Work is not None:
            self._Work._WorkTasks.append(self)

    Work = property(getWork, setWork)

    def getWorkFlowStep(self):
        
        return self._WorkFlowStep

    def setWorkFlowStep(self, value):
        if self._WorkFlowStep is not None:
            filtered = [x for x in self.WorkFlowStep.WorkTasks if x != self]
            self._WorkFlowStep._WorkTasks = filtered

        self._WorkFlowStep = value
        if self._WorkFlowStep is not None:
            self._WorkFlowStep._WorkTasks.append(self)

    WorkFlowStep = property(getWorkFlowStep, setWorkFlowStep)

    def getLaborItems(self):
        
        return self._LaborItems

    def setLaborItems(self, value):
        for x in self._LaborItems:
            x._WorkTask = None
        for y in value:
            y._WorkTask = self
        self._LaborItems = value

    LaborItems = property(getLaborItems, setLaborItems)

    def addLaborItems(self, *LaborItems):
        for obj in LaborItems:
            obj._WorkTask = self
            self._LaborItems.append(obj)

    def removeLaborItems(self, *LaborItems):
        for obj in LaborItems:
            obj._WorkTask = None
            self._LaborItems.remove(obj)

    def getMaterialItems(self):
        
        return self._MaterialItems

    def setMaterialItems(self, value):
        for x in self._MaterialItems:
            x._WorkTask = None
        for y in value:
            y._WorkTask = self
        self._MaterialItems = value

    MaterialItems = property(getMaterialItems, setMaterialItems)

    def addMaterialItems(self, *MaterialItems):
        for obj in MaterialItems:
            obj._WorkTask = self
            self._MaterialItems.append(obj)

    def removeMaterialItems(self, *MaterialItems):
        for obj in MaterialItems:
            obj._WorkTask = None
            self._MaterialItems.remove(obj)

    def getEquipmentItems(self):
        
        return self._EquipmentItems

    def setEquipmentItems(self, value):
        for x in self._EquipmentItems:
            x._WorkTask = None
        for y in value:
            y._WorkTask = self
        self._EquipmentItems = value

    EquipmentItems = property(getEquipmentItems, setEquipmentItems)

    def addEquipmentItems(self, *EquipmentItems):
        for obj in EquipmentItems:
            obj._WorkTask = self
            self._EquipmentItems.append(obj)

    def removeEquipmentItems(self, *EquipmentItems):
        for obj in EquipmentItems:
            obj._WorkTask = None
            self._EquipmentItems.remove(obj)

    def getDesignLocationCUs(self):
        
        return self._DesignLocationCUs

    def setDesignLocationCUs(self, value):
        for p in self._DesignLocationCUs:
            filtered = [q for q in p.WorkTasks if q != self]
            self._DesignLocationCUs._WorkTasks = filtered
        for r in value:
            if self not in r._WorkTasks:
                r._WorkTasks.append(self)
        self._DesignLocationCUs = value

    DesignLocationCUs = property(getDesignLocationCUs, setDesignLocationCUs)

    def addDesignLocationCUs(self, *DesignLocationCUs):
        for obj in DesignLocationCUs:
            if self not in obj._WorkTasks:
                obj._WorkTasks.append(self)
            self._DesignLocationCUs.append(obj)

    def removeDesignLocationCUs(self, *DesignLocationCUs):
        for obj in DesignLocationCUs:
            if self in obj._WorkTasks:
                obj._WorkTasks.remove(self)
            self._DesignLocationCUs.remove(obj)

    def getOverheadCost(self):
        
        return self._OverheadCost

    def setOverheadCost(self, value):
        if self._OverheadCost is not None:
            filtered = [x for x in self.OverheadCost.WorkTasks if x != self]
            self._OverheadCost._WorkTasks = filtered

        self._OverheadCost = value
        if self._OverheadCost is not None:
            self._OverheadCost._WorkTasks.append(self)

    OverheadCost = property(getOverheadCost, setOverheadCost)

    def getAssets(self):
        
        return self._Assets

    def setAssets(self, value):
        for x in self._Assets:
            x._WorkTask = None
        for y in value:
            y._WorkTask = self
        self._Assets = value

    Assets = property(getAssets, setAssets)

    def addAssets(self, *Assets):
        for obj in Assets:
            obj._WorkTask = self
            self._Assets.append(obj)

    def removeAssets(self, *Assets):
        for obj in Assets:
            obj._WorkTask = None
            self._Assets.remove(obj)

    def getCapabilities(self):
        
        return self._Capabilities

    def setCapabilities(self, value):
        for p in self._Capabilities:
            filtered = [q for q in p.WorkTasks if q != self]
            self._Capabilities._WorkTasks = filtered
        for r in value:
            if self not in r._WorkTasks:
                r._WorkTasks.append(self)
        self._Capabilities = value

    Capabilities = property(getCapabilities, setCapabilities)

    def addCapabilities(self, *Capabilities):
        for obj in Capabilities:
            if self not in obj._WorkTasks:
                obj._WorkTasks.append(self)
            self._Capabilities.append(obj)

    def removeCapabilities(self, *Capabilities):
        for obj in Capabilities:
            if self in obj._WorkTasks:
                obj._WorkTasks.remove(self)
            self._Capabilities.remove(obj)

    def getMiscCostItems(self):
        
        return self._MiscCostItems

    def setMiscCostItems(self, value):
        for x in self._MiscCostItems:
            x._WorkTask = None
        for y in value:
            y._WorkTask = self
        self._MiscCostItems = value

    MiscCostItems = property(getMiscCostItems, setMiscCostItems)

    def addMiscCostItems(self, *MiscCostItems):
        for obj in MiscCostItems:
            obj._WorkTask = self
            self._MiscCostItems.append(obj)

    def removeMiscCostItems(self, *MiscCostItems):
        for obj in MiscCostItems:
            obj._WorkTask = None
            self._MiscCostItems.remove(obj)

    def getSwitchingSchedules(self):
        
        return self._SwitchingSchedules

    def setSwitchingSchedules(self, value):
        for x in self._SwitchingSchedules:
            x._WorkTask = None
        for y in value:
            y._WorkTask = self
        self._SwitchingSchedules = value

    SwitchingSchedules = property(getSwitchingSchedules, setSwitchingSchedules)

    def addSwitchingSchedules(self, *SwitchingSchedules):
        for obj in SwitchingSchedules:
            obj._WorkTask = self
            self._SwitchingSchedules.append(obj)

    def removeSwitchingSchedules(self, *SwitchingSchedules):
        for obj in SwitchingSchedules:
            obj._WorkTask = None
            self._SwitchingSchedules.remove(obj)

    def getDesign(self):
        
        return self._Design

    def setDesign(self, value):
        if self._Design is not None:
            filtered = [x for x in self.Design.WorkTasks if x != self]
            self._Design._WorkTasks = filtered

        self._Design = value
        if self._Design is not None:
            self._Design._WorkTasks.append(self)

    Design = property(getDesign, setDesign)

