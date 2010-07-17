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

""" This package contains the core information classes that support asset management applications with specialized classes for asset-level models for objects (as opposed to power system resource models, mainly defined in IEC61970::Wires package).
"""
#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CIM.IEC61970.Core import IdentifiedObject
from CIM import Element
from CIM.IEC61970.Domain import Money
from CIM.IEC61970.Domain import PerCent
from CIM.IEC61970.Domain import Susceptance
from CIM.IEC61970.Domain import Resistance
from CIM.IEC61970.Domain import Frequency
from CIM.IEC61970.Domain import Conductance
from CIM.IEC61970.Domain import Voltage
from CIM.IEC61970.Domain import Reactance
from CIM.IEC61970.Domain import CurrentFlow
from CIM.IEC61970.Domain import ApparentPower



from enthought.traits.api import Instance, List, Property, Enum, Str, Date, Bool, Int
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------

# Kind of seal condition.
SealConditionKind = Enum("locked", "open", "missing", "broken", "other", desc="Kind of seal condition.")
# Kind of seal.
SealKind = Enum("other", "steel", "lock", "lead", desc="Kind of seal.")

#------------------------------------------------------------------------------
#  "Seal" class:
#------------------------------------------------------------------------------

class Seal(IdentifiedObject):
    """ Physically controls access to AssetContainers.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Asset container to which this seal is applied.
    AssetContainer = Instance("CIM.IEC61968.Assets.AssetContainer",
        desc="Asset container to which this seal is applied.",
        transient=True,
        opposite="Seals",
        editor=InstanceEditor(name="_assetcontainers"))

    def _get_assetcontainers(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Assets.AssetContainer" ]
        else:
            return []

    _assetcontainers = Property(fget=_get_assetcontainers)

    # Condition of seal.
    condition = SealConditionKind(desc="Condition of seal.")

    # Kind of seal.
    kind = SealKind(desc="Kind of seal.")

    # (reserved word) Seal number.
    sealNumber = Str(desc="(reserved word) Seal number.")

    # Date and time this seal has been applied.
    appliedDateTime = Date(desc="Date and time this seal has been applied.")

    #--------------------------------------------------------------------------
    #  Begin "Seal" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "condition", "kind", "sealNumber", "appliedDateTime",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "AssetContainer",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Assets.Seal",
        title="Seal",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Seal" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Asset" class:
#------------------------------------------------------------------------------

class Asset(IdentifiedObject):
    """ Tangible resource of the utility, including power system equipment, cabinets, buildings, etc. For electrical network equipment, the role of the asset is defined through PowerSystemResource and its subclasses, defined mainly in the Wires model (refer to IEC61970-301 and model package IEC61970::Wires). Asset description places emphasis on the physical characteristics of the equipment fulfilling that role.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Measurements = List(Instance("CIM.IEC61970.Meas.Measurement"))

    Hazards = List(Instance("CIM.IEC61968.Informative.InfLocations.Hazard"))

    ErpOrganisationRoles = List(Instance("CIM.IEC61968.Informative.InfAssets.OrgAssetRole"))

    DimensionsInfo = Instance("CIM.IEC61968.Informative.InfAssets.DimensionsInfo",
        transient=True,
        opposite="Assets",
        editor=InstanceEditor(name="_dimensionsinfos"))

    def _get_dimensionsinfos(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssets.DimensionsInfo" ]
        else:
            return []

    _dimensionsinfos = Property(fget=_get_dimensionsinfos)

    ScheduledEvents = List(Instance("CIM.IEC61968.Informative.InfCommon.ScheduledEvent"))

    Mediums = List(Instance("CIM.IEC61968.Informative.InfAssets.Medium"))

    AssetFunctions = List(Instance("CIM.IEC61968.Assets.AssetFunction"))

    # UserAttributes used to specify further properties of this asset. Use 'name' to specify what kind of property it is, and 'value.value' attribute for the actual value.
    Properties = List(Instance("CIM.IEC61968.Common.UserAttribute"),
        desc="UserAttributes used to specify further properties of this asset. Use 'name' to specify what kind of property it is, and 'value.value' attribute for the actual value.")

    AssetContainer = Instance("CIM.IEC61968.Assets.AssetContainer",
        transient=True,
        opposite="Assets",
        editor=InstanceEditor(name="_assetcontainers"))

    def _get_assetcontainers(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Assets.AssetContainer" ]
        else:
            return []

    _assetcontainers = Property(fget=_get_assetcontainers)

    # UserAttributes used to specify ratings of this asset. Ratings also can be used to set the initial value of operational measurement limits. Use 'name' to specify what kind of rating it is (e.g., voltage, current), and 'value' attribute for the actual value and unit information of the rating.
    Ratings = List(Instance("CIM.IEC61968.Common.UserAttribute"),
        desc="UserAttributes used to specify ratings of this asset. Ratings also can be used to set the initial value of operational measurement limits. Use 'name' to specify what kind of rating it is (e.g., voltage, current), and 'value' attribute for the actual value and unit information of the rating.")

    # All activity records created for this asset.
    ActivityRecords = List(Instance("CIM.IEC61968.Common.ActivityRecord"),
        desc="All activity records created for this asset.")

    FromAssetRoles = List(Instance("CIM.IEC61968.Informative.InfAssets.AssetAssetRole"))

    LocationRoles = List(Instance("CIM.IEC61968.Informative.InfLocations.AssetLocRole"))

    PowerSystemResourceRoles = List(Instance("CIM.IEC61968.Informative.InfAssets.AssetPsrRole"))

    DocumentRoles = List(Instance("CIM.IEC61968.Informative.InfAssets.DocAssetRole"))

    ChangeItems = List(Instance("CIM.IEC61968.Informative.InfOperations.ChangeItem"))

    ErpItemMaster = Instance("CIM.IEC61968.Informative.InfERPSupport.ErpItemMaster",
        transient=True,
        opposite="Asset",
        editor=InstanceEditor(name="_erpitemmasters"))

    def _get_erpitemmasters(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfERPSupport.ErpItemMaster" ]
        else:
            return []

    _erpitemmasters = Property(fget=_get_erpitemmasters)

    # All electronic addresses of this asset.
    ElectronicAddresses = List(Instance("CIM.IEC61968.Common.ElectronicAddress"),
        desc="All electronic addresses of this asset.")

    WorkTask = Instance("CIM.IEC61968.Informative.InfWork.WorkTask",
        transient=True,
        opposite="Assets",
        editor=InstanceEditor(name="_worktasks"))

    def _get_worktasks(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfWork.WorkTask" ]
        else:
            return []

    _worktasks = Property(fget=_get_worktasks)

    ErpRecDeliveryItems = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpRecDelvLineItem"))

    ReliabilityInfos = List(Instance("CIM.IEC61968.Informative.InfAssets.ReliabilityInfo"))

    ToAssetRoles = List(Instance("CIM.IEC61968.Informative.InfAssets.AssetAssetRole"))

    AssetPropertyCurves = List(Instance("CIM.IEC61968.Informative.InfAssets.AssetPropertyCurve"))

    FinancialInfo = Instance("CIM.IEC61968.Informative.InfAssets.FinancialInfo",
        transient=True,
        opposite="Asset",
        editor=InstanceEditor(name="_financialinfos"))

    def _get_financialinfos(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssets.FinancialInfo" ]
        else:
            return []

    _financialinfos = Property(fget=_get_financialinfos)

    ErpInventory = Instance("CIM.IEC61968.Informative.InfERPSupport.ErpInventory",
        transient=True,
        opposite="Asset",
        editor=InstanceEditor(name="_erpinventorys"))

    def _get_erpinventorys(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfERPSupport.ErpInventory" ]
        else:
            return []

    _erpinventorys = Property(fget=_get_erpinventorys)

    # Information on acceptance test.
    acceptanceTest = Instance("CIM.IEC61968.Assets.AcceptanceTest",
        desc="Information on acceptance test.",
        transient=True,
        editor=InstanceEditor(name="_acceptancetests"))

    def _get_acceptancetests(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Assets.AcceptanceTest" ]
        else:
            return []

    _acceptancetests = Property(fget=_get_acceptancetests)

    # Status of this asset.
    status = Instance("CIM.IEC61968.Common.Status",
        desc="Status of this asset.",
        transient=True,
        editor=InstanceEditor(name="_statuss"))

    def _get_statuss(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Status" ]
        else:
            return []

    _statuss = Property(fget=_get_statuss)

    # Condition of asset in inventory or at time of installation. Examples include new, rebuilt, overhaul required, other. Refer to inspection data for information on the most current condition of the asset.
    initialCondition = Str(desc="Condition of asset in inventory or at time of installation. Examples include new, rebuilt, overhaul required, other. Refer to inspection data for information on the most current condition of the asset.")

    # Extension mechanism to accommodate utility-specific categorisation of Asset and its subtypes, according to their corporate standards, practices, and existing IT systems (e.g., for management of assets, maintenance, work, outage, customers, etc.).
    category = Str(desc="Extension mechanism to accommodate utility-specific categorisation of Asset and its subtypes, according to their corporate standards, practices, and existing IT systems (e.g., for management of assets, maintenance, work, outage, customers, etc.).")

    # Lot number for this asset. Even for the same model and version number, many assets are manufactured in lots.
    lotNumber = Str(desc="Lot number for this asset. Even for the same model and version number, many assets are manufactured in lots.")

    # The way this particular asset is being used in this installation. For example, the application of a bushing when attached to a specific transformer winding would be one of the following: H1, H2, H3, H0, X1, X2, X3, X0, Y1, Y2, Y3, Y0.
    application = Str(desc="The way this particular asset is being used in this installation. For example, the application of a bushing when attached to a specific transformer winding would be one of the following: H1, H2, H3, H0, X1, X2, X3, X0, Y1, Y2, Y3, Y0.")

    # Serial number of this asset.
    serialNumber = Str(desc="Serial number of this asset.")

    # (if applicable) Date current installation was completed, which may not be the same as the in-service date. Asset may have been installed at other locations previously. Ignored if asset is (1) not currently installed (e.g., stored in a depot) or (2) not intended to be installed (e.g., vehicle, tool).
    installationDate = Date(desc="(if applicable) Date current installation was completed, which may not be the same as the in-service date. Asset may have been installed at other locations previously. Ignored if asset is (1) not currently installed (e.g., stored in a depot) or (2) not intended to be installed (e.g., vehicle, tool).")

    # Code for this type of asset.
    corporateCode = Str(desc="Code for this type of asset.")

    # Purchase price of asset.
    purchasePrice = Money(desc="Purchase price of asset.")

    # Date this asset was manufactured.
    manufacturedDate = Date(desc="Date this asset was manufactured.")

    # Whenever an asset is reconditioned, percentage of expected life for the asset when it was new; zero for new devices.
    initialLossOfLife = PerCent(desc="Whenever an asset is reconditioned, percentage of expected life for the asset when it was new; zero for new devices.")

    # Uniquely Tracked Commodity (UTC) number.
    utcNumber = Str(desc="Uniquely Tracked Commodity (UTC) number.")

    # True if asset is considered critical for some reason (for example, a pole with critical attachments).
    critical = Bool(desc="True if asset is considered critical for some reason (for example, a pole with critical attachments).")

    #--------------------------------------------------------------------------
    #  Begin "Asset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "initialCondition", "category", "lotNumber", "application", "serialNumber", "installationDate", "corporateCode", "purchasePrice", "manufacturedDate", "initialLossOfLife", "utcNumber", "critical",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "Measurements", "Hazards", "ErpOrganisationRoles", "DimensionsInfo", "ScheduledEvents", "Mediums", "AssetFunctions", "Properties", "AssetContainer", "Ratings", "ActivityRecords", "FromAssetRoles", "LocationRoles", "PowerSystemResourceRoles", "DocumentRoles", "ChangeItems", "ErpItemMaster", "ElectronicAddresses", "WorkTask", "ErpRecDeliveryItems", "ReliabilityInfos", "ToAssetRoles", "AssetPropertyCurves", "FinancialInfo", "ErpInventory", "acceptanceTest", "status",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Assets.Asset",
        title="Asset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Asset" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ElectricalInfo" class:
#------------------------------------------------------------------------------

class ElectricalInfo(IdentifiedObject):
    """ Electrical properties of an asset or of an asset model (product by a manufacturer). Can also be used to define electrical properties for each phase individually. Not every attribute will be required for each type of asset or asset model. For example, a transformer may only have requirements for 'ratedVoltage', 'ratedApparentPower' and 'phaseCount' attributes, while a conductor will have 'r', 'x', 'b' and 'g' requirements per unit length on top of a 'ratedCurrent' and 'ratedVoltage'.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # All end device assets having this set of electrical properties.
    EndDeviceAssets = List(Instance("CIM.IEC61968.Metering.EndDeviceAsset"),
        desc="All end device assets having this set of electrical properties.")

    ElectricalTypeAssets = List(Instance("CIM.IEC61968.Informative.InfTypeAsset.ElectricalTypeAsset"))

    ElectricalAssets = List(Instance("CIM.IEC61968.Informative.InfAssets.ElectricalAsset"))

    ElectricalAssetModels = List(Instance("CIM.IEC61968.Informative.InfAssetModels.ElectricalAssetModel"))

    # Positive sequence susceptance.
    b = Susceptance(desc="Positive sequence susceptance.")

    # For an installed asset, this is the total number of electrical wires that are physically connected to it. For an AssetModel, this is the total number of wires that can potentially be connected to this asset type. This is particularly useful to understand overall electrical configurations for distribution secondary where the number of wires can not be derived from phase information alone. For example, 120v 2 Wires; 240v 2 Wires; 480v 1Ph 2 Wires; 120/240v 1Ph; 120/208v 3Ph Y; 120/208v 1Ph Y; 120/240v 3Ph D; 240/480v 1Ph 3 Wires; 480v 3Ph D; 240/480v 3Ph D; 277/480v 3Ph Y.
    wireCount = Int(desc="For an installed asset, this is the total number of electrical wires that are physically connected to it. For an AssetModel, this is the total number of wires that can potentially be connected to this asset type. This is particularly useful to understand overall electrical configurations for distribution secondary where the number of wires can not be derived from phase information alone. For example, 120v 2 Wires; 240v 2 Wires; 480v 1Ph 2 Wires; 120/240v 1Ph; 120/208v 3Ph Y; 120/208v 1Ph Y; 120/240v 3Ph D; 240/480v 1Ph 3 Wires; 480v 3Ph D; 240/480v 3Ph D; 277/480v 3Ph Y.")

    # Zero sequence series resistance.
    r0 = Resistance(desc="Zero sequence series resistance.")

    # Frequency at which stated device ratings apply, typically 50 Hz or 60 Hz.
    frequency = Frequency(desc="Frequency at which stated device ratings apply, typically 50 Hz or 60 Hz.")

    # Positive sequence conductance.
    g = Conductance(desc="Positive sequence conductance.")

    # Rated voltage.
    ratedVoltage = Voltage(desc="Rated voltage.")

    # Positive sequence series reactance.
    x = Reactance(desc="Positive sequence series reactance.")

    # Number of potential phases the asset supports, typically 0, 1 or 3. The actual phases connected are determined from 'ConductingEquipment.phases' attribute in the ConductingEquipment subclass associated with the asset or from 'ElectricalAsset.phaseCode' attribute.
    phaseCount = Int(desc="Number of potential phases the asset supports, typically 0, 1 or 3. The actual phases connected are determined from 'ConductingEquipment.phases' attribute in the ConductingEquipment subclass associated with the asset or from 'ElectricalAsset.phaseCode' attribute.")

    # Rated current.
    ratedCurrent = CurrentFlow(desc="Rated current.")

    # Zero sequence susceptance.
    b0 = Susceptance(desc="Zero sequence susceptance.")

    # Positive sequence series resistance.
    r = Resistance(desc="Positive sequence series resistance.")

    # Zero sequence conductance.
    g0 = Conductance(desc="Zero sequence conductance.")

    # Rated apparent power.
    ratedApparentPower = ApparentPower(desc="Rated apparent power.")

    # Zero sequence series reactance.
    x0 = Reactance(desc="Zero sequence series reactance.")

    # Basic Insulation Level (BIL) for switchgear, insulators, etc. A reference insulation level expressed as the impulse crest voltage of a nominal wave, typically 1,2 x 50 microsecond. This is a measure of the ability of the insulation to withstand very high voltage surges.
    bil = Voltage(desc="Basic Insulation Level (BIL) for switchgear, insulators, etc. A reference insulation level expressed as the impulse crest voltage of a nominal wave, typically 1,2 x 50 microsecond. This is a measure of the ability of the insulation to withstand very high voltage surges.")

    #--------------------------------------------------------------------------
    #  Begin "ElectricalInfo" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "b", "wireCount", "r0", "frequency", "g", "ratedVoltage", "x", "phaseCount", "ratedCurrent", "b0", "r", "g0", "ratedApparentPower", "x0", "bil",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "EndDeviceAssets", "ElectricalTypeAssets", "ElectricalAssets", "ElectricalAssetModels",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Assets.ElectricalInfo",
        title="ElectricalInfo",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ElectricalInfo" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "AcceptanceTest" class:
#------------------------------------------------------------------------------

class AcceptanceTest(Element):
    """ Acceptance test for assets.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Date and time the asset was last tested using the 'type' of test and yielding the current status in 'success' attribute.
    dateTime = Date(desc="Date and time the asset was last tested using the 'type' of test and yielding the current status in 'success' attribute.")

    # True if asset has passed acceptance test and may be placed in or is in service. It is set to false if asset is removed from service and is required to be tested again before being placed back in service, possibly in a new location. Since asset may go through multiple tests during its life cycle, the date of each acceptance test may be recorded in Asset.ActivityRecord.status.dateTime.
    success = Bool(desc="True if asset has passed acceptance test and may be placed in or is in service. It is set to false if asset is removed from service and is required to be tested again before being placed back in service, possibly in a new location. Since asset may go through multiple tests during its life cycle, the date of each acceptance test may be recorded in Asset.ActivityRecord.status.dateTime.")

    # Type of test or group of tests that was conducted on 'dateTime'.
    type = Str(desc="Type of test or group of tests that was conducted on 'dateTime'.")

    #--------------------------------------------------------------------------
    #  Begin "AcceptanceTest" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "dateTime", "success", "type",
                label="Attributes"),
            VGroup("Parent",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Assets.AcceptanceTest",
        title="AcceptanceTest",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "AcceptanceTest" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "AssetFunction" class:
#------------------------------------------------------------------------------

class AssetFunction(Asset):
    """ Function performed by an asset. Often, function is a module (or a board that plugs into a backplane) that can be replaced or updated without impacting the rest of the asset. Therefore functions are treated as assets because they have life-cycles that are independent of the asset containing the function.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Asset = Instance("CIM.IEC61968.Assets.Asset",
        transient=True,
        opposite="AssetFunctions",
        editor=InstanceEditor(name="_assets"))

    def _get_assets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Assets.Asset" ]
        else:
            return []

    _assets = Property(fget=_get_assets)

    AssetFunctionAssetModel = Instance("CIM.IEC61968.Informative.InfAssetModels.AssetFunctionAssetModel",
        transient=True,
        opposite="AssetFunctions",
        editor=InstanceEditor(name="_assetfunctionassetmodels"))

    def _get_assetfunctionassetmodels(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssetModels.AssetFunctionAssetModel" ]
        else:
            return []

    _assetfunctionassetmodels = Property(fget=_get_assetfunctionassetmodels)

    # Hardware version.
    hardwareID = Str(desc="Hardware version.")

    # Configuration specified for this function.
    configID = Str(desc="Configuration specified for this function.")

    # Name of program.
    programID = Str(desc="Name of program.")

    # Password needed to access this function.
    password = Str(desc="Password needed to access this function.")

    # Firmware version.
    firmwareID = Str(desc="Firmware version.")

    #--------------------------------------------------------------------------
    #  Begin "AssetFunction" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "initialCondition", "category", "lotNumber", "application", "serialNumber", "installationDate", "corporateCode", "purchasePrice", "manufacturedDate", "initialLossOfLife", "utcNumber", "critical", "hardwareID", "configID", "programID", "password", "firmwareID",
                label="Attributes", columns=2),
            VGroup("Parent", "ModelingAuthoritySet", "Measurements", "Hazards", "ErpOrganisationRoles", "DimensionsInfo", "ScheduledEvents", "Mediums", "AssetFunctions", "Properties", "AssetContainer", "Ratings", "ActivityRecords", "FromAssetRoles", "LocationRoles", "PowerSystemResourceRoles", "DocumentRoles", "ChangeItems", "ErpItemMaster", "ElectronicAddresses", "WorkTask", "ErpRecDeliveryItems", "ReliabilityInfos", "ToAssetRoles", "AssetPropertyCurves", "FinancialInfo", "ErpInventory", "acceptanceTest", "status", "Asset", "AssetFunctionAssetModel",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Assets.AssetFunction",
        title="AssetFunction",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "AssetFunction" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ComMediaAsset" class:
#------------------------------------------------------------------------------

class ComMediaAsset(Asset):
    """ Communication media such as fibre optic cable, power-line, telephone, etc.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "ComMediaAsset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "initialCondition", "category", "lotNumber", "application", "serialNumber", "installationDate", "corporateCode", "purchasePrice", "manufacturedDate", "initialLossOfLife", "utcNumber", "critical",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "Measurements", "Hazards", "ErpOrganisationRoles", "DimensionsInfo", "ScheduledEvents", "Mediums", "AssetFunctions", "Properties", "AssetContainer", "Ratings", "ActivityRecords", "FromAssetRoles", "LocationRoles", "PowerSystemResourceRoles", "DocumentRoles", "ChangeItems", "ErpItemMaster", "ElectronicAddresses", "WorkTask", "ErpRecDeliveryItems", "ReliabilityInfos", "ToAssetRoles", "AssetPropertyCurves", "FinancialInfo", "ErpInventory", "acceptanceTest", "status",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Assets.ComMediaAsset",
        title="ComMediaAsset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ComMediaAsset" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "AssetContainer" class:
#------------------------------------------------------------------------------

class AssetContainer(Asset):
    """ Asset that is aggregation of other assets such as conductors, transformers, switchgear, land, fences, buildings, equipment, vehicles, etc.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    LandProperties = List(Instance("CIM.IEC61968.Informative.InfLocations.LandProperty"))

    Assets = List(Instance("CIM.IEC61968.Assets.Asset"))

    # All seals applied to this asset container.
    Seals = List(Instance("CIM.IEC61968.Assets.Seal"),
        desc="All seals applied to this asset container.")

    #--------------------------------------------------------------------------
    #  Begin "AssetContainer" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "initialCondition", "category", "lotNumber", "application", "serialNumber", "installationDate", "corporateCode", "purchasePrice", "manufacturedDate", "initialLossOfLife", "utcNumber", "critical",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "Measurements", "Hazards", "ErpOrganisationRoles", "DimensionsInfo", "ScheduledEvents", "Mediums", "AssetFunctions", "Properties", "AssetContainer", "Ratings", "ActivityRecords", "FromAssetRoles", "LocationRoles", "PowerSystemResourceRoles", "DocumentRoles", "ChangeItems", "ErpItemMaster", "ElectronicAddresses", "WorkTask", "ErpRecDeliveryItems", "ReliabilityInfos", "ToAssetRoles", "AssetPropertyCurves", "FinancialInfo", "ErpInventory", "acceptanceTest", "status", "LandProperties", "Assets", "Seals",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Assets.AssetContainer",
        title="AssetContainer",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "AssetContainer" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
