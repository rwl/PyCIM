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

from CIM15.IEC61968.Common.Document import Document

class WorkTask(Document):
    """A set of tasks is required to implement a design.A set of tasks is required to implement a design.
    """

    def __init__(self, priority='', schedOverride='', EquipmentItems=None, Usages=None, MiscCostItems=None, Crews=None, Work=None, OverheadCost=None, DesignLocationCUs=None, ContractorItems=None, SwitchingSchedules=None, WorkFlowStep=None, Design=None, QualificationRequirements=None, Capabilities=None, WorkCostDetails=None, Assets=None, LaborItems=None, MaterialItems=None, *args, **kw_args):
        """Initialises a new 'WorkTask' instance.

        @param priority: The priority of this work task. 
        @param schedOverride: If specified, override schedule and perform this task in accordance with instructions specified here. 
        @param EquipmentItems:
        @param Usages:
        @param MiscCostItems:
        @param Crews: All Crews participating in this WorkTask.
        @param Work:
        @param OverheadCost:
        @param DesignLocationCUs:
        @param ContractorItems:
        @param SwitchingSchedules:
        @param WorkFlowStep:
        @param Design:
        @param QualificationRequirements:
        @param Capabilities:
        @param WorkCostDetails:
        @param Assets:
        @param LaborItems:
        @param MaterialItems:
        """
        #: The priority of this work task.
        self.priority = priority

        #: If specified, override schedule and perform this task in accordance with instructions specified here.
        self.schedOverride = schedOverride

        self._EquipmentItems = []
        self.EquipmentItems = [] if EquipmentItems is None else EquipmentItems

        self._Usages = []
        self.Usages = [] if Usages is None else Usages

        self._MiscCostItems = []
        self.MiscCostItems = [] if MiscCostItems is None else MiscCostItems

        self._Crews = []
        self.Crews = [] if Crews is None else Crews

        self._Work = None
        self.Work = Work

        self._OverheadCost = None
        self.OverheadCost = OverheadCost

        self._DesignLocationCUs = []
        self.DesignLocationCUs = [] if DesignLocationCUs is None else DesignLocationCUs

        self._ContractorItems = []
        self.ContractorItems = [] if ContractorItems is None else ContractorItems

        self._SwitchingSchedules = []
        self.SwitchingSchedules = [] if SwitchingSchedules is None else SwitchingSchedules

        self._WorkFlowStep = None
        self.WorkFlowStep = WorkFlowStep

        self._Design = None
        self.Design = Design

        self._QualificationRequirements = []
        self.QualificationRequirements = [] if QualificationRequirements is None else QualificationRequirements

        self._Capabilities = []
        self.Capabilities = [] if Capabilities is None else Capabilities

        self._WorkCostDetails = []
        self.WorkCostDetails = [] if WorkCostDetails is None else WorkCostDetails

        self._Assets = []
        self.Assets = [] if Assets is None else Assets

        self._LaborItems = []
        self.LaborItems = [] if LaborItems is None else LaborItems

        self._MaterialItems = []
        self.MaterialItems = [] if MaterialItems is None else MaterialItems

        super(WorkTask, self).__init__(*args, **kw_args)

    _attrs = ["priority", "schedOverride"]
    _attr_types = {"priority": str, "schedOverride": str}
    _defaults = {"priority": '', "schedOverride": ''}
    _enums = {}
    _refs = ["EquipmentItems", "Usages", "MiscCostItems", "Crews", "Work", "OverheadCost", "DesignLocationCUs", "ContractorItems", "SwitchingSchedules", "WorkFlowStep", "Design", "QualificationRequirements", "Capabilities", "WorkCostDetails", "Assets", "LaborItems", "MaterialItems"]
    _many_refs = ["EquipmentItems", "Usages", "MiscCostItems", "Crews", "DesignLocationCUs", "ContractorItems", "SwitchingSchedules", "QualificationRequirements", "Capabilities", "WorkCostDetails", "Assets", "LaborItems", "MaterialItems"]

    def getEquipmentItems(self):
        
        return self._EquipmentItems

    def setEquipmentItems(self, value):
        for x in self._EquipmentItems:
            x.WorkTask = None
        for y in value:
            y._WorkTask = self
        self._EquipmentItems = value

    EquipmentItems = property(getEquipmentItems, setEquipmentItems)

    def addEquipmentItems(self, *EquipmentItems):
        for obj in EquipmentItems:
            obj.WorkTask = self

    def removeEquipmentItems(self, *EquipmentItems):
        for obj in EquipmentItems:
            obj.WorkTask = None

    def getUsages(self):
        
        return self._Usages

    def setUsages(self, value):
        for x in self._Usages:
            x.WorkTask = None
        for y in value:
            y._WorkTask = self
        self._Usages = value

    Usages = property(getUsages, setUsages)

    def addUsages(self, *Usages):
        for obj in Usages:
            obj.WorkTask = self

    def removeUsages(self, *Usages):
        for obj in Usages:
            obj.WorkTask = None

    def getMiscCostItems(self):
        
        return self._MiscCostItems

    def setMiscCostItems(self, value):
        for x in self._MiscCostItems:
            x.WorkTask = None
        for y in value:
            y._WorkTask = self
        self._MiscCostItems = value

    MiscCostItems = property(getMiscCostItems, setMiscCostItems)

    def addMiscCostItems(self, *MiscCostItems):
        for obj in MiscCostItems:
            obj.WorkTask = self

    def removeMiscCostItems(self, *MiscCostItems):
        for obj in MiscCostItems:
            obj.WorkTask = None

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

    def getWork(self):
        
        return self._Work

    def setWork(self, value):
        if self._Work is not None:
            filtered = [x for x in self.Work.WorkTasks if x != self]
            self._Work._WorkTasks = filtered

        self._Work = value
        if self._Work is not None:
            if self not in self._Work._WorkTasks:
                self._Work._WorkTasks.append(self)

    Work = property(getWork, setWork)

    def getOverheadCost(self):
        
        return self._OverheadCost

    def setOverheadCost(self, value):
        if self._OverheadCost is not None:
            filtered = [x for x in self.OverheadCost.WorkTasks if x != self]
            self._OverheadCost._WorkTasks = filtered

        self._OverheadCost = value
        if self._OverheadCost is not None:
            if self not in self._OverheadCost._WorkTasks:
                self._OverheadCost._WorkTasks.append(self)

    OverheadCost = property(getOverheadCost, setOverheadCost)

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

    def getContractorItems(self):
        
        return self._ContractorItems

    def setContractorItems(self, value):
        for x in self._ContractorItems:
            x.WorkTask = None
        for y in value:
            y._WorkTask = self
        self._ContractorItems = value

    ContractorItems = property(getContractorItems, setContractorItems)

    def addContractorItems(self, *ContractorItems):
        for obj in ContractorItems:
            obj.WorkTask = self

    def removeContractorItems(self, *ContractorItems):
        for obj in ContractorItems:
            obj.WorkTask = None

    def getSwitchingSchedules(self):
        
        return self._SwitchingSchedules

    def setSwitchingSchedules(self, value):
        for x in self._SwitchingSchedules:
            x.WorkTask = None
        for y in value:
            y._WorkTask = self
        self._SwitchingSchedules = value

    SwitchingSchedules = property(getSwitchingSchedules, setSwitchingSchedules)

    def addSwitchingSchedules(self, *SwitchingSchedules):
        for obj in SwitchingSchedules:
            obj.WorkTask = self

    def removeSwitchingSchedules(self, *SwitchingSchedules):
        for obj in SwitchingSchedules:
            obj.WorkTask = None

    def getWorkFlowStep(self):
        
        return self._WorkFlowStep

    def setWorkFlowStep(self, value):
        if self._WorkFlowStep is not None:
            filtered = [x for x in self.WorkFlowStep.WorkTasks if x != self]
            self._WorkFlowStep._WorkTasks = filtered

        self._WorkFlowStep = value
        if self._WorkFlowStep is not None:
            if self not in self._WorkFlowStep._WorkTasks:
                self._WorkFlowStep._WorkTasks.append(self)

    WorkFlowStep = property(getWorkFlowStep, setWorkFlowStep)

    def getDesign(self):
        
        return self._Design

    def setDesign(self, value):
        if self._Design is not None:
            filtered = [x for x in self.Design.WorkTasks if x != self]
            self._Design._WorkTasks = filtered

        self._Design = value
        if self._Design is not None:
            if self not in self._Design._WorkTasks:
                self._Design._WorkTasks.append(self)

    Design = property(getDesign, setDesign)

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

    def getWorkCostDetails(self):
        
        return self._WorkCostDetails

    def setWorkCostDetails(self, value):
        for x in self._WorkCostDetails:
            x.WorkTask = None
        for y in value:
            y._WorkTask = self
        self._WorkCostDetails = value

    WorkCostDetails = property(getWorkCostDetails, setWorkCostDetails)

    def addWorkCostDetails(self, *WorkCostDetails):
        for obj in WorkCostDetails:
            obj.WorkTask = self

    def removeWorkCostDetails(self, *WorkCostDetails):
        for obj in WorkCostDetails:
            obj.WorkTask = None

    def getAssets(self):
        
        return self._Assets

    def setAssets(self, value):
        for x in self._Assets:
            x.WorkTask = None
        for y in value:
            y._WorkTask = self
        self._Assets = value

    Assets = property(getAssets, setAssets)

    def addAssets(self, *Assets):
        for obj in Assets:
            obj.WorkTask = self

    def removeAssets(self, *Assets):
        for obj in Assets:
            obj.WorkTask = None

    def getLaborItems(self):
        
        return self._LaborItems

    def setLaborItems(self, value):
        for x in self._LaborItems:
            x.WorkTask = None
        for y in value:
            y._WorkTask = self
        self._LaborItems = value

    LaborItems = property(getLaborItems, setLaborItems)

    def addLaborItems(self, *LaborItems):
        for obj in LaborItems:
            obj.WorkTask = self

    def removeLaborItems(self, *LaborItems):
        for obj in LaborItems:
            obj.WorkTask = None

    def getMaterialItems(self):
        
        return self._MaterialItems

    def setMaterialItems(self, value):
        for x in self._MaterialItems:
            x.WorkTask = None
        for y in value:
            y._WorkTask = self
        self._MaterialItems = value

    MaterialItems = property(getMaterialItems, setMaterialItems)

    def addMaterialItems(self, *MaterialItems):
        for obj in MaterialItems:
            obj.WorkTask = self

    def removeMaterialItems(self, *MaterialItems):
        for obj in MaterialItems:
            obj.WorkTask = None

