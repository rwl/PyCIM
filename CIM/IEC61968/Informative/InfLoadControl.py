#------------------------------------------------------------------------------
# Copyright (C) 2010 Richard Lincoln
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CIM.IEC61968.Metering import DeviceFunction
from CIM.IEC61968.Common import ActivityRecord
from CIM.IEC61970.Domain import Minutes
from CIM.IEC61970.Domain import Seconds
from CIM.IEC61970.Domain import ActivePower



from enthought.traits.api import Instance, List, Property, Enum, Bool
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------

# Scheduling basis for a load management function.
LoadMgmtKind = Enum("tariffBased", "remoteControl", "manualControl", "timeBased", desc="Scheduling basis for a load management function.")
# Different states of the load.
LoadStateKind = Enum("noLoad", "fullLoad", "limitedLoad", desc="Different states of the load.")

#------------------------------------------------------------------------------
#  "LoadMgmtFunction" class:
#------------------------------------------------------------------------------

class LoadMgmtFunction(DeviceFunction):
    """ A collective function at an end device that manages the customer load.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Switches = List(Instance("CIM.IEC61970.Wires.Switch"))

    LoadMgmtRecords = List(Instance("CIM.IEC61968.Informative.InfLoadControl.LoadMgmtRecord"))

    # The basis of Load Management scheduling used here: Time Based, Tariff Based, Remote Control and Manual Control.
    schedulingBasis = LoadMgmtKind(desc="The basis of Load Management scheduling used here: Time Based, Tariff Based, Remote Control and Manual Control.")

    # The present state of the load being either shed (noLoad), limited (limitedLoad) or fully connected (fullLoad). This refers only to the portion of the customer load that is under control of the LoadMgmtFunction.
    loadStatus = LoadStateKind(desc="The present state of the load being either shed (noLoad), limited (limitedLoad) or fully connected (fullLoad). This refers only to the portion of the customer load that is under control of the LoadMgmtFunction.")

    # True if the currently active schedule is being manually over-ridden to either shed load or to limit load.
    manualOverRide = Bool(desc="True if the currently active schedule is being manually over-ridden to either shed load or to limit load.")

    # After a command had been received to activate the mannualOverRide state or remoteOverRideState, the normal (halted) schedule will resume after this specified time duration had elapsed.
    overRideTimeOut = Minutes(desc="After a command had been received to activate the mannualOverRide state or remoteOverRideState, the normal (halted) schedule will resume after this specified time duration had elapsed.")

    # True if the currently active schedule is being remotely over-ridden to either shed load or to limit load.
    remoteOverRide = Bool(desc="True if the currently active schedule is being remotely over-ridden to either shed load or to limit load.")

    # True if LoadMgmtFunction operates under automatic control, otherwise it operates under manual control.
    isAutoOp = Bool(desc="True if LoadMgmtFunction operates under automatic control, otherwise it operates under manual control.")

    #--------------------------------------------------------------------------
    #  Begin "LoadMgmtFunction" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "initialCondition", "category", "lotNumber", "application", "serialNumber", "installationDate", "corporateCode", "purchasePrice", "manufacturedDate", "initialLossOfLife", "utcNumber", "critical", "hardwareID", "configID", "programID", "password", "firmwareID", "disabled", "schedulingBasis", "loadStatus", "manualOverRide", "overRideTimeOut", "remoteOverRide", "isAutoOp",
                label="Attributes", columns=2),
            VGroup("Parent", "ModelingAuthoritySet", "Measurements", "Hazards", "ErpOrganisationRoles", "DimensionsInfo", "ScheduledEvents", "Mediums", "AssetFunctions", "Properties", "AssetContainer", "Ratings", "ActivityRecords", "FromAssetRoles", "LocationRoles", "PowerSystemResourceRoles", "DocumentRoles", "ChangeItems", "ErpItemMaster", "ElectronicAddresses", "WorkTask", "ErpRecDeliveryItems", "ReliabilityInfos", "ToAssetRoles", "AssetPropertyCurves", "FinancialInfo", "ErpInventory", "acceptanceTest", "status", "Asset", "AssetFunctionAssetModel", "ComEquipmentAsset", "EndDeviceAsset", "Registers", "EndDeviceEvents", "Switches", "LoadMgmtRecords",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfLoadControl.LoadMgmtFunction",
        title="LoadMgmtFunction",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "LoadMgmtFunction" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "LoadMgmtRecord" class:
#------------------------------------------------------------------------------

class LoadMgmtRecord(ActivityRecord):
    """ A log of actual measured load reductions as a result of load shed operations.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    LoadMgmtFunction = Instance("CIM.IEC61968.Informative.InfLoadControl.LoadMgmtFunction",
        transient=True,
        opposite="LoadMgmtRecords",
        editor=InstanceEditor(name="_loadmgmtfunctions"))

    def _get_loadmgmtfunctions(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfLoadControl.LoadMgmtFunction" ]
        else:
            return []

    _loadmgmtfunctions = Property(fget=_get_loadmgmtfunctions)

    # The measured reduction of the total load power as a result of the load shed activation. Thus it is the difference in power before and after the load shed operation.
    loadReduction = ActivePower(desc="The measured reduction of the total load power as a result of the load shed activation. Thus it is the difference in power before and after the load shed operation.")

    #--------------------------------------------------------------------------
    #  Begin "LoadMgmtRecord" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "reason", "category", "severity", "createdDateTime", "loadReduction",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "MarketFactors", "Documents", "Organisations", "ScheduledEvent", "Assets", "ErpPersons", "Locations", "status", "LoadMgmtFunction",
                label="References", columns=1),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfLoadControl.LoadMgmtRecord",
        title="LoadMgmtRecord",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "LoadMgmtRecord" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "LoadLimitFunction" class:
