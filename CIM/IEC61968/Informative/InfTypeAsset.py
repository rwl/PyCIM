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

from CIM.IEC61968.Common import Document
from CIM.IEC61970.Core import IdentifiedObject
from CIM.IEC61970.Domain import StringQuantity
from CIM.IEC61970.Domain import Money
from CIM.IEC61970.Domain import ApparentPower
from CIM.IEC61970.Core import PhaseCode
from CIM.IEC61970.Domain import Voltage
from CIM.IEC61970.Domain import ActivePower
from CIM.IEC61970.Domain import Length
from CIM.IEC61970.Domain import CurrentFlow
from CIM.IEC61970.Domain import Resistance
from CIM.IEC61970.Domain import Reactance
from CIM.IEC61970.Domain import ReactivePower



from enthought.traits.api import Instance, List, Property, Enum, Bool, Int, Float, Str
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------

# Kind of resetting the fault indicators.
FaultIndicatorResetKind = Enum("other", "remote", "manual", "automatic", desc="Kind of resetting the fault indicators.")

#------------------------------------------------------------------------------
#  "TypeAsset" class:
#------------------------------------------------------------------------------

class TypeAsset(Document):
    """ Whereas an AssetModel is a particular model and version of a vendor's product, a TypeAsset is documentation for a generic asset or material item that may be used for design purposes. Any number of AssetModels may be used to perform this generic function. The primary role of the TypeAsset is typically defined by the PowereSystemResource it is associated with.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    CUWorkEquipmentAsset = Instance("CIM.IEC61968.Informative.InfWork.CUWorkEquipmentItem",
        transient=True,
        opposite="TypeAsset",
        editor=InstanceEditor(name="_cuworkequipmentitems"))

    def _get_cuworkequipmentitems(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfWork.CUWorkEquipmentItem" ]
        else:
            return []

    _cuworkequipmentitems = Property(fget=_get_cuworkequipmentitems)

    CUAsset = Instance("CIM.IEC61968.Informative.InfWork.CUAsset",
        transient=True,
        opposite="TypeAsset",
        editor=InstanceEditor(name="_cuassets"))

    def _get_cuassets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfWork.CUAsset" ]
        else:
            return []

    _cuassets = Property(fget=_get_cuassets)

    TypeAssetCatalogue = Instance("CIM.IEC61968.Informative.InfTypeAsset.TypeAssetCatalogue",
        transient=True,
        opposite="TypeAssets",
        editor=InstanceEditor(name="_typeassetcatalogues"))

    def _get_typeassetcatalogues(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfTypeAsset.TypeAssetCatalogue" ]
        else:
            return []

    _typeassetcatalogues = Property(fget=_get_typeassetcatalogues)

    # A type of asset may be satisified with many different types of asset models.
    AssetModels = List(Instance("CIM.IEC61968.AssetModels.AssetModel"),
        desc="A type of asset may be satisified with many different types of asset models.")

    ErpInventoryIssues = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpIssueInventory"))

    ErpReqLineItems = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpReqLineItem"))

    ErpBomItemDatas = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpBomItemData"))

    # The value, unit of measure, and multiplier for the quantity.
    quantity = StringQuantity(desc="The value, unit of measure, and multiplier for the quantity.")

    # True if item is a stock item (default).
    stockItem = Bool(desc="True if item is a stock item (default).")

    # Estimated unit cost (or cost per unit length) of this type of asset. It does not include labor to install/construct or configure it.
    estimatedUnitCost = Money(desc="Estimated unit cost (or cost per unit length) of this type of asset. It does not include labor to install/construct or configure it.")

    #--------------------------------------------------------------------------
    #  Begin "TypeAsset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "quantity", "stockItem", "estimatedUnitCost",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "CUWorkEquipmentAsset", "CUAsset", "TypeAssetCatalogue", "AssetModels", "ErpInventoryIssues", "ErpReqLineItems", "ErpBomItemDatas",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfTypeAsset.TypeAsset",
        title="TypeAsset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TypeAsset" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "MountingPoint" class:
#------------------------------------------------------------------------------

class MountingPoint(IdentifiedObject):
    """ Point on a structure that a connection may have a conductor connected to. Defined with an x and y coordinate plus a phase. A connection may have multiple mounting points, one for each phase.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    OverheadConductors = List(Instance("CIM.IEC61968.Informative.InfAssets.OverheadConductorAsset"))

    Connections = List(Instance("CIM.IEC61968.Informative.InfTypeAsset.Connection"))

    phaseCode = PhaseCode

    yCoord = Int

    xCoord = Int

    #--------------------------------------------------------------------------
    #  Begin "MountingPoint" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "phaseCode", "yCoord", "xCoord",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "OverheadConductors", "Connections",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfTypeAsset.MountingPoint",
        title="MountingPoint",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "MountingPoint" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "TypeAssetCatalogue" class:
#------------------------------------------------------------------------------

class TypeAssetCatalogue(IdentifiedObject):
    """ Catalogue of generic types of assets (TypeAsset) that may be used for design purposes. It is not associated with a particular manufacturer.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    TypeAssets = List(Instance("CIM.IEC61968.Informative.InfTypeAsset.TypeAsset"))

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

    #--------------------------------------------------------------------------
    #  Begin "TypeAssetCatalogue" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "TypeAssets", "status",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfTypeAsset.TypeAssetCatalogue",
        title="TypeAssetCatalogue",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TypeAssetCatalogue" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Connection" class:
#------------------------------------------------------------------------------

class Connection(IdentifiedObject):
    """ A structure can have multiple connection points for electrical connections (e.g. line) each with multiple mounting points, one for each phase. e.g. a Tower may have three Connections, two with three mounting points, one for each phase and a third with a single mounting point for the neutral line. A pole, on the other hand, may have a single Connection with one, two or three mounting points depending on whether it is carrying 1,2 or 3 phases.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    StructureTypeAssets = List(Instance("CIM.IEC61968.Informative.InfTypeAsset.StructureTypeAsset"))

    MountingPoints = List(Instance("CIM.IEC61968.Informative.InfTypeAsset.MountingPoint"))

    #--------------------------------------------------------------------------
    #  Begin "Connection" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "StructureTypeAssets", "MountingPoints",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfTypeAsset.Connection",
        title="Connection",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Connection" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ElectricalTypeAsset" class:
