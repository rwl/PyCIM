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

"""The package covers all types of work, including inspection, maintenance, repair, restoration, and construction. It covers the full life cycle including request, initiate, track and record work. Standardized designs (compatible units) are used where possible.  TODO: The following has been copied from a very old version of draft Part 11, so the references are wrong, but we store the knowledge here to reuse later: 'The Work package is used to define classes related to work. There are several different aspects of work. The Work Initiation (Work, Project, Request). The Work Design package is used for managing designs (CompatibleUnit, Design, DesignLocation, WorkTask). The Work Schedule package is used for the scheduling and coordination of work (AccessPermit, MaterialItem, OneCallRequest, Regulation). The Work Closing package is used for tracking costs of work (CostType, LaborItem, WorkCostDetail, VehicleItem). The Work Standards package is used for the definition of compatible units (CULaborItem, CUVehicleItem, CUGroup). This package is used for inspection and maintenance (InspectionDataSet, Procedure). The WorkService package defines Appointment class.'
"""

ns_prefix = "cimInfWork"
ns_uri = "http://iec.ch/TC57/CIM-generic#InfWork"

from CIM14v13.IEC61968.Informative.InfWork.DesignLocation import DesignLocation
from CIM14v13.IEC61968.Informative.InfWork.Capability import Capability
from CIM14v13.IEC61968.Informative.InfWork.Design import Design
from CIM14v13.IEC61968.Informative.InfWork.LaborItem import LaborItem
from CIM14v13.IEC61968.Informative.InfWork.CUMaterialItem import CUMaterialItem
from CIM14v13.IEC61968.Informative.InfWork.NonStandardItem import NonStandardItem
from CIM14v13.IEC61968.Informative.InfWork.TypeMaterial import TypeMaterial
from CIM14v13.IEC61968.Informative.InfWork.Appointment import Appointment
from CIM14v13.IEC61968.Informative.InfWork.MaterialItem import MaterialItem
from CIM14v13.IEC61968.Informative.InfWork.CUContractorItem import CUContractorItem
from CIM14v13.IEC61968.Informative.InfWork.CompatibleUnit import CompatibleUnit
from CIM14v13.IEC61968.Informative.InfWork.InfoQuestion import InfoQuestion
from CIM14v13.IEC61968.Informative.InfWork.MaintenanceDataSet import MaintenanceDataSet
from CIM14v13.IEC61968.Informative.InfWork.Regulation import Regulation
from CIM14v13.IEC61968.Informative.InfWork.Usage import Usage
from CIM14v13.IEC61968.Informative.InfWork.AccessPermit import AccessPermit
from CIM14v13.IEC61968.Informative.InfWork.WorkStatusEntry import WorkStatusEntry
from CIM14v13.IEC61968.Informative.InfWork.WorkTask import WorkTask
from CIM14v13.IEC61968.Informative.InfWork.Request import Request
from CIM14v13.IEC61968.Informative.InfWork.CUAllowableAction import CUAllowableAction
from CIM14v13.IEC61968.Informative.InfWork.Project import Project
from CIM14v13.IEC61968.Informative.InfWork.CUAsset import CUAsset
from CIM14v13.IEC61968.Informative.InfWork.PropertyUnit import PropertyUnit
from CIM14v13.IEC61968.Informative.InfWork.InspectionDataSet import InspectionDataSet
from CIM14v13.IEC61968.Informative.InfWork.CostType import CostType
from CIM14v13.IEC61968.Informative.InfWork.WorkCostSummary import WorkCostSummary
from CIM14v13.IEC61968.Informative.InfWork.MiscCostItem import MiscCostItem
from CIM14v13.IEC61968.Informative.InfWork.CULaborItem import CULaborItem
from CIM14v13.IEC61968.Informative.InfWork.CULaborCode import CULaborCode
from CIM14v13.IEC61968.Informative.InfWork.ShiftPattern import ShiftPattern
from CIM14v13.IEC61968.Informative.InfWork.OverheadCost import OverheadCost
from CIM14v13.IEC61968.Informative.InfWork.DesignLocationCU import DesignLocationCU
from CIM14v13.IEC61968.Informative.InfWork.WorkFlowStep import WorkFlowStep
from CIM14v13.IEC61968.Informative.InfWork.ConditionFactor import ConditionFactor
from CIM14v13.IEC61968.Informative.InfWork.OneCallRequest import OneCallRequest
from CIM14v13.IEC61968.Informative.InfWork.Assignment import Assignment
from CIM14v13.IEC61968.Informative.InfWork.QualificationRequirement import QualificationRequirement
from CIM14v13.IEC61968.Informative.InfWork.Crew import Crew
from CIM14v13.IEC61968.Informative.InfWork.DiagnosisDataSet import DiagnosisDataSet
from CIM14v13.IEC61968.Informative.InfWork.ContractorItem import ContractorItem
from CIM14v13.IEC61968.Informative.InfWork.CUGroup import CUGroup
from CIM14v13.IEC61968.Informative.InfWork.CUWorkEquipmentItem import CUWorkEquipmentItem
from CIM14v13.IEC61968.Informative.InfWork.WorkLocation import WorkLocation
from CIM14v13.IEC61968.Informative.InfWork.WorkCostDetail import WorkCostDetail
from CIM14v13.IEC61968.Informative.InfWork.EquipmentItem import EquipmentItem
from CIM14v13.IEC61968.Informative.InfWork.BusinessCase import BusinessCase
