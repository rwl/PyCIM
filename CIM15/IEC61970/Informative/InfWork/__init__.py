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

"""The package covers all types of work, including inspection, maintenance, repair, restoration, and construction. It covers the full life cycle including request, initiate, track and record work. Standardized designs (compatible units) are used where possible.  TODO: The following has been copied from a very old version of draft Part 11, so the references are wrong, but we store the knowledge here to reuse later: 'The Work package is used to define classes related to work. There are several different aspects of work. The Work Initiation (Work, Project, Request). The Work Design package is used for managing designs (CompatibleUnit, Design, DesignLocation, WorkTask). The Work Schedule package is used for the scheduling and coordination of work (AccessPermit, MaterialItem, OneCallRequest, Regulation). The Work Closing package is used for tracking costs of work (CostType, LaborItem, WorkCostDetail, VehicleItem). The Work Standards package is used for the definition of compatible units (CULaborItem, CUVehicleItem, CUGroup). This package is used for inspection and maintenance (InspectionDataSet, Procedure). The WorkService package defines Appointment class.'
"""

from CIM15.IEC61970.Informative.InfWork.EquipmentItem import EquipmentItem
from CIM15.IEC61970.Informative.InfWork.Appointment import Appointment
from CIM15.IEC61970.Informative.InfWork.WorkStatusEntry import WorkStatusEntry
from CIM15.IEC61970.Informative.InfWork.BusinessCase import BusinessCase
from CIM15.IEC61970.Informative.InfWork.TypeMaterial import TypeMaterial
from CIM15.IEC61970.Informative.InfWork.DesignLocation import DesignLocation
from CIM15.IEC61970.Informative.InfWork.OverheadCost import OverheadCost
from CIM15.IEC61970.Informative.InfWork.Crew import Crew
from CIM15.IEC61970.Informative.InfWork.DiagnosisDataSet import DiagnosisDataSet
from CIM15.IEC61970.Informative.InfWork.CUAsset import CUAsset
from CIM15.IEC61970.Informative.InfWork.Request import Request
from CIM15.IEC61970.Informative.InfWork.Design import Design
from CIM15.IEC61970.Informative.InfWork.WorkTask import WorkTask
from CIM15.IEC61970.Informative.InfWork.ConditionFactor import ConditionFactor
from CIM15.IEC61970.Informative.InfWork.QualificationRequirement import QualificationRequirement
from CIM15.IEC61970.Informative.InfWork.WorkLocation import WorkLocation
from CIM15.IEC61970.Informative.InfWork.CostType import CostType
from CIM15.IEC61970.Informative.InfWork.CUMaterialItem import CUMaterialItem
from CIM15.IEC61970.Informative.InfWork.PropertyUnit import PropertyUnit
from CIM15.IEC61970.Informative.InfWork.Project import Project
from CIM15.IEC61970.Informative.InfWork.CULaborItem import CULaborItem
from CIM15.IEC61970.Informative.InfWork.LaborItem import LaborItem
from CIM15.IEC61970.Informative.InfWork.WorkFlowStep import WorkFlowStep
from CIM15.IEC61970.Informative.InfWork.InspectionDataSet import InspectionDataSet
from CIM15.IEC61970.Informative.InfWork.WorkCostDetail import WorkCostDetail
from CIM15.IEC61970.Informative.InfWork.CompatibleUnit import CompatibleUnit
from CIM15.IEC61970.Informative.InfWork.WorkCostSummary import WorkCostSummary
from CIM15.IEC61970.Informative.InfWork.NonStandardItem import NonStandardItem
from CIM15.IEC61970.Informative.InfWork.InfoQuestion import InfoQuestion
from CIM15.IEC61970.Informative.InfWork.Regulation import Regulation
from CIM15.IEC61970.Informative.InfWork.ContractorItem import ContractorItem
from CIM15.IEC61970.Informative.InfWork.CUAllowableAction import CUAllowableAction
from CIM15.IEC61970.Informative.InfWork.CULaborCode import CULaborCode
from CIM15.IEC61970.Informative.InfWork.AccessPermit import AccessPermit
from CIM15.IEC61970.Informative.InfWork.CUWorkEquipmentItem import CUWorkEquipmentItem
from CIM15.IEC61970.Informative.InfWork.DesignLocationCU import DesignLocationCU
from CIM15.IEC61970.Informative.InfWork.MaintenanceDataSet import MaintenanceDataSet
from CIM15.IEC61970.Informative.InfWork.MiscCostItem import MiscCostItem
from CIM15.IEC61970.Informative.InfWork.MaterialItem import MaterialItem
from CIM15.IEC61970.Informative.InfWork.ShiftPattern import ShiftPattern
from CIM15.IEC61970.Informative.InfWork.Capability import Capability
from CIM15.IEC61970.Informative.InfWork.Usage import Usage
from CIM15.IEC61970.Informative.InfWork.OneCallRequest import OneCallRequest
from CIM15.IEC61970.Informative.InfWork.Assignment import Assignment
from CIM15.IEC61970.Informative.InfWork.CUContractorItem import CUContractorItem
from CIM15.IEC61970.Informative.InfWork.CUGroup import CUGroup

nsURI = "http://iec.ch/TC57/2010/CIM-schema-cim15#InfWork"
nsPrefix = "cimInfWork"


class ConditionFactorKind(str):
    """Values are: material, travel, accountAllocation, labor, other
    """
    pass

class WorkActionKind(str):
    """Values are: install, remove, transfer, abandon
    """
    pass

class DesignKind(str):
    """Values are: asBuilt, other, estimated
    """
    pass