#------------------------------------------------------------------------------

class ElectricalTypeAsset(TypeAsset):
    """ Generic TypeAsset for all types of component in the network that have electrical characteristics.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ElectricalInfos = List(Instance("CIM.IEC61968.Assets.ElectricalInfo"))

    #--------------------------------------------------------------------------
    #  Begin "ElectricalTypeAsset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "quantity", "stockItem", "estimatedUnitCost",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "CUWorkEquipmentAsset", "CUAsset", "TypeAssetCatalogue", "AssetModels", "ErpInventoryIssues", "ErpReqLineItems", "ErpBomItemDatas", "ElectricalInfos",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfTypeAsset.ElectricalTypeAsset",
        title="ElectricalTypeAsset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ElectricalTypeAsset" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ShuntCompensatorTypeAsset" class:
#------------------------------------------------------------------------------

class ShuntCompensatorTypeAsset(ElectricalTypeAsset):
    """ Documentation for a generic shunt compensator that may be used for design purposes.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ShuntImpedanceInfo = Instance("CIM.IEC61968.Informative.InfAssets.ShuntImpedanceInfo",
        transient=True,
        opposite="ShuntCompensatorTypeAsset",
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

    ShuntCompensatorAssetModels = List(Instance("CIM.IEC61968.Informative.InfAssetModels.ShuntCompensatorAssetModel"))

    # Maximum allowed Apparent Power loss
    maxPowerLoss = ApparentPower(desc="Maximum allowed Apparent Power loss")

    #--------------------------------------------------------------------------
    #  Begin "ShuntCompensatorTypeAsset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "quantity", "stockItem", "estimatedUnitCost", "maxPowerLoss",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "CUWorkEquipmentAsset", "CUAsset", "TypeAssetCatalogue", "AssetModels", "ErpInventoryIssues", "ErpReqLineItems", "ErpBomItemDatas", "ElectricalInfos", "ShuntImpedanceInfo", "ShuntCompensatorAssetModels",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfTypeAsset.ShuntCompensatorTypeAsset",
        title="ShuntCompensatorTypeAsset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ShuntCompensatorTypeAsset" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "EndDeviceTypeAsset" class:
#------------------------------------------------------------------------------

class EndDeviceTypeAsset(TypeAsset):
    """ Documentation for generic End Device that may be used for various purposes such as work planning.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    EndDeviceModels = List(Instance("CIM.IEC61968.AssetModels.EndDeviceModel"))

    #--------------------------------------------------------------------------
    #  Begin "EndDeviceTypeAsset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "quantity", "stockItem", "estimatedUnitCost",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "CUWorkEquipmentAsset", "CUAsset", "TypeAssetCatalogue", "AssetModels", "ErpInventoryIssues", "ErpReqLineItems", "ErpBomItemDatas", "EndDeviceModels",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfTypeAsset.EndDeviceTypeAsset",
        title="EndDeviceTypeAsset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "EndDeviceTypeAsset" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "BusbarTypeAsset" class:
#------------------------------------------------------------------------------

class BusbarTypeAsset(ElectricalTypeAsset):
    """ Documentation for a generic busbar that may be used for design purposes. It is typically associated with PoserSystemResource BusbarSection.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    BusbarTypeAssets = List(Instance("CIM.IEC61968.Informative.InfAssetModels.BusbarAssetModel"))

    #--------------------------------------------------------------------------
    #  Begin "BusbarTypeAsset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "quantity", "stockItem", "estimatedUnitCost",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "CUWorkEquipmentAsset", "CUAsset", "TypeAssetCatalogue", "AssetModels", "ErpInventoryIssues", "ErpReqLineItems", "ErpBomItemDatas", "ElectricalInfos", "BusbarTypeAssets",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfTypeAsset.BusbarTypeAsset",
        title="BusbarTypeAsset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "BusbarTypeAsset" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "WorkEquipmentTypeAsset" class:
#------------------------------------------------------------------------------

class WorkEquipmentTypeAsset(TypeAsset):
    """ Documentation for generic equipment that may be used for various purposes such as work planning.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    WorkEquipmentAssetModels = List(Instance("CIM.IEC61968.Informative.InfAssetModels.WorkEquipmentAssetModel"))

    #--------------------------------------------------------------------------
    #  Begin "WorkEquipmentTypeAsset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "quantity", "stockItem", "estimatedUnitCost",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "CUWorkEquipmentAsset", "CUAsset", "TypeAssetCatalogue", "AssetModels", "ErpInventoryIssues", "ErpReqLineItems", "ErpBomItemDatas", "WorkEquipmentAssetModels",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfTypeAsset.WorkEquipmentTypeAsset",
        title="WorkEquipmentTypeAsset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "WorkEquipmentTypeAsset" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SwitchTypeAsset" class:
#------------------------------------------------------------------------------

class SwitchTypeAsset(ElectricalTypeAsset):
    """ Documentation for a generic switch asset that may be used for design purposes.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    SwitchAssetModels = List(Instance("CIM.IEC61968.Informative.InfAssetModels.SwitchAssetModel"))

    CompositeSwitchTypeAsset = Instance("CIM.IEC61968.Informative.InfTypeAsset.CompositeSwitchTypeAsset",
        transient=True,
        opposite="SwitchTypesAssets",
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

    SwitchInfo = Instance("CIM.IEC61968.Informative.InfAssets.SwitchInfo",
        transient=True,
        opposite="SwitchTypeAsset",
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
    #  Begin "SwitchTypeAsset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "quantity", "stockItem", "estimatedUnitCost",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "CUWorkEquipmentAsset", "CUAsset", "TypeAssetCatalogue", "AssetModels", "ErpInventoryIssues", "ErpReqLineItems", "ErpBomItemDatas", "ElectricalInfos", "SwitchAssetModels", "CompositeSwitchTypeAsset", "SwitchInfo",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfTypeAsset.SwitchTypeAsset",
        title="SwitchTypeAsset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SwitchTypeAsset" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "StructureTypeAsset" class:
#------------------------------------------------------------------------------

class StructureTypeAsset(TypeAsset):
    """ A Type of Structural Asset with properties common to a large number of asset models.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    MountConnections = List(Instance("CIM.IEC61968.Informative.InfTypeAsset.Connection"))

    # Maximum rated voltage of the equipment that can be mounted on/contained within the structure.
    ratedVoltage = Voltage(desc="Maximum rated voltage of the equipment that can be mounted on/contained within the structure.")

    #--------------------------------------------------------------------------
    #  Begin "StructureTypeAsset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "quantity", "stockItem", "estimatedUnitCost", "ratedVoltage",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "CUWorkEquipmentAsset", "CUAsset", "TypeAssetCatalogue", "AssetModels", "ErpInventoryIssues", "ErpReqLineItems", "ErpBomItemDatas", "MountConnections",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfTypeAsset.StructureTypeAsset",
        title="StructureTypeAsset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "StructureTypeAsset" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "TowerTypeAsset" class:
#------------------------------------------------------------------------------

class TowerTypeAsset(StructureTypeAsset):
    """ Documentation for a generic tower that may be used for various purposes such as work planning. A transmission tower carrying two 3-phase circuits will have 2 instances of Connection, each of which will have 3 MountingPoint instances, one for each phase all with coordinates relative to a common origin on the tower. (It may also have a 3rd Connection with a single MountingPoint for the Neutral line).
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    TowerAssetModels = List(Instance("CIM.IEC61968.Informative.InfAssetModels.TowerAssetModel"))

    #--------------------------------------------------------------------------
    #  Begin "TowerTypeAsset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "quantity", "stockItem", "estimatedUnitCost", "ratedVoltage",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "CUWorkEquipmentAsset", "CUAsset", "TypeAssetCatalogue", "AssetModels", "ErpInventoryIssues", "ErpReqLineItems", "ErpBomItemDatas", "MountConnections", "TowerAssetModels",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfTypeAsset.TowerTypeAsset",
        title="TowerTypeAsset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TowerTypeAsset" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "StreetlightTypeAsset" class:
#------------------------------------------------------------------------------

class StreetlightTypeAsset(ElectricalTypeAsset):
    """ Documentation for a generic streetlight that may be used for various purposes such as work planning. Use 'category' for utility specific categorisation, such as luminar, grid light, lantern, open bottom, flood, etc.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    StreetlightAssetModels = List(Instance("CIM.IEC61968.Informative.InfAssetModels.StreetlightAssetModel"))

    # Nominal (as designed) power rating of light.
    lightRating = ActivePower(desc="Nominal (as designed) power rating of light.")

    #--------------------------------------------------------------------------
    #  Begin "StreetlightTypeAsset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "quantity", "stockItem", "estimatedUnitCost", "lightRating",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "CUWorkEquipmentAsset", "CUAsset", "TypeAssetCatalogue", "AssetModels", "ErpInventoryIssues", "ErpReqLineItems", "ErpBomItemDatas", "ElectricalInfos", "StreetlightAssetModels",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfTypeAsset.StreetlightTypeAsset",
        title="StreetlightTypeAsset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "StreetlightTypeAsset" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ToolTypeAsset" class:
#------------------------------------------------------------------------------

class ToolTypeAsset(TypeAsset):
    """ Documentation for a generic tool that may be used for various purposes such as work planning.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ToolAssetModels = List(Instance("CIM.IEC61968.Informative.InfAssetModels.ToolAssetModel"))

    #--------------------------------------------------------------------------
    #  Begin "ToolTypeAsset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "quantity", "stockItem", "estimatedUnitCost",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "CUWorkEquipmentAsset", "CUAsset", "TypeAssetCatalogue", "AssetModels", "ErpInventoryIssues", "ErpReqLineItems", "ErpBomItemDatas", "ToolAssetModels",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfTypeAsset.ToolTypeAsset",
        title="ToolTypeAsset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ToolTypeAsset" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "CompositeSwitchTypeAsset" class:
#------------------------------------------------------------------------------

class CompositeSwitchTypeAsset(TypeAsset):
    """ Documentation for a generic composite switch asset that may be used for design purposes. A composite wwitch is an amalgamation of multiple Switches.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    CompositeSwitchAssetModels = List(Instance("CIM.IEC61968.Informative.InfAssetModels.CompositeSwitchAssetModel"))

    SwitchTypesAssets = List(Instance("CIM.IEC61968.Informative.InfTypeAsset.SwitchTypeAsset"))

    CompositeSwitchInfo = Instance("CIM.IEC61968.Informative.InfAssets.CompositeSwitchInfo",
        transient=True,
        opposite="CompositeSwitchTypeAsset",
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

    #--------------------------------------------------------------------------
    #  Begin "CompositeSwitchTypeAsset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "quantity", "stockItem", "estimatedUnitCost",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "CUWorkEquipmentAsset", "CUAsset", "TypeAssetCatalogue", "AssetModels", "ErpInventoryIssues", "ErpReqLineItems", "ErpBomItemDatas", "CompositeSwitchAssetModels", "SwitchTypesAssets", "CompositeSwitchInfo",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfTypeAsset.CompositeSwitchTypeAsset",
        title="CompositeSwitchTypeAsset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "CompositeSwitchTypeAsset" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ComEquipmentTypeAsset" class:
#------------------------------------------------------------------------------

class ComEquipmentTypeAsset(TypeAsset):
    """ Documentation for a piece of Communication Equipment (e.g., gateway, router, network hub, etc.) that may be used for design purposes.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "ComEquipmentTypeAsset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "quantity", "stockItem", "estimatedUnitCost",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "CUWorkEquipmentAsset", "CUAsset", "TypeAssetCatalogue", "AssetModels", "ErpInventoryIssues", "ErpReqLineItems", "ErpBomItemDatas",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfTypeAsset.ComEquipmentTypeAsset",
        title="ComEquipmentTypeAsset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ComEquipmentTypeAsset" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "FACTSDeviceTypeAsset" class:
#------------------------------------------------------------------------------

class FACTSDeviceTypeAsset(ElectricalTypeAsset):
    """ Documentation for generic Flexible alternating current transmission systems (FACTS) devices that may be used for various purposes such as work planning.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    FACTSDeviceAssetModels = List(Instance("CIM.IEC61968.Informative.InfAssetModels.FACTSDeviceAssetModel"))

    #--------------------------------------------------------------------------
    #  Begin "FACTSDeviceTypeAsset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "quantity", "stockItem", "estimatedUnitCost",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "CUWorkEquipmentAsset", "CUAsset", "TypeAssetCatalogue", "AssetModels", "ErpInventoryIssues", "ErpReqLineItems", "ErpBomItemDatas", "ElectricalInfos", "FACTSDeviceAssetModels",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfTypeAsset.FACTSDeviceTypeAsset",
        title="FACTSDeviceTypeAsset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "FACTSDeviceTypeAsset" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SVCTypeAsset" class:
#------------------------------------------------------------------------------

class SVCTypeAsset(FACTSDeviceTypeAsset):
    """ Documentation for a generic Static Var Compensator (SVC) that may be used for various purposes such as work planning.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    SvcInfos = List(Instance("CIM.IEC61968.Informative.InfAssets.SVCInfo"))

    SVCAssetModels = List(Instance("CIM.IEC61968.Informative.InfAssetModels.SVCAssetModel"))

    #--------------------------------------------------------------------------
    #  Begin "SVCTypeAsset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "quantity", "stockItem", "estimatedUnitCost",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "CUWorkEquipmentAsset", "CUAsset", "TypeAssetCatalogue", "AssetModels", "ErpInventoryIssues", "ErpReqLineItems", "ErpBomItemDatas", "ElectricalInfos", "FACTSDeviceAssetModels", "SvcInfos", "SVCAssetModels",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfTypeAsset.SVCTypeAsset",
        title="SVCTypeAsset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SVCTypeAsset" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ResistorTypeAsset" class:
#------------------------------------------------------------------------------

class ResistorTypeAsset(ElectricalTypeAsset):
    """ Documentation for a generic resistor that may be used for design purposes.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ResistorAssetModels = List(Instance("CIM.IEC61968.Informative.InfAssetModels.ResistorAssetModel"))

    Resistors = List(Instance("CIM.IEC61970.Wires.Resistor"))

    #--------------------------------------------------------------------------
    #  Begin "ResistorTypeAsset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "quantity", "stockItem", "estimatedUnitCost",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "CUWorkEquipmentAsset", "CUAsset", "TypeAssetCatalogue", "AssetModels", "ErpInventoryIssues", "ErpReqLineItems", "ErpBomItemDatas", "ElectricalInfos", "ResistorAssetModels", "Resistors",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfTypeAsset.ResistorTypeAsset",
        title="ResistorTypeAsset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ResistorTypeAsset" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SeriesCompensatorTypeAsset" class:
#------------------------------------------------------------------------------

class SeriesCompensatorTypeAsset(ElectricalTypeAsset):
    """ Documentation for a generic series compensator that may be used for design purposes.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ShuntCompensatorAssetModels = List(Instance("CIM.IEC61968.Informative.InfAssetModels.SeriesCompensatorAssetModel"))

    #--------------------------------------------------------------------------
    #  Begin "SeriesCompensatorTypeAsset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "quantity", "stockItem", "estimatedUnitCost",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "CUWorkEquipmentAsset", "CUAsset", "TypeAssetCatalogue", "AssetModels", "ErpInventoryIssues", "ErpReqLineItems", "ErpBomItemDatas", "ElectricalInfos", "ShuntCompensatorAssetModels",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfTypeAsset.SeriesCompensatorTypeAsset",
        title="SeriesCompensatorTypeAsset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SeriesCompensatorTypeAsset" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "FaultIndicatorTypeAsset" class:
#------------------------------------------------------------------------------

class FaultIndicatorTypeAsset(ElectricalTypeAsset):
    """ Documentation for a generic fault indicator that may be used for design purposes.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    FaultIndicatorAssetModels = List(Instance("CIM.IEC61968.Informative.InfAssetModels.FaultIndicatorAssetModel"))

    FaultIndicators = List(Instance("CIM.IEC61970.Protection.FaultIndicator"))

    # Kind of reset mechanisim of this fault indicator.
    resetKind = FaultIndicatorResetKind(desc="Kind of reset mechanisim of this fault indicator.")

    #--------------------------------------------------------------------------
    #  Begin "FaultIndicatorTypeAsset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "quantity", "stockItem", "estimatedUnitCost", "resetKind",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "CUWorkEquipmentAsset", "CUAsset", "TypeAssetCatalogue", "AssetModels", "ErpInventoryIssues", "ErpReqLineItems", "ErpBomItemDatas", "ElectricalInfos", "FaultIndicatorAssetModels", "FaultIndicators",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfTypeAsset.FaultIndicatorTypeAsset",
        title="FaultIndicatorTypeAsset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "FaultIndicatorTypeAsset" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "VehicleTypeAsset" class:
#------------------------------------------------------------------------------

class VehicleTypeAsset(TypeAsset):
    """ Documentation for a generic vehicle that may be used for various purposes such as work planning.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    VehicleAssetModels = List(Instance("CIM.IEC61968.Informative.InfAssetModels.VehicleAssetModel"))

    #--------------------------------------------------------------------------
    #  Begin "VehicleTypeAsset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "quantity", "stockItem", "estimatedUnitCost",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "CUWorkEquipmentAsset", "CUAsset", "TypeAssetCatalogue", "AssetModels", "ErpInventoryIssues", "ErpReqLineItems", "ErpBomItemDatas", "VehicleAssetModels",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfTypeAsset.VehicleTypeAsset",
        title="VehicleTypeAsset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "VehicleTypeAsset" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "BreakerTypeAsset" class:
#------------------------------------------------------------------------------

class BreakerTypeAsset(ElectricalTypeAsset):
    """ Documentation for a generic breaker asset that may be used for design purposes.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    BreakerInfo = Instance("CIM.IEC61968.Informative.InfAssets.BreakerInfo",
        transient=True,
        opposite="BreakerTypeAsset",
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

    BreakerAssetModels = List(Instance("CIM.IEC61968.Informative.InfAssetModels.BreakerAssetModel"))

    #--------------------------------------------------------------------------
    #  Begin "BreakerTypeAsset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "quantity", "stockItem", "estimatedUnitCost",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "CUWorkEquipmentAsset", "CUAsset", "TypeAssetCatalogue", "AssetModels", "ErpInventoryIssues", "ErpReqLineItems", "ErpBomItemDatas", "ElectricalInfos", "BreakerInfo", "BreakerAssetModels",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfTypeAsset.BreakerTypeAsset",
        title="BreakerTypeAsset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "BreakerTypeAsset" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "PoleTypeAsset" class:
#------------------------------------------------------------------------------

class PoleTypeAsset(StructureTypeAsset):
    """ Documentation for a generic pole that may be used for various purposes such as work planning. A pole typically has a single Connection with 1,2 or 3 mounting points.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    PoleModels = List(Instance("CIM.IEC61968.Informative.InfAssetModels.PoleModel"))

    # Length of the pole (inclusive of any section of the pole that may be underground post-installation).
    length = Length(desc="Length of the pole (inclusive of any section of the pole that may be underground post-installation).")

    # Diameter of the pole.
    diameter = Length(desc="Diameter of the pole.")

    #--------------------------------------------------------------------------
    #  Begin "PoleTypeAsset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "quantity", "stockItem", "estimatedUnitCost", "ratedVoltage", "length", "diameter",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "CUWorkEquipmentAsset", "CUAsset", "TypeAssetCatalogue", "AssetModels", "ErpInventoryIssues", "ErpReqLineItems", "ErpBomItemDatas", "MountConnections", "PoleModels",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfTypeAsset.PoleTypeAsset",
        title="PoleTypeAsset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "PoleTypeAsset" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "DuctTypeAsset" class:
#------------------------------------------------------------------------------

class DuctTypeAsset(StructureTypeAsset):
    """ A Duct contains underground cables and is contained within a duct bank. The xCoord and yCoord attributes define its positioning within the DuctBank.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    CableAssets = List(Instance("CIM.IEC61968.Informative.InfAssets.CableAsset"))

    DuctBankTypeAsset = Instance("CIM.IEC61968.Informative.InfTypeAsset.DuctBankTypeAsset",
        transient=True,
        opposite="DuctTypeAssets",
        editor=InstanceEditor(name="_ductbanktypeassets"))

    def _get_ductbanktypeassets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfTypeAsset.DuctBankTypeAsset" ]
        else:
            return []

    _ductbanktypeassets = Property(fget=_get_ductbanktypeassets)

    # X position of the duct within the duct bank.
    xCoord = Int(desc="X position of the duct within the duct bank.")

    # Y position of the duct within the duct bank.
    yCoord = Int(desc="Y position of the duct within the duct bank.")

    #--------------------------------------------------------------------------
    #  Begin "DuctTypeAsset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "quantity", "stockItem", "estimatedUnitCost", "ratedVoltage", "xCoord", "yCoord",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "CUWorkEquipmentAsset", "CUAsset", "TypeAssetCatalogue", "AssetModels", "ErpInventoryIssues", "ErpReqLineItems", "ErpBomItemDatas", "MountConnections", "CableAssets", "DuctBankTypeAsset",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfTypeAsset.DuctTypeAsset",
        title="DuctTypeAsset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "DuctTypeAsset" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SurgeProtectorTypeAsset" class:
#------------------------------------------------------------------------------

class SurgeProtectorTypeAsset(ElectricalTypeAsset):
    """ Documentation for a generic surge arrestor that may be used for design purposes.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    SurgeProtectors = List(Instance("CIM.IEC61970.Protection.SurgeProtector"))

    SurgeProtectorAssetModels = List(Instance("CIM.IEC61968.Informative.InfAssetModels.SurgeProtectorAssetModel"))

    maximumEnergyAbsorption = Float

    maximumContinousOperatingVoltage = Voltage

    maximumCurrentRating = CurrentFlow

    nominalDesignVoltage = Voltage

    #--------------------------------------------------------------------------
    #  Begin "SurgeProtectorTypeAsset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "quantity", "stockItem", "estimatedUnitCost", "maximumEnergyAbsorption", "maximumContinousOperatingVoltage", "maximumCurrentRating", "nominalDesignVoltage",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "CUWorkEquipmentAsset", "CUAsset", "TypeAssetCatalogue", "AssetModels", "ErpInventoryIssues", "ErpReqLineItems", "ErpBomItemDatas", "ElectricalInfos", "SurgeProtectors", "SurgeProtectorAssetModels",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfTypeAsset.SurgeProtectorTypeAsset",
        title="SurgeProtectorTypeAsset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SurgeProtectorTypeAsset" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ComFunctionTypeAsset" class:
#------------------------------------------------------------------------------

class ComFunctionTypeAsset(ElectricalTypeAsset):
    """ Documentation for a generic communication function that may be used for various purposes such as work planning.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ComFunctionAssetModels = List(Instance("CIM.IEC61968.Informative.InfAssetModels.ComFunctionAssetModel"))

    #--------------------------------------------------------------------------
    #  Begin "ComFunctionTypeAsset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "quantity", "stockItem", "estimatedUnitCost",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "CUWorkEquipmentAsset", "CUAsset", "TypeAssetCatalogue", "AssetModels", "ErpInventoryIssues", "ErpReqLineItems", "ErpBomItemDatas", "ElectricalInfos", "ComFunctionAssetModels",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfTypeAsset.ComFunctionTypeAsset",
        title="ComFunctionTypeAsset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ComFunctionTypeAsset" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ProtectionEquipmentTypeAsset" class:
#------------------------------------------------------------------------------

class ProtectionEquipmentTypeAsset(ElectricalTypeAsset):
    """ Documentation for generic protection equiment that may be used for design purposes.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ProtectionEquipmentAssetModels = List(Instance("CIM.IEC61968.Informative.InfAssetModels.ProtectionEquipmentAssetModel"))

    # Default phase trip setting for this type of relay, if applicable.
    defaultPhaseTrip = CurrentFlow(desc="Default phase trip setting for this type of relay, if applicable.")

    # Default ground trip setting for this type of relay, if applicable.
    defaultGroundTrip = CurrentFlow(desc="Default ground trip setting for this type of relay, if applicable.")

    #--------------------------------------------------------------------------
    #  Begin "ProtectionEquipmentTypeAsset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "quantity", "stockItem", "estimatedUnitCost", "defaultPhaseTrip", "defaultGroundTrip",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "CUWorkEquipmentAsset", "CUAsset", "TypeAssetCatalogue", "AssetModels", "ErpInventoryIssues", "ErpReqLineItems", "ErpBomItemDatas", "ElectricalInfos", "ProtectionEquipmentAssetModels",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfTypeAsset.ProtectionEquipmentTypeAsset",
        title="ProtectionEquipmentTypeAsset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ProtectionEquipmentTypeAsset" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "CabinetTypeAsset" class:
#------------------------------------------------------------------------------

class CabinetTypeAsset(StructureTypeAsset):
    """ Documentation for a generic cabinet that may be used for various purposes such as work planning.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    CabinetModels = List(Instance("CIM.IEC61968.Informative.InfAssetModels.CabinetModel"))

    #--------------------------------------------------------------------------
    #  Begin "CabinetTypeAsset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "quantity", "stockItem", "estimatedUnitCost", "ratedVoltage",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "CUWorkEquipmentAsset", "CUAsset", "TypeAssetCatalogue", "AssetModels", "ErpInventoryIssues", "ErpReqLineItems", "ErpBomItemDatas", "MountConnections", "CabinetModels",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfTypeAsset.CabinetTypeAsset",
        title="CabinetTypeAsset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "CabinetTypeAsset" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "MeterTypeAsset" class:
#------------------------------------------------------------------------------

class MeterTypeAsset(ElectricalTypeAsset):
    """ Documentation for a generic meter that may be used for design purposes. Rather than being associated with CustomerMeter, it is associated with EnergyConsumer as it may be used for many applications, such as tie line metering, in addition to customer metering.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    MeterAssetModels = List(Instance("CIM.IEC61968.Informative.InfAssetModels.MeterAssetModel"))

    #--------------------------------------------------------------------------
    #  Begin "MeterTypeAsset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "quantity", "stockItem", "estimatedUnitCost",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "CUWorkEquipmentAsset", "CUAsset", "TypeAssetCatalogue", "AssetModels", "ErpInventoryIssues", "ErpReqLineItems", "ErpBomItemDatas", "ElectricalInfos", "MeterAssetModels",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfTypeAsset.MeterTypeAsset",
        title="MeterTypeAsset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "MeterTypeAsset" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GeneratorTypeAsset" class:
#------------------------------------------------------------------------------

class GeneratorTypeAsset(ElectricalTypeAsset):
    """ Documentation for generic generation equipment that may be used for various purposes such as work planning. It defines both the Real and Reactive power properties (modelled at the PSR level as a GeneratingUnit + SynchronousMachine)
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    GeneratorAssetModels = List(Instance("CIM.IEC61968.Informative.InfAssetModels.GeneratorAssetModel"))

    # Direct-axis subtransient resistance
    rDirectSubtrans = Resistance(desc="Direct-axis subtransient resistance")

    # Direct-axis subtransient reactance
    xDirectSubtrans = Reactance(desc="Direct-axis subtransient reactance")

    # Quadrature-axis Transient resistance
    rQuadTrans = Resistance(desc="Quadrature-axis Transient resistance")

    # Quadrature-axis transient reactance.
    xQuadTrans = Reactance(desc="Quadrature-axis transient reactance.")

    # Quadrature-axis synchronous reactance
    xQuadSync = Reactance(desc="Quadrature-axis synchronous reactance")

    # Direct-axis synchronous reactance
    xDirectSync = Reactance(desc="Direct-axis synchronous reactance")

    # Quadrature-axis synchronous resistance
    rQuadSync = Resistance(desc="Quadrature-axis synchronous resistance")

    # Maximum reactive power limit.
    maxQ = ReactivePower(desc="Maximum reactive power limit.")

    # Direct-axis synchronous resistance
    rDirectSync = Resistance(desc="Direct-axis synchronous resistance")

    # Direct-axis Transient resistance
    rDirectTrans = Resistance(desc="Direct-axis Transient resistance")

    # Quadrature-axis subtransient resistance
    rQuadSubtrans = Resistance(desc="Quadrature-axis subtransient resistance")

    # Minimum reactive power generated.
    minQ = ReactivePower(desc="Minimum reactive power generated.")

    # Minimum real power generated.
    minP = ActivePower(desc="Minimum real power generated.")

    # Maximum real power limit.
    maxP = ActivePower(desc="Maximum real power limit.")

    # Direct-axis Transient reactance
    xDirectTrans = Reactance(desc="Direct-axis Transient reactance")

    # Quadrature-axis subtransient reactance
    xQuadSubtrans = Reactance(desc="Quadrature-axis subtransient reactance")

    #--------------------------------------------------------------------------
    #  Begin "GeneratorTypeAsset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "quantity", "stockItem", "estimatedUnitCost", "rDirectSubtrans", "xDirectSubtrans", "rQuadTrans", "xQuadTrans", "xQuadSync", "xDirectSync", "rQuadSync", "maxQ", "rDirectSync", "rDirectTrans", "rQuadSubtrans", "minQ", "minP", "maxP", "xDirectTrans", "xQuadSubtrans",
                label="Attributes", columns=2),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "CUWorkEquipmentAsset", "CUAsset", "TypeAssetCatalogue", "AssetModels", "ErpInventoryIssues", "ErpReqLineItems", "ErpBomItemDatas", "ElectricalInfos", "GeneratorAssetModels",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfTypeAsset.GeneratorTypeAsset",
        title="GeneratorTypeAsset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GeneratorTypeAsset" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SubstationTypeAsset" class:
#------------------------------------------------------------------------------

class SubstationTypeAsset(TypeAsset):
    """ Documentation for a type of substation that may be used for design purposes.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "SubstationTypeAsset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "quantity", "stockItem", "estimatedUnitCost",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "CUWorkEquipmentAsset", "CUAsset", "TypeAssetCatalogue", "AssetModels", "ErpInventoryIssues", "ErpReqLineItems", "ErpBomItemDatas",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfTypeAsset.SubstationTypeAsset",
        title="SubstationTypeAsset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SubstationTypeAsset" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "AssetFunctionTypeAsset" class:
#------------------------------------------------------------------------------

class AssetFunctionTypeAsset(TypeAsset):
    """ Documentation for a generic Asset Function that may be used for various purposes such as work planning.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    AssetFunctionAssetModels = List(Instance("CIM.IEC61968.Informative.InfAssetModels.AssetFunctionAssetModel"))

    #--------------------------------------------------------------------------
    #  Begin "AssetFunctionTypeAsset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "quantity", "stockItem", "estimatedUnitCost",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "CUWorkEquipmentAsset", "CUAsset", "TypeAssetCatalogue", "AssetModels", "ErpInventoryIssues", "ErpReqLineItems", "ErpBomItemDatas", "AssetFunctionAssetModels",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfTypeAsset.AssetFunctionTypeAsset",
        title="AssetFunctionTypeAsset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "AssetFunctionTypeAsset" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "PotentialTransformerTypeAsset" class:
#------------------------------------------------------------------------------

class PotentialTransformerTypeAsset(ElectricalTypeAsset):
    """ Documentation for a generic Potential Transformer (PT) that may be used for various purposes such as work planning.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    nominalRatio = Instance("CIM.IEC61968.Informative.InfCommon.Ratio",
        transient=True,
        editor=InstanceEditor(name="_ratios"))

    def _get_ratios(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfCommon.Ratio" ]
        else:
            return []

    _ratios = Property(fget=_get_ratios)

    PotentialTransformers = List(Instance("CIM.IEC61970.Meas.PotentialTransformer"))

    PotentialTransformerAssetModels = List(Instance("CIM.IEC61968.Informative.InfAssetModels.PotentialTransformerAssetModel"))

    PotentialTransformerInfo = Instance("CIM.IEC61968.Informative.InfAssets.PotentialTransformerInfo",
        transient=True,
        opposite="PotentialTransformerTypeAsset",
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

    ptClass = Str

    accuracyClass = Str

    #--------------------------------------------------------------------------
    #  Begin "PotentialTransformerTypeAsset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "quantity", "stockItem", "estimatedUnitCost", "ptClass", "accuracyClass",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "CUWorkEquipmentAsset", "CUAsset", "TypeAssetCatalogue", "AssetModels", "ErpInventoryIssues", "ErpReqLineItems", "ErpBomItemDatas", "ElectricalInfos", "nominalRatio", "PotentialTransformers", "PotentialTransformerAssetModels", "PotentialTransformerInfo",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfTypeAsset.PotentialTransformerTypeAsset",
        title="PotentialTransformerTypeAsset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "PotentialTransformerTypeAsset" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "RecloserTypeAsset" class:
#------------------------------------------------------------------------------

class RecloserTypeAsset(ElectricalTypeAsset):
    """ Documentation for a generic recloser asset that may be used for design purposes.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    RecloserInfo = Instance("CIM.IEC61968.Informative.InfAssets.RecloserInfo",
        transient=True,
        opposite="RecloserTypeAsset",
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

    RecloserAssetModels = List(Instance("CIM.IEC61968.Informative.InfAssetModels.RecloserAssetModel"))

    #--------------------------------------------------------------------------
    #  Begin "RecloserTypeAsset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "quantity", "stockItem", "estimatedUnitCost",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "CUWorkEquipmentAsset", "CUAsset", "TypeAssetCatalogue", "AssetModels", "ErpInventoryIssues", "ErpReqLineItems", "ErpBomItemDatas", "ElectricalInfos", "RecloserInfo", "RecloserAssetModels",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfTypeAsset.RecloserTypeAsset",
        title="RecloserTypeAsset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "RecloserTypeAsset" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "CurrentTransformerTypeAsset" class:
#------------------------------------------------------------------------------

class CurrentTransformerTypeAsset(ElectricalTypeAsset):
    """ Documentation for a generic Current Transformer (CT) that may be used for various purposes such as work planning.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    CurrentTransformerInfo = Instance("CIM.IEC61968.Informative.InfAssets.CurrentTransformerInfo",
        transient=True,
        opposite="CurrentTransformerTypeAsset",
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

    CurrentTransformerAssetModels = List(Instance("CIM.IEC61968.Informative.InfAssetModels.CurrentTransformerAssetModel"))

    CurrentTransformers = List(Instance("CIM.IEC61970.Meas.CurrentTransformer"))

    # Nominal ratio between the primary and secondary current; i.e. 100:5
    nominalRatio = Instance("CIM.IEC61968.Informative.InfCommon.Ratio",
        desc="Nominal ratio between the primary and secondary current; i.e. 100:5",
        transient=True,
        editor=InstanceEditor(name="_ratios"))

    def _get_ratios(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfCommon.Ratio" ]
        else:
            return []

    _ratios = Property(fget=_get_ratios)

    # Maximum ratio between the primary and secondary current.
    maxRatio = Instance("CIM.IEC61968.Informative.InfCommon.Ratio",
        desc="Maximum ratio between the primary and secondary current.",
        transient=True,
        editor=InstanceEditor(name="_ratios"))

    def _get_ratios(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfCommon.Ratio" ]
        else:
            return []

    _ratios = Property(fget=_get_ratios)

    # eg. metering, protection, etc
    usage = Str(desc="eg. metering, protection, etc")

    # CT accuracy classification
    accuracyClass = Str(desc="CT accuracy classification")

    accuracyLimit = CurrentFlow

    # Maximum primary current where the CT still displays linear characteristicts.
    kneePointCurrent = CurrentFlow(desc="Maximum primary current where the CT still displays linear characteristicts.")

    # Power burden of the CT core
    coreBurden = ActivePower(desc="Power burden of the CT core")

    ctClass = Str

    # Number of cores.
    coreCount = Int(desc="Number of cores.")

    # Maximum voltage across the secondary terminals where the CT still displays linear characteristicts.
    kneePointVoltage = Voltage(desc="Maximum voltage across the secondary terminals where the CT still displays linear characteristicts.")

    #--------------------------------------------------------------------------
    #  Begin "CurrentTransformerTypeAsset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "quantity", "stockItem", "estimatedUnitCost", "usage", "accuracyClass", "accuracyLimit", "kneePointCurrent", "coreBurden", "ctClass", "coreCount", "kneePointVoltage",
                label="Attributes", columns=2),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "CUWorkEquipmentAsset", "CUAsset", "TypeAssetCatalogue", "AssetModels", "ErpInventoryIssues", "ErpReqLineItems", "ErpBomItemDatas", "ElectricalInfos", "CurrentTransformerInfo", "CurrentTransformerAssetModels", "CurrentTransformers", "nominalRatio", "maxRatio",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfTypeAsset.CurrentTransformerTypeAsset",
        title="CurrentTransformerTypeAsset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "CurrentTransformerTypeAsset" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "DuctBankTypeAsset" class:
#------------------------------------------------------------------------------

class DuctBankTypeAsset(StructureTypeAsset):
    """ A DuctBank contains multiple Ducts. The DuctBank itself should have no connections, since these are defined by the individual ducts within it. However, it will have a ConstructionType and the material it is constructed from.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    DuctTypeAssets = List(Instance("CIM.IEC61968.Informative.InfTypeAsset.DuctTypeAsset"))

    DuctBanks = List(Instance("CIM.IEC61968.Informative.InfAssets.DuctBank"))

    #--------------------------------------------------------------------------
    #  Begin "DuctBankTypeAsset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "quantity", "stockItem", "estimatedUnitCost", "ratedVoltage",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "CUWorkEquipmentAsset", "CUAsset", "TypeAssetCatalogue", "AssetModels", "ErpInventoryIssues", "ErpReqLineItems", "ErpBomItemDatas", "MountConnections", "DuctTypeAssets", "DuctBanks",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfTypeAsset.DuctBankTypeAsset",
        title="DuctBankTypeAsset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "DuctBankTypeAsset" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
