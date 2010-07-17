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

from CIM.IEC61968.AssetModels import AssetModel
from CIM.IEC61968.Common import Document
from CIM.IEC61970.Core import IdentifiedObject
from CIM.IEC61970.Domain import Money
from CIM.IEC61970.Domain import Frequency
from CIM.IEC61970.Domain import PerCent
from CIM.IEC61970.Domain import CurrentFlow
from CIM.IEC61970.Domain import Seconds
from CIM.IEC61970.Domain import Voltage
from CIM.IEC61970.Domain import AngleDegrees
from CIM.IEC61970.Domain import ApparentPower
from CIM.IEC61970.Domain import Weight
from CIM.IEC61968.Informative.InfAssets import StreetlightLampKind
from CIM.IEC61970.Domain import ActivePower



from enthought.traits.api import Instance, List, Property, Enum, Bool, Int, Float, Str
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------

# Kind of transformer construction.
TransformerCoreKind = Enum("core", "shell", desc="Kind of transformer construction.")
# Kind of transformer construction.
TransformerConstructionKind = Enum("padmountDeadFront", "onePhase", "unknown", "valut", "padmounted", "aerial", "underground", "padmountLiveFront", "network", "vaultThreePhase", "subway", "dryType", "padmountLoopThrough", "overhead", "threePhase", "padmountFeedThrough", desc="Kind of transformer construction.")
# Insulation kind for windings.
WindingInsulationKind = Enum("other", "nomex", "paper", "thermallyUpgradedPaper", desc="Insulation kind for windings.")
# Kind of shield for a cable.
CableShieldKind = Enum("supersmooth", "superclean", "freeForm", "other", "conventional", desc="Kind of shield for a cable.")
# Switching kind of tap changer.
TapChangerSwitchingKind = Enum("vacuum", "reactive", "other", "resistive", desc="Switching kind of tap changer.")
# Function of a transformer.
TransformerFunctionKind = Enum("other", "voltageRegulator", "secondaryTransformer", "autotransformer", "powerTransformer", desc="Function of a transformer.")
# Insulation kind for bushings.
BushingInsulationKind = Enum("paperoil", "compound", "other", "solidPorcelain", desc="Insulation kind for bushings.")
# Kind of oil preservation.
OilPreservationKind = Enum("nitrogenBlanket", "freeBreathing", "conservator", "other", desc="Kind of oil preservation.")

#------------------------------------------------------------------------------
#  "ElectricalAssetModel" class:
#------------------------------------------------------------------------------

class ElectricalAssetModel(AssetModel):
    """ Documentation for a type of ElectricalAsset of a particular product model made by a manufacturer.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ElectricalInfos = List(Instance("CIM.IEC61968.Assets.ElectricalInfo"))

    #--------------------------------------------------------------------------
    #  Begin "ElectricalAssetModel" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "corporateStandardKind", "usageKind", "modelNumber", "weightTotal", "modelVersion",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "ErpInventoryCounts", "TypeAsset", "AssetModelCatalogueItems", "ElectricalInfos",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssetModels.ElectricalAssetModel",
        title="ElectricalAssetModel",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ElectricalAssetModel" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "VehicleAssetModel" class:
#------------------------------------------------------------------------------

class VehicleAssetModel(AssetModel):
    """ Documentation for a type of a vehicle of a particular product model made by a manufacturer.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Vehicles = List(Instance("CIM.IEC61968.Informative.InfAssets.Vehicle"))

    VehicleTypeAsset = Instance("CIM.IEC61968.Informative.InfTypeAsset.VehicleTypeAsset",
        transient=True,
        opposite="VehicleAssetModels",
        editor=InstanceEditor(name="_vehicletypeassets"))

    def _get_vehicletypeassets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfTypeAsset.VehicleTypeAsset" ]
        else:
            return []

    _vehicletypeassets = Property(fget=_get_vehicletypeassets)

    #--------------------------------------------------------------------------
    #  Begin "VehicleAssetModel" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "corporateStandardKind", "usageKind", "modelNumber", "weightTotal", "modelVersion",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "ErpInventoryCounts", "TypeAsset", "AssetModelCatalogueItems", "Vehicles", "VehicleTypeAsset",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssetModels.VehicleAssetModel",
        title="VehicleAssetModel",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "VehicleAssetModel" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "WorkEquipmentAssetModel" class:
#------------------------------------------------------------------------------