#------------------------------------------------------------------------------

class LoadLimitFunction(LoadMgmtFunction):
    """ A kind of LoadMgmtFunction that limits the customer load to a given value.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # True if the switch will reconnect automatically, otherwise it will reconnect under manual control.
    isAutoReconOp = Bool(desc="True if the switch will reconnect automatically, otherwise it will reconnect under manual control.")

    # From the point when the maximumLoad threshold is crossed there may be a finite delay before the switch actually disconnects the load. Typically this is to buffer against transient load fluctuations.
    disconnectTimeDelay = Seconds(desc="From the point when the maximumLoad threshold is crossed there may be a finite delay before the switch actually disconnects the load. Typically this is to buffer against transient load fluctuations.")

    # From the point when the load recovers from an overload condition and crosses the maximumLoad threshold going down, there may be a finite time delay before the switch actually reconnects the load. Typically this is to give overload conditions sufficient time to clear, thus preventing unnecessary load switching activity.
    reconnectTimeDelay = Seconds(desc="From the point when the load recovers from an overload condition and crosses the maximumLoad threshold going down, there may be a finite time delay before the switch actually reconnects the load. Typically this is to give overload conditions sufficient time to clear, thus preventing unnecessary load switching activity.")

    # The power level, to which the customer load is being limited when this function activates. When the maximum load is exceeded the switch will typically open to shed the complete customer load.
    maximumLoad = ActivePower(desc="The power level, to which the customer load is being limited when this function activates. When the maximum load is exceeded the switch will typically open to shed the complete customer load.")

    #--------------------------------------------------------------------------
    #  Begin "LoadLimitFunction" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "initialCondition", "category", "lotNumber", "application", "serialNumber", "installationDate", "corporateCode", "purchasePrice", "manufacturedDate", "initialLossOfLife", "utcNumber", "critical", "hardwareID", "configID", "programID", "password", "firmwareID", "disabled", "schedulingBasis", "loadStatus", "manualOverRide", "overRideTimeOut", "remoteOverRide", "isAutoOp", "isAutoReconOp", "disconnectTimeDelay", "reconnectTimeDelay", "maximumLoad",
                label="Attributes", columns=2),
            VGroup("Parent", "ModelingAuthoritySet", "Measurements", "Hazards", "ErpOrganisationRoles", "DimensionsInfo", "ScheduledEvents", "Mediums", "AssetFunctions", "Properties", "AssetContainer", "Ratings", "ActivityRecords", "FromAssetRoles", "LocationRoles", "PowerSystemResourceRoles", "DocumentRoles", "ChangeItems", "ErpItemMaster", "ElectronicAddresses", "WorkTask", "ErpRecDeliveryItems", "ReliabilityInfos", "ToAssetRoles", "AssetPropertyCurves", "FinancialInfo", "ErpInventory", "acceptanceTest", "status", "Asset", "AssetFunctionAssetModel", "ComEquipmentAsset", "EndDeviceAsset", "Registers", "EndDeviceEvents", "Switches", "LoadMgmtRecords",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfLoadControl.LoadLimitFunction",
        title="LoadLimitFunction",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "LoadLimitFunction" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "LoadShedFunction" class:
#------------------------------------------------------------------------------

class LoadShedFunction(LoadMgmtFunction):
    """ A kind of LoadMgmtFunction that sheds a part of the customer load.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The value of the load that is connected to the shedding switch. Typically this is a noted nominal value rather than a measured value.
    switchedLoad = ActivePower(desc="The value of the load that is connected to the shedding switch. Typically this is a noted nominal value rather than a measured value.")

    #--------------------------------------------------------------------------
    #  Begin "LoadShedFunction" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "initialCondition", "category", "lotNumber", "application", "serialNumber", "installationDate", "corporateCode", "purchasePrice", "manufacturedDate", "initialLossOfLife", "utcNumber", "critical", "hardwareID", "configID", "programID", "password", "firmwareID", "disabled", "schedulingBasis", "loadStatus", "manualOverRide", "overRideTimeOut", "remoteOverRide", "isAutoOp", "switchedLoad",
                label="Attributes", columns=2),
            VGroup("Parent", "ModelingAuthoritySet", "Measurements", "Hazards", "ErpOrganisationRoles", "DimensionsInfo", "ScheduledEvents", "Mediums", "AssetFunctions", "Properties", "AssetContainer", "Ratings", "ActivityRecords", "FromAssetRoles", "LocationRoles", "PowerSystemResourceRoles", "DocumentRoles", "ChangeItems", "ErpItemMaster", "ElectronicAddresses", "WorkTask", "ErpRecDeliveryItems", "ReliabilityInfos", "ToAssetRoles", "AssetPropertyCurves", "FinancialInfo", "ErpInventory", "acceptanceTest", "status", "Asset", "AssetFunctionAssetModel", "ComEquipmentAsset", "EndDeviceAsset", "Registers", "EndDeviceEvents", "Switches", "LoadMgmtRecords",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfLoadControl.LoadShedFunction",
        title="LoadShedFunction",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "LoadShedFunction" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
