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

"""This package shows all the root level subpackage dependencies of the combined CIM model.
"""
# Modified by Gustav Holm (guholm@kth.se) & Francis J. Gómez (fragom@kth.se)
# Modified date: 05/06/2017

from CIM16.CombinedVersion import CombinedVersion
from CIM16.Element import Element
from CIM16.Stereotype import Stereotype
from CIM16.Package import Package

nsURI = "http://iec.ch/TC57/2013/CIM-schema-cim16"
nsPrefix = "cim"

packageMap = {
    "CombinedVersion": "CIM16",
    "Element": "CIM16",
    "Stereotype": "CIM16",
    "Package": "CIM16",
    "IEC61970CIMVersion": "CIM16.IEC61970",
    "RemoteSource": "CIM16.IEC61970.SCADA",
    "RemotePoint": "CIM16.IEC61970.SCADA",
    "RemoteUnit": "CIM16.IEC61970.SCADA",
    "RemoteControl": "CIM16.IEC61970.SCADA",
    "CommunicationLink": "CIM16.IEC61970.SCADA",
    "Reservoir": "CIM16.IEC61970.Generation.Production",
    "CogenerationPlant": "CIM16.IEC61970.Generation.Production",
    "GenUnitOpSchedule": "CIM16.IEC61970.Generation.Production",
    "FuelAllocationSchedule": "CIM16.IEC61970.Generation.Production",
    "GrossToNetActivePowerCurve": "CIM16.IEC61970.Generation.Production",
    "LevelVsVolumeCurve": "CIM16.IEC61970.Generation.Production",
    "StartRampCurve": "CIM16.IEC61970.Generation.Production",
    "NuclearGeneratingUnit": "CIM16.IEC61970.Generation.Production",
    "EmissionCurve": "CIM16.IEC61970.Generation.Production",
    "HydroPumpOpSchedule": "CIM16.IEC61970.Generation.Production",
    "SteamSendoutSchedule": "CIM16.IEC61970.Generation.Production",
    "TargetLevelSchedule": "CIM16.IEC61970.Generation.Production",
    "CombinedCyclePlant": "CIM16.IEC61970.Generation.Production",
    "HeatRateCurve": "CIM16.IEC61970.Generation.Production",
    "ThermalGeneratingUnit": "CIM16.IEC61970.Generation.Production",
    "EmissionAccount": "CIM16.IEC61970.Generation.Production",
    "PenstockLossCurve": "CIM16.IEC61970.Generation.Production",
    "StartupModel": "CIM16.IEC61970.Generation.Production",
    "HydroGeneratingUnit": "CIM16.IEC61970.Generation.Production",
    "GenUnitOpCostCurve": "CIM16.IEC61970.Generation.Production",
    "IncrementalHeatRateCurve": "CIM16.IEC61970.Generation.Production",
    "FossilFuel": "CIM16.IEC61970.Generation.Production",
    "GeneratingUnit": "CIM16.IEC61970.Generation.Production",
    "StartIgnFuelCurve": "CIM16.IEC61970.Generation.Production",
    "StartMainFuelCurve": "CIM16.IEC61970.Generation.Production",
    "TailbayLossCurve": "CIM16.IEC61970.Generation.Production",
    "HydroPump": "CIM16.IEC61970.Generation.Production",
    "InflowForecast": "CIM16.IEC61970.Generation.Production",
    "HydroGeneratingEfficiencyCurve": "CIM16.IEC61970.Generation.Production",
    "ShutdownCurve": "CIM16.IEC61970.Generation.Production",
    "HydroPowerPlant": "CIM16.IEC61970.Generation.Production",
    "CAESPlant": "CIM16.IEC61970.Generation.Production",
    "AirCompressor": "CIM16.IEC61970.Generation.Production",
    "HeatInputCurve": "CIM16.IEC61970.Generation.Production",
    "WindGeneratingUnit": "CIM16.IEC61970.Generation.Production",
    "BWRSteamSupply": "CIM16.IEC61970.Generation.GenerationDynamics",
    "HydroTurbine": "CIM16.IEC61970.Generation.GenerationDynamics",
    "SteamTurbine": "CIM16.IEC61970.Generation.GenerationDynamics",
    "SteamSupply": "CIM16.IEC61970.Generation.GenerationDynamics",
    "FossilSteamSupply": "CIM16.IEC61970.Generation.GenerationDynamics",
    "Subcritical": "CIM16.IEC61970.Generation.GenerationDynamics",
    "PWRSteamSupply": "CIM16.IEC61970.Generation.GenerationDynamics",
    "PrimeMover": "CIM16.IEC61970.Generation.GenerationDynamics",
    "CombustionTurbine": "CIM16.IEC61970.Generation.GenerationDynamics",
    "HeatRecoveryBoiler": "CIM16.IEC61970.Generation.GenerationDynamics",
    "Supercritical": "CIM16.IEC61970.Generation.GenerationDynamics",
    "DrumBoiler": "CIM16.IEC61970.Generation.GenerationDynamics",
    "CTTempActivePowerCurve": "CIM16.IEC61970.Generation.GenerationDynamics",
    "EquipmentItem": "CIM16.IEC61970.Informative.InfWork",
    "Appointment": "CIM16.IEC61970.Informative.InfWork",
    "WorkStatusEntry": "CIM16.IEC61970.Informative.InfWork",
    "BusinessCase": "CIM16.IEC61970.Informative.InfWork",
    "TypeMaterial": "CIM16.IEC61970.Informative.InfWork",
    "DesignLocation": "CIM16.IEC61970.Informative.InfWork",
    "OverheadCost": "CIM16.IEC61970.Informative.InfWork",
    "Crew": "CIM16.IEC61970.Informative.InfWork",
    "DiagnosisDataSet": "CIM16.IEC61970.Informative.InfWork",
    "CUAsset": "CIM16.IEC61970.Informative.InfWork",
    "Request": "CIM16.IEC61970.Informative.InfWork",
    "Design": "CIM16.IEC61970.Informative.InfWork",
    "WorkTask": "CIM16.IEC61970.Informative.InfWork",
    "ConditionFactor": "CIM16.IEC61970.Informative.InfWork",
    "QualificationRequirement": "CIM16.IEC61970.Informative.InfWork",
    "WorkLocation": "CIM16.IEC61970.Informative.InfWork",
    "CostType": "CIM16.IEC61970.Informative.InfWork",
    "CUMaterialItem": "CIM16.IEC61970.Informative.InfWork",
    "PropertyUnit": "CIM16.IEC61970.Informative.InfWork",
    "Project": "CIM16.IEC61970.Informative.InfWork",
    "CULaborItem": "CIM16.IEC61970.Informative.InfWork",
    "LaborItem": "CIM16.IEC61970.Informative.InfWork",
    "WorkFlowStep": "CIM16.IEC61970.Informative.InfWork",
    "InspectionDataSet": "CIM16.IEC61970.Informative.InfWork",
    "WorkCostDetail": "CIM16.IEC61970.Informative.InfWork",
    "CompatibleUnit": "CIM16.IEC61970.Informative.InfWork",
    "WorkCostSummary": "CIM16.IEC61970.Informative.InfWork",
    "NonStandardItem": "CIM16.IEC61970.Informative.InfWork",
    "InfoQuestion": "CIM16.IEC61970.Informative.InfWork",
    "Regulation": "CIM16.IEC61970.Informative.InfWork",
    "ContractorItem": "CIM16.IEC61970.Informative.InfWork",
    "CUAllowableAction": "CIM16.IEC61970.Informative.InfWork",
    "CULaborCode": "CIM16.IEC61970.Informative.InfWork",
    "AccessPermit": "CIM16.IEC61970.Informative.InfWork",
    "CUWorkEquipmentItem": "CIM16.IEC61970.Informative.InfWork",
    "DesignLocationCU": "CIM16.IEC61970.Informative.InfWork",
    "MaintenanceDataSet": "CIM16.IEC61970.Informative.InfWork",
    "MiscCostItem": "CIM16.IEC61970.Informative.InfWork",
    "MaterialItem": "CIM16.IEC61970.Informative.InfWork",
    "ShiftPattern": "CIM16.IEC61970.Informative.InfWork",
    "Capability": "CIM16.IEC61970.Informative.InfWork",
    "Usage": "CIM16.IEC61970.Informative.InfWork",
    "OneCallRequest": "CIM16.IEC61970.Informative.InfWork",
    "Assignment": "CIM16.IEC61970.Informative.InfWork",
    "CUContractorItem": "CIM16.IEC61970.Informative.InfWork",
    "CUGroup": "CIM16.IEC61970.Informative.InfWork",
    "ErpRecDelvLineItem": "CIM16.IEC61970.Informative.InfERPSupport",
    "ErpLedgerBudget": "CIM16.IEC61970.Informative.InfERPSupport",
    "ErpTimeEntry": "CIM16.IEC61970.Informative.InfERPSupport",
    "ErpCompetency": "CIM16.IEC61970.Informative.InfERPSupport",
    "ErpPurchaseOrder": "CIM16.IEC61970.Informative.InfERPSupport",
    "ErpEngChangeOrder": "CIM16.IEC61970.Informative.InfERPSupport",
    "ErpProjectAccounting": "CIM16.IEC61970.Informative.InfERPSupport",
    "ErpRecLineItem": "CIM16.IEC61970.Informative.InfERPSupport",
    "ErpPayableLineItem": "CIM16.IEC61970.Informative.InfERPSupport",
    "ErpLedBudLineItem": "CIM16.IEC61970.Informative.InfERPSupport",
    "ErpRequisition": "CIM16.IEC61970.Informative.InfERPSupport",
    "ErpOrganisation": "CIM16.IEC61970.Informative.InfERPSupport",
    "ErpInvoice": "CIM16.IEC61970.Informative.InfERPSupport",
    "DocErpPersonRole": "CIM16.IEC61970.Informative.InfERPSupport",
    "ErpBankAccount": "CIM16.IEC61970.Informative.InfERPSupport",
    "ErpQuote": "CIM16.IEC61970.Informative.InfERPSupport",
    "ErpPerson": "CIM16.IEC61970.Informative.InfERPSupport",
    "ErpItemMaster": "CIM16.IEC61970.Informative.InfERPSupport",
    "ErpBOM": "CIM16.IEC61970.Informative.InfERPSupport",
    "ErpInventoryCount": "CIM16.IEC61970.Informative.InfERPSupport",
    "ErpIssueInventory": "CIM16.IEC61970.Informative.InfERPSupport",
    "ErpPayable": "CIM16.IEC61970.Informative.InfERPSupport",
    "ErpLedger": "CIM16.IEC61970.Informative.InfERPSupport",
    "ErpPOLineItem": "CIM16.IEC61970.Informative.InfERPSupport",
    "ErpLedgerEntry": "CIM16.IEC61970.Informative.InfERPSupport",
    "ErpPayment": "CIM16.IEC61970.Informative.InfERPSupport",
    "ErpReceivable": "CIM16.IEC61970.Informative.InfERPSupport",
    "DocOrgRole": "CIM16.IEC61970.Informative.InfERPSupport",
    "ErpReqLineItem": "CIM16.IEC61970.Informative.InfERPSupport",
    "ErpTimeSheet": "CIM16.IEC61970.Informative.InfERPSupport",
    "ErpInventory": "CIM16.IEC61970.Informative.InfERPSupport",
    "ErpChartOfAccounts": "CIM16.IEC61970.Informative.InfERPSupport",
    "ErpSiteLevelData": "CIM16.IEC61970.Informative.InfERPSupport",
    "OrgErpPersonRole": "CIM16.IEC61970.Informative.InfERPSupport",
    "ErpReceiveDelivery": "CIM16.IEC61970.Informative.InfERPSupport",
    "ErpSalesOrder": "CIM16.IEC61970.Informative.InfERPSupport",
    "ErpJournalEntry": "CIM16.IEC61970.Informative.InfERPSupport",
    "ErpInvoiceLineItem": "CIM16.IEC61970.Informative.InfERPSupport",
    "OrgOrgRole": "CIM16.IEC61970.Informative.InfERPSupport",
    "ErpJournal": "CIM16.IEC61970.Informative.InfERPSupport",
    "ErpPersonnel": "CIM16.IEC61970.Informative.InfERPSupport",
    "ErpQuoteLineItem": "CIM16.IEC61970.Informative.InfERPSupport",
    "ErpBomItemData": "CIM16.IEC61970.Informative.InfERPSupport",
    "Role": "CIM16.IEC61970.Informative.InfCommon",
    "Bank": "CIM16.IEC61970.Informative.InfCommon",
    "Skill": "CIM16.IEC61970.Informative.InfCommon",
    "BusinessRole": "CIM16.IEC61970.Informative.InfCommon",
    "ScheduledEvent": "CIM16.IEC61970.Informative.InfCommon",
    "ScheduleParameterInfo": "CIM16.IEC61970.Informative.InfCommon",
    "DocPsrRole": "CIM16.IEC61970.Informative.InfCommon",
    "Ratio": "CIM16.IEC61970.Informative.InfCommon",
    "BankAccount": "CIM16.IEC61970.Informative.InfCommon",
    "Craft": "CIM16.IEC61970.Informative.InfCommon",
    "DocDocRole": "CIM16.IEC61970.Informative.InfCommon",
    "BusinessPlan": "CIM16.IEC61970.Informative.InfCommon",
    "FACTSDevice": "CIM16.IEC61970.Informative.InfAssets",
    "DocAssetRole": "CIM16.IEC61970.Informative.InfAssets",
    "DuctBank": "CIM16.IEC61970.Informative.InfAssets",
    "ConductorAsset": "CIM16.IEC61970.Informative.InfAssets",
    "FinancialInfo": "CIM16.IEC61970.Informative.InfAssets",
    "ProtectionEquipmentInfo": "CIM16.IEC61970.Informative.InfAssets",
    "ProcedureDataSet": "CIM16.IEC61970.Informative.InfAssets",
    "WindingInsulation": "CIM16.IEC61970.Informative.InfAssets",
    "Specification": "CIM16.IEC61970.Informative.InfAssets",
    "UndergroundStructure": "CIM16.IEC61970.Informative.InfAssets",
    "PotentialTransformerInfo": "CIM16.IEC61970.Informative.InfAssets",
    "Structure": "CIM16.IEC61970.Informative.InfAssets",
    "CurrentTransformerInfo": "CIM16.IEC61970.Informative.InfAssets",
    "BushingInsulationPF": "CIM16.IEC61970.Informative.InfAssets",
    "Joint": "CIM16.IEC61970.Informative.InfAssets",
    "ElectricalInfo": "CIM16.IEC61970.Informative.InfAssets",
    "WorkEquipment": "CIM16.IEC61970.Informative.InfAssets",
    "FaultIndicatorInfo": "CIM16.IEC61970.Informative.InfAssets",
    "Duct": "CIM16.IEC61970.Informative.InfAssets",
    "PowerRating": "CIM16.IEC61970.Informative.InfAssets",
    "AssetAssetRole": "CIM16.IEC61970.Informative.InfAssets",
    "TransformerAsset": "CIM16.IEC61970.Informative.InfAssets",
    "Procedure": "CIM16.IEC61970.Informative.InfAssets",
    "BreakerInfo": "CIM16.IEC61970.Informative.InfAssets",
    "CompositeSwitchInfo": "CIM16.IEC61970.Informative.InfAssets",
    "Cabinet": "CIM16.IEC61970.Informative.InfAssets",
    "Bushing": "CIM16.IEC61970.Informative.InfAssets",
    "Vehicle": "CIM16.IEC61970.Informative.InfAssets",
    "SurgeProtectorInfo": "CIM16.IEC61970.Informative.InfAssets",
    "StructureSupport": "CIM16.IEC61970.Informative.InfAssets",
    "ComEquipment": "CIM16.IEC61970.Informative.InfAssets",
    "AssetPropertyCurve": "CIM16.IEC61970.Informative.InfAssets",
    "FailureEvent": "CIM16.IEC61970.Informative.InfAssets",
    "DimensionsInfo": "CIM16.IEC61970.Informative.InfAssets",
    "Tower": "CIM16.IEC61970.Informative.InfAssets",
    "MountingConnection": "CIM16.IEC61970.Informative.InfAssets",
    "Medium": "CIM16.IEC61970.Informative.InfAssets",
    "RecloserInfo": "CIM16.IEC61970.Informative.InfAssets",
    "Facility": "CIM16.IEC61970.Informative.InfAssets",
    "ShuntImpedanceInfo": "CIM16.IEC61970.Informative.InfAssets",
    "ShuntCompensatorInfo": "CIM16.IEC61970.Informative.InfAssets",
    "MountingPoint": "CIM16.IEC61970.Informative.InfAssets",
    "SubstationAsset": "CIM16.IEC61970.Informative.InfAssets",
    "Streetlight": "CIM16.IEC61970.Informative.InfAssets",
    "Tool": "CIM16.IEC61970.Informative.InfAssets",
    "SVC": "CIM16.IEC61970.Informative.InfAssets",
    "OrgAssetRole": "CIM16.IEC61970.Informative.InfAssets",
    "TestDataSet": "CIM16.IEC61970.Informative.InfAssets",
    "GenericAssetModelOrMaterial": "CIM16.IEC61970.Informative.InfAssets",
    "ReliabilityInfo": "CIM16.IEC61970.Informative.InfAssets",
    "TransformerObservation": "CIM16.IEC61970.Informative.InfAssets",
    "Pole": "CIM16.IEC61970.Informative.InfAssets",
    "SwitchInfo": "CIM16.IEC61970.Informative.InfAssets",
    "StandardIndustryCode": "CIM16.IEC61970.Informative.InfCustomers",
    "OutageHistory": "CIM16.IEC61970.Informative.InfCustomers",
    "ComplianceEvent": "CIM16.IEC61970.Informative.InfCustomers",
    "CustomerBillingInfo": "CIM16.IEC61970.Informative.InfCustomers",
    "ServiceGuarantee": "CIM16.IEC61970.Informative.InfCustomers",
    "SubscribePowerCurve": "CIM16.IEC61970.Informative.InfCustomers",
    "ExternalCustomerAgreement": "CIM16.IEC61970.Informative.InfCustomers",
    "PowerQualityPricing": "CIM16.IEC61970.Informative.InfCustomers",
    "WorkBillingInfo": "CIM16.IEC61970.Informative.InfCustomers",
    "OutageRecord": "CIM16.IEC61970.Informative.InfOperations",
    "OutageReport": "CIM16.IEC61970.Informative.InfOperations",
    "ChangeItem": "CIM16.IEC61970.Informative.InfOperations",
    "PSREvent": "CIM16.IEC61970.Informative.InfOperations",
    "PlannedOutage": "CIM16.IEC61970.Informative.InfOperations",
    "CircuitSection": "CIM16.IEC61970.Informative.InfOperations",
    "SafetyDocument": "CIM16.IEC61970.Informative.InfOperations",
    "OperationalRestriction": "CIM16.IEC61970.Informative.InfOperations",
    "ChangeSet": "CIM16.IEC61970.Informative.InfOperations",
    "SwitchingSchedule": "CIM16.IEC61970.Informative.InfOperations",
    "Circuit": "CIM16.IEC61970.Informative.InfOperations",
    "NetworkDataSet": "CIM16.IEC61970.Informative.InfOperations",
    "OutageStep": "CIM16.IEC61970.Informative.InfOperations",
    "OrgPsrRole": "CIM16.IEC61970.Informative.InfOperations",
    "OutageCode": "CIM16.IEC61970.Informative.InfOperations",
    "IncidentCode": "CIM16.IEC61970.Informative.InfOperations",
    "LandBase": "CIM16.IEC61970.Informative.InfOperations",
    "ErpPersonScheduleStepRole": "CIM16.IEC61970.Informative.InfOperations",
    "SwitchingStep": "CIM16.IEC61970.Informative.InfOperations",
    "CallBack": "CIM16.IEC61970.Informative.InfOperations",
    "TroubleTicket": "CIM16.IEC61970.Informative.InfOperations",
    "IncidentRecord": "CIM16.IEC61970.Informative.InfOperations",
    "OutageNotification": "CIM16.IEC61970.Informative.InfOperations",
    "OutageStepPsrRole": "CIM16.IEC61970.Informative.InfOperations",
    "LocationGrant": "CIM16.IEC61970.Informative.InfLocations",
    "RightOfWay": "CIM16.IEC61970.Informative.InfLocations",
    "PersonPropertyRole": "CIM16.IEC61970.Informative.InfLocations",
    "Zone": "CIM16.IEC61970.Informative.InfLocations",
    "RedLine": "CIM16.IEC61970.Informative.InfLocations",
    "Route": "CIM16.IEC61970.Informative.InfLocations",
    "OrgPropertyRole": "CIM16.IEC61970.Informative.InfLocations",
    "Direction": "CIM16.IEC61970.Informative.InfLocations",
    "LandProperty": "CIM16.IEC61970.Informative.InfLocations",
    "Hazard": "CIM16.IEC61970.Informative.InfLocations",
    "GmlFeatureType": "CIM16.IEC61970.Informative.InfGMLSupport",
    "Map": "CIM16.IEC61970.Informative.InfGMLSupport",
    "GmlPointGeometry": "CIM16.IEC61970.Informative.InfGMLSupport",
    "GmlHalo": "CIM16.IEC61970.Informative.InfGMLSupport",
    "GmlColour": "CIM16.IEC61970.Informative.InfGMLSupport",
    "GmlFont": "CIM16.IEC61970.Informative.InfGMLSupport",
    "GmlPolygonSymbol": "CIM16.IEC61970.Informative.InfGMLSupport",
    "GmlStroke": "CIM16.IEC61970.Informative.InfGMLSupport",
    "GmlBaseSymbol": "CIM16.IEC61970.Informative.InfGMLSupport",
    "GmlPosition": "CIM16.IEC61970.Informative.InfGMLSupport",
    "GmlTextSymbol": "CIM16.IEC61970.Informative.InfGMLSupport",
    "GmlPolygonGeometry": "CIM16.IEC61970.Informative.InfGMLSupport",
    "GmlObservation": "CIM16.IEC61970.Informative.InfGMLSupport",
    "GmlMark": "CIM16.IEC61970.Informative.InfGMLSupport",
    "GmlGraphic": "CIM16.IEC61970.Informative.InfGMLSupport",
    "GmlLabelPlacement": "CIM16.IEC61970.Informative.InfGMLSupport",
    "GmlGeometryStyle": "CIM16.IEC61970.Informative.InfGMLSupport",
    "GmlLineGeometry": "CIM16.IEC61970.Informative.InfGMLSupport",
    "GmlValue": "CIM16.IEC61970.Informative.InfGMLSupport",
    "GmlLineSymbol": "CIM16.IEC61970.Informative.InfGMLSupport",
    "GmlDiagramObject": "CIM16.IEC61970.Informative.InfGMLSupport",
    "GmlPointSymbol": "CIM16.IEC61970.Informative.InfGMLSupport",
    "GmlTopologyStyle": "CIM16.IEC61970.Informative.InfGMLSupport",
    "GmlSelector": "CIM16.IEC61970.Informative.InfGMLSupport",
    "GmlSvgParameter": "CIM16.IEC61970.Informative.InfGMLSupport",
    "GmlLabelStyle": "CIM16.IEC61970.Informative.InfGMLSupport",
    "GmlFill": "CIM16.IEC61970.Informative.InfGMLSupport",
    "Diagram": "CIM16.IEC61970.Informative.InfGMLSupport",
    "GmlSymbol": "CIM16.IEC61970.Informative.InfGMLSupport",
    "GmlFeatureStyle": "CIM16.IEC61970.Informative.InfGMLSupport",
    "GmlRasterSymbol": "CIM16.IEC61970.Informative.InfGMLSupport",
    "ModelingAuthority": "CIM16.IEC61970.Informative.InfCore",
    "ModelingAuthoritySet": "CIM16.IEC61970.Informative.InfCore",
    "LoadMgmtRecord": "CIM16.IEC61970.Informative.InfLoadControl",
    "LoadShedFunction": "CIM16.IEC61970.Informative.InfLoadControl",
    "LoadMgmtFunction": "CIM16.IEC61970.Informative.InfLoadControl",
    "LoadLimitFunction": "CIM16.IEC61970.Informative.InfLoadControl",
    "GasMeteringFunction": "CIM16.IEC61970.Informative.InfMetering",
    "WaterMeteringFunction": "CIM16.IEC61970.Informative.InfMetering",
    "AssetModelCatalogue": "CIM16.IEC61970.Informative.InfAssetModels",
    "TransformerAssetModel": "CIM16.IEC61970.Informative.InfAssetModels",
    "AssetModelCatalogueItem": "CIM16.IEC61970.Informative.InfAssetModels",
    "TypeAssetCatalogue": "CIM16.IEC61970.Informative.InfTypeAsset",
    "GeneratorTypeAsset": "CIM16.IEC61970.Informative.InfTypeAsset",
    "SvVoltage": "CIM16.IEC61970.StateVariables",
    "SvShortCircuit": "CIM16.IEC61970.StateVariables",
    "SvShuntCompensatorSections": "CIM16.IEC61970.StateVariables",
    "StateVariable": "CIM16.IEC61970.StateVariables",
    "SvTapStep": "CIM16.IEC61970.StateVariables",
    "SvStatus": "CIM16.IEC61970.StateVariables",
    "SvInjection": "CIM16.IEC61970.StateVariables",
    "SvPowerFlow": "CIM16.IEC61970.StateVariables",
    "TopologicalIsland": "CIM16.IEC61970.StateVariables",
    "PhaseImpedanceData": "CIM16.IEC61970.Wires",
    "TapSchedule": "CIM16.IEC61970.Wires",
    "TransformerStarImpedance": "CIM16.IEC61970.Wires",
    "Recloser": "CIM16.IEC61970.Wires",
    "RatioTapChangerTabularPoint": "CIM16.IEC61970.Wires",
    "PhaseTapChangerTabular": "CIM16.IEC61970.Wires",
    "RatioTapChanger": "CIM16.IEC61970.Wires",
    "PhaseTapChangerLinear": "CIM16.IEC61970.Wires",
    "ACLineSegment": "CIM16.IEC61970.Wires",
    "ACLineSegmentPhase": "CIM16.IEC61970.WiresPhaseModel",
    "PowerTransformerEnd": "CIM16.IEC61970.Wires",
    "Junction": "CIM16.IEC61970.Wires",
    "RegulatingCondEq": "CIM16.IEC61970.Wires",
    "Sectionaliser": "CIM16.IEC61970.Wires",
    "RatioTapChangerTabular": "CIM16.IEC61970.Wires",
    "PowerTransformer": "CIM16.IEC61970.Wires",
    "Fuse": "CIM16.IEC61970.Wires",
    "EnergyConsumer": "CIM16.IEC61970.Wires",
    "Disconnector": "CIM16.IEC61970.Wires",
    "Connector": "CIM16.IEC61970.Wires",
    "ReactiveCapabilityCurve": "CIM16.IEC61970.Wires",
    "Plant": "CIM16.IEC61970.Wires",
    "GroundDisconnector": "CIM16.IEC61970.Wires",
    "Resistor": "CIM16.IEC61970.Wires",
    "SynchronousMachine": "CIM16.IEC61970.Wires",
    "PhaseTapChangerAsymetrical": "CIM16.IEC61970.Wires",
    "RectifierInverter": "CIM16.IEC61970.Wires",
    "SeriesCompensator": "CIM16.IEC61970.Wires",
    "TapChangerControl": "CIM16.IEC61970.Wires",
    "RegulatingControl": "CIM16.IEC61970.Wires",
    "ProtectedSwitch": "CIM16.IEC61970.Wires",
    "PhaseTapChanger": "CIM16.IEC61970.Wires",
    "Ground": "CIM16.IEC61970.Wires",
    "CompositeSwitch": "CIM16.IEC61970.Wires",
    "RegulationSchedule": "CIM16.IEC61970.Wires",
    "TransformerTankEnd": "CIM16.IEC61970.Wires",
    "Breaker": "CIM16.IEC61970.Wires",
    "MutualCoupling": "CIM16.IEC61970.Wires",
    "Line": "CIM16.IEC61970.Wires",
    "PerLengthPhaseImpedance": "CIM16.IEC61970.Wires",
    "FrequencyConverter": "CIM16.IEC61970.Wires",
    "ShuntCompensator": "CIM16.IEC61970.Wires",
    "VoltageControlZone": "CIM16.IEC61970.Wires",
    "LoadBreakSwitch": "CIM16.IEC61970.Wires",
    "BusbarSection": "CIM16.IEC61970.Wires",
    "TransformerEnd": "CIM16.IEC61970.Wires",
    "TransformerCoreAdmittance": "CIM16.IEC61970.Wires",
    "StaticVarCompensator": "CIM16.IEC61970.Wires",
    "Switch": "CIM16.IEC61970.Wires",
    "PerLengthSequenceImpedance": "CIM16.IEC61970.Wires",
    "TransformerMeshImpedance": "CIM16.IEC61970.Wires",
    "SwitchSchedule": "CIM16.IEC61970.Wires",
    "EnergySource": "CIM16.IEC61970.Wires",
    "TransformerTank": "CIM16.IEC61970.Wires",
    "PhaseTapChangerTabularPoint": "CIM16.IEC61970.Wires",
    "DCLineSegment": "CIM16.IEC61970.Wires",
    "TapChanger": "CIM16.IEC61970.Wires",
    "Conductor": "CIM16.IEC61970.Wires",
    "PhaseTapChangerNonLinear": "CIM16.IEC61970.Wires",
    "PhaseTapChangerSymetrical": "CIM16.IEC61970.Wires",
    "Jumper": "CIM16.IEC61970.Wires",
    "AccumulatorLimit": "CIM16.IEC61970.Meas",
    "ValueToAlias": "CIM16.IEC61970.Meas",
    "MeasurementValueSource": "CIM16.IEC61970.Meas",
    "Analog": "CIM16.IEC61970.Meas",
    "AnalogValue": "CIM16.IEC61970.Meas",
    "Measurement": "CIM16.IEC61970.Meas",
    "ControlType": "CIM16.IEC61970.Meas",
    "StringMeasurementValue": "CIM16.IEC61970.Meas",
    "StringMeasurement": "CIM16.IEC61970.Meas",
    "AnalogLimit": "CIM16.IEC61970.Meas",
    "SetPoint": "CIM16.IEC61970.Meas",
    "Limit": "CIM16.IEC61970.Meas",
    "Discrete": "CIM16.IEC61970.Meas",
    "ValueAliasSet": "CIM16.IEC61970.Meas",
    "Quality61850": "CIM16.IEC61970.Meas",
    "AccumulatorValue": "CIM16.IEC61970.Meas",
    "Command": "CIM16.IEC61970.Meas",
    "Accumulator": "CIM16.IEC61970.Meas",
    "MeasurementValueQuality": "CIM16.IEC61970.Meas",
    "MeasurementValue": "CIM16.IEC61970.Meas",
    "DiscreteValue": "CIM16.IEC61970.Meas",
    "AnalogLimitSet": "CIM16.IEC61970.Meas",
    "LimitSet": "CIM16.IEC61970.Meas",
    "AccumulatorLimitSet": "CIM16.IEC61970.Meas",
    "Control": "CIM16.IEC61970.Meas",
    "ConformLoad": "CIM16.IEC61970.LoadModel",
    "ConformLoadGroup": "CIM16.IEC61970.LoadModel",
    "SeasonDayTypeSchedule": "CIM16.IEC61970.LoadModel",
    "LoadGroup": "CIM16.IEC61970.LoadModel",
    "ConformLoadSchedule": "CIM16.IEC61970.LoadModel",
    "LoadArea": "CIM16.IEC61970.LoadModel",
    "PowerCutZone": "CIM16.IEC61970.LoadModel",
    "LoadResponseCharacteristic": "CIM16.IEC61970.LoadModel",
    "NonConformLoad": "CIM16.IEC61970.LoadModel",
    "StationSupply": "CIM16.IEC61970.LoadModel",
    "EnergyArea": "CIM16.IEC61970.LoadModel",
    "NonConformLoadSchedule": "CIM16.IEC61970.LoadModel",
    "NonConformLoadGroup": "CIM16.IEC61970.LoadModel",
    "DayType": "CIM16.IEC61970.LoadModel",
    "SubLoadArea": "CIM16.IEC61970.LoadModel",
    "Season": "CIM16.IEC61970.LoadModel",
    "SwitchPhase": "CIM16.IEC61970.WiresPhaseModel",
    "ShuntCompensatorPhase": "CIM16.IEC61970.WiresPhaseModel",
    "EnergyConsumerPhase": "CIM16.IEC61970.WiresPhaseModel",
    "AltTieMeas": "CIM16.IEC61970.ControlArea",
    "AltGeneratingUnitMeas": "CIM16.IEC61970.ControlArea",
    "TieFlow": "CIM16.IEC61970.ControlArea",
    "ControlArea": "CIM16.IEC61970.ControlArea",
    "ControlAreaGeneratingUnit": "CIM16.IEC61970.ControlArea",
    "PotentialTransformer": "CIM16.IEC61970.AuxiliaryEquipment",
    "Sensor": "CIM16.IEC61970.AuxiliaryEquipment",
    "AuxiliaryEquipment": "CIM16.IEC61970.AuxiliaryEquipment",
    "CurrentTransformer": "CIM16.IEC61970.AuxiliaryEquipment",
    "SurgeProtector": "CIM16.IEC61970.AuxiliaryEquipment",
    "FaultIndicator": "CIM16.IEC61970.AuxiliaryEquipment",
    "DateTimeInterval": "CIM16.IEC61970.Domain",
    "PowerSystemResource": "CIM16.IEC61970.Core",
    "NameTypeAuthority": "CIM16.IEC61970.Core",
    "Equipment": "CIM16.IEC61970.Core",
    "ConductingEquipment": "CIM16.IEC61970.Core",
    "RegularTimePoint": "CIM16.IEC61970.Core",
    "ConnectivityNode": "CIM16.IEC61970.Core",
    "PSRType": "CIM16.IEC61970.Core",
    "ConnectivityNodeContainer": "CIM16.IEC61970.Core",
    "Bay": "CIM16.IEC61970.Core",
    "EquipmentContainer": "CIM16.IEC61970.Core",
    "ReportingGroup": "CIM16.IEC61970.Core",
    "BasePower": "CIM16.IEC61970.Core",
    "PsrList": "CIM16.IEC61970.Core",
    "IdentifiedObject": "CIM16.IEC61970.Core",
    "BasicIntervalSchedule": "CIM16.IEC61970.Core",
    "Curve": "CIM16.IEC61970.Core",
    "GeographicalRegion": "CIM16.IEC61970.Core",
    "CurveData": "CIM16.IEC61970.Core",
    "SubGeographicalRegion": "CIM16.IEC61970.Core",
    "NameType": "CIM16.IEC61970.Core",
    "Substation": "CIM16.IEC61970.Core",
    "Name": "CIM16.IEC61970.Core",
    "BaseVoltage": "CIM16.IEC61970.Core",
    "Terminal": "CIM16.IEC61970.Core",
    "IrregularIntervalSchedule": "CIM16.IEC61970.Core",
    "RegularIntervalSchedule": "CIM16.IEC61970.Core",
    "OperatingParticipant": "CIM16.IEC61970.Core",
    "OperatingShare": "CIM16.IEC61970.Core",
    "VoltageLevel": "CIM16.IEC61970.Core",
    "ReportingSuperGroup": "CIM16.IEC61970.Core",
    "IrregularTimePoint": "CIM16.IEC61970.Core",
    "TextDiagramObject": "CIM16.IEC61970.Graphics",
    "DiagramObjectGluePoint": "CIM16.IEC61970.Graphics",
    "DiagramObject": "CIM16.IEC61970.Graphics",
    "DiagramObjectStyle": "CIM16.IEC61970.Graphics",
    "DiagramObjectPoint": "CIM16.IEC61970.Graphics",
    "VisibilityLayer": "CIM16.IEC61970.Graphics",
    "ApparentPowerLimit": "CIM16.IEC61970.OperationalLimits",
    "ActivePowerLimit": "CIM16.IEC61970.OperationalLimits",
    "OperationalLimitType": "CIM16.IEC61970.OperationalLimits",
    "BranchGroup": "CIM16.IEC61970.OperationalLimits",
    "OperationalLimitSet": "CIM16.IEC61970.OperationalLimits",
    "ActivePowerLimitSet": "CIM16.IEC61970.OperationalLimits",
    "CurrentLimit": "CIM16.IEC61970.OperationalLimits",
    "CurrentLimitSet": "CIM16.IEC61970.OperationalLimits",
    "ApparentPowerLimitSet": "CIM16.IEC61970.OperationalLimits",
    "BranchGroupTerminal": "CIM16.IEC61970.OperationalLimits",
    "VoltageLimitSet": "CIM16.IEC61970.OperationalLimits",
    "VoltageLimit": "CIM16.IEC61970.OperationalLimits",
    "OperationalLimit": "CIM16.IEC61970.OperationalLimits",
    "SwitchingOperation": "CIM16.IEC61970.Outage",
    "OutageSchedule": "CIM16.IEC61970.Outage",
    "ClearanceTagType": "CIM16.IEC61970.Outage",
    "ClearanceTag": "CIM16.IEC61970.Outage",
    "Cut": "CIM16.IEC61970.CutsJumpers",
    "Clamp": "CIM16.IEC61970.CutsJumpers",
    "RecloseSequence": "CIM16.IEC61970.Protection",
    "SynchrocheckRelay": "CIM16.IEC61970.Protection",
    "CurrentRelay": "CIM16.IEC61970.Protection",
    "ProtectionEquipment": "CIM16.IEC61970.Protection",
    "EquivalentShunt": "CIM16.IEC61970.Equivalents",
    "EquivalentEquipment": "CIM16.IEC61970.Equivalents",
    "EquivalentNetwork": "CIM16.IEC61970.Equivalents",
    "EquivalentInjection": "CIM16.IEC61970.Equivalents",
    "EquivalentBranch": "CIM16.IEC61970.Equivalents",
    "ContingencyEquipment": "CIM16.IEC61970.Contingency",
    "Contingency": "CIM16.IEC61970.Contingency",
    "ContingencyElement": "CIM16.IEC61970.Contingency",
    "BusNameMarker": "CIM16.IEC61970.Topology",
    "TopologicalNode": "CIM16.IEC61970.Topology",
    "IEC61968CIMVersion": "CIM16.IEC61968",
    "PostalAddress": "CIM16.IEC61968.Common",
    "Status": "CIM16.IEC61968.Common",
    "ElectronicAddress": "CIM16.IEC61968.Common",
    "Location": "CIM16.IEC61968.Common",
    "TownDetail": "CIM16.IEC61968.Common",
    "CoordinateSystem": "CIM16.IEC61968.Common",
    "Document": "CIM16.IEC61968.Common",
    "PositionPoint": "CIM16.IEC61968.Common",
    "UserAttribute": "CIM16.IEC61968.Common",
    "StreetAddress": "CIM16.IEC61968.Common",
    "StreetDetail": "CIM16.IEC61968.Common",
    "TimeSchedule": "CIM16.IEC61968.Common",
    "ActivityRecord": "CIM16.IEC61968.Common",
    "TimePoint": "CIM16.IEC61968.Common",
    "Organisation": "CIM16.IEC61968.Common",
    "TelephoneNumber": "CIM16.IEC61968.Common",
    "Agreement": "CIM16.IEC61968.Common",
    "ShortCircuitTest": "CIM16.IEC61968.AssetModels",
    "EndDeviceInfo": "CIM16.IEC61968.AssetModels",
    "WireType": "CIM16.IEC61968.AssetModels",
    "TapeShieldCableInfo": "CIM16.IEC61968.AssetModels",
    "ConductorInfo": "CIM16.IEC61968.AssetModels",
    "TapChangerInfo": "CIM16.IEC61968.AssetModels",
    "TransformerTankInfo": "CIM16.IEC61968.AssetModels",
    "PowerTransformerInfo": "CIM16.IEC61968.AssetModels",
    "OpenCircuitTest": "CIM16.IEC61968.AssetModels",
    "CableInfo": "CIM16.IEC61968.AssetModels",
    "TransformerEndInfo": "CIM16.IEC61968.AssetModels",
    "NoLoadTest": "CIM16.IEC61968.AssetModels",
    "OverheadConductorInfo": "CIM16.IEC61968.AssetModels",
    "ConcentricNeutralCableInfo": "CIM16.IEC61968.AssetModels",
    "WireArrangement": "CIM16.IEC61968.AssetModels",
    "TransformerTest": "CIM16.IEC61968.AssetModels",
    "SDPLocation": "CIM16.IEC61968.Metering",
    "Reading": "CIM16.IEC61968.Metering",
    "ServiceDeliveryPoint": "CIM16.IEC61968.Metering",
    "ElectricMeteringFunction": "CIM16.IEC61968.Metering",
    "DemandResponseProgram": "CIM16.IEC61968.Metering",
    "ReadingMultiplier": "CIM16.IEC61968.Metering",
    "MeterReading": "CIM16.IEC61968.Metering",
    "ReadingQuality": "CIM16.IEC61968.Metering",
    "EndDeviceEvent": "CIM16.IEC61968.Metering",
    "IntervalReading": "CIM16.IEC61968.Metering",
    "Meter": "CIM16.IEC61968.Metering",
    "MeterServiceWork": "CIM16.IEC61968.Metering",
    "PendingCalculation": "CIM16.IEC61968.Metering",
    "IntervalBlock": "CIM16.IEC61968.Metering",
    "EndDeviceFunction": "CIM16.IEC61968.Metering",
    "ComFunction": "CIM16.IEC61968.Metering",
    "EndDevice": "CIM16.IEC61968.Metering",
    "SimpleEndDeviceFunction": "CIM16.IEC61968.Metering",
    "EndDeviceGroup": "CIM16.IEC61968.Metering",
    "Register": "CIM16.IEC61968.Metering",
    "EndDeviceControl": "CIM16.IEC61968.Metering",
    "DynamicDemand": "CIM16.IEC61968.Metering",
    "ReadingType": "CIM16.IEC61968.Metering",
    "VendorShift": "CIM16.IEC61968.PaymentMetering",
    "Transactor": "CIM16.IEC61968.PaymentMetering",
    "CashierShift": "CIM16.IEC61968.PaymentMetering",
    "TariffProfile": "CIM16.IEC61968.PaymentMetering",
    "AccountingUnit": "CIM16.IEC61968.PaymentMetering",
    "Transaction": "CIM16.IEC61968.PaymentMetering",
    "TimeTariffInterval": "CIM16.IEC61968.PaymentMetering",
    "Charge": "CIM16.IEC61968.PaymentMetering",
    "AuxiliaryAgreement": "CIM16.IEC61968.PaymentMetering",
    "Tender": "CIM16.IEC61968.PaymentMetering",
    "ServiceSupplier": "CIM16.IEC61968.PaymentMetering",
    "MerchantAgreement": "CIM16.IEC61968.PaymentMetering",
    "LineDetail": "CIM16.IEC61968.PaymentMetering",
    "ConsumptionTariffInterval": "CIM16.IEC61968.PaymentMetering",
    "Vendor": "CIM16.IEC61968.PaymentMetering",
    "Cheque": "CIM16.IEC61968.PaymentMetering",
    "AccountMovement": "CIM16.IEC61968.PaymentMetering",
    "Shift": "CIM16.IEC61968.PaymentMetering",
    "Receipt": "CIM16.IEC61968.PaymentMetering",
    "Due": "CIM16.IEC61968.PaymentMetering",
    "BankAccountDetail": "CIM16.IEC61968.PaymentMetering",
    "AuxiliaryAccount": "CIM16.IEC61968.PaymentMetering",
    "Cashier": "CIM16.IEC61968.PaymentMetering",
    "Card": "CIM16.IEC61968.PaymentMetering",
    "MerchantAccount": "CIM16.IEC61968.PaymentMetering",
    "PointOfSale": "CIM16.IEC61968.PaymentMetering",
    "ProductAssetModel": "CIM16.IEC61968.Assets",
    "AssetModel": "CIM16.IEC61968.Assets",
    "Asset": "CIM16.IEC61968.Assets",
    "ComMedia": "CIM16.IEC61968.Assets",
    "AssetContainer": "CIM16.IEC61968.Assets",
    "AssetFunction": "CIM16.IEC61968.Assets",
    "Seal": "CIM16.IEC61968.Assets",
    "AssetInfo": "CIM16.IEC61968.Assets",
    "AcceptanceTest": "CIM16.IEC61968.Assets",
    "Work": "CIM16.IEC61968.Work",
    "Tariff": "CIM16.IEC61968.Customers",
    "CustomerAccount": "CIM16.IEC61968.Customers",
    "ServiceLocation": "CIM16.IEC61968.Customers",
    "CustomerAgreement": "CIM16.IEC61968.Customers",
    "ServiceCategory": "CIM16.IEC61968.Customers",
    "PricingStructure": "CIM16.IEC61968.Customers",
    "Customer": "CIM16.IEC61968.Customers",
    "ConnectDisconnectFunction": "CIM16.IEC61968.LoadControl",
    "RemoteConnectDisconnectInfo": "CIM16.IEC61968.LoadControl",
    "MarketParticipant": "CIM16.IEC62325",
    "IEC62325CIMVersion": "CIM16.IEC62325",
    "MarketRole": "CIM16.IEC62325",
    "PackageDependenciesCIMVeresion": "CIM16.PackageDependencies",
    "RotatingMachineDynamics": "CIM16.IEC61970.Dynamics",
    "SynchronousMachineTimeConstantReactance": "CIM16.IEC61970.Dynamics",
    "SynchronousMachineDynamics": "CIM16.IEC61970.Dynamics",
    "DynamicsFunctionBlock": "CIM16.IEC61970.Dynamics",
    "SynchronousMachineUserDefined": "CIM16.IEC61970.Dynamics",
    "SynchronousMachineDetailed": "CIM16.IEC61970.Dynamics",
    "SynchronousMachineSimplified": "CIM16.IEC61970.Dynamics",
    "SynchronousMachineEquivalentCircuit": "CIM16.IEC61970.Dynamics",

}


class CIMTime(str):
    pass

class CIMDateTime(str):
    pass

class CIMDuration(str):
    pass

class CIMGYear(str):
    pass

class CIMDate(str):
    pass

class CIMGMonthDay(str):
    pass

class CIMGMonth(str):
    pass

class CIMGDay(str):
    pass

class CIMGYearMonth(str):
    pass
