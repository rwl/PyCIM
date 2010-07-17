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

from CIM.IEC61970.Core import IdentifiedObject
from CIM.IEC61968.Metering import DeviceFunction



from enthought.traits.api import Instance, List, Property
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
#  "ComPort" class:
#------------------------------------------------------------------------------

class ComPort(IdentifiedObject):
    """ Port information used for communication connectivity purposes. The 'port' names the physical association to another device from the perspective of the parent asset. For example, a communications module may need to list the meters which it can talk to as meter serial number '123' is on 'port 0', S/N '456' is on port '1', etc. A meter or load control device may need to know that a hot-water heater load is on 'port 0', and an air-conditioner on 'port 1'.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "ComPort" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfMetering.ComPort",
        title="ComPort",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ComPort" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "WaterMeteringFunction" class:
#------------------------------------------------------------------------------

class WaterMeteringFunction(DeviceFunction):
    """ Functionality performed by a water meter. It's entirely possible that the metering system would carry information to/from water meters even though it was built primarily to carry the higher-value electric meter data.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "WaterMeteringFunction" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "initialCondition", "category", "lotNumber", "application", "serialNumber", "installationDate", "corporateCode", "purchasePrice", "manufacturedDate", "initialLossOfLife", "utcNumber", "critical", "hardwareID", "configID", "programID", "password", "firmwareID", "disabled",
                label="Attributes", columns=2),
            VGroup("Parent", "ModelingAuthoritySet", "Measurements", "Hazards", "ErpOrganisationRoles", "DimensionsInfo", "ScheduledEvents", "Mediums", "AssetFunctions", "Properties", "AssetContainer", "Ratings", "ActivityRecords", "FromAssetRoles", "LocationRoles", "PowerSystemResourceRoles", "DocumentRoles", "ChangeItems", "ErpItemMaster", "ElectronicAddresses", "WorkTask", "ErpRecDeliveryItems", "ReliabilityInfos", "ToAssetRoles", "AssetPropertyCurves", "FinancialInfo", "ErpInventory", "acceptanceTest", "status", "Asset", "AssetFunctionAssetModel", "ComEquipmentAsset", "EndDeviceAsset", "Registers", "EndDeviceEvents",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfMetering.WaterMeteringFunction",
        title="WaterMeteringFunction",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "WaterMeteringFunction" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GasMeteringFunction" class:
#------------------------------------------------------------------------------

class GasMeteringFunction(DeviceFunction):
    """ Functionality performed by a gas meter. It's entirely possible that the metering system would carry information to/from gas meters even though it was built primarily to carry the higher-value electric meter data.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "GasMeteringFunction" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "initialCondition", "category", "lotNumber", "application", "serialNumber", "installationDate", "corporateCode", "purchasePrice", "manufacturedDate", "initialLossOfLife", "utcNumber", "critical", "hardwareID", "configID", "programID", "password", "firmwareID", "disabled",
                label="Attributes", columns=2),
            VGroup("Parent", "ModelingAuthoritySet", "Measurements", "Hazards", "ErpOrganisationRoles", "DimensionsInfo", "ScheduledEvents", "Mediums", "AssetFunctions", "Properties", "AssetContainer", "Ratings", "ActivityRecords", "FromAssetRoles", "LocationRoles", "PowerSystemResourceRoles", "DocumentRoles", "ChangeItems", "ErpItemMaster", "ElectronicAddresses", "WorkTask", "ErpRecDeliveryItems", "ReliabilityInfos", "ToAssetRoles", "AssetPropertyCurves", "FinancialInfo", "ErpInventory", "acceptanceTest", "status", "Asset", "AssetFunctionAssetModel", "ComEquipmentAsset", "EndDeviceAsset", "Registers", "EndDeviceEvents",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfMetering.GasMeteringFunction",
        title="GasMeteringFunction",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GasMeteringFunction" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "MeteringFunctionConfiguration" class:
#------------------------------------------------------------------------------

class MeteringFunctionConfiguration(IdentifiedObject):
    """ The configuration of data for a given meter function.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # All electric metering functions with this configuration.
    ElectricMeteringFunctions = List(Instance("CIM.IEC61968.Metering.ElectricMeteringFunction"),
        desc="All electric metering functions with this configuration.")

    #--------------------------------------------------------------------------
    #  Begin "MeteringFunctionConfiguration" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ElectricMeteringFunctions",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfMetering.MeteringFunctionConfiguration",
        title="MeteringFunctionConfiguration",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "MeteringFunctionConfiguration" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