class WorkEquipmentAssetModel(AssetModel):
    """ Documentation for a type of an equipment used for work of a particular product model made by a manufacturer.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    WorkEquipmentTypeAsset = Instance("CIM.IEC61968.Informative.InfTypeAsset.WorkEquipmentTypeAsset",
        transient=True,
        opposite="WorkEquipmentAssetModels",
        editor=InstanceEditor(name="_workequipmenttypeassets"))

    def _get_workequipmenttypeassets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfTypeAsset.WorkEquipmentTypeAsset" ]
        else:
            return []

    _workequipmenttypeassets = Property(fget=_get_workequipmenttypeassets)

    WorkEquipmentAssets = List(Instance("CIM.IEC61968.Informative.InfAssets.WorkEquipmentAsset"))

    #--------------------------------------------------------------------------
    #  Begin "WorkEquipmentAssetModel" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "corporateStandardKind", "usageKind", "modelNumber", "weightTotal", "modelVersion",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "ErpInventoryCounts", "TypeAsset", "AssetModelCatalogueItems", "WorkEquipmentTypeAsset", "WorkEquipmentAssets",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssetModels.WorkEquipmentAssetModel",
        title="WorkEquipmentAssetModel",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "WorkEquipmentAssetModel" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "AssetModelCatalogueItem" class:
#------------------------------------------------------------------------------

class AssetModelCatalogueItem(Document):
    """ Provides pricing and other relevant information about a specific manufacturer's product (i.e., AssetModel), and its price from a given supplier. A single AssetModel may be availble from multiple suppliers. Note that manufacturer and supplier are both types of organisation, which the association is inherited from Document.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ErpQuoteLineItems = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpQuoteLineItem"))

    ErpPOLineItems = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpPOLineItem"))

    AssetModel = Instance("CIM.IEC61968.AssetModels.AssetModel",
        transient=True,
        opposite="AssetModelCatalogueItems",
        editor=InstanceEditor(name="_assetmodels"))

    def _get_assetmodels(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.AssetModels.AssetModel" ]
        else:
            return []

    _assetmodels = Property(fget=_get_assetmodels)

    AssetModelCatalogue = Instance("CIM.IEC61968.Informative.InfAssetModels.AssetModelCatalogue",
        transient=True,
        opposite="AssetModelCatalogueItems",
        editor=InstanceEditor(name="_assetmodelcatalogues"))

    def _get_assetmodelcatalogues(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssetModels.AssetModelCatalogue" ]
        else:
            return []

    _assetmodelcatalogues = Property(fget=_get_assetmodelcatalogues)

    # Unit cost for an asset model from a specific supplier, either for a unit cost or cost per unit length. Cost is for material or asset only and does not include labor to install/construct or configure it.
    unitCost = Money(desc="Unit cost for an asset model from a specific supplier, either for a unit cost or cost per unit length. Cost is for material or asset only and does not include labor to install/construct or configure it.")

    #--------------------------------------------------------------------------
    #  Begin "AssetModelCatalogueItem" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "unitCost",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "ErpQuoteLineItems", "ErpPOLineItems", "AssetModel", "AssetModelCatalogue",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssetModels.AssetModelCatalogueItem",
        title="AssetModelCatalogueItem",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "AssetModelCatalogueItem" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ToolAssetModel" class:
#------------------------------------------------------------------------------

class ToolAssetModel(AssetModel):
    """ Documentation for a type of a tool of a particular product model made by a manufacturer.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Tools = List(Instance("CIM.IEC61968.Informative.InfAssets.Tool"))

    ToolTypeAsset = Instance("CIM.IEC61968.Informative.InfTypeAsset.ToolTypeAsset",
        transient=True,
        opposite="ToolAssetModels",
        editor=InstanceEditor(name="_tooltypeassets"))

    def _get_tooltypeassets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfTypeAsset.ToolTypeAsset" ]
        else:
            return []

    _tooltypeassets = Property(fget=_get_tooltypeassets)

    #--------------------------------------------------------------------------
    #  Begin "ToolAssetModel" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "corporateStandardKind", "usageKind", "modelNumber", "weightTotal", "modelVersion",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "ErpInventoryCounts", "TypeAsset", "AssetModelCatalogueItems", "Tools", "ToolTypeAsset",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssetModels.ToolAssetModel",
        title="ToolAssetModel",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ToolAssetModel" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "TapChangerAssetModel" class:
#------------------------------------------------------------------------------

class TapChangerAssetModel(AssetModel):
    """ Documentation for a type of a tap changer of a particular product model made by a manufacturer.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    TapChangerAssets = List(Instance("CIM.IEC61968.Informative.InfAssets.TapChangerAsset"))

    # Switching kind of tap changer.
    switchingKind = TapChangerSwitchingKind(desc="Switching kind of tap changer.")

    # The neutral tap step position for this type of winding.
    neutralStep = Int(desc="The neutral tap step position for this type of winding.")

    # Lowest possible tap step position, retard from neutral
    lowStep = Int(desc="Lowest possible tap step position, retard from neutral")

    # Frequency at which stated device ratings apply, typically 50Hz or 60Hz.
    frequency = Frequency(desc="Frequency at which stated device ratings apply, typically 50Hz or 60Hz.")

    # Tap step increment, in per cent of nominal voltage, per step position.
    stepVoltageIncrement = PerCent(desc="Tap step increment, in per cent of nominal voltage, per step position.")

    # Rated current.
    ratedCurrent = CurrentFlow(desc="Rated current.")

    # Maximum allowed delay for initial tap changer operation (first step change)
    initialDelay = Seconds(desc="Maximum allowed delay for initial tap changer operation (first step change)")

    # Number of taps.
    tapCount = Int(desc="Number of taps.")

    # Rated voltage.
    ratedVoltage = Voltage(desc="Rated voltage.")

    # Phase shift, in degrees, per step position
    stepPhaseIncrement = AngleDegrees(desc="Phase shift, in degrees, per step position")

    # Maximum allowed delay for isubsequent tap changer operations
    subsequentDelay = Seconds(desc="Maximum allowed delay for isubsequent tap changer operations")

    # Highest possible tap step position, advance from neutral
    highStep = Int(desc="Highest possible tap step position, advance from neutral")

    # Rated apparent power.
    ratedApparentPower = ApparentPower(desc="Rated apparent power.")

    # Number of potential phases the asset supports, typically 0, 1 or 3. The actual phases connected are determined from 'ConductingEquipment.phases' attribute in the ConductingEquipment subclass associated with the asset or from 'ElectricalAsset.phaseCode' attribute.
    phaseCount = Int(desc="Number of potential phases the asset supports, typically 0, 1 or 3. The actual phases connected are determined from 'ConductingEquipment.phases' attribute in the ConductingEquipment subclass associated with the asset or from 'ElectricalAsset.phaseCode' attribute.")

    # Basic Insulation Level (BIL) for switchgear, insulators, etc. A reference insulation level expressed as the impulse crest voltage of a nominal wave, typically 1.2 X 50 microsecond. This is a measure of the ability of the insulation to withstand very high voltage surges.
    bil = Voltage(desc="Basic Insulation Level (BIL) for switchgear, insulators, etc. A reference insulation level expressed as the impulse crest voltage of a nominal wave, typically 1.2 X 50 microsecond. This is a measure of the ability of the insulation to withstand very high voltage surges.")

    #--------------------------------------------------------------------------
    #  Begin "TapChangerAssetModel" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "corporateStandardKind", "usageKind", "modelNumber", "weightTotal", "modelVersion", "switchingKind", "neutralStep", "lowStep", "frequency", "stepVoltageIncrement", "ratedCurrent", "initialDelay", "tapCount", "ratedVoltage", "stepPhaseIncrement", "subsequentDelay", "highStep", "ratedApparentPower", "phaseCount", "bil",
                label="Attributes", columns=2),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "ErpInventoryCounts", "TypeAsset", "AssetModelCatalogueItems", "TapChangerAssets",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssetModels.TapChangerAssetModel",
        title="TapChangerAssetModel",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TapChangerAssetModel" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "CabinetModel" class:
#------------------------------------------------------------------------------

class CabinetModel(AssetModel):
    """ Documentation for a type of Cabinet of a particular product model made by a manufacturer.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Cabinets = List(Instance("CIM.IEC61968.Informative.InfAssets.Cabinet"))

    CabinetTypeAsset = Instance("CIM.IEC61968.Informative.InfTypeAsset.CabinetTypeAsset",
        transient=True,
        opposite="CabinetModels",
        editor=InstanceEditor(name="_cabinettypeassets"))

    def _get_cabinettypeassets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfTypeAsset.CabinetTypeAsset" ]
        else:
            return []

    _cabinettypeassets = Property(fget=_get_cabinettypeassets)

    #--------------------------------------------------------------------------
    #  Begin "CabinetModel" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "corporateStandardKind", "usageKind", "modelNumber", "weightTotal", "modelVersion",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "ErpInventoryCounts", "TypeAsset", "AssetModelCatalogueItems", "Cabinets", "CabinetTypeAsset",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssetModels.CabinetModel",
        title="CabinetModel",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "CabinetModel" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "CompositeSwitchAssetModel" class:
#------------------------------------------------------------------------------

class CompositeSwitchAssetModel(AssetModel):
    """ Documentation for a type of a composite switch asset of a particular product model made by a manufacturer.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    CompositeSwitchInfo = Instance("CIM.IEC61968.Informative.InfAssets.CompositeSwitchInfo",
        transient=True,
        opposite="CompositeSwitchAssetModel",
        editor=InstanceEditor(name="_compositeswitchinfos"))

    def _get_compositeswitchinfos(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssets.CompositeSwitchInfo" ]
        else:
            return []

    _compositeswitchinfos = Property(fget=_get_compositeswitchinfos)

    CompositeSwitchAssets = List(Instance("CIM.IEC61968.Informative.InfAssets.CompositeSwitchAsset"))

    CompositeSwitchTypeAsset = Instance("CIM.IEC61968.Informative.InfTypeAsset.CompositeSwitchTypeAsset",
        transient=True,
        opposite="CompositeSwitchAssetModels",
        editor=InstanceEditor(name="_compositeswitchtypeassets"))

    def _get_compositeswitchtypeassets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfTypeAsset.CompositeSwitchTypeAsset" ]
        else:
            return []

    _compositeswitchtypeassets = Property(fget=_get_compositeswitchtypeassets)

    #--------------------------------------------------------------------------
    #  Begin "CompositeSwitchAssetModel" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "corporateStandardKind", "usageKind", "modelNumber", "weightTotal", "modelVersion",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "ErpInventoryCounts", "TypeAsset", "AssetModelCatalogueItems", "CompositeSwitchInfo", "CompositeSwitchAssets", "CompositeSwitchTypeAsset",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssetModels.CompositeSwitchAssetModel",
        title="CompositeSwitchAssetModel",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "CompositeSwitchAssetModel" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "AssetModelCatalogue" class:
#------------------------------------------------------------------------------

class AssetModelCatalogue(IdentifiedObject):
    """ Catalogue of available types of products and materials that are used to build or install, maintain or operate an Asset. Each catalogue item is for a specific product (AssetModel) available from a specific supplier.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    status = Instance("CIM.IEC61968.Common.Status",
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

    AssetModelCatalogueItems = List(Instance("CIM.IEC61968.Informative.InfAssetModels.AssetModelCatalogueItem"))

    #--------------------------------------------------------------------------
    #  Begin "AssetModelCatalogue" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "status", "AssetModelCatalogueItems",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssetModels.AssetModelCatalogue",
        title="AssetModelCatalogue",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "AssetModelCatalogue" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "TransformerAssetModel" class:
#------------------------------------------------------------------------------

class TransformerAssetModel(AssetModel):
    """ Documentation for a type of a transformer of a particular product model made by a manufacturer.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    TransformerAssets = List(Instance("CIM.IEC61968.Informative.InfAssets.TransformerAsset"))

    TransformerInfo = Instance("CIM.IEC61968.AssetModels.TransformerInfo",
        transient=True,
        opposite="TransformerAssetModels",
        editor=InstanceEditor(name="_transformerinfos"))

    def _get_transformerinfos(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.AssetModels.TransformerInfo" ]
        else:
            return []

    _transformerinfos = Property(fget=_get_transformerinfos)

    # Function of this transformer.
    function = TransformerFunctionKind(desc="Function of this transformer.")

    # Kind of construction for this transformer.
    constructionKind = TransformerConstructionKind(desc="Kind of construction for this transformer.")

    # Type of insultation used for transformer windings: Paper, Thermally Upgraded Paper, Nomex, other
    windingInsulationKind = WindingInsulationKind(desc="Type of insultation used for transformer windings: Paper, Thermally Upgraded Paper, Nomex, other")

    # Kind of oil preservation system.
    oilPreservationKind = OilPreservationKind(desc="Kind of oil preservation system.")

    # Core kind of this transformer product.
    coreKind = TransformerCoreKind(desc="Core kind of this transformer product.")

    # True if this is an autotransformer, false otherwise.
    autoTransformer = Bool(desc="True if this is an autotransformer, false otherwise.")

    # True if windings can be re-configured to result in a different input or output voltage.
    reconfigWinding = Bool(desc="True if windings can be re-configured to result in a different input or output voltage.")

    # 24-hour overload rating.
    dayOverLoadRating = ApparentPower(desc="24-hour overload rating.")

    # Nominal voltage rating for alternate configuration for secondary winding.
    altSecondaryNomVoltage = Voltage(desc="Nominal voltage rating for alternate configuration for secondary winding.")

    # Nominal voltage rating for alternate configuration for primary winding.
    altPrimaryNomVoltage = Voltage(desc="Nominal voltage rating for alternate configuration for primary winding.")

    # Weight of core and coils in transformer.
    coreCoilsWeight = Weight(desc="Weight of core and coils in transformer.")

    # Weight of solid insultation in transformer.
    solidInsulationWeight = Weight(desc="Weight of solid insultation in transformer.")

    # 1-hour overload rating.
    hourOverLoadRating = ApparentPower(desc="1-hour overload rating.")

    # Basic Insulation Level of Neutral
    neutralBIL = Voltage(desc="Basic Insulation Level of Neutral")

    #--------------------------------------------------------------------------
    #  Begin "TransformerAssetModel" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "corporateStandardKind", "usageKind", "modelNumber", "weightTotal", "modelVersion", "function", "constructionKind", "windingInsulationKind", "oilPreservationKind", "coreKind", "autoTransformer", "reconfigWinding", "dayOverLoadRating", "altSecondaryNomVoltage", "altPrimaryNomVoltage", "coreCoilsWeight", "solidInsulationWeight", "hourOverLoadRating", "neutralBIL",
                label="Attributes", columns=2),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "ErpInventoryCounts", "TypeAsset", "AssetModelCatalogueItems", "TransformerAssets", "TransformerInfo",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssetModels.TransformerAssetModel",
        title="TransformerAssetModel",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TransformerAssetModel" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "TowerAssetModel" class:
#------------------------------------------------------------------------------

class TowerAssetModel(AssetModel):
    """ A type of tower supplied by a given manufacturer or constructed from a common design.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    TowerTypeAsset = Instance("CIM.IEC61968.Informative.InfTypeAsset.TowerTypeAsset",
        transient=True,
        opposite="TowerAssetModels",
        editor=InstanceEditor(name="_towertypeassets"))

    def _get_towertypeassets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfTypeAsset.TowerTypeAsset" ]
        else:
            return []

    _towertypeassets = Property(fget=_get_towertypeassets)

    Towers = List(Instance("CIM.IEC61968.Informative.InfAssets.Tower"))

    #--------------------------------------------------------------------------
    #  Begin "TowerAssetModel" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "corporateStandardKind", "usageKind", "modelNumber", "weightTotal", "modelVersion",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "ErpInventoryCounts", "TypeAsset", "AssetModelCatalogueItems", "TowerTypeAsset", "Towers",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssetModels.TowerAssetModel",
        title="TowerAssetModel",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TowerAssetModel" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "PoleModel" class:
#------------------------------------------------------------------------------

class PoleModel(AssetModel):
    """ A type of pole supplied by a given manufacturer.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    PoleTypeAsset = Instance("CIM.IEC61968.Informative.InfTypeAsset.PoleTypeAsset",
        transient=True,
        opposite="PoleModels",
        editor=InstanceEditor(name="_poletypeassets"))

    def _get_poletypeassets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfTypeAsset.PoleTypeAsset" ]
        else:
            return []

    _poletypeassets = Property(fget=_get_poletypeassets)

    Poles = List(Instance("CIM.IEC61968.Informative.InfAssets.Pole"))

    # Pole species. Aluminum, Aluminum Davit, Concrete, Fiberglass, Galvanized Davit, Galvanized, Steel Davit Primed, Steel Davit, Steel Standard Primed, Steel, Truncated, Wood-Treated, Wood-Hard, Wood-Salt Treated, Wood-Soft, Wood, Other, Unknown.
    speciesType = Str(desc="Pole species. Aluminum, Aluminum Davit, Concrete, Fiberglass, Galvanized Davit, Galvanized, Steel Davit Primed, Steel Davit, Steel Standard Primed, Steel, Truncated, Wood-Treated, Wood-Hard, Wood-Salt Treated, Wood-Soft, Wood, Other, Unknown.")

    # Pole class: 1, 2, 3, 4, 5, 6, 7, H1, H2, Other, Unknown.
    classification = Str(desc="Pole class: 1, 2, 3, 4, 5, 6, 7, H1, H2, Other, Unknown.")

    #--------------------------------------------------------------------------
    #  Begin "PoleModel" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "corporateStandardKind", "usageKind", "modelNumber", "weightTotal", "modelVersion", "speciesType", "classification",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "ErpInventoryCounts", "TypeAsset", "AssetModelCatalogueItems", "PoleTypeAsset", "Poles",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssetModels.PoleModel",
        title="PoleModel",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "PoleModel" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "AssetFunctionAssetModel" class:
#------------------------------------------------------------------------------

class AssetFunctionAssetModel(AssetModel):
    """ Documentation for a type of an asset function of a particular product model made by a manufacturer.(Organisation). Asset Functions are typically component parts of Assets or Asset Containers.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    AssetFunctionTypeAsset = Instance("CIM.IEC61968.Informative.InfTypeAsset.AssetFunctionTypeAsset",
        transient=True,
        opposite="AssetFunctionAssetModels",
        editor=InstanceEditor(name="_assetfunctiontypeassets"))

    def _get_assetfunctiontypeassets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfTypeAsset.AssetFunctionTypeAsset" ]
        else:
            return []

    _assetfunctiontypeassets = Property(fget=_get_assetfunctiontypeassets)

    AssetFunctions = List(Instance("CIM.IEC61968.Assets.AssetFunction"))

    #--------------------------------------------------------------------------
    #  Begin "AssetFunctionAssetModel" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "corporateStandardKind", "usageKind", "modelNumber", "weightTotal", "modelVersion",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "ErpInventoryCounts", "TypeAsset", "AssetModelCatalogueItems", "AssetFunctionTypeAsset", "AssetFunctions",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssetModels.AssetFunctionAssetModel",
        title="AssetFunctionAssetModel",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "AssetFunctionAssetModel" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ConductorAssetModel" class:
#------------------------------------------------------------------------------

class ConductorAssetModel(AssetModel):
    """ A type of conductor made by a particular manufacturer (Organisation). Its ElectricalProperties are defined as being per unit length (which is defined by the unitLength attribute)
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ConductorAssets = List(Instance("CIM.IEC61968.Informative.InfAssets.ConductorAsset"))

    ConductorInfo = Instance("CIM.IEC61968.AssetModels.ConductorInfo",
        transient=True,
        opposite="ConductorAssetModel",
        editor=InstanceEditor(name="_conductorinfos"))

    def _get_conductorinfos(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.AssetModels.ConductorInfo" ]
        else:
            return []

    _conductorinfos = Property(fget=_get_conductorinfos)

    #--------------------------------------------------------------------------
    #  Begin "ConductorAssetModel" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "corporateStandardKind", "usageKind", "modelNumber", "weightTotal", "modelVersion",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "ErpInventoryCounts", "TypeAsset", "AssetModelCatalogueItems", "ConductorAssets", "ConductorInfo",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssetModels.ConductorAssetModel",
        title="ConductorAssetModel",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ConductorAssetModel" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ComFunctionAssetModel" class:
#------------------------------------------------------------------------------

class ComFunctionAssetModel(ElectricalAssetModel):
    """ Documentation for a type of communication function of a particular product model made by a manufacturer.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ComFunctionTypeAsset = Instance("CIM.IEC61968.Informative.InfTypeAsset.ComFunctionTypeAsset",
        transient=True,
        opposite="ComFunctionAssetModels",
        editor=InstanceEditor(name="_comfunctiontypeassets"))

    def _get_comfunctiontypeassets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfTypeAsset.ComFunctionTypeAsset" ]
        else:
            return []

    _comfunctiontypeassets = Property(fget=_get_comfunctiontypeassets)

    #--------------------------------------------------------------------------
    #  Begin "ComFunctionAssetModel" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "corporateStandardKind", "usageKind", "modelNumber", "weightTotal", "modelVersion",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "ErpInventoryCounts", "TypeAsset", "AssetModelCatalogueItems", "ElectricalInfos", "ComFunctionTypeAsset",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssetModels.ComFunctionAssetModel",
        title="ComFunctionAssetModel",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ComFunctionAssetModel" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SwitchAssetModel" class:
#------------------------------------------------------------------------------

class SwitchAssetModel(ElectricalAssetModel):
    """ Documentation for a type of a switch asset of a particular product model made by a manufacturer.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    SwitchTypeAsset = Instance("CIM.IEC61968.Informative.InfTypeAsset.SwitchTypeAsset",
        transient=True,
        opposite="SwitchAssetModels",
        editor=InstanceEditor(name="_switchtypeassets"))

    def _get_switchtypeassets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfTypeAsset.SwitchTypeAsset" ]
        else:
            return []

    _switchtypeassets = Property(fget=_get_switchtypeassets)

    SwitchAssets = List(Instance("CIM.IEC61968.Informative.InfAssets.SwitchAsset"))

    SwitchInfo = Instance("CIM.IEC61968.Informative.InfAssets.SwitchInfo",
        transient=True,
        opposite="SwitchAssetModel",
        editor=InstanceEditor(name="_switchinfos"))

    def _get_switchinfos(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssets.SwitchInfo" ]
        else:
            return []

    _switchinfos = Property(fget=_get_switchinfos)

    #--------------------------------------------------------------------------
    #  Begin "SwitchAssetModel" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "corporateStandardKind", "usageKind", "modelNumber", "weightTotal", "modelVersion",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "ErpInventoryCounts", "TypeAsset", "AssetModelCatalogueItems", "ElectricalInfos", "SwitchTypeAsset", "SwitchAssets", "SwitchInfo",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssetModels.SwitchAssetModel",
        title="SwitchAssetModel",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SwitchAssetModel" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "MeterAssetModel" class:
#------------------------------------------------------------------------------

class MeterAssetModel(ElectricalAssetModel):
    """ Documentation for a type of a meter asset of a particular product model made by a manufacturer.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    MeterTypeAsset = Instance("CIM.IEC61968.Informative.InfTypeAsset.MeterTypeAsset",
        transient=True,
        opposite="MeterAssetModels",
        editor=InstanceEditor(name="_metertypeassets"))

    def _get_metertypeassets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfTypeAsset.MeterTypeAsset" ]
        else:
            return []

    _metertypeassets = Property(fget=_get_metertypeassets)

    MeterAssets = List(Instance("CIM.IEC61968.Metering.MeterAsset"))

    # True when the meter is capable of metering apparent energy in kVAh.
    kVAhMeter = Bool(desc="True when the meter is capable of metering apparent energy in kVAh.")

    # True when the meter or the installed AMR option is capable of capturing interval data for a user selectable measurement (kWh, Volts, or some other billing or engineering quantity).
    intervalDataMeter = Bool(desc="True when the meter or the installed AMR option is capable of capturing interval data for a user selectable measurement (kWh, Volts, or some other billing or engineering quantity).")

    # Maximum number of registers this meter model can support. The actual number in use is based on the number of Registers associated with a given MeterAsset.
    maxRegisterCount = Int(desc="Maximum number of registers this meter model can support. The actual number in use is based on the number of Registers associated with a given MeterAsset.")

    # Number of wires.
    wireCount = Int(desc="Number of wires.")

    # Meter kh (watthour) constant. This constant is the number of watthours that must be applied to the meter to cause one disk revolution for an electromechanical meter or the number of watthours represented by one increment pulse for an electronic meter.
    kH = Float(desc="Meter kh (watthour) constant. This constant is the number of watthours that must be applied to the meter to cause one disk revolution for an electromechanical meter or the number of watthours represented by one increment pulse for an electronic meter.")

    # True when the meter or meter+AMR module are capable of offering TOU data.
    timeOfUseMeter = Bool(desc="True when the meter or meter+AMR module are capable of offering TOU data.")

    # Meter form number.
    form = Str(desc="Meter form number.")

    # Meter register ratio.
    registerRatio = Float(desc="Meter register ratio.")

    # True when the meter or installed AMR option is capable of capturing demand data.
    demandMeter = Bool(desc="True when the meter or installed AMR option is capable of capturing demand data.")

    # True when the meter is capable of metering reactive energy in kVArh.
    reactiveMeter = Bool(desc="True when the meter is capable of metering reactive energy in kVArh.")

    # True when the meter or the installed AMR option is capable of capturing kWh interval data.
    loadProfileMeter = Bool(desc="True when the meter or the installed AMR option is capable of capturing kWh interval data.")

    # True when the meter is capable of metering real energy in kWh.
    kwhMeter = Bool(desc="True when the meter is capable of metering real energy in kWh.")

    # True when the meter is capable of metering reactive energy in kQh.
    qMeter = Bool(desc="True when the meter is capable of metering reactive energy in kQh.")

    #--------------------------------------------------------------------------
    #  Begin "MeterAssetModel" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "corporateStandardKind", "usageKind", "modelNumber", "weightTotal", "modelVersion", "kVAhMeter", "intervalDataMeter", "maxRegisterCount", "wireCount", "kH", "timeOfUseMeter", "form", "registerRatio", "demandMeter", "reactiveMeter", "loadProfileMeter", "kwhMeter", "qMeter",
                label="Attributes", columns=2),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "ErpInventoryCounts", "TypeAsset", "AssetModelCatalogueItems", "ElectricalInfos", "MeterTypeAsset", "MeterAssets",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssetModels.MeterAssetModel",
        title="MeterAssetModel",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "MeterAssetModel" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "FACTSDeviceAssetModel" class:
#------------------------------------------------------------------------------

class FACTSDeviceAssetModel(ElectricalAssetModel):
    """ A particular model of FACTS device provided from a manufacturer. A FACTS devices are used for the dynamic control of voltage, impedance and phase angle of high voltage AC transmission lines. FACTS device types include: - SVC = Static Var Compensator - STATCOM = Static Synchronous Compensator - TCPAR = Thyristor Controlled Phase-Angle Regulator - TCSC = Thyristor Controlled Series Capacitor - TCVL = Thyristor Controlled Voltage Limiter - TSBR = Thyristor Switched Braking Resistor - TSSC = Thyristor Switched Series Capacitor - UPFC = Unified Power Flow Controller
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    FACTSDeviceAssets = List(Instance("CIM.IEC61968.Informative.InfAssets.FACTSDeviceAsset"))

    FACTSDeviceTypeAsset = Instance("CIM.IEC61968.Informative.InfTypeAsset.FACTSDeviceTypeAsset",
        transient=True,
        opposite="FACTSDeviceAssetModels",
        editor=InstanceEditor(name="_factsdevicetypeassets"))

    def _get_factsdevicetypeassets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfTypeAsset.FACTSDeviceTypeAsset" ]
        else:
            return []

    _factsdevicetypeassets = Property(fget=_get_factsdevicetypeassets)

    #--------------------------------------------------------------------------
    #  Begin "FACTSDeviceAssetModel" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "corporateStandardKind", "usageKind", "modelNumber", "weightTotal", "modelVersion",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "ErpInventoryCounts", "TypeAsset", "AssetModelCatalogueItems", "ElectricalInfos", "FACTSDeviceAssets", "FACTSDeviceTypeAsset",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssetModels.FACTSDeviceAssetModel",
        title="FACTSDeviceAssetModel",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "FACTSDeviceAssetModel" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "RecloserAssetModel" class:
#------------------------------------------------------------------------------

class RecloserAssetModel(ElectricalAssetModel):
    """ Documentation for a type of a recloser asset of a particular product model made by a manufacturer.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    RecloserInfo = Instance("CIM.IEC61968.Informative.InfAssets.RecloserInfo",
        transient=True,
        opposite="RecloserAssetModels",
        editor=InstanceEditor(name="_recloserinfos"))

    def _get_recloserinfos(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssets.RecloserInfo" ]
        else:
            return []

    _recloserinfos = Property(fget=_get_recloserinfos)

    RecloserTypeAsset = Instance("CIM.IEC61968.Informative.InfTypeAsset.RecloserTypeAsset",
        transient=True,
        opposite="RecloserAssetModels",
        editor=InstanceEditor(name="_reclosertypeassets"))

    def _get_reclosertypeassets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfTypeAsset.RecloserTypeAsset" ]
        else:
            return []

    _reclosertypeassets = Property(fget=_get_reclosertypeassets)

    RecloserAssets = List(Instance("CIM.IEC61968.Informative.InfAssets.RecloserAsset"))

    #--------------------------------------------------------------------------
    #  Begin "RecloserAssetModel" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "corporateStandardKind", "usageKind", "modelNumber", "weightTotal", "modelVersion",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "ErpInventoryCounts", "TypeAsset", "AssetModelCatalogueItems", "ElectricalInfos", "RecloserInfo", "RecloserTypeAsset", "RecloserAssets",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssetModels.RecloserAssetModel",
        title="RecloserAssetModel",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "RecloserAssetModel" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ShuntCompensatorAssetModel" class:
#------------------------------------------------------------------------------

class ShuntCompensatorAssetModel(ElectricalAssetModel):
    """ For application as shunt capacitor or reactor or switchable bank of shunt capacitors or reactors, this is documentation for a type of a capacitor or reactor of a particular product model made by a manufacturer (Organisation). There are typically many instances of an asset associated with a single asset model.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ShuntCompensatorAssets = List(Instance("CIM.IEC61968.Informative.InfAssets.ShuntCompensatorAsset"))

    ShuntCompensatorTypeAsset = Instance("CIM.IEC61968.Informative.InfTypeAsset.ShuntCompensatorTypeAsset",
        transient=True,
        opposite="ShuntCompensatorAssetModels",
        editor=InstanceEditor(name="_shuntcompensatortypeassets"))

    def _get_shuntcompensatortypeassets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfTypeAsset.ShuntCompensatorTypeAsset" ]
        else:
            return []

    _shuntcompensatortypeassets = Property(fget=_get_shuntcompensatortypeassets)

    ShuntImpedanceInfo = Instance("CIM.IEC61968.Informative.InfAssets.ShuntImpedanceInfo",
        transient=True,
        opposite="ShuntCompensatorAssetModel",
        editor=InstanceEditor(name="_shuntimpedanceinfos"))

    def _get_shuntimpedanceinfos(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssets.ShuntImpedanceInfo" ]
        else:
            return []

    _shuntimpedanceinfos = Property(fget=_get_shuntimpedanceinfos)

    #--------------------------------------------------------------------------
    #  Begin "ShuntCompensatorAssetModel" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "corporateStandardKind", "usageKind", "modelNumber", "weightTotal", "modelVersion",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "ErpInventoryCounts", "TypeAsset", "AssetModelCatalogueItems", "ElectricalInfos", "ShuntCompensatorAssets", "ShuntCompensatorTypeAsset", "ShuntImpedanceInfo",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssetModels.ShuntCompensatorAssetModel",
        title="ShuntCompensatorAssetModel",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ShuntCompensatorAssetModel" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SVCAssetModel" class:
#------------------------------------------------------------------------------

class SVCAssetModel(FACTSDeviceAssetModel):
    """ Documentation for a type of a Static Var Compensator of a particular product model made by a manufacturer.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    SvcInfo = Instance("CIM.IEC61968.Informative.InfAssets.SVCInfo",
        transient=True,
        opposite="SVCAssetModel",
        editor=InstanceEditor(name="_svcinfos"))

    def _get_svcinfos(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssets.SVCInfo" ]
        else:
            return []

    _svcinfos = Property(fget=_get_svcinfos)

    SVCTypeAsset = Instance("CIM.IEC61968.Informative.InfTypeAsset.SVCTypeAsset",
        transient=True,
        opposite="SVCAssetModels",
        editor=InstanceEditor(name="_svctypeassets"))

    def _get_svctypeassets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfTypeAsset.SVCTypeAsset" ]
        else:
            return []

    _svctypeassets = Property(fget=_get_svctypeassets)

    SVCAssets = List(Instance("CIM.IEC61968.Informative.InfAssets.SVCAsset"))

    #--------------------------------------------------------------------------
    #  Begin "SVCAssetModel" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "corporateStandardKind", "usageKind", "modelNumber", "weightTotal", "modelVersion",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "ErpInventoryCounts", "TypeAsset", "AssetModelCatalogueItems", "ElectricalInfos", "FACTSDeviceAssets", "FACTSDeviceTypeAsset", "SvcInfo", "SVCTypeAsset", "SVCAssets",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssetModels.SVCAssetModel",
        title="SVCAssetModel",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SVCAssetModel" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "BreakerAssetModel" class:
#------------------------------------------------------------------------------

class BreakerAssetModel(ElectricalAssetModel):
    """ Documentation for a type of a breaker asset of a particular product model made by a manufacturer.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    BreakerInfo = Instance("CIM.IEC61968.Informative.InfAssets.BreakerInfo",
        transient=True,
        opposite="BreakerAssetModels",
        editor=InstanceEditor(name="_breakerinfos"))

    def _get_breakerinfos(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssets.BreakerInfo" ]
        else:
            return []

    _breakerinfos = Property(fget=_get_breakerinfos)

    BreakerAssets = List(Instance("CIM.IEC61968.Informative.InfAssets.BreakerAsset"))

    BreakerTypeAsset = Instance("CIM.IEC61968.Informative.InfTypeAsset.BreakerTypeAsset",
        transient=True,
        opposite="BreakerAssetModels",
        editor=InstanceEditor(name="_breakertypeassets"))

    def _get_breakertypeassets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfTypeAsset.BreakerTypeAsset" ]
        else:
            return []

    _breakertypeassets = Property(fget=_get_breakertypeassets)

    #--------------------------------------------------------------------------
    #  Begin "BreakerAssetModel" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "corporateStandardKind", "usageKind", "modelNumber", "weightTotal", "modelVersion",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "ErpInventoryCounts", "TypeAsset", "AssetModelCatalogueItems", "ElectricalInfos", "BreakerInfo", "BreakerAssets", "BreakerTypeAsset",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssetModels.BreakerAssetModel",
        title="BreakerAssetModel",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "BreakerAssetModel" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GeneratorAssetModel" class:
#------------------------------------------------------------------------------

class GeneratorAssetModel(ElectricalAssetModel):
    """ Documentation for a type of generation equipment of a particular product model made by a manufacturer.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    GeneratorAssets = List(Instance("CIM.IEC61968.Informative.InfAssets.GeneratorAsset"))

    GeneratorTypeAsset = Instance("CIM.IEC61968.Informative.InfTypeAsset.GeneratorTypeAsset",
        transient=True,
        opposite="GeneratorAssetModels",
        editor=InstanceEditor(name="_generatortypeassets"))

    def _get_generatortypeassets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfTypeAsset.GeneratorTypeAsset" ]
        else:
            return []

    _generatortypeassets = Property(fget=_get_generatortypeassets)

    #--------------------------------------------------------------------------
    #  Begin "GeneratorAssetModel" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "corporateStandardKind", "usageKind", "modelNumber", "weightTotal", "modelVersion",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "ErpInventoryCounts", "TypeAsset", "AssetModelCatalogueItems", "ElectricalInfos", "GeneratorAssets", "GeneratorTypeAsset",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssetModels.GeneratorAssetModel",
        title="GeneratorAssetModel",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GeneratorAssetModel" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ResistorAssetModel" class:
#------------------------------------------------------------------------------

class ResistorAssetModel(ElectricalAssetModel):
    """ Documentation for a type of a resistor asset of a particular product model made by a manufacturer.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ResistorTypeAsset = Instance("CIM.IEC61968.Informative.InfTypeAsset.ResistorTypeAsset",
        transient=True,
        opposite="ResistorAssetModels",
        editor=InstanceEditor(name="_resistortypeassets"))

    def _get_resistortypeassets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfTypeAsset.ResistorTypeAsset" ]
        else:
            return []

    _resistortypeassets = Property(fget=_get_resistortypeassets)

    ResistorAssets = List(Instance("CIM.IEC61968.Informative.InfAssets.ResistorAsset"))

    #--------------------------------------------------------------------------
    #  Begin "ResistorAssetModel" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "corporateStandardKind", "usageKind", "modelNumber", "weightTotal", "modelVersion",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "ErpInventoryCounts", "TypeAsset", "AssetModelCatalogueItems", "ElectricalInfos", "ResistorTypeAsset", "ResistorAssets",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssetModels.ResistorAssetModel",
        title="ResistorAssetModel",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ResistorAssetModel" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SurgeProtectorAssetModel" class:
#------------------------------------------------------------------------------

class SurgeProtectorAssetModel(ElectricalAssetModel):
    """ Documentation for a type of an SurgeProtector asset of a particular product model made by a manufacturer.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    SurgeProtectorTypeAsset = Instance("CIM.IEC61968.Informative.InfTypeAsset.SurgeProtectorTypeAsset",
        transient=True,
        opposite="SurgeProtectorAssetModels",
        editor=InstanceEditor(name="_surgeprotectortypeassets"))

    def _get_surgeprotectortypeassets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfTypeAsset.SurgeProtectorTypeAsset" ]
        else:
            return []

    _surgeprotectortypeassets = Property(fget=_get_surgeprotectortypeassets)

    SurgeProtectorAssets = List(Instance("CIM.IEC61968.Informative.InfAssets.SurgeProtectorAsset"))

    #--------------------------------------------------------------------------
    #  Begin "SurgeProtectorAssetModel" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "corporateStandardKind", "usageKind", "modelNumber", "weightTotal", "modelVersion",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "ErpInventoryCounts", "TypeAsset", "AssetModelCatalogueItems", "ElectricalInfos", "SurgeProtectorTypeAsset", "SurgeProtectorAssets",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssetModels.SurgeProtectorAssetModel",
        title="SurgeProtectorAssetModel",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SurgeProtectorAssetModel" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ProtectionEquipmentAssetModel" class:
#------------------------------------------------------------------------------

class ProtectionEquipmentAssetModel(ElectricalAssetModel):
    """ Documentation for a type of protection equipment asset of a particular product model made by a manufacturer.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ProtectionEquipmentAssets = List(Instance("CIM.IEC61968.Informative.InfAssets.ProtectionEquipmentAsset"))

    ProtectionEquipmentTypeAsset = Instance("CIM.IEC61968.Informative.InfTypeAsset.ProtectionEquipmentTypeAsset",
        transient=True,
        opposite="ProtectionEquipmentAssetModels",
        editor=InstanceEditor(name="_protectionequipmenttypeassets"))

    def _get_protectionequipmenttypeassets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfTypeAsset.ProtectionEquipmentTypeAsset" ]
        else:
            return []

    _protectionequipmenttypeassets = Property(fget=_get_protectionequipmenttypeassets)

    #--------------------------------------------------------------------------
    #  Begin "ProtectionEquipmentAssetModel" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "corporateStandardKind", "usageKind", "modelNumber", "weightTotal", "modelVersion",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "ErpInventoryCounts", "TypeAsset", "AssetModelCatalogueItems", "ElectricalInfos", "ProtectionEquipmentAssets", "ProtectionEquipmentTypeAsset",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssetModels.ProtectionEquipmentAssetModel",
        title="ProtectionEquipmentAssetModel",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ProtectionEquipmentAssetModel" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "PotentialTransformerAssetModel" class:
#------------------------------------------------------------------------------

class PotentialTransformerAssetModel(ElectricalAssetModel):
    """ A particular model supplied by a manufacturer of a Potential Transformer (PT), wich is used to measure electrical qualities of the circuit that is being protected and/or monitored.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    PotentialTransformerTypeAsset = Instance("CIM.IEC61968.Informative.InfTypeAsset.PotentialTransformerTypeAsset",
        transient=True,
        opposite="PotentialTransformerAssetModels",
        editor=InstanceEditor(name="_potentialtransformertypeassets"))

    def _get_potentialtransformertypeassets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfTypeAsset.PotentialTransformerTypeAsset" ]
        else:
            return []

    _potentialtransformertypeassets = Property(fget=_get_potentialtransformertypeassets)

    PotentialTransformerInfo = Instance("CIM.IEC61968.Informative.InfAssets.PotentialTransformerInfo",
        transient=True,
        opposite="PotentialTransformerAssetModels",
        editor=InstanceEditor(name="_potentialtransformerinfos"))

    def _get_potentialtransformerinfos(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssets.PotentialTransformerInfo" ]
        else:
            return []

    _potentialtransformerinfos = Property(fget=_get_potentialtransformerinfos)

    PotentialTransformerAssets = List(Instance("CIM.IEC61968.Informative.InfAssets.PotentialTransformerAsset"))

    #--------------------------------------------------------------------------
    #  Begin "PotentialTransformerAssetModel" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "corporateStandardKind", "usageKind", "modelNumber", "weightTotal", "modelVersion",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "ErpInventoryCounts", "TypeAsset", "AssetModelCatalogueItems", "ElectricalInfos", "PotentialTransformerTypeAsset", "PotentialTransformerInfo", "PotentialTransformerAssets",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssetModels.PotentialTransformerAssetModel",
        title="PotentialTransformerAssetModel",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "PotentialTransformerAssetModel" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "BushingModel" class:
#------------------------------------------------------------------------------

class BushingModel(ElectricalAssetModel):
    """ Documentation for a type of a bushing of a particular product model made by a manufacturer.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    BushingAsset = Instance("CIM.IEC61968.Informative.InfAssets.BushingAsset",
        transient=True,
        opposite="BushingModel",
        editor=InstanceEditor(name="_bushingassets"))

    def _get_bushingassets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssets.BushingAsset" ]
        else:
            return []

    _bushingassets = Property(fget=_get_bushingassets)

    # Kind of insulation used in this bushing model.
    insulationKind = BushingInsulationKind(desc="Kind of insulation used in this bushing model.")

    #--------------------------------------------------------------------------
    #  Begin "BushingModel" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "corporateStandardKind", "usageKind", "modelNumber", "weightTotal", "modelVersion", "insulationKind",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "ErpInventoryCounts", "TypeAsset", "AssetModelCatalogueItems", "ElectricalInfos", "BushingAsset",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssetModels.BushingModel",
        title="BushingModel",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "BushingModel" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "CurrentTransformerAssetModel" class:
#------------------------------------------------------------------------------

class CurrentTransformerAssetModel(ElectricalAssetModel):
    """ A particular model supplied by a manufacturer of a Current Transformer (CT), wich is used to measure electrical qualities of the circuit that is being protected and/or monitored.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    CurrentTransformerTypeAsset = Instance("CIM.IEC61968.Informative.InfTypeAsset.CurrentTransformerTypeAsset",
        transient=True,
        opposite="CurrentTransformerAssetModels",
        editor=InstanceEditor(name="_currenttransformertypeassets"))

    def _get_currenttransformertypeassets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfTypeAsset.CurrentTransformerTypeAsset" ]
        else:
            return []

    _currenttransformertypeassets = Property(fget=_get_currenttransformertypeassets)

    CurrentTransformerInfo = Instance("CIM.IEC61968.Informative.InfAssets.CurrentTransformerInfo",
        transient=True,
        opposite="CurrentTransformerAssertModels",
        editor=InstanceEditor(name="_currenttransformerinfos"))

    def _get_currenttransformerinfos(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssets.CurrentTransformerInfo" ]
        else:
            return []

    _currenttransformerinfos = Property(fget=_get_currenttransformerinfos)

    CurrentTransformerAssets = List(Instance("CIM.IEC61968.Informative.InfAssets.CurrentTransformerAsset"))

    #--------------------------------------------------------------------------
    #  Begin "CurrentTransformerAssetModel" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "corporateStandardKind", "usageKind", "modelNumber", "weightTotal", "modelVersion",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "ErpInventoryCounts", "TypeAsset", "AssetModelCatalogueItems", "ElectricalInfos", "CurrentTransformerTypeAsset", "CurrentTransformerInfo", "CurrentTransformerAssets",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssetModels.CurrentTransformerAssetModel",
        title="CurrentTransformerAssetModel",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "CurrentTransformerAssetModel" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "FaultIndicatorAssetModel" class:
#------------------------------------------------------------------------------

class FaultIndicatorAssetModel(ElectricalAssetModel):
    """ Documentation for a type of an FaultIndicator asset of a particular product model made by a manufacturer.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    FaultIndicatorTypeAsset = Instance("CIM.IEC61968.Informative.InfTypeAsset.FaultIndicatorTypeAsset",
        transient=True,
        opposite="FaultIndicatorAssetModels",
        editor=InstanceEditor(name="_faultindicatortypeassets"))

    def _get_faultindicatortypeassets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfTypeAsset.FaultIndicatorTypeAsset" ]
        else:
            return []

    _faultindicatortypeassets = Property(fget=_get_faultindicatortypeassets)

    FaultIndicatorAssets = List(Instance("CIM.IEC61968.Informative.InfAssets.FaultIndicatorAsset"))

    #--------------------------------------------------------------------------
    #  Begin "FaultIndicatorAssetModel" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "corporateStandardKind", "usageKind", "modelNumber", "weightTotal", "modelVersion",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "ErpInventoryCounts", "TypeAsset", "AssetModelCatalogueItems", "ElectricalInfos", "FaultIndicatorTypeAsset", "FaultIndicatorAssets",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssetModels.FaultIndicatorAssetModel",
        title="FaultIndicatorAssetModel",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "FaultIndicatorAssetModel" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "StreetlightAssetModel" class:
#------------------------------------------------------------------------------

class StreetlightAssetModel(ElectricalAssetModel):
    """ Documentation for a type of a streelight of a particular product model made by a manufacturer.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Streetlights = List(Instance("CIM.IEC61968.Informative.InfAssets.Streetlight"))

    StreetlightTypeAssets = List(Instance("CIM.IEC61968.Informative.InfTypeAsset.StreetlightTypeAsset"))

    # Lamp kind supplied from manufacturer (vs. one that has been replaced in the field).
    lampKind = StreetlightLampKind(desc="Lamp kind supplied from manufacturer (vs. one that has been replaced in the field).")

    # Power rating of light as supplied by the manufacturer.
    lightRating = ActivePower(desc="Power rating of light as supplied by the manufacturer.")

    #--------------------------------------------------------------------------
    #  Begin "StreetlightAssetModel" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "corporateStandardKind", "usageKind", "modelNumber", "weightTotal", "modelVersion", "lampKind", "lightRating",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "ErpInventoryCounts", "TypeAsset", "AssetModelCatalogueItems", "ElectricalInfos", "Streetlights", "StreetlightTypeAssets",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssetModels.StreetlightAssetModel",
        title="StreetlightAssetModel",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "StreetlightAssetModel" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SeriesCompensatorAssetModel" class:
#------------------------------------------------------------------------------

class SeriesCompensatorAssetModel(ElectricalAssetModel):
    """ For application as a series capacitor or reactor, this is documentation for a type of a capacitor or reactor of a particular product model made by a manufacturer.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    SeriesCompensatorAsset = Instance("CIM.IEC61968.Informative.InfAssets.SeriesCompensatorAsset",
        transient=True,
        opposite="SeriesCompensatorAssetModel",
        editor=InstanceEditor(name="_seriescompensatorassets"))

    def _get_seriescompensatorassets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssets.SeriesCompensatorAsset" ]
        else:
            return []

    _seriescompensatorassets = Property(fget=_get_seriescompensatorassets)

    ShuntCompensatorTypeAsset = Instance("CIM.IEC61968.Informative.InfTypeAsset.SeriesCompensatorTypeAsset",
        transient=True,
        opposite="ShuntCompensatorAssetModels",
        editor=InstanceEditor(name="_seriescompensatortypeassets"))

    def _get_seriescompensatortypeassets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfTypeAsset.SeriesCompensatorTypeAsset" ]
        else:
            return []

    _seriescompensatortypeassets = Property(fget=_get_seriescompensatortypeassets)

    #--------------------------------------------------------------------------
    #  Begin "SeriesCompensatorAssetModel" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "corporateStandardKind", "usageKind", "modelNumber", "weightTotal", "modelVersion",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "ErpInventoryCounts", "TypeAsset", "AssetModelCatalogueItems", "ElectricalInfos", "SeriesCompensatorAsset", "ShuntCompensatorTypeAsset",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssetModels.SeriesCompensatorAssetModel",
        title="SeriesCompensatorAssetModel",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SeriesCompensatorAssetModel" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "BusbarAssetModel" class:
#------------------------------------------------------------------------------

class BusbarAssetModel(ElectricalAssetModel):
    """ Documentation for a type of a busbar asset of a particular product model made by a manufacturer.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    BusbarAssets = List(Instance("CIM.IEC61968.Informative.InfAssets.BusbarAsset"))

    BusbarAssetModel = Instance("CIM.IEC61968.Informative.InfTypeAsset.BusbarTypeAsset",
        transient=True,
        opposite="BusbarTypeAssets",
        editor=InstanceEditor(name="_busbartypeassets"))

    def _get_busbartypeassets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfTypeAsset.BusbarTypeAsset" ]
        else:
            return []

    _busbartypeassets = Property(fget=_get_busbartypeassets)

    #--------------------------------------------------------------------------
    #  Begin "BusbarAssetModel" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "corporateStandardKind", "usageKind", "modelNumber", "weightTotal", "modelVersion",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "ErpInventoryCounts", "TypeAsset", "AssetModelCatalogueItems", "ElectricalInfos", "BusbarAssets", "BusbarAssetModel",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssetModels.BusbarAssetModel",
        title="BusbarAssetModel",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "BusbarAssetModel" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
