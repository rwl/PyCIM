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

""" The package is used to define asset-level models for objects. Assets may be comprised of other assets and may have relationships to other assets. Assets also have owners and values. Assets may also have a relationship to a PowerSystemResource in the Wires model.  TODO: The following has been copied from a very old version of draft Part 11, so the references are wrong, but we store the knowledge here to reuse later: 'Assets are the basic units which define a physical infrastructure. PowerSystemResources are logical objects meaningful to operations which are constructed from one or more Assets, although PowerSystemResources are not required to specifiy their component Assets. The Asset package is comprosed of several packages. The key concepts of an Asset are as follows: <ul> 	<li>Assets can have names, through inheritance to the Naming package</li> 	<li>Assets are physical entities which have a lifecycle</li> 	<li>One or more assets can be associated to create a PowerSystemResource</li> 	<li>Assets can be grouped (aggregated) with other Assets</li> 	<li>Assets are typically either 'point' or 'linear' assets, which relate to physical geometry</li> 	<li>Assets have a close relationship to Work as a consequence of their lifecycle</li> </ul> The following sections describe the packages in the Assets package. The AssetBasics package defines the relationship between Asset and other classes, such as Organization, PowerSystemResource and Document. Point assets are those assets whose physical location can be described in terms of a single coordinate, such as a pole or a switch. Linear assets are those assets whose physical location is best described in terms of a line, plyline or polygon. Asset work triggers are used to determine when inspection and/or maintenance are required for assets.'
"""
#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CIM.IEC61968.Common import ActivityRecord
from CIM.IEC61968.Assets import Asset
from CIM.IEC61968.Assets import ElectricalInfo
from CIM.IEC61970.Core import IdentifiedObject
from CIM.IEC61968.Common import Document
from CIM.IEC61968.Assets import AssetContainer
from CIM.IEC61968.Informative.InfCommon import Role
from CIM.IEC61970.Core import Curve
from CIM.IEC61970.Core import PhaseCode
from CIM.IEC61970.Domain import CurrentFlow
from CIM.IEC61970.Domain import Voltage
from CIM.IEC61970.Domain import ApparentPower
from CIM.IEC61970.Domain import Length
from CIM.IEC61970.Domain import AngleDegrees
from CIM.IEC61970.Domain import Volume
from CIM.IEC61970.Domain import AbsoluteDate
from CIM.IEC61970.Domain import Reactance
from CIM.IEC61970.Domain import Temperature
from CIM.IEC61970.Domain import PU
from CIM.IEC61970.Domain import Hours
from CIM.IEC61970.Domain import ReactivePower
from CIM.IEC61970.Domain import ActivePower
from CIM.IEC61970.Domain import Capacitance
from CIM.IEC61970.Domain import PerCent
from CIM.IEC61970.Domain import Money
from CIM.IEC61970.Domain import IntegerQuantity



from enthought.traits.api import Instance, List, Property, Enum, Str, Bool, Int, Date, Float
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------

# How the failure has been isolated.
FailureIsolationMethodKind = Enum("manuallyIsolated", "burnedInTheClear", "fuse", "other", "breakerOperation", desc="How the failure has been isolated.")
# Usage of a vehicle.
VehicleUsageKind = Enum("contractor", "other", "crew", "user", desc="Usage of a vehicle.")
# Kind of medium.
MediumKind = Enum("solid", "gas", "liquid", desc="Kind of medium.")
# Kind of base for poles.
PoleBaseKind = Enum("cement", "dirt", "unknown", "other", "asphalt", desc="Kind of base for poles.")
# Kind of FACTS device.
FactsDeviceKind = Enum("tsbr", "statcom", "tcvl", "tssc", "tcpar", "svc", "upfc", "tcsc", desc="Kind of FACTS device.")
# Kind of control for shunt impedance.
ShuntImpedanceControlKind = Enum("fixed", "remoteWithLocalOverride", "remoteOnly", "localOnly", desc="Kind of control for shunt impedance.")
# Function of a substation.
SubstationFunctionKind = Enum("industrial", "subTransmission", "generation", "distribution", "transmission", "other", desc="Function of a substation.")
# Kind of composite switch.
CompositeSwitchKind = Enum("ugMultiSwitch", "throwOver", "escoThrowOver", "gral", "ral", "other", "regulatorBypass", desc="Kind of composite switch.")
# Preservative kind for poles.
PolePreservativeKind = Enum("naphthena", "unknown", "other", "chemonite", "penta", "cellon", "creosote", desc="Preservative kind for poles.")
# Kind of PF test for bushing insulation.
BushingInsulationPfTestKind = Enum("c1", "c2", desc="Kind of PF test for bushing insulation.")
# Kind of material used for structures.
StructureMaterialKind = Enum("concrete", "wood", "other", "steel", desc="Kind of material used for structures.")
# Kind of treatment for poles.
PoleTreatmentKind = Enum("grayStain", "other", "natural", "greenStain", "full", "unknown", "butt", "penta", desc="Kind of treatment for poles.")
# Kind of anchor.
AnchorKind = Enum("other", "concrete", "rod", "screw", "multiHelix", "helix", "unknown", desc="Kind of anchor.")
# Kind of regulation branch for shunt impedance.
RegulationBranchKind = Enum("transformer", "line", "fuse", "sectionner", "other", "breaker", "switch", "recloser", desc="Kind of regulation branch for shunt impedance.")
# Kind of fill for Joint.
JointFillKind = Enum("bluefill254", "airNoFilling", "epoxy", "insoluseal", "noVoid", "noFillPrefab", "asphaltic", "other", "oil", "petrolatum", desc="Kind of fill for Joint.")
# Kind of cooling.
CoolingKind = Enum("other", "forcedAir", "forcedOilAndAir", "selfCooling", desc="Kind of cooling.")
# Kind of procedure.
ProcedureKind = Enum("test", "diagnosis", "inspection", "other", "maintenance", desc="Kind of procedure.")
# Kind of configuration for joints.
JointConfigurationKind = Enum("wires2to1", "wires1to1", "other", "wires3to1", desc="Kind of configuration for joints.")
# Kind of tower construction.
TowerConstructionKind = Enum("suspension", "tension", desc="Kind of tower construction.")
# Kind of local control for shunt impedance.
ShuntImpedanceLocalControlKind = Enum("none", "current", "reactivePower", "time", "temperature", "voltage", "powerFactor", desc="Kind of local control for shunt impedance.")
# Kind of facility.
FacilityKind = Enum("storage", "switching", "generation", "plant", "building", desc="Kind of facility.")
# Kind of lamp for the streetlight.
StreetlightLampKind = Enum("highPressureSodium", "other", "metalHalide", "mercuryVapor", desc="Kind of lamp for the streetlight.")

#------------------------------------------------------------------------------
#  "FailureEvent" class:
#------------------------------------------------------------------------------

class FailureEvent(ActivityRecord):
    """ An event where an asset has failed to perform its functions within specified parameters.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # How the asset failure was isolated from the system.
    failureIsolationMethod = FailureIsolationMethodKind(desc="How the asset failure was isolated from the system.")

    # Code for asset failure.
    corporateCode = Str(desc="Code for asset failure.")

    # The method used for locating the faulted part of the asset. For example, cable options include: Cap Discharge-Thumping, Bridge Method, Visual Inspection, Other.
    faultLocatingMethod = Str(desc="The method used for locating the faulted part of the asset. For example, cable options include: Cap Discharge-Thumping, Bridge Method, Visual Inspection, Other.")

    # Failure location on an object.
    location = Str(desc="Failure location on an object.")

    #--------------------------------------------------------------------------
    #  Begin "FailureEvent" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "reason", "category", "severity", "createdDateTime", "failureIsolationMethod", "corporateCode", "faultLocatingMethod", "location",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "MarketFactors", "Documents", "Organisations", "ScheduledEvent", "Assets", "ErpPersons", "Locations", "status",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.FailureEvent",
        title="FailureEvent",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "FailureEvent" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ElectricalAsset" class:
#------------------------------------------------------------------------------

class ElectricalAsset(Asset):
    """ An asset that has (or can have) a role in the electrical network.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ElectricalInfos = List(Instance("CIM.IEC61968.Assets.ElectricalInfo"))

    ConductingEquipment = Instance("CIM.IEC61970.Core.ConductingEquipment",
        transient=True,
        opposite="ElectricalAssets",
        editor=InstanceEditor(name="_conductingequipments"))

    def _get_conductingequipments(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Core.ConductingEquipment" ]
        else:
            return []

    _conductingequipments = Property(fget=_get_conductingequipments)

    # If 'isConnected' is true, then this is the as-built phase(s) that the asset is associatied with.
    phaseCode = PhaseCode(desc="If 'isConnected' is true, then this is the as-built phase(s) that the asset is associatied with.")

    # True if the asset is physically connected to electrical network (as opposed to being in a warehouse, being refurbished, etc.). Note that this attribute is not intended to imply energization status and/or whether the asset is actually being used.
    isConnected = Bool(desc="True if the asset is physically connected to electrical network (as opposed to being in a warehouse, being refurbished, etc.). Note that this attribute is not intended to imply energization status and/or whether the asset is actually being used.")

    #--------------------------------------------------------------------------
    #  Begin "ElectricalAsset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "initialCondition", "category", "lotNumber", "application", "serialNumber", "installationDate", "corporateCode", "purchasePrice", "manufacturedDate", "initialLossOfLife", "utcNumber", "critical", "phaseCode", "isConnected",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "Measurements", "Hazards", "ErpOrganisationRoles", "DimensionsInfo", "ScheduledEvents", "Mediums", "AssetFunctions", "Properties", "AssetContainer", "Ratings", "ActivityRecords", "FromAssetRoles", "LocationRoles", "PowerSystemResourceRoles", "DocumentRoles", "ChangeItems", "ErpItemMaster", "ElectronicAddresses", "WorkTask", "ErpRecDeliveryItems", "ReliabilityInfos", "ToAssetRoles", "AssetPropertyCurves", "FinancialInfo", "ErpInventory", "acceptanceTest", "status", "ElectricalInfos", "ConductingEquipment",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.ElectricalAsset",
        title="ElectricalAsset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ElectricalAsset" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SwitchInfo" class:
#------------------------------------------------------------------------------

class SwitchInfo(ElectricalInfo):
    """ Properties of a switch.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    SwitchAssets = List(Instance("CIM.IEC61968.Informative.InfAssets.SwitchAsset"))

    SwitchAssetModel = Instance("CIM.IEC61968.Informative.InfAssetModels.SwitchAssetModel",
        transient=True,
        opposite="SwitchInfo",
        editor=InstanceEditor(name="_switchassetmodels"))

    def _get_switchassetmodels(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssetModels.SwitchAssetModel" ]
        else:
            return []

    _switchassetmodels = Property(fget=_get_switchassetmodels)

    SwitchTypeAsset = Instance("CIM.IEC61968.Informative.InfTypeAsset.SwitchTypeAsset",
        transient=True,
        opposite="SwitchInfo",
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

    # The highest value of current the switch can make at the rated voltage under specified operating conditions without suffering significant deterioration of its performance.
    makingCapacity = CurrentFlow(desc="The highest value of current the switch can make at the rated voltage under specified operating conditions without suffering significant deterioration of its performance.")

    # Number of poles (i.e. of current carrying conductors that are switched).
    poleCount = Int(desc="Number of poles (i.e. of current carrying conductors that are switched).")

    # Breaking capacity, or short circuit rating, is the maximum rated current which the device can safely interrupt at the rated voltage.
    interruptingRating = CurrentFlow(desc="Breaking capacity, or short circuit rating, is the maximum rated current which the device can safely interrupt at the rated voltage.")

    # The highest value of current the switch can carry in the closed position at the rated voltage under specified operating conditions without suffering significant deterioration of its performance.
    withstandCurrent = CurrentFlow(desc="The highest value of current the switch can carry in the closed position at the rated voltage under specified operating conditions without suffering significant deterioration of its performance.")

    # The lowest value of current that the switch can make, carry and break in uninterrupted duty at the rated voltage under specified operating conditions without suffering significant deterioration of its performance.
    minimumCurrent = CurrentFlow(desc="The lowest value of current that the switch can make, carry and break in uninterrupted duty at the rated voltage under specified operating conditions without suffering significant deterioration of its performance.")

    # True if switch has load breaking capabiity. Unless specified false, this is always assumed to be true for breakers and reclosers.
    loadBreak = Bool(desc="True if switch has load breaking capabiity. Unless specified false, this is always assumed to be true for breakers and reclosers.")

    # True if multi-phase switch controls all phases concurrently.
    gang = Bool(desc="True if multi-phase switch controls all phases concurrently.")

    # The maximum rms voltage that may be applied across an open contact without breaking down the dielectric properties of the switch in the open position.
    dielectricStrength = Voltage(desc="The maximum rms voltage that may be applied across an open contact without breaking down the dielectric properties of the switch in the open position.")

    # True if device is capable of being operated by remote control.
    remote = Bool(desc="True if device is capable of being operated by remote control.")

    #--------------------------------------------------------------------------
    #  Begin "SwitchInfo" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "b", "wireCount", "r0", "frequency", "g", "ratedVoltage", "x", "phaseCount", "ratedCurrent", "b0", "r", "g0", "ratedApparentPower", "x0", "bil", "makingCapacity", "poleCount", "interruptingRating", "withstandCurrent", "minimumCurrent", "loadBreak", "gang", "dielectricStrength", "remote",
                label="Attributes", columns=2),
            VGroup("Parent", "ModelingAuthoritySet", "EndDeviceAssets", "ElectricalTypeAssets", "ElectricalAssets", "ElectricalAssetModels", "SwitchAssets", "SwitchAssetModel", "SwitchTypeAsset",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.SwitchInfo",
        title="SwitchInfo",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SwitchInfo" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "PowerRating" class:
#------------------------------------------------------------------------------

class PowerRating(IdentifiedObject):
    """ There are often stages of power which are associated with stages of cooling. For instance, a transformer may be rated 121kV on the primary, 15kV on the secondary and 4kV on the tertiary winding. These are voltage ratings and the power ratings are generally the same for all three windings and independent of the voltage ratings, there are instances where the tertiary may have a lower power rating. For example, for three stages, the power rating may be 15/20/25 MVA and the cooling is OA/FA/FOA. The 15 MVA rating goes with the OA cooling (Oil and Air cooling). This is called the self cooled rating as there are no external cooling enhancements. The 20 MVA rating goes with the FA cooling (Forced Air cooling), this means that when the fans are running and thus enhancing the cooling characteristics, the transformer can operate at a power level of 20 MVA. The 25 MVA rating goes with the FOA cooling (Forced Oil and Air cooling), this means that when the fans and pumps are running and thus enhancing the cooling characteristics even more than before, the transformer can operate at a power level of 25 MVA. This 15/20/25 MVA does not state how the power is split between the various windings. It may be 25 MVA input on the primary, 25 MVA output on the secondary and 0 MVA output on the tertiary. It may also operate at 25 MVA input on the primary, 17 MVA output on the secondary and 8 MVA output on the tertiary.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    TransformerAssets = List(Instance("CIM.IEC61968.Informative.InfAssets.TransformerAsset"))

    # Kind of cooling system.
    coolingKind = CoolingKind(desc="Kind of cooling system.")

    # The power rating associated with type of cooling specified for this stage.
    powerRating = ApparentPower(desc="The power rating associated with type of cooling specified for this stage.")

    # Stage of cooling and associated power rating.
    stage = Int(desc="Stage of cooling and associated power rating.")

    #--------------------------------------------------------------------------
    #  Begin "PowerRating" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "coolingKind", "powerRating", "stage",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "TransformerAssets",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.PowerRating",
        title="PowerRating",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "PowerRating" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "StructureSupport" class:
#------------------------------------------------------------------------------

class StructureSupport(Asset):
    """ Support for Structures.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    SecuredStructure = Instance("CIM.IEC61968.Informative.InfAssets.Structure",
        transient=True,
        opposite="StructureSupports",
        editor=InstanceEditor(name="_structures"))

    def _get_structures(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssets.Structure" ]
        else:
            return []

    _structures = Property(fget=_get_structures)

    # Length of anchor lead or guy.
    length = Length(desc="Length of anchor lead or guy.")

    # Direction of supporting anchor or guy.
    direction = AngleDegrees(desc="Direction of supporting anchor or guy.")

    # Size of anchor or guy.
    size = Str(desc="Size of anchor or guy.")

    # Length of rod used for an anchor.
    rodLength = Length(desc="Length of rod used for an anchor.")

    # Number of rods used for an anchor.
    rodCount = Int(desc="Number of rods used for an anchor.")

    #--------------------------------------------------------------------------
    #  Begin "StructureSupport" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "initialCondition", "category", "lotNumber", "application", "serialNumber", "installationDate", "corporateCode", "purchasePrice", "manufacturedDate", "initialLossOfLife", "utcNumber", "critical", "length", "direction", "size", "rodLength", "rodCount",
                label="Attributes", columns=2),
            VGroup("Parent", "ModelingAuthoritySet", "Measurements", "Hazards", "ErpOrganisationRoles", "DimensionsInfo", "ScheduledEvents", "Mediums", "AssetFunctions", "Properties", "AssetContainer", "Ratings", "ActivityRecords", "FromAssetRoles", "LocationRoles", "PowerSystemResourceRoles", "DocumentRoles", "ChangeItems", "ErpItemMaster", "ElectronicAddresses", "WorkTask", "ErpRecDeliveryItems", "ReliabilityInfos", "ToAssetRoles", "AssetPropertyCurves", "FinancialInfo", "ErpInventory", "acceptanceTest", "status", "SecuredStructure",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.StructureSupport",
        title="StructureSupport",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "StructureSupport" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "CurrentTransformerInfo" class:
#------------------------------------------------------------------------------

class CurrentTransformerInfo(ElectricalInfo):
    """ Used to define either the required additional electrical properties of a type of Current Transformer (CT) or a CT Model.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    CurrentTransformerTypeAsset = Instance("CIM.IEC61968.Informative.InfTypeAsset.CurrentTransformerTypeAsset",
        transient=True,
        opposite="CurrentTransformerInfo",
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

    # Ratio for the secondary winding tap changer.
    secondaryRatio = Instance("CIM.IEC61968.Informative.InfCommon.Ratio",
        desc="Ratio for the secondary winding tap changer.",
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

    CurrentTransformerAssets = List(Instance("CIM.IEC61968.Informative.InfAssets.CurrentTransformerAsset"))

    CurrentTransformerAssertModels = List(Instance("CIM.IEC61968.Informative.InfAssetModels.CurrentTransformerAssetModel"))

    # Ratio for the primary winding tap changer.
    primaryRatio = Instance("CIM.IEC61968.Informative.InfCommon.Ratio",
        desc="Ratio for the primary winding tap changer.",
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

    # Ratio for the tertiary winding tap changer.
    tertiaryRatio = Instance("CIM.IEC61968.Informative.InfCommon.Ratio",
        desc="Ratio for the tertiary winding tap changer.",
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

    # Full load secondary (FLS) rating for tertiary winding.
    tertiaryFlsRating = CurrentFlow(desc="Full load secondary (FLS) rating for tertiary winding.")

    # Full load secondary (FLS) rating for secondary winding.
    secondaryFlsRating = CurrentFlow(desc="Full load secondary (FLS) rating for secondary winding.")

    # Full load secondary (FLS) rating for primary winding.
    primaryFlsRating = CurrentFlow(desc="Full load secondary (FLS) rating for primary winding.")

    #--------------------------------------------------------------------------
    #  Begin "CurrentTransformerInfo" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "b", "wireCount", "r0", "frequency", "g", "ratedVoltage", "x", "phaseCount", "ratedCurrent", "b0", "r", "g0", "ratedApparentPower", "x0", "bil", "tertiaryFlsRating", "secondaryFlsRating", "primaryFlsRating",
                label="Attributes", columns=2),
            VGroup("Parent", "ModelingAuthoritySet", "EndDeviceAssets", "ElectricalTypeAssets", "ElectricalAssets", "ElectricalAssetModels", "CurrentTransformerTypeAsset", "secondaryRatio", "CurrentTransformerAssets", "CurrentTransformerAssertModels", "primaryRatio", "tertiaryRatio",
                label="References", columns=1),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.CurrentTransformerInfo",
        title="CurrentTransformerInfo",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "CurrentTransformerInfo" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ConductorAsset" class:
#------------------------------------------------------------------------------

class ConductorAsset(Asset):
    """ Physical asset used to perform the conductor's role.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    CircuitSection = Instance("CIM.IEC61968.Informative.InfOperations.CircuitSection",
        transient=True,
        opposite="ConductorAssets",
        editor=InstanceEditor(name="_circuitsections"))

    def _get_circuitsections(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfOperations.CircuitSection" ]
        else:
            return []

    _circuitsections = Property(fget=_get_circuitsections)

    ConductorAssetModel = Instance("CIM.IEC61968.Informative.InfAssetModels.ConductorAssetModel",
        transient=True,
        opposite="ConductorAssets",
        editor=InstanceEditor(name="_conductorassetmodels"))

    def _get_conductorassetmodels(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssetModels.ConductorAssetModel" ]
        else:
            return []

    _conductorassetmodels = Property(fget=_get_conductorassetmodels)

    ConductorSegment = Instance("CIM.IEC61968.WiresExt.DistributionLineSegment",
        transient=True,
        opposite="ConductorAssets",
        editor=InstanceEditor(name="_distributionlinesegments"))

    def _get_distributionlinesegments(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.WiresExt.DistributionLineSegment" ]
        else:
            return []

    _distributionlinesegments = Property(fget=_get_distributionlinesegments)

    # Description of the method used for grounding the conductor. For a cable, the grounding/bonding shield may be multi-point, single-point, cross cable, or other.
    groundingMethod = Str(desc="Description of the method used for grounding the conductor. For a cable, the grounding/bonding shield may be multi-point, single-point, cross cable, or other.")

    # True when orientation is horizontal (e.g., transmission and distribution lines), false if vertical (e.g. a riser for underground to overhead service).
    isHorizontal = Bool(desc="True when orientation is horizontal (e.g., transmission and distribution lines), false if vertical (e.g. a riser for underground to overhead service).")

    # True if conductor asset has an insulator around the core material.
    insulated = Bool(desc="True if conductor asset has an insulator around the core material.")

    #--------------------------------------------------------------------------
    #  Begin "ConductorAsset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "initialCondition", "category", "lotNumber", "application", "serialNumber", "installationDate", "corporateCode", "purchasePrice", "manufacturedDate", "initialLossOfLife", "utcNumber", "critical", "groundingMethod", "isHorizontal", "insulated",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "Measurements", "Hazards", "ErpOrganisationRoles", "DimensionsInfo", "ScheduledEvents", "Mediums", "AssetFunctions", "Properties", "AssetContainer", "Ratings", "ActivityRecords", "FromAssetRoles", "LocationRoles", "PowerSystemResourceRoles", "DocumentRoles", "ChangeItems", "ErpItemMaster", "ElectronicAddresses", "WorkTask", "ErpRecDeliveryItems", "ReliabilityInfos", "ToAssetRoles", "AssetPropertyCurves", "FinancialInfo", "ErpInventory", "acceptanceTest", "status", "CircuitSection", "ConductorAssetModel", "ConductorSegment",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.ConductorAsset",
        title="ConductorAsset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ConductorAsset" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Medium" class:
#------------------------------------------------------------------------------

class Medium(IdentifiedObject):
    """ A substance that either (1) provides the means of transmission of a force or effect, such as hydraulic fluid, or (2) is used for a surrounding or enveloping substance, such as oil in a transformer or circuit breaker.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Assets = List(Instance("CIM.IEC61968.Assets.Asset"))

    Specification = Instance("CIM.IEC61968.Informative.InfAssets.Specification",
        transient=True,
        opposite="Mediums",
        editor=InstanceEditor(name="_specifications"))

    def _get_specifications(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssets.Specification" ]
        else:
            return []

    _specifications = Property(fget=_get_specifications)

    # Kind of this medium.
    kind = MediumKind(desc="Kind of this medium.")

    # The volume of the medium specified for this application. Note that the actual volume is a type of measurement associated witht the asset.
    volumeSpec = Volume(desc="The volume of the medium specified for this application. Note that the actual volume is a type of measurement associated witht the asset.")

    #--------------------------------------------------------------------------
    #  Begin "Medium" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "kind", "volumeSpec",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Assets", "Specification",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.Medium",
        title="Medium",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Medium" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ProcedureDataSet" class:
#------------------------------------------------------------------------------

class ProcedureDataSet(Document):
    """ A data set recorded each time a procedure is executed. Observed results are captured in associated measurement values and/or values for properties relevant to the type of procedure performed.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Procedure = Instance("CIM.IEC61968.Informative.InfAssets.Procedure",
        transient=True,
        opposite="ProcedureDataSets",
        editor=InstanceEditor(name="_procedures"))

    def _get_procedures(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssets.Procedure" ]
        else:
            return []

    _procedures = Property(fget=_get_procedures)

    # UserAttributes used to specify further properties of this procedure data set. Use 'name' to specify what kind of property it is, and 'value.value' attribute for the actual value.
    Properties = List(Instance("CIM.IEC61968.Common.UserAttribute"),
        desc="UserAttributes used to specify further properties of this procedure data set. Use 'name' to specify what kind of property it is, and 'value.value' attribute for the actual value.")

    MeasurementValues = List(Instance("CIM.IEC61970.Meas.MeasurementValue"))

    TransformerObservations = List(Instance("CIM.IEC61968.Informative.InfAssets.TransformerObservation"))

    # Date and time procedure was completed.
    completedDateTime = Date(desc="Date and time procedure was completed.")

    #--------------------------------------------------------------------------
    #  Begin "ProcedureDataSet" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "completedDateTime",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "Procedure", "Properties", "MeasurementValues", "TransformerObservations",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.ProcedureDataSet",
        title="ProcedureDataSet",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ProcedureDataSet" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Vehicle" class:
#------------------------------------------------------------------------------

class Vehicle(Asset):
    """ A vehicle is a type of utility asset.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Crew = Instance("CIM.IEC61968.Informative.InfWork.Crew",
        transient=True,
        opposite="Vehicles",
        editor=InstanceEditor(name="_crews"))

    def _get_crews(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfWork.Crew" ]
        else:
            return []

    _crews = Property(fget=_get_crews)

    VehicleAssetModel = Instance("CIM.IEC61968.Informative.InfAssetModels.VehicleAssetModel",
        transient=True,
        opposite="Vehicles",
        editor=InstanceEditor(name="_vehicleassetmodels"))

    def _get_vehicleassetmodels(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssetModels.VehicleAssetModel" ]
        else:
            return []

    _vehicleassetmodels = Property(fget=_get_vehicleassetmodels)

    # The general categorization type of vehicle as categorized by the utility's asset management standards and practices. Note: (1) Vehicle model is defined by VehicleAssetModel, and (2) Specific people and organizations and their roles relative to this vehicle may be determined by the inherited Asset-ErpPerson and Asset-Organization associations.
    usageKind = VehicleUsageKind(desc="The general categorization type of vehicle as categorized by the utility's asset management standards and practices. Note: (1) Vehicle model is defined by VehicleAssetModel, and (2) Specific people and organizations and their roles relative to this vehicle may be determined by the inherited Asset-ErpPerson and Asset-Organization associations.")

    # Odometer reading of this vehicle as of the 'odometerReadingDateTime'. Refer to associated ActivityRecords for earlier readings.
    odometerReading = Length(desc="Odometer reading of this vehicle as of the 'odometerReadingDateTime'. Refer to associated ActivityRecords for earlier readings.")

    # Date and time the last odometer reading was recorded.
    odometerReadDateTime = Date(desc="Date and time the last odometer reading was recorded.")

    #--------------------------------------------------------------------------
    #  Begin "Vehicle" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "initialCondition", "category", "lotNumber", "application", "serialNumber", "installationDate", "corporateCode", "purchasePrice", "manufacturedDate", "initialLossOfLife", "utcNumber", "critical", "usageKind", "odometerReading", "odometerReadDateTime",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "Measurements", "Hazards", "ErpOrganisationRoles", "DimensionsInfo", "ScheduledEvents", "Mediums", "AssetFunctions", "Properties", "AssetContainer", "Ratings", "ActivityRecords", "FromAssetRoles", "LocationRoles", "PowerSystemResourceRoles", "DocumentRoles", "ChangeItems", "ErpItemMaster", "ElectronicAddresses", "WorkTask", "ErpRecDeliveryItems", "ReliabilityInfos", "ToAssetRoles", "AssetPropertyCurves", "FinancialInfo", "ErpInventory", "acceptanceTest", "status", "Crew", "VehicleAssetModel",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.Vehicle",
        title="Vehicle",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Vehicle" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "WorkEquipmentAsset" class:
#------------------------------------------------------------------------------

class WorkEquipmentAsset(Asset):
    """ Various equipment used to perform units of work by crews, office staff, etc.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    WorkEquipmentAssetModel = Instance("CIM.IEC61968.Informative.InfAssetModels.WorkEquipmentAssetModel",
        transient=True,
        opposite="WorkEquipmentAssets",
        editor=InstanceEditor(name="_workequipmentassetmodels"))

    def _get_workequipmentassetmodels(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssetModels.WorkEquipmentAssetModel" ]
        else:
            return []

    _workequipmentassetmodels = Property(fget=_get_workequipmentassetmodels)

    Crew = Instance("CIM.IEC61968.Informative.InfWork.Crew",
        transient=True,
        opposite="WorkEquipmentAssets",
        editor=InstanceEditor(name="_crews"))

    def _get_crews(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfWork.Crew" ]
        else:
            return []

    _crews = Property(fget=_get_crews)

    Usages = List(Instance("CIM.IEC61968.Informative.InfWork.Usage"))

    #--------------------------------------------------------------------------
    #  Begin "WorkEquipmentAsset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "initialCondition", "category", "lotNumber", "application", "serialNumber", "installationDate", "corporateCode", "purchasePrice", "manufacturedDate", "initialLossOfLife", "utcNumber", "critical",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "Measurements", "Hazards", "ErpOrganisationRoles", "DimensionsInfo", "ScheduledEvents", "Mediums", "AssetFunctions", "Properties", "AssetContainer", "Ratings", "ActivityRecords", "FromAssetRoles", "LocationRoles", "PowerSystemResourceRoles", "DocumentRoles", "ChangeItems", "ErpItemMaster", "ElectronicAddresses", "WorkTask", "ErpRecDeliveryItems", "ReliabilityInfos", "ToAssetRoles", "AssetPropertyCurves", "FinancialInfo", "ErpInventory", "acceptanceTest", "status", "WorkEquipmentAssetModel", "Crew", "Usages",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.WorkEquipmentAsset",
        title="WorkEquipmentAsset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "WorkEquipmentAsset" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Tool" class:
#------------------------------------------------------------------------------

class Tool(Asset):
    """ Utility asset typically used by utility resources like crews and persons. As is the case for other assets, tools must be maintained.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ToolAssetModel = Instance("CIM.IEC61968.Informative.InfAssetModels.ToolAssetModel",
        transient=True,
        opposite="Tools",
        editor=InstanceEditor(name="_toolassetmodels"))

    def _get_toolassetmodels(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssetModels.ToolAssetModel" ]
        else:
            return []

    _toolassetmodels = Property(fget=_get_toolassetmodels)

    Crew = Instance("CIM.IEC61968.Informative.InfWork.Crew",
        transient=True,
        opposite="Tools",
        editor=InstanceEditor(name="_crews"))

    def _get_crews(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfWork.Crew" ]
        else:
            return []

    _crews = Property(fget=_get_crews)

    # Date the tool was last caibrated, if applicable.
    lastCalibrationDate = AbsoluteDate(desc="Date the tool was last caibrated, if applicable.")

    #--------------------------------------------------------------------------
    #  Begin "Tool" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "initialCondition", "category", "lotNumber", "application", "serialNumber", "installationDate", "corporateCode", "purchasePrice", "manufacturedDate", "initialLossOfLife", "utcNumber", "critical", "lastCalibrationDate",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "Measurements", "Hazards", "ErpOrganisationRoles", "DimensionsInfo", "ScheduledEvents", "Mediums", "AssetFunctions", "Properties", "AssetContainer", "Ratings", "ActivityRecords", "FromAssetRoles", "LocationRoles", "PowerSystemResourceRoles", "DocumentRoles", "ChangeItems", "ErpItemMaster", "ElectronicAddresses", "WorkTask", "ErpRecDeliveryItems", "ReliabilityInfos", "ToAssetRoles", "AssetPropertyCurves", "FinancialInfo", "ErpInventory", "acceptanceTest", "status", "ToolAssetModel", "Crew",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.Tool",
        title="Tool",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Tool" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "TransformerAsset" class:
#------------------------------------------------------------------------------

class TransformerAsset(Asset):
    """ A specific physical (vs. logical) transformer.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    TransformerInfo = Instance("CIM.IEC61968.AssetModels.TransformerInfo",
        transient=True,
        opposite="TransformerAssets",
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

    PowerRatings = List(Instance("CIM.IEC61968.Informative.InfAssets.PowerRating"))

    TransformerObservations = List(Instance("CIM.IEC61968.Informative.InfAssets.TransformerObservation"))

    TransformerAssetModel = Instance("CIM.IEC61968.Informative.InfAssetModels.TransformerAssetModel",
        transient=True,
        opposite="TransformerAssets",
        editor=InstanceEditor(name="_transformerassetmodels"))

    def _get_transformerassetmodels(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssetModels.TransformerAssetModel" ]
        else:
            return []

    _transformerassetmodels = Property(fget=_get_transformerassetmodels)

    # Date and time this asset was last reconditioned or had a major overhaul.
    reconditionedDateTime = Date(desc="Date and time this asset was last reconditioned or had a major overhaul.")

    #--------------------------------------------------------------------------
    #  Begin "TransformerAsset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "initialCondition", "category", "lotNumber", "application", "serialNumber", "installationDate", "corporateCode", "purchasePrice", "manufacturedDate", "initialLossOfLife", "utcNumber", "critical", "reconditionedDateTime",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "Measurements", "Hazards", "ErpOrganisationRoles", "DimensionsInfo", "ScheduledEvents", "Mediums", "AssetFunctions", "Properties", "AssetContainer", "Ratings", "ActivityRecords", "FromAssetRoles", "LocationRoles", "PowerSystemResourceRoles", "DocumentRoles", "ChangeItems", "ErpItemMaster", "ElectronicAddresses", "WorkTask", "ErpRecDeliveryItems", "ReliabilityInfos", "ToAssetRoles", "AssetPropertyCurves", "FinancialInfo", "ErpInventory", "acceptanceTest", "status", "TransformerInfo", "PowerRatings", "TransformerObservations", "TransformerAssetModel",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.TransformerAsset",
        title="TransformerAsset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TransformerAsset" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Facility" class:
#------------------------------------------------------------------------------

class Facility(AssetContainer):
    """ A facility may contain buildings, storage facilities, switching facilities, power generation, manufacturing facilities, maintenance facilities, etc.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Kind of this facility.
    kind = Str(desc="Kind of this facility.")

    #--------------------------------------------------------------------------
    #  Begin "Facility" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "initialCondition", "category", "lotNumber", "application", "serialNumber", "installationDate", "corporateCode", "purchasePrice", "manufacturedDate", "initialLossOfLife", "utcNumber", "critical", "kind",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "Measurements", "Hazards", "ErpOrganisationRoles", "DimensionsInfo", "ScheduledEvents", "Mediums", "AssetFunctions", "Properties", "AssetContainer", "Ratings", "ActivityRecords", "FromAssetRoles", "LocationRoles", "PowerSystemResourceRoles", "DocumentRoles", "ChangeItems", "ErpItemMaster", "ElectronicAddresses", "WorkTask", "ErpRecDeliveryItems", "ReliabilityInfos", "ToAssetRoles", "AssetPropertyCurves", "FinancialInfo", "ErpInventory", "acceptanceTest", "status", "LandProperties", "Assets", "Seals",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.Facility",
        title="Facility",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Facility" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Structure" class:
#------------------------------------------------------------------------------

class Structure(AssetContainer):
    """ Construction holding assets such as conductors, transformers, switchgear, etc.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    StructureSupports = List(Instance("CIM.IEC61968.Informative.InfAssets.StructureSupport"))

    # Material this structure is made of.
    materialKind = StructureMaterialKind(desc="Material this structure is made of.")

    # Visible height of structure above ground level for overhead construction (e.g., Pole or Tower) or below ground level for an underground vault, manhole, etc. Refer to associated DimensionPropertiesInfo for other types of dimensions.
    height = Length(desc="Visible height of structure above ground level for overhead construction (e.g., Pole or Tower) or below ground level for an underground vault, manhole, etc. Refer to associated DimensionPropertiesInfo for other types of dimensions.")

    # True if weeds are to be removed around asset.
    removeWeed = Bool(desc="True if weeds are to be removed around asset.")

    # Date weed were last removed.
    weedRemovedDate = AbsoluteDate(desc="Date weed were last removed.")

    # Date fumigant was last applied.
    fumigantAppliedDate = AbsoluteDate(desc="Date fumigant was last applied.")

    # Name of fumigant.
    fumigantName = Str(desc="Name of fumigant.")

    #--------------------------------------------------------------------------
    #  Begin "Structure" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "initialCondition", "category", "lotNumber", "application", "serialNumber", "installationDate", "corporateCode", "purchasePrice", "manufacturedDate", "initialLossOfLife", "utcNumber", "critical", "materialKind", "height", "removeWeed", "weedRemovedDate", "fumigantAppliedDate", "fumigantName",
                label="Attributes", columns=2),
            VGroup("Parent", "ModelingAuthoritySet", "Measurements", "Hazards", "ErpOrganisationRoles", "DimensionsInfo", "ScheduledEvents", "Mediums", "AssetFunctions", "Properties", "AssetContainer", "Ratings", "ActivityRecords", "FromAssetRoles", "LocationRoles", "PowerSystemResourceRoles", "DocumentRoles", "ChangeItems", "ErpItemMaster", "ElectronicAddresses", "WorkTask", "ErpRecDeliveryItems", "ReliabilityInfos", "ToAssetRoles", "AssetPropertyCurves", "FinancialInfo", "ErpInventory", "acceptanceTest", "status", "LandProperties", "Assets", "Seals", "StructureSupports",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.Structure",
        title="Structure",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Structure" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "AssetAssetRole" class:
#------------------------------------------------------------------------------

class AssetAssetRole(Role):
    """ Roles played between Assets and other Assets.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ToAsset = Instance("CIM.IEC61968.Assets.Asset",
        transient=True,
        opposite="FromAssetRoles",
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

    FromAsset = Instance("CIM.IEC61968.Assets.Asset",
        transient=True,
        opposite="ToAssetRoles",
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

    #--------------------------------------------------------------------------
    #  Begin "AssetAssetRole" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "category",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "status", "ToAsset", "FromAsset",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.AssetAssetRole",
        title="AssetAssetRole",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "AssetAssetRole" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "WindingInsulation" class:
#------------------------------------------------------------------------------

class WindingInsulation(IdentifiedObject):
    """ Winding insulation condition as a result of a test.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    FromWinding = Instance("CIM.IEC61968.WiresExt.DistributionTransformerWinding",
        transient=True,
        opposite="FromWindingInsulations",
        editor=InstanceEditor(name="_distributiontransformerwindings"))

    def _get_distributiontransformerwindings(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.WiresExt.DistributionTransformerWinding" ]
        else:
            return []

    _distributiontransformerwindings = Property(fget=_get_distributiontransformerwindings)

    Ground = Instance("CIM.IEC61970.Wires.Ground",
        transient=True,
        opposite="WindingInsulations",
        editor=InstanceEditor(name="_grounds"))

    def _get_grounds(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Wires.Ground" ]
        else:
            return []

    _grounds = Property(fget=_get_grounds)

    TransformerObservation = Instance("CIM.IEC61968.Informative.InfAssets.TransformerObservation",
        transient=True,
        opposite="WindingInsulationPFs",
        editor=InstanceEditor(name="_transformerobservations"))

    def _get_transformerobservations(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssets.TransformerObservation" ]
        else:
            return []

    _transformerobservations = Property(fget=_get_transformerobservations)

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

    ToWinding = Instance("CIM.IEC61968.WiresExt.DistributionTransformerWinding",
        transient=True,
        opposite="ToWindingInsulations",
        editor=InstanceEditor(name="_distributiontransformerwindings"))

    def _get_distributiontransformerwindings(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.WiresExt.DistributionTransformerWinding" ]
        else:
            return []

    _distributiontransformerwindings = Property(fget=_get_distributiontransformerwindings)

    # Status of Winding Insulation Power Factor as of statusDate: Acceptable, Minor Deterioration or Moisture Absorption, Major Deterioration or Moisture Absorption, Failed.
    insulationPFStatus = Str(desc="Status of Winding Insulation Power Factor as of statusDate: Acceptable, Minor Deterioration or Moisture Absorption, Major Deterioration or Moisture Absorption, Failed.")

    # As of statusDate, the leakage reactance measured at the 'from' winding with the 'to' winding short-circuited and all other windings open-circuited.
    leakageReactance = Reactance(desc="As of statusDate, the leakage reactance measured at the 'from' winding with the 'to' winding short-circuited and all other windings open-circuited.")

    # For testType, status of Winding Insulation Resistance as of statusDate. Typical values are: Acceptable, Questionable, Failed.
    insulationResistance = Str(desc="For testType, status of Winding Insulation Resistance as of statusDate. Typical values are: Acceptable, Questionable, Failed.")

    #--------------------------------------------------------------------------
    #  Begin "WindingInsulation" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "insulationPFStatus", "leakageReactance", "insulationResistance",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "FromWinding", "Ground", "TransformerObservation", "status", "ToWinding",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.WindingInsulation",
        title="WindingInsulation",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "WindingInsulation" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "TransformerObservation" class:
#------------------------------------------------------------------------------

class TransformerObservation(IdentifiedObject):
    """ Common information captured during transformer inspections and/or diagnostics. Note that some properties may be measured through other means and therefore have measurement values in addition to the observed values recorded here.
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

    WindingInsulationPFs = List(Instance("CIM.IEC61968.Informative.InfAssets.WindingInsulation"))

    TransformerAsset = Instance("CIM.IEC61968.Informative.InfAssets.TransformerAsset",
        transient=True,
        opposite="TransformerObservations",
        editor=InstanceEditor(name="_transformerassets"))

    def _get_transformerassets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssets.TransformerAsset" ]
        else:
            return []

    _transformerassets = Property(fget=_get_transformerassets)

    Transformer = Instance("CIM.IEC61968.WiresExt.DistributionTransformer",
        transient=True,
        opposite="TransformerObservations",
        editor=InstanceEditor(name="_distributiontransformers"))

    def _get_distributiontransformers(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.WiresExt.DistributionTransformer" ]
        else:
            return []

    _distributiontransformers = Property(fget=_get_distributiontransformers)

    BushingInsultationPFs = List(Instance("CIM.IEC61968.Informative.InfAssets.BushingInsulationPF"))

    ProcedureDataSets = List(Instance("CIM.IEC61968.Informative.InfAssets.ProcedureDataSet"))

    # Oil Quality Analysis-Neutralization Number - Number - Mg KOH.
    oilNeutralizationNumber = Str(desc="Oil Quality Analysis-Neutralization Number - Number - Mg KOH.")

    # Top oil temperature.
    topOilTemp = Temperature(desc="Top oil temperature.")

    # Dissolved Gas Analysis. Typical values are: Acceptable, Overheating, Corona, Sparking, Arcing.
    dga = Str(desc="Dissolved Gas Analysis. Typical values are: Acceptable, Overheating, Corona, Sparking, Arcing.")

    # Pump vibration, with typical values being: nominal, high.
    pumpVibration = Str(desc="Pump vibration, with typical values being: nominal, high.")

    # Oil Quality Analysis-Color.
    oilColor = Str(desc="Oil Quality Analysis-Color.")

    # Oil Quality Analysis- inter facial tension (IFT) - number-Dynes/CM.
    oilIFT = Str(desc="Oil Quality Analysis- inter facial tension (IFT) - number-Dynes/CM.")

    # Oil Quality Analysis-Dielectric Strength.
    oilDielectricStrength = Voltage(desc="Oil Quality Analysis-Dielectric Strength.")

    # Hotspot oil temperature.
    hotSpotTemp = Temperature(desc="Hotspot oil temperature.")

    # The level of oil in the transformer.
    oilLevel = Str(desc="The level of oil in the transformer.")

    # Water Content expressed in parts per million.
    waterContent = Str(desc="Water Content expressed in parts per million.")

    # Bushing temperature.
    bushingTemp = Temperature(desc="Bushing temperature.")

    # Overall measure of furfural in oil and mechanical strength of paper. DP, the degree of polymerization, is the strength of the paper. Furfural is a measure of furfural compounds, often expressed in parts per million.
    furfuralDP = Str(desc="Overall measure of furfural in oil and mechanical strength of paper. DP, the degree of polymerization, is the strength of the paper. Furfural is a measure of furfural compounds, often expressed in parts per million.")

    # Frequency Response Analysis. Typical values are: acceptable, slight movement, significant movement, failed, near failure. A graphic of the response diagram, which is a type of document, may be associated with this analysis through the recursive document relationship of the ProcedureDataSet.
    freqResp = Str(desc="Frequency Response Analysis. Typical values are: acceptable, slight movement, significant movement, failed, near failure. A graphic of the response diagram, which is a type of document, may be associated with this analysis through the recursive document relationship of the ProcedureDataSet.")

    #--------------------------------------------------------------------------
    #  Begin "TransformerObservation" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "oilNeutralizationNumber", "topOilTemp", "dga", "pumpVibration", "oilColor", "oilIFT", "oilDielectricStrength", "hotSpotTemp", "oilLevel", "waterContent", "bushingTemp", "furfuralDP", "freqResp",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "status", "WindingInsulationPFs", "TransformerAsset", "Transformer", "BushingInsultationPFs", "ProcedureDataSets",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.TransformerObservation",
        title="TransformerObservation",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TransformerObservation" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "CompositeSwitchInfo" class:
#------------------------------------------------------------------------------

class CompositeSwitchInfo(IdentifiedObject):
    """ Properties of a composite switch.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    CompositeSwitchAssetModel = Instance("CIM.IEC61968.Informative.InfAssetModels.CompositeSwitchAssetModel",
        transient=True,
        opposite="CompositeSwitchInfo",
        editor=InstanceEditor(name="_compositeswitchassetmodels"))

    def _get_compositeswitchassetmodels(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssetModels.CompositeSwitchAssetModel" ]
        else:
            return []

    _compositeswitchassetmodels = Property(fget=_get_compositeswitchassetmodels)

    CompositeSwitchAssets = List(Instance("CIM.IEC61968.Informative.InfAssets.CompositeSwitchAsset"))

    CompositeSwitchTypeAsset = Instance("CIM.IEC61968.Informative.InfTypeAsset.CompositeSwitchTypeAsset",
        transient=True,
        opposite="CompositeSwitchInfo",
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

    # Phases carried, if applicable.
    phaseCode = PhaseCode(desc="Phases carried, if applicable.")

    # Rated voltage.
    ratedVoltage = Voltage(desc="Rated voltage.")

    # Supported number of phases, typically 0, 1 or 3.
    phaseCount = Int(desc="Supported number of phases, typically 0, 1 or 3.")

    # True if device is capable of being operated by remote control.
    remote = Bool(desc="True if device is capable of being operated by remote control.")

    # Initial operating mode, with the following values: Automatic, Manual.
    initOpMode = Str(desc="Initial operating mode, with the following values: Automatic, Manual.")

    # True if multi-phase switch controls all phases concurrently.
    gang = Bool(desc="True if multi-phase switch controls all phases concurrently.")

    # Number of switch states represented by the composite switch.
    switchStateCount = Int(desc="Number of switch states represented by the composite switch.")

    # Breaking capacity, or short circuit rating, is the maximum rated current which the device can safely interrupt at the rated voltage.
    interruptingRating = CurrentFlow(desc="Breaking capacity, or short circuit rating, is the maximum rated current which the device can safely interrupt at the rated voltage.")

    #--------------------------------------------------------------------------
    #  Begin "CompositeSwitchInfo" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "phaseCode", "ratedVoltage", "phaseCount", "remote", "initOpMode", "gang", "switchStateCount", "interruptingRating",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "CompositeSwitchAssetModel", "CompositeSwitchAssets", "CompositeSwitchTypeAsset",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.CompositeSwitchInfo",
        title="CompositeSwitchInfo",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "CompositeSwitchInfo" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ShuntImpedanceInfo" class:
#------------------------------------------------------------------------------

class ShuntImpedanceInfo(ElectricalInfo):
    """ Properties of a shunt impedance.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ShuntCompensatorTypeAsset = Instance("CIM.IEC61968.Informative.InfTypeAsset.ShuntCompensatorTypeAsset",
        transient=True,
        opposite="ShuntImpedanceInfo",
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

    ShuntCompensatorAssetModel = Instance("CIM.IEC61968.Informative.InfAssetModels.ShuntCompensatorAssetModel",
        transient=True,
        opposite="ShuntImpedanceInfo",
        editor=InstanceEditor(name="_shuntcompensatorassetmodels"))

    def _get_shuntcompensatorassetmodels(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssetModels.ShuntCompensatorAssetModel" ]
        else:
            return []

    _shuntcompensatorassetmodels = Property(fget=_get_shuntcompensatorassetmodels)

    ShuntCompensatorAssets = List(Instance("CIM.IEC61968.Informative.InfAssets.ShuntCompensatorAsset"))

    # Kind of control (if any).
    controlKind = ShuntImpedanceControlKind(desc="Kind of control (if any).")

    # Phases that are measured for controlling the device.
    sensingPhaseCode = PhaseCode(desc="Phases that are measured for controlling the device.")

    # (For VAR, amp, or power factor locally controlled shunt impedances) Kind of regulation branch.
    regBranchKind = RegulationBranchKind(desc="(For VAR, amp, or power factor locally controlled shunt impedances) Kind of regulation branch.")

    # Kind of local controller.
    localControlKind = ShuntImpedanceLocalControlKind(desc="Kind of local controller.")

    # For VAR, amp, or power factor locally controlled shunt impedances, the index of the regulation branch.
    regBranch = Str(desc="For VAR, amp, or power factor locally controlled shunt impedances, the index of the regulation branch.")

    # For locally controlled shunt impedances which have a voltage override feature, the low voltage override value. If the voltage is below this value, the shunt impedance will be turned on regardless of the other local controller settings.
    lowVoltageOverride = PU(desc="For locally controlled shunt impedances which have a voltage override feature, the low voltage override value. If the voltage is below this value, the shunt impedance will be turned on regardless of the other local controller settings.")

    # Time interval between consecutive switching operations.
    switchOperationCycle = Hours(desc="Time interval between consecutive switching operations.")

    # For locally controlled shunt impedances which have a voltage override feature, the high voltage override value. If the voltage is above this value, the shunt impedance will be turned off regardless of the other local controller settings.
    highVoltageOverride = PU(desc="For locally controlled shunt impedances which have a voltage override feature, the high voltage override value. If the voltage is above this value, the shunt impedance will be turned off regardless of the other local controller settings.")

    # True if the locally controlled capacitor has voltage override capability.
    localOverride = Bool(desc="True if the locally controlled capacitor has voltage override capability.")

    # For VAR, amp, or power factor locally controlled shunt impedances, the end of the branch that is regulated. The field has the following values: from side, to side, and tertiary (only if the branch is a transformer).
    regBranchEnd = Int(desc="For VAR, amp, or power factor locally controlled shunt impedances, the end of the branch that is regulated. The field has the following values: from side, to side, and tertiary (only if the branch is a transformer).")

    # Upper control setting.
    localOffLevel = Str(desc="Upper control setting.")

    # For VAR, amp, or power factor locally controlled shunt impedances, the flow direction: in, out.
    branchDirect = Int(desc="For VAR, amp, or power factor locally controlled shunt impedances, the flow direction: in, out.")

    # True if open is normal status for a fixed capacitor bank, otherwise normal status is closed.
    normalOpen = Bool(desc="True if open is normal status for a fixed capacitor bank, otherwise normal status is closed.")

    # The size of the individual units that make up the bank.
    cellSize = ReactivePower(desc="The size of the individual units that make up the bank.")

    # Lower control setting.
    localOnLevel = Str(desc="Lower control setting.")

    # IdmsShuntImpedanceData.maxNumSwitchOps
    maxSwitchOperationCount = Int(desc="IdmsShuntImpedanceData.maxNumSwitchOps")

    # True if regulated voltages are measured line to line, otherwise they are measured line to ground.
    vRegLineLine = Bool(desc="True if regulated voltages are measured line to line, otherwise they are measured line to ground.")

    #--------------------------------------------------------------------------
    #  Begin "ShuntImpedanceInfo" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "b", "wireCount", "r0", "frequency", "g", "ratedVoltage", "x", "phaseCount", "ratedCurrent", "b0", "r", "g0", "ratedApparentPower", "x0", "bil", "controlKind", "sensingPhaseCode", "regBranchKind", "localControlKind", "regBranch", "lowVoltageOverride", "switchOperationCycle", "highVoltageOverride", "localOverride", "regBranchEnd", "localOffLevel", "branchDirect", "normalOpen", "cellSize", "localOnLevel", "maxSwitchOperationCount", "vRegLineLine",
                label="Attributes", columns=3),
            VGroup("Parent", "ModelingAuthoritySet", "EndDeviceAssets", "ElectricalTypeAssets", "ElectricalAssets", "ElectricalAssetModels", "ShuntCompensatorTypeAsset", "ShuntCompensatorAssetModel", "ShuntCompensatorAssets",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.ShuntImpedanceInfo",
        title="ShuntImpedanceInfo",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ShuntImpedanceInfo" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "DuctBank" class:
#------------------------------------------------------------------------------

class DuctBank(Asset):
    """ A duct bank may contain many ducts. Each duct contains individual lines that are expressed as conductor assets (thereby describing each line's physical asset characteristics), which are each associated with ACLineSegments and other classes describing their electrical characteristics.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    CableAssets = List(Instance("CIM.IEC61968.Informative.InfAssets.CableAsset"))

    DuctBankTypeAsset = Instance("CIM.IEC61968.Informative.InfTypeAsset.DuctBankTypeAsset",
        transient=True,
        opposite="DuctBanks",
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

    # Number of circuits in duct bank. Refer to associations between a duct (ConductorAsset) and an ACLineSegment to understand which circuits are in which ducts.
    circuitCount = Int(desc="Number of circuits in duct bank. Refer to associations between a duct (ConductorAsset) and an ACLineSegment to understand which circuits are in which ducts.")

    # Number of ducts in duct bank.
    ductCount = Int(desc="Number of ducts in duct bank.")

    #--------------------------------------------------------------------------
    #  Begin "DuctBank" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "initialCondition", "category", "lotNumber", "application", "serialNumber", "installationDate", "corporateCode", "purchasePrice", "manufacturedDate", "initialLossOfLife", "utcNumber", "critical", "circuitCount", "ductCount",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "Measurements", "Hazards", "ErpOrganisationRoles", "DimensionsInfo", "ScheduledEvents", "Mediums", "AssetFunctions", "Properties", "AssetContainer", "Ratings", "ActivityRecords", "FromAssetRoles", "LocationRoles", "PowerSystemResourceRoles", "DocumentRoles", "ChangeItems", "ErpItemMaster", "ElectronicAddresses", "WorkTask", "ErpRecDeliveryItems", "ReliabilityInfos", "ToAssetRoles", "AssetPropertyCurves", "FinancialInfo", "ErpInventory", "acceptanceTest", "status", "CableAssets", "DuctBankTypeAsset",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.DuctBank",
        title="DuctBank",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "DuctBank" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Procedure" class:
#------------------------------------------------------------------------------

class Procedure(Document):
    """ A documented procedure for various types of Work or Work Tasks. One or more procedures guide a compatible unit, a standard way of performing a unit of work. The type of procedure is defined in Procedure.type. For example, when type=Inspection, this procedure coupled with Schedule and other information provides the key items of an inspection plan. Another type of Procedure is a Diagnosis. Note that each specific values and settings to be used in a procedure is intended to be described in an instance of ProcedureValue. A maintenance ticket, a type of Work, is generated whenever maintenance is determined to be needed as a result of an inspection or diagnosis.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    CompatibleUnits = List(Instance("CIM.IEC61968.Informative.InfWork.CompatibleUnit"))

    ProcedureDataSets = List(Instance("CIM.IEC61968.Informative.InfAssets.ProcedureDataSet"))

    # UserAttributes used to specify procedure values. An example is to have an instance for each of the following settings when conducting a test: voltage, current, frequency, temperature specified in 'name' attribute, and the corresponding value and units in 'value' attribute.
    ProcedureValues = List(Instance("CIM.IEC61968.Common.UserAttribute"),
        desc="UserAttributes used to specify procedure values. An example is to have an instance for each of the following settings when conducting a test: voltage, current, frequency, temperature specified in 'name' attribute, and the corresponding value and units in 'value' attribute.")

    Limits = List(Instance("CIM.IEC61970.Meas.Limit"))

    # Kind of this procedure.
    kind = ProcedureKind(desc="Kind of this procedure.")

    # The textual description of the procedure, which references instances of ProcedureValue as appropriate.
    instruction = Str(desc="The textual description of the procedure, which references instances of ProcedureValue as appropriate.")

    # Sequence number in a sequence of procedures being performed.
    sequenceNumber = Str(desc="Sequence number in a sequence of procedures being performed.")

    # Code for this kind of procedure.
    corporateCode = Str(desc="Code for this kind of procedure.")

    #--------------------------------------------------------------------------
    #  Begin "Procedure" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "kind", "instruction", "sequenceNumber", "corporateCode",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "CompatibleUnits", "ProcedureDataSets", "ProcedureValues", "Limits",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.Procedure",
        title="Procedure",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Procedure" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "TapChangerAsset" class:
#------------------------------------------------------------------------------

class TapChangerAsset(Asset):
    """ Physical asset performing TapChanger function.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    TapChangerAssetModel = Instance("CIM.IEC61968.Informative.InfAssetModels.TapChangerAssetModel",
        transient=True,
        opposite="TapChangerAssets",
        editor=InstanceEditor(name="_tapchangerassetmodels"))

    def _get_tapchangerassetmodels(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssetModels.TapChangerAssetModel" ]
        else:
            return []

    _tapchangerassetmodels = Property(fget=_get_tapchangerassetmodels)

    #--------------------------------------------------------------------------
    #  Begin "TapChangerAsset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "initialCondition", "category", "lotNumber", "application", "serialNumber", "installationDate", "corporateCode", "purchasePrice", "manufacturedDate", "initialLossOfLife", "utcNumber", "critical",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "Measurements", "Hazards", "ErpOrganisationRoles", "DimensionsInfo", "ScheduledEvents", "Mediums", "AssetFunctions", "Properties", "AssetContainer", "Ratings", "ActivityRecords", "FromAssetRoles", "LocationRoles", "PowerSystemResourceRoles", "DocumentRoles", "ChangeItems", "ErpItemMaster", "ElectronicAddresses", "WorkTask", "ErpRecDeliveryItems", "ReliabilityInfos", "ToAssetRoles", "AssetPropertyCurves", "FinancialInfo", "ErpInventory", "acceptanceTest", "status", "TapChangerAssetModel",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.TapChangerAsset",
        title="TapChangerAsset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TapChangerAsset" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "PotentialTransformerInfo" class:
#------------------------------------------------------------------------------

class PotentialTransformerInfo(ElectricalInfo):
    """ Used to define either the required additional electrical properties of a type of a Potential Transformer (PT), or a PT Model.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Ratio for the primary winding tap changer.
    primaryRatio = Instance("CIM.IEC61968.Informative.InfCommon.Ratio",
        desc="Ratio for the primary winding tap changer.",
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

    # Ratio for the tertiary winding tap changer.
    tertiaryRatio = Instance("CIM.IEC61968.Informative.InfCommon.Ratio",
        desc="Ratio for the tertiary winding tap changer.",
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

    # Ratio for the secondary winding tap changer.
    secondaryRatio = Instance("CIM.IEC61968.Informative.InfCommon.Ratio",
        desc="Ratio for the secondary winding tap changer.",
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

    PotentialTransformerAssets = List(Instance("CIM.IEC61968.Informative.InfAssets.PotentialTransformerAsset"))

    PotentialTransformerAssetModels = List(Instance("CIM.IEC61968.Informative.InfAssetModels.PotentialTransformerAssetModel"))

    PotentialTransformerTypeAsset = Instance("CIM.IEC61968.Informative.InfTypeAsset.PotentialTransformerTypeAsset",
        transient=True,
        opposite="PotentialTransformerInfo",
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

    #--------------------------------------------------------------------------
    #  Begin "PotentialTransformerInfo" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "b", "wireCount", "r0", "frequency", "g", "ratedVoltage", "x", "phaseCount", "ratedCurrent", "b0", "r", "g0", "ratedApparentPower", "x0", "bil",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "EndDeviceAssets", "ElectricalTypeAssets", "ElectricalAssets", "ElectricalAssetModels", "primaryRatio", "tertiaryRatio", "secondaryRatio", "PotentialTransformerAssets", "PotentialTransformerAssetModels", "PotentialTransformerTypeAsset",
                label="References", columns=1),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.PotentialTransformerInfo",
        title="PotentialTransformerInfo",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "PotentialTransformerInfo" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "AssetPsrRole" class:
#------------------------------------------------------------------------------

class AssetPsrRole(Role):
    """ Roles played between Assets and Power System Resources.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    PowerSystemResource = Instance("CIM.IEC61970.Core.PowerSystemResource",
        transient=True,
        opposite="AssetRoles",
        editor=InstanceEditor(name="_powersystemresources"))

    def _get_powersystemresources(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Core.PowerSystemResource" ]
        else:
            return []

    _powersystemresources = Property(fget=_get_powersystemresources)

    Asset = Instance("CIM.IEC61968.Assets.Asset",
        transient=True,
        opposite="PowerSystemResourceRoles",
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

    #--------------------------------------------------------------------------
    #  Begin "AssetPsrRole" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "category",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "status", "PowerSystemResource", "Asset",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.AssetPsrRole",
        title="AssetPsrRole",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "AssetPsrRole" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "DocAssetRole" class:
#------------------------------------------------------------------------------

class DocAssetRole(Role):
    """ Roles played between Documents and Assets.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Asset = Instance("CIM.IEC61968.Assets.Asset",
        transient=True,
        opposite="DocumentRoles",
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

    Document = Instance("CIM.IEC61968.Common.Document",
        transient=True,
        opposite="AssetRoles",
        editor=InstanceEditor(name="_documents"))

    def _get_documents(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Document" ]
        else:
            return []

    _documents = Property(fget=_get_documents)

    #--------------------------------------------------------------------------
    #  Begin "DocAssetRole" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "category",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "status", "Asset", "Document",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.DocAssetRole",
        title="DocAssetRole",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "DocAssetRole" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SubstationAsset" class:
#------------------------------------------------------------------------------

class SubstationAsset(AssetContainer):
    """ A grouping of assets such as conductors, transformers, switchgear, etc. When located on the ground surface, it is usually surrounded by some kind of fence with a locked gate. It may also be located inside buildings, in underground vaults, and on structures. Use 'category' for utility-specific categorisation (such as Air Cooled, Gas Insultated, etc.).
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Substation = Instance("CIM.IEC61970.Core.Substation",
        transient=True,
        opposite="SubstationAsset",
        editor=InstanceEditor(name="_substations"))

    def _get_substations(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Core.Substation" ]
        else:
            return []

    _substations = Property(fget=_get_substations)

    # Function of this substation asset.
    function = SubstationFunctionKind(desc="Function of this substation asset.")

    #--------------------------------------------------------------------------
    #  Begin "SubstationAsset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "initialCondition", "category", "lotNumber", "application", "serialNumber", "installationDate", "corporateCode", "purchasePrice", "manufacturedDate", "initialLossOfLife", "utcNumber", "critical", "function",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "Measurements", "Hazards", "ErpOrganisationRoles", "DimensionsInfo", "ScheduledEvents", "Mediums", "AssetFunctions", "Properties", "AssetContainer", "Ratings", "ActivityRecords", "FromAssetRoles", "LocationRoles", "PowerSystemResourceRoles", "DocumentRoles", "ChangeItems", "ErpItemMaster", "ElectronicAddresses", "WorkTask", "ErpRecDeliveryItems", "ReliabilityInfos", "ToAssetRoles", "AssetPropertyCurves", "FinancialInfo", "ErpInventory", "acceptanceTest", "status", "LandProperties", "Assets", "Seals", "Substation",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.SubstationAsset",
        title="SubstationAsset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SubstationAsset" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SVCInfo" class:
#------------------------------------------------------------------------------

class SVCInfo(ElectricalInfo):
    """ Properties for an SVC, allowing the capacitive and inductive ratings for each phase to be specified individually if required.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    SVCTypeAssets = List(Instance("CIM.IEC61968.Informative.InfTypeAsset.SVCTypeAsset"))

    SVCAsset = Instance("CIM.IEC61968.Informative.InfAssets.SVCAsset",
        transient=True,
        opposite="SvcInfo",
        editor=InstanceEditor(name="_svcassets"))

    def _get_svcassets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssets.SVCAsset" ]
        else:
            return []

    _svcassets = Property(fget=_get_svcassets)

    SVCAssetModel = Instance("CIM.IEC61968.Informative.InfAssetModels.SVCAssetModel",
        transient=True,
        opposite="SvcInfo",
        editor=InstanceEditor(name="_svcassetmodels"))

    def _get_svcassetmodels(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssetModels.SVCAssetModel" ]
        else:
            return []

    _svcassetmodels = Property(fget=_get_svcassetmodels)

    # Maximum capacitive reactive power
    capacitiveRating = Reactance(desc="Maximum capacitive reactive power")

    # Maximum inductive reactive power
    inductiveRating = Reactance(desc="Maximum inductive reactive power")

    #--------------------------------------------------------------------------
    #  Begin "SVCInfo" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "b", "wireCount", "r0", "frequency", "g", "ratedVoltage", "x", "phaseCount", "ratedCurrent", "b0", "r", "g0", "ratedApparentPower", "x0", "bil", "capacitiveRating", "inductiveRating",
                label="Attributes", columns=2),
            VGroup("Parent", "ModelingAuthoritySet", "EndDeviceAssets", "ElectricalTypeAssets", "ElectricalAssets", "ElectricalAssetModels", "SVCTypeAssets", "SVCAsset", "SVCAssetModel",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.SVCInfo",
        title="SVCInfo",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SVCInfo" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "CompositeSwitchAsset" class:
#------------------------------------------------------------------------------

class CompositeSwitchAsset(Asset):
    """ Physical asset that performs a given CompositeSwitch's role.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    CompositeSwitchInfo = Instance("CIM.IEC61968.Informative.InfAssets.CompositeSwitchInfo",
        transient=True,
        opposite="CompositeSwitchAssets",
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

    CompositeSwitchAssetModel = Instance("CIM.IEC61968.Informative.InfAssetModels.CompositeSwitchAssetModel",
        transient=True,
        opposite="CompositeSwitchAssets",
        editor=InstanceEditor(name="_compositeswitchassetmodels"))

    def _get_compositeswitchassetmodels(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssetModels.CompositeSwitchAssetModel" ]
        else:
            return []

    _compositeswitchassetmodels = Property(fget=_get_compositeswitchassetmodels)

    # Kind of composite switch.
    kind = CompositeSwitchKind(desc="Kind of composite switch.")

    #--------------------------------------------------------------------------
    #  Begin "CompositeSwitchAsset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "initialCondition", "category", "lotNumber", "application", "serialNumber", "installationDate", "corporateCode", "purchasePrice", "manufacturedDate", "initialLossOfLife", "utcNumber", "critical", "kind",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "Measurements", "Hazards", "ErpOrganisationRoles", "DimensionsInfo", "ScheduledEvents", "Mediums", "AssetFunctions", "Properties", "AssetContainer", "Ratings", "ActivityRecords", "FromAssetRoles", "LocationRoles", "PowerSystemResourceRoles", "DocumentRoles", "ChangeItems", "ErpItemMaster", "ElectronicAddresses", "WorkTask", "ErpRecDeliveryItems", "ReliabilityInfos", "ToAssetRoles", "AssetPropertyCurves", "FinancialInfo", "ErpInventory", "acceptanceTest", "status", "CompositeSwitchInfo", "CompositeSwitchAssetModel",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.CompositeSwitchAsset",
        title="CompositeSwitchAsset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "CompositeSwitchAsset" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "AssetPropertyCurve" class:
#------------------------------------------------------------------------------

class AssetPropertyCurve(Curve):
    """ An Asset Property that is described through curves rather than as a data point. The relationship is to be defined between an independent variable (X-axis) and one or two dependent variables (Y1-axis and Y2-axis).
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Specification = Instance("CIM.IEC61968.Informative.InfAssets.Specification",
        transient=True,
        opposite="AssetPropertyCurves",
        editor=InstanceEditor(name="_specifications"))

    def _get_specifications(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssets.Specification" ]
        else:
            return []

    _specifications = Property(fget=_get_specifications)

    Assets = List(Instance("CIM.IEC61968.Assets.Asset"))

    #--------------------------------------------------------------------------
    #  Begin "AssetPropertyCurve" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "y3Multiplier", "y2Multiplier", "xMultiplier", "y2Unit", "curveStyle", "y1Unit", "y1Multiplier", "y3Unit", "xUnit",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "CurveDatas", "Specification", "Assets",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.AssetPropertyCurve",
        title="AssetPropertyCurve",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "AssetPropertyCurve" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Specification" class:
#------------------------------------------------------------------------------

class Specification(Document):
    """ Specification can be used for various purposes relative to an asset, a logical device (PowerSystemResource), location, etc. Examples include documents supplied by manufacturers such as asset installation instructions, asset maintenance instructions, etc.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # UserAttributes used to specify further properties of the asset covered with this specification. Use 'name' to specify what kind of property it is, and 'value.value' attribute for the actual value.
    AssetProperites = List(Instance("CIM.IEC61968.Common.UserAttribute"),
        desc="UserAttributes used to specify further properties of the asset covered with this specification. Use 'name' to specify what kind of property it is, and 'value.value' attribute for the actual value.")

    QualificationRequirements = List(Instance("CIM.IEC61968.Informative.InfWork.QualificationRequirement"))

    # UserAttributes used to specify ratings of the asset covered by this specification. Ratings also can be used to set the initial value of operational measurement limits. Use 'name' to specify what kind of rating it is (e.g., voltage, current), and 'value' attribute for the actual value and unit information of the rating.
    Ratings = List(Instance("CIM.IEC61968.Common.UserAttribute"),
        desc="UserAttributes used to specify ratings of the asset covered by this specification. Ratings also can be used to set the initial value of operational measurement limits. Use 'name' to specify what kind of rating it is (e.g., voltage, current), and 'value' attribute for the actual value and unit information of the rating.")

    DimensionsInfos = List(Instance("CIM.IEC61968.Informative.InfAssets.DimensionsInfo"))

    ReliabilityInfos = List(Instance("CIM.IEC61968.Informative.InfAssets.ReliabilityInfo"))

    Mediums = List(Instance("CIM.IEC61968.Informative.InfAssets.Medium"))

    AssetPropertyCurves = List(Instance("CIM.IEC61968.Informative.InfAssets.AssetPropertyCurve"))

    #--------------------------------------------------------------------------
    #  Begin "Specification" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "AssetProperites", "QualificationRequirements", "Ratings", "DimensionsInfos", "ReliabilityInfos", "Mediums", "AssetPropertyCurves",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.Specification",
        title="Specification",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Specification" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "BushingInsulationPF" class:
#------------------------------------------------------------------------------

class BushingInsulationPF(IdentifiedObject):
    """ Bushing insulation power factor condition as a result of a test. Typical status values are: Acceptable, Minor Deterioration or Moisture Absorption, Major Deterioration or Moisture Absorption, Failed.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    BushingAsset = Instance("CIM.IEC61968.Informative.InfAssets.BushingAsset",
        transient=True,
        opposite="BushingInsulationPFs",
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

    TransformerObservation = Instance("CIM.IEC61968.Informative.InfAssets.TransformerObservation",
        transient=True,
        opposite="BushingInsultationPFs",
        editor=InstanceEditor(name="_transformerobservations"))

    def _get_transformerobservations(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssets.TransformerObservation" ]
        else:
            return []

    _transformerobservations = Property(fget=_get_transformerobservations)

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

    # Kind of test for this bushing.
    testKind = BushingInsulationPfTestKind(desc="Kind of test for this bushing.")

    #--------------------------------------------------------------------------
    #  Begin "BushingInsulationPF" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "testKind",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "BushingAsset", "TransformerObservation", "status",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.BushingInsulationPF",
        title="BushingInsulationPF",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "BushingInsulationPF" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "DimensionsInfo" class:
#------------------------------------------------------------------------------

class DimensionsInfo(IdentifiedObject):
    """ As applicable, the basic linear, area, or volume dimensions of an asset, asset type (AssetModel) or other type of object (such as land area). Units and multipliers are specified per dimension.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Assets = List(Instance("CIM.IEC61968.Assets.Asset"))

    Specifications = List(Instance("CIM.IEC61968.Informative.InfAssets.Specification"))

    Locations = List(Instance("CIM.IEC61968.Common.Location"))

    # Length measurement.
    sizeLength = Length(desc="Length measurement.")

    # Depth measurement.
    sizeDepth = Length(desc="Depth measurement.")

    # Diameter measurement.
    sizeDiameter = Length(desc="Diameter measurement.")

    # A description of the orientation of the object relative to the dimensions. As an example, a vault may have north-south orientation for the sizeLength measurement and sizeDepth may be the height of the vault.
    orientation = Str(desc="A description of the orientation of the object relative to the dimensions. As an example, a vault may have north-south orientation for the sizeLength measurement and sizeDepth may be the height of the vault.")

    # Width measurement.
    sizeWidth = Length(desc="Width measurement.")

    #--------------------------------------------------------------------------
    #  Begin "DimensionsInfo" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "sizeLength", "sizeDepth", "sizeDiameter", "orientation", "sizeWidth",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Assets", "Specifications", "Locations",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.DimensionsInfo",
        title="DimensionsInfo",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "DimensionsInfo" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ComEquipmentAsset" class:
#------------------------------------------------------------------------------

class ComEquipmentAsset(AssetContainer):
    """ Communicaiton equipment, other than media, such as gateways, routers, controllers, etc.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # All device functions of this communication equipment asset.
    DeviceFunctions = List(Instance("CIM.IEC61968.Metering.DeviceFunction"),
        desc="All device functions of this communication equipment asset.")

    #--------------------------------------------------------------------------
    #  Begin "ComEquipmentAsset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "initialCondition", "category", "lotNumber", "application", "serialNumber", "installationDate", "corporateCode", "purchasePrice", "manufacturedDate", "initialLossOfLife", "utcNumber", "critical",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "Measurements", "Hazards", "ErpOrganisationRoles", "DimensionsInfo", "ScheduledEvents", "Mediums", "AssetFunctions", "Properties", "AssetContainer", "Ratings", "ActivityRecords", "FromAssetRoles", "LocationRoles", "PowerSystemResourceRoles", "DocumentRoles", "ChangeItems", "ErpItemMaster", "ElectronicAddresses", "WorkTask", "ErpRecDeliveryItems", "ReliabilityInfos", "ToAssetRoles", "AssetPropertyCurves", "FinancialInfo", "ErpInventory", "acceptanceTest", "status", "LandProperties", "Assets", "Seals", "DeviceFunctions",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.ComEquipmentAsset",
        title="ComEquipmentAsset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ComEquipmentAsset" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "BushingAsset" class:
#------------------------------------------------------------------------------

class BushingAsset(Asset):
    """ Physical bushing that insulates and protects from abrasion a conductor that passes through it. It is associated with a specific Terminal, which is in turn associated with a ConductingEquipment.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Terminal = Instance("CIM.IEC61970.Core.Terminal",
        transient=True,
        opposite="BushingAsset",
        editor=InstanceEditor(name="_terminals"))

    def _get_terminals(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Core.Terminal" ]
        else:
            return []

    _terminals = Property(fget=_get_terminals)

    BushingInsulationPFs = List(Instance("CIM.IEC61968.Informative.InfAssets.BushingInsulationPF"))

    BushingModel = Instance("CIM.IEC61968.Informative.InfAssetModels.BushingModel",
        transient=True,
        opposite="BushingAsset",
        editor=InstanceEditor(name="_bushingmodels"))

    def _get_bushingmodels(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssetModels.BushingModel" ]
        else:
            return []

    _bushingmodels = Property(fget=_get_bushingmodels)

    # Factory measured capacitance measured between the power factor tap and ground.
    c2Capacitance = Capacitance(desc="Factory measured capacitance measured between the power factor tap and ground.")

    # Factory measured insulation power factor, measured between the power factor tap and the bushing conductor.
    c1PowerFactor = Float(desc="Factory measured insulation power factor, measured between the power factor tap and the bushing conductor.")

    # Factory measured insulation power factor, measured between the power factor tap and ground.
    c2PowerFactor = Float(desc="Factory measured insulation power factor, measured between the power factor tap and ground.")

    # Factory measured capacitance, measured between the power factor tap and the bushing conductor.
    c1Capacitance = Capacitance(desc="Factory measured capacitance, measured between the power factor tap and the bushing conductor.")

    #--------------------------------------------------------------------------
    #  Begin "BushingAsset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "initialCondition", "category", "lotNumber", "application", "serialNumber", "installationDate", "corporateCode", "purchasePrice", "manufacturedDate", "initialLossOfLife", "utcNumber", "critical", "c2Capacitance", "c1PowerFactor", "c2PowerFactor", "c1Capacitance",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "Measurements", "Hazards", "ErpOrganisationRoles", "DimensionsInfo", "ScheduledEvents", "Mediums", "AssetFunctions", "Properties", "AssetContainer", "Ratings", "ActivityRecords", "FromAssetRoles", "LocationRoles", "PowerSystemResourceRoles", "DocumentRoles", "ChangeItems", "ErpItemMaster", "ElectronicAddresses", "WorkTask", "ErpRecDeliveryItems", "ReliabilityInfos", "ToAssetRoles", "AssetPropertyCurves", "FinancialInfo", "ErpInventory", "acceptanceTest", "status", "Terminal", "BushingInsulationPFs", "BushingModel",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.BushingAsset",
        title="BushingAsset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "BushingAsset" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Cabinet" class:
#------------------------------------------------------------------------------

class Cabinet(AssetContainer):
    """ Enclosure that offers protection to the equipment it contains and/or safety to people/animals outside it.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    CabinetModel = Instance("CIM.IEC61968.Informative.InfAssetModels.CabinetModel",
        transient=True,
        opposite="Cabinets",
        editor=InstanceEditor(name="_cabinetmodels"))

    def _get_cabinetmodels(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssetModels.CabinetModel" ]
        else:
            return []

    _cabinetmodels = Property(fget=_get_cabinetmodels)

    #--------------------------------------------------------------------------
    #  Begin "Cabinet" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "initialCondition", "category", "lotNumber", "application", "serialNumber", "installationDate", "corporateCode", "purchasePrice", "manufacturedDate", "initialLossOfLife", "utcNumber", "critical",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "Measurements", "Hazards", "ErpOrganisationRoles", "DimensionsInfo", "ScheduledEvents", "Mediums", "AssetFunctions", "Properties", "AssetContainer", "Ratings", "ActivityRecords", "FromAssetRoles", "LocationRoles", "PowerSystemResourceRoles", "DocumentRoles", "ChangeItems", "ErpItemMaster", "ElectronicAddresses", "WorkTask", "ErpRecDeliveryItems", "ReliabilityInfos", "ToAssetRoles", "AssetPropertyCurves", "FinancialInfo", "ErpInventory", "acceptanceTest", "status", "LandProperties", "Assets", "Seals", "CabinetModel",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.Cabinet",
        title="Cabinet",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Cabinet" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ReliabilityInfo" class:
#------------------------------------------------------------------------------

class ReliabilityInfo(IdentifiedObject):
    """ Information regarding the experienced and expected reliability of a specific asset, type of asset, or asset model.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Specification = Instance("CIM.IEC61968.Informative.InfAssets.Specification",
        transient=True,
        opposite="ReliabilityInfos",
        editor=InstanceEditor(name="_specifications"))

    def _get_specifications(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssets.Specification" ]
        else:
            return []

    _specifications = Property(fget=_get_specifications)

    Assets = List(Instance("CIM.IEC61968.Assets.Asset"))

    # Momentary failure rate (temporary failures/kft-year).
    momFailureRate = PerCent(desc="Momentary failure rate (temporary failures/kft-year).")

    # Mean time to repair (MTTR - hours).
    mTTR = Hours(desc="Mean time to repair (MTTR - hours).")

    #--------------------------------------------------------------------------
    #  Begin "ReliabilityInfo" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "momFailureRate", "mTTR",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Specification", "Assets",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.ReliabilityInfo",
        title="ReliabilityInfo",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ReliabilityInfo" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "OrgAssetRole" class:
#------------------------------------------------------------------------------

class OrgAssetRole(Role):
    """ The roles played between an Organisations and an Asset.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Asset = Instance("CIM.IEC61968.Assets.Asset",
        transient=True,
        opposite="ErpOrganisationRoles",
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

    ErpOrganisation = Instance("CIM.IEC61968.Informative.InfERPSupport.ErpOrganisation",
        transient=True,
        opposite="AssetRoles",
        editor=InstanceEditor(name="_erporganisations"))

    def _get_erporganisations(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfERPSupport.ErpOrganisation" ]
        else:
            return []

    _erporganisations = Property(fget=_get_erporganisations)

    # If the role type is 'owner,' this indicate the percentage of ownership.
    percentOwnership = Float(desc="If the role type is 'owner,' this indicate the percentage of ownership.")

    #--------------------------------------------------------------------------
    #  Begin "OrgAssetRole" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "category", "percentOwnership",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "status", "Asset", "ErpOrganisation",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.OrgAssetRole",
        title="OrgAssetRole",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "OrgAssetRole" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "FinancialInfo" class:
#------------------------------------------------------------------------------

class FinancialInfo(IdentifiedObject):
    """ Various current financial properties associated with a particular asset. Historical properties may be determined by ActivityRecords associated with the asset.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Asset = Instance("CIM.IEC61968.Assets.Asset",
        transient=True,
        opposite="FinancialInfo",
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

    # Category of cost to which this Material Item belongs.
    costType = Str(desc="Category of cost to which this Material Item belongs.")

    # Date and time asset's financial value was put in plant for regulatory accounting purposes (e.g., for rate base calculations). This is sometime referred to as the 'in-service date.'
    plantTransferDateTime = Date(desc="Date and time asset's financial value was put in plant for regulatory accounting purposes (e.g., for rate base calculations). This is sometime referred to as the 'in-service date.'")

    # The actual purchase cost of this particular asset.
    actualPurchaseCost = Money(desc="The actual purchase cost of this particular asset.")

    # Date and time asset was purchased.
    purchaseDateTime = Date(desc="Date and time asset was purchased.")

    # Purchase order identifier.
    purchaseOrderNumber = Str(desc="Purchase order identifier.")

    # Date and time warranty on asset expires.
    warrantyEndDateTime = Date(desc="Date and time warranty on asset expires.")

    # Date and time at which the financial value was last established.
    valueDateTime = Date(desc="Date and time at which the financial value was last established.")

    # The account to which this actual material item is charged.
    account = Str(desc="The account to which this actual material item is charged.")

    # Value of asset as of 'valueDateTime'.
    financialValue = Money(desc="Value of asset as of 'valueDateTime'.")

    # The quantity of the asset if per unit length, for example conductor.
    quantity = IntegerQuantity(desc="The quantity of the asset if per unit length, for example conductor.")

    # Description of the cost.
    costDescription = Str(desc="Description of the cost.")

    #--------------------------------------------------------------------------
    #  Begin "FinancialInfo" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "costType", "plantTransferDateTime", "actualPurchaseCost", "purchaseDateTime", "purchaseOrderNumber", "warrantyEndDateTime", "valueDateTime", "account", "financialValue", "quantity", "costDescription",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "Asset",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.FinancialInfo",
        title="FinancialInfo",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "FinancialInfo" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SwitchAsset" class:
#------------------------------------------------------------------------------

class SwitchAsset(ElectricalAsset):
    """ Physical asset performing Switch function.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    SwitchInfo = Instance("CIM.IEC61968.Informative.InfAssets.SwitchInfo",
        transient=True,
        opposite="SwitchAssets",
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

    SwitchAssetModel = Instance("CIM.IEC61968.Informative.InfAssetModels.SwitchAssetModel",
        transient=True,
        opposite="SwitchAssets",
        editor=InstanceEditor(name="_switchassetmodels"))

    def _get_switchassetmodels(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssetModels.SwitchAssetModel" ]
        else:
            return []

    _switchassetmodels = Property(fget=_get_switchassetmodels)

    #--------------------------------------------------------------------------
    #  Begin "SwitchAsset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "initialCondition", "category", "lotNumber", "application", "serialNumber", "installationDate", "corporateCode", "purchasePrice", "manufacturedDate", "initialLossOfLife", "utcNumber", "critical", "phaseCode", "isConnected",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "Measurements", "Hazards", "ErpOrganisationRoles", "DimensionsInfo", "ScheduledEvents", "Mediums", "AssetFunctions", "Properties", "AssetContainer", "Ratings", "ActivityRecords", "FromAssetRoles", "LocationRoles", "PowerSystemResourceRoles", "DocumentRoles", "ChangeItems", "ErpItemMaster", "ElectronicAddresses", "WorkTask", "ErpRecDeliveryItems", "ReliabilityInfos", "ToAssetRoles", "AssetPropertyCurves", "FinancialInfo", "ErpInventory", "acceptanceTest", "status", "ElectricalInfos", "ConductingEquipment", "SwitchInfo", "SwitchAssetModel",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.SwitchAsset",
        title="SwitchAsset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SwitchAsset" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "RecloserInfo" class:
#------------------------------------------------------------------------------

class RecloserInfo(SwitchInfo):
    """ Properties of reclosers.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    RecloserAssetModels = List(Instance("CIM.IEC61968.Informative.InfAssetModels.RecloserAssetModel"))

    RecloserTypeAsset = Instance("CIM.IEC61968.Informative.InfTypeAsset.RecloserTypeAsset",
        transient=True,
        opposite="RecloserInfo",
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

    # True if normal status of ground trip is enabled.
    groundTripNormalEnabled = Bool(desc="True if normal status of ground trip is enabled.")

    # True if device has ground trip capability.
    groundTripCapable = Bool(desc="True if device has ground trip capability.")

    # Ground trip rating.
    groundTripRating = CurrentFlow(desc="Ground trip rating.")

    # Phase trip rating.
    phaseTripRating = CurrentFlow(desc="Phase trip rating.")

    # Total number of phase reclose operations.
    recloseLockoutCount = Int(desc="Total number of phase reclose operations.")

    #--------------------------------------------------------------------------
    #  Begin "RecloserInfo" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "b", "wireCount", "r0", "frequency", "g", "ratedVoltage", "x", "phaseCount", "ratedCurrent", "b0", "r", "g0", "ratedApparentPower", "x0", "bil", "makingCapacity", "poleCount", "interruptingRating", "withstandCurrent", "minimumCurrent", "loadBreak", "gang", "dielectricStrength", "remote", "groundTripNormalEnabled", "groundTripCapable", "groundTripRating", "phaseTripRating", "recloseLockoutCount",
                label="Attributes", columns=3),
            VGroup("Parent", "ModelingAuthoritySet", "EndDeviceAssets", "ElectricalTypeAssets", "ElectricalAssets", "ElectricalAssetModels", "SwitchAssets", "SwitchAssetModel", "SwitchTypeAsset", "RecloserAssetModels", "RecloserTypeAsset", "RecloserAssets",
                label="References", columns=1),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.RecloserInfo",
        title="RecloserInfo",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "RecloserInfo" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "BusbarAsset" class:
#------------------------------------------------------------------------------

class BusbarAsset(ElectricalAsset):
    """ Physical asset used to perform the BusbarSection's role.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    BusbarAssetModel = Instance("CIM.IEC61968.Informative.InfAssetModels.BusbarAssetModel",
        transient=True,
        opposite="BusbarAssets",
        editor=InstanceEditor(name="_busbarassetmodels"))

    def _get_busbarassetmodels(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssetModels.BusbarAssetModel" ]
        else:
            return []

    _busbarassetmodels = Property(fget=_get_busbarassetmodels)

    #--------------------------------------------------------------------------
    #  Begin "BusbarAsset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "initialCondition", "category", "lotNumber", "application", "serialNumber", "installationDate", "corporateCode", "purchasePrice", "manufacturedDate", "initialLossOfLife", "utcNumber", "critical", "phaseCode", "isConnected",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "Measurements", "Hazards", "ErpOrganisationRoles", "DimensionsInfo", "ScheduledEvents", "Mediums", "AssetFunctions", "Properties", "AssetContainer", "Ratings", "ActivityRecords", "FromAssetRoles", "LocationRoles", "PowerSystemResourceRoles", "DocumentRoles", "ChangeItems", "ErpItemMaster", "ElectronicAddresses", "WorkTask", "ErpRecDeliveryItems", "ReliabilityInfos", "ToAssetRoles", "AssetPropertyCurves", "FinancialInfo", "ErpInventory", "acceptanceTest", "status", "ElectricalInfos", "ConductingEquipment", "BusbarAssetModel",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.BusbarAsset",
        title="BusbarAsset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "BusbarAsset" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Guy" class:
#------------------------------------------------------------------------------

class Guy(StructureSupport):
    """ A type of support for structures.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "Guy" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "initialCondition", "category", "lotNumber", "application", "serialNumber", "installationDate", "corporateCode", "purchasePrice", "manufacturedDate", "initialLossOfLife", "utcNumber", "critical", "length", "direction", "size", "rodLength", "rodCount",
                label="Attributes", columns=2),
            VGroup("Parent", "ModelingAuthoritySet", "Measurements", "Hazards", "ErpOrganisationRoles", "DimensionsInfo", "ScheduledEvents", "Mediums", "AssetFunctions", "Properties", "AssetContainer", "Ratings", "ActivityRecords", "FromAssetRoles", "LocationRoles", "PowerSystemResourceRoles", "DocumentRoles", "ChangeItems", "ErpItemMaster", "ElectronicAddresses", "WorkTask", "ErpRecDeliveryItems", "ReliabilityInfos", "ToAssetRoles", "AssetPropertyCurves", "FinancialInfo", "ErpInventory", "acceptanceTest", "status", "SecuredStructure",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.Guy",
        title="Guy",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Guy" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "CableAsset" class:
#------------------------------------------------------------------------------

class CableAsset(ConductorAsset):
    """ Insultated physical cable for performing the Conductor role used in undergrond and other applications..
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    DuctBanks = List(Instance("CIM.IEC61968.Informative.InfAssets.DuctBank"))

    DuctBankTypeAsset = Instance("CIM.IEC61968.Informative.InfTypeAsset.DuctTypeAsset",
        transient=True,
        opposite="CableAssets",
        editor=InstanceEditor(name="_ducttypeassets"))

    def _get_ducttypeassets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfTypeAsset.DuctTypeAsset" ]
        else:
            return []

    _ducttypeassets = Property(fget=_get_ducttypeassets)

    #--------------------------------------------------------------------------
    #  Begin "CableAsset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "initialCondition", "category", "lotNumber", "application", "serialNumber", "installationDate", "corporateCode", "purchasePrice", "manufacturedDate", "initialLossOfLife", "utcNumber", "critical", "groundingMethod", "isHorizontal", "insulated",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "Measurements", "Hazards", "ErpOrganisationRoles", "DimensionsInfo", "ScheduledEvents", "Mediums", "AssetFunctions", "Properties", "AssetContainer", "Ratings", "ActivityRecords", "FromAssetRoles", "LocationRoles", "PowerSystemResourceRoles", "DocumentRoles", "ChangeItems", "ErpItemMaster", "ElectronicAddresses", "WorkTask", "ErpRecDeliveryItems", "ReliabilityInfos", "ToAssetRoles", "AssetPropertyCurves", "FinancialInfo", "ErpInventory", "acceptanceTest", "status", "CircuitSection", "ConductorAssetModel", "ConductorSegment", "DuctBanks", "DuctBankTypeAsset",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.CableAsset",
        title="CableAsset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "CableAsset" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GeneratorAsset" class:
#------------------------------------------------------------------------------

class GeneratorAsset(ElectricalAsset):
    """ Physical asset performing the Generator role.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    GeneratorAssetModel = Instance("CIM.IEC61968.Informative.InfAssetModels.GeneratorAssetModel",
        transient=True,
        opposite="GeneratorAssets",
        editor=InstanceEditor(name="_generatorassetmodels"))

    def _get_generatorassetmodels(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssetModels.GeneratorAssetModel" ]
        else:
            return []

    _generatorassetmodels = Property(fget=_get_generatorassetmodels)

    #--------------------------------------------------------------------------
    #  Begin "GeneratorAsset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "initialCondition", "category", "lotNumber", "application", "serialNumber", "installationDate", "corporateCode", "purchasePrice", "manufacturedDate", "initialLossOfLife", "utcNumber", "critical", "phaseCode", "isConnected",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "Measurements", "Hazards", "ErpOrganisationRoles", "DimensionsInfo", "ScheduledEvents", "Mediums", "AssetFunctions", "Properties", "AssetContainer", "Ratings", "ActivityRecords", "FromAssetRoles", "LocationRoles", "PowerSystemResourceRoles", "DocumentRoles", "ChangeItems", "ErpItemMaster", "ElectronicAddresses", "WorkTask", "ErpRecDeliveryItems", "ReliabilityInfos", "ToAssetRoles", "AssetPropertyCurves", "FinancialInfo", "ErpInventory", "acceptanceTest", "status", "ElectricalInfos", "ConductingEquipment", "GeneratorAssetModel",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.GeneratorAsset",
        title="GeneratorAsset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GeneratorAsset" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "UndergroundStructure" class:
#------------------------------------------------------------------------------

class UndergroundStructure(Structure):
    """ Abstract class for underground structures. Typical structure types are: BURD, Enclosure, Hand Hole, Manhole, Pad/Slab, Subsurface Enclosure, Trench, Tunnel, Vault, Pull/Splice Box.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Date sealing warranty expires.
    sealingWarrantyExpiresDate = AbsoluteDate(desc="Date sealing warranty expires.")

    # True if vault is ventilating.
    ventilation = Bool(desc="True if vault is ventilating.")

    # Primary material of underground structure.
    material = Str(desc="Primary material of underground structure.")

    #--------------------------------------------------------------------------
    #  Begin "UndergroundStructure" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "initialCondition", "category", "lotNumber", "application", "serialNumber", "installationDate", "corporateCode", "purchasePrice", "manufacturedDate", "initialLossOfLife", "utcNumber", "critical", "materialKind", "height", "removeWeed", "weedRemovedDate", "fumigantAppliedDate", "fumigantName", "sealingWarrantyExpiresDate", "ventilation", "material",
                label="Attributes", columns=2),
            VGroup("Parent", "ModelingAuthoritySet", "Measurements", "Hazards", "ErpOrganisationRoles", "DimensionsInfo", "ScheduledEvents", "Mediums", "AssetFunctions", "Properties", "AssetContainer", "Ratings", "ActivityRecords", "FromAssetRoles", "LocationRoles", "PowerSystemResourceRoles", "DocumentRoles", "ChangeItems", "ErpItemMaster", "ElectronicAddresses", "WorkTask", "ErpRecDeliveryItems", "ReliabilityInfos", "ToAssetRoles", "AssetPropertyCurves", "FinancialInfo", "ErpInventory", "acceptanceTest", "status", "LandProperties", "Assets", "Seals", "StructureSupports",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.UndergroundStructure",
        title="UndergroundStructure",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "UndergroundStructure" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ShuntCompensatorAsset" class:
#------------------------------------------------------------------------------

class ShuntCompensatorAsset(ElectricalAsset):
    """ For a shunt capacitor or reactor or switchable bank of shunt capacitors or reactors, this is the physical asset performing the ShuntCompensator role (PSR).
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ShuntCompensatorAssetModel = Instance("CIM.IEC61968.Informative.InfAssetModels.ShuntCompensatorAssetModel",
        transient=True,
        opposite="ShuntCompensatorAssets",
        editor=InstanceEditor(name="_shuntcompensatorassetmodels"))

    def _get_shuntcompensatorassetmodels(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssetModels.ShuntCompensatorAssetModel" ]
        else:
            return []

    _shuntcompensatorassetmodels = Property(fget=_get_shuntcompensatorassetmodels)

    ShuntImpedanceInfo = Instance("CIM.IEC61968.Informative.InfAssets.ShuntImpedanceInfo",
        transient=True,
        opposite="ShuntCompensatorAssets",
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
    #  Begin "ShuntCompensatorAsset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "initialCondition", "category", "lotNumber", "application", "serialNumber", "installationDate", "corporateCode", "purchasePrice", "manufacturedDate", "initialLossOfLife", "utcNumber", "critical", "phaseCode", "isConnected",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "Measurements", "Hazards", "ErpOrganisationRoles", "DimensionsInfo", "ScheduledEvents", "Mediums", "AssetFunctions", "Properties", "AssetContainer", "Ratings", "ActivityRecords", "FromAssetRoles", "LocationRoles", "PowerSystemResourceRoles", "DocumentRoles", "ChangeItems", "ErpItemMaster", "ElectronicAddresses", "WorkTask", "ErpRecDeliveryItems", "ReliabilityInfos", "ToAssetRoles", "AssetPropertyCurves", "FinancialInfo", "ErpInventory", "acceptanceTest", "status", "ElectricalInfos", "ConductingEquipment", "ShuntCompensatorAssetModel", "ShuntImpedanceInfo",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.ShuntCompensatorAsset",
        title="ShuntCompensatorAsset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ShuntCompensatorAsset" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SurgeProtectorAsset" class:
#------------------------------------------------------------------------------

class SurgeProtectorAsset(ElectricalAsset):
    """ Physical asset performing SurgeProtector function.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    SurgeProtector = Instance("CIM.IEC61970.Protection.SurgeProtector",
        transient=True,
        opposite="SurgeProtectorAsset",
        editor=InstanceEditor(name="_surgeprotectors"))

    def _get_surgeprotectors(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Protection.SurgeProtector" ]
        else:
            return []

    _surgeprotectors = Property(fget=_get_surgeprotectors)

    SurgeProtectorAssetModel = Instance("CIM.IEC61968.Informative.InfAssetModels.SurgeProtectorAssetModel",
        transient=True,
        opposite="SurgeProtectorAssets",
        editor=InstanceEditor(name="_surgeprotectorassetmodels"))

    def _get_surgeprotectorassetmodels(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssetModels.SurgeProtectorAssetModel" ]
        else:
            return []

    _surgeprotectorassetmodels = Property(fget=_get_surgeprotectorassetmodels)

    #--------------------------------------------------------------------------
    #  Begin "SurgeProtectorAsset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "initialCondition", "category", "lotNumber", "application", "serialNumber", "installationDate", "corporateCode", "purchasePrice", "manufacturedDate", "initialLossOfLife", "utcNumber", "critical", "phaseCode", "isConnected",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "Measurements", "Hazards", "ErpOrganisationRoles", "DimensionsInfo", "ScheduledEvents", "Mediums", "AssetFunctions", "Properties", "AssetContainer", "Ratings", "ActivityRecords", "FromAssetRoles", "LocationRoles", "PowerSystemResourceRoles", "DocumentRoles", "ChangeItems", "ErpItemMaster", "ElectronicAddresses", "WorkTask", "ErpRecDeliveryItems", "ReliabilityInfos", "ToAssetRoles", "AssetPropertyCurves", "FinancialInfo", "ErpInventory", "acceptanceTest", "status", "ElectricalInfos", "ConductingEquipment", "SurgeProtector", "SurgeProtectorAssetModel",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.SurgeProtectorAsset",
        title="SurgeProtectorAsset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SurgeProtectorAsset" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "PotentialTransformerAsset" class:
#------------------------------------------------------------------------------

class PotentialTransformerAsset(ElectricalAsset):
    """ Physical asset performing Potential Transformer (PT) function.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    PotentialTransformer = Instance("CIM.IEC61970.Meas.PotentialTransformer",
        transient=True,
        opposite="PotentialTransformerAsset",
        editor=InstanceEditor(name="_potentialtransformers"))

    def _get_potentialtransformers(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Meas.PotentialTransformer" ]
        else:
            return []

    _potentialtransformers = Property(fget=_get_potentialtransformers)

    PotentialTransformerInfo = Instance("CIM.IEC61968.Informative.InfAssets.PotentialTransformerInfo",
        transient=True,
        opposite="PotentialTransformerAssets",
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

    PotentialTransformerAssetModel = Instance("CIM.IEC61968.Informative.InfAssetModels.PotentialTransformerAssetModel",
        transient=True,
        opposite="PotentialTransformerAssets",
        editor=InstanceEditor(name="_potentialtransformerassetmodels"))

    def _get_potentialtransformerassetmodels(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssetModels.PotentialTransformerAssetModel" ]
        else:
            return []

    _potentialtransformerassetmodels = Property(fget=_get_potentialtransformerassetmodels)

    #--------------------------------------------------------------------------
    #  Begin "PotentialTransformerAsset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "initialCondition", "category", "lotNumber", "application", "serialNumber", "installationDate", "corporateCode", "purchasePrice", "manufacturedDate", "initialLossOfLife", "utcNumber", "critical", "phaseCode", "isConnected",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "Measurements", "Hazards", "ErpOrganisationRoles", "DimensionsInfo", "ScheduledEvents", "Mediums", "AssetFunctions", "Properties", "AssetContainer", "Ratings", "ActivityRecords", "FromAssetRoles", "LocationRoles", "PowerSystemResourceRoles", "DocumentRoles", "ChangeItems", "ErpItemMaster", "ElectronicAddresses", "WorkTask", "ErpRecDeliveryItems", "ReliabilityInfos", "ToAssetRoles", "AssetPropertyCurves", "FinancialInfo", "ErpInventory", "acceptanceTest", "status", "ElectricalInfos", "ConductingEquipment", "PotentialTransformer", "PotentialTransformerInfo", "PotentialTransformerAssetModel",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.PotentialTransformerAsset",
        title="PotentialTransformerAsset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "PotentialTransformerAsset" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "TestDataSet" class:
#------------------------------------------------------------------------------

class TestDataSet(ProcedureDataSet):
    """ Test results, usually obtained by a lab or other independent organisation.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Identifier of specimen used in inspection or test.
    specimenID = Str(desc="Identifier of specimen used in inspection or test.")

    # Conclusion drawn from test results.
    conclusion = Str(desc="Conclusion drawn from test results.")

    # Date and time the specimen was received by the lab.
    specimenToLabDateTime = Date(desc="Date and time the specimen was received by the lab.")

    #--------------------------------------------------------------------------
    #  Begin "TestDataSet" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "completedDateTime", "specimenID", "conclusion", "specimenToLabDateTime",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "Procedure", "Properties", "MeasurementValues", "TransformerObservations",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.TestDataSet",
        title="TestDataSet",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TestDataSet" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "FACTSDeviceAsset" class:
#------------------------------------------------------------------------------

class FACTSDeviceAsset(ElectricalAsset):
    """ Physical asset used to perform the FACTSDevice's role.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    FACTSDeviceAssetModel = Instance("CIM.IEC61968.Informative.InfAssetModels.FACTSDeviceAssetModel",
        transient=True,
        opposite="FACTSDeviceAssets",
        editor=InstanceEditor(name="_factsdeviceassetmodels"))

    def _get_factsdeviceassetmodels(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssetModels.FACTSDeviceAssetModel" ]
        else:
            return []

    _factsdeviceassetmodels = Property(fget=_get_factsdeviceassetmodels)

    # Kind of FACTS device.
    kind = FactsDeviceKind(desc="Kind of FACTS device.")

    #--------------------------------------------------------------------------
    #  Begin "FACTSDeviceAsset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "initialCondition", "category", "lotNumber", "application", "serialNumber", "installationDate", "corporateCode", "purchasePrice", "manufacturedDate", "initialLossOfLife", "utcNumber", "critical", "phaseCode", "isConnected", "kind",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "Measurements", "Hazards", "ErpOrganisationRoles", "DimensionsInfo", "ScheduledEvents", "Mediums", "AssetFunctions", "Properties", "AssetContainer", "Ratings", "ActivityRecords", "FromAssetRoles", "LocationRoles", "PowerSystemResourceRoles", "DocumentRoles", "ChangeItems", "ErpItemMaster", "ElectronicAddresses", "WorkTask", "ErpRecDeliveryItems", "ReliabilityInfos", "ToAssetRoles", "AssetPropertyCurves", "FinancialInfo", "ErpInventory", "acceptanceTest", "status", "ElectricalInfos", "ConductingEquipment", "FACTSDeviceAssetModel",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.FACTSDeviceAsset",
        title="FACTSDeviceAsset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "FACTSDeviceAsset" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "OverheadConductorAsset" class:
#------------------------------------------------------------------------------

class OverheadConductorAsset(ConductorAsset):
    """ Physical conductor performing the Conductor role that is used in overhead applications.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    MountingPoint = Instance("CIM.IEC61968.Informative.InfTypeAsset.MountingPoint",
        transient=True,
        opposite="OverheadConductors",
        editor=InstanceEditor(name="_mountingpoints"))

    def _get_mountingpoints(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfTypeAsset.MountingPoint" ]
        else:
            return []

    _mountingpoints = Property(fget=_get_mountingpoints)

    #--------------------------------------------------------------------------
    #  Begin "OverheadConductorAsset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "initialCondition", "category", "lotNumber", "application", "serialNumber", "installationDate", "corporateCode", "purchasePrice", "manufacturedDate", "initialLossOfLife", "utcNumber", "critical", "groundingMethod", "isHorizontal", "insulated",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "Measurements", "Hazards", "ErpOrganisationRoles", "DimensionsInfo", "ScheduledEvents", "Mediums", "AssetFunctions", "Properties", "AssetContainer", "Ratings", "ActivityRecords", "FromAssetRoles", "LocationRoles", "PowerSystemResourceRoles", "DocumentRoles", "ChangeItems", "ErpItemMaster", "ElectronicAddresses", "WorkTask", "ErpRecDeliveryItems", "ReliabilityInfos", "ToAssetRoles", "AssetPropertyCurves", "FinancialInfo", "ErpInventory", "acceptanceTest", "status", "CircuitSection", "ConductorAssetModel", "ConductorSegment", "MountingPoint",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.OverheadConductorAsset",
        title="OverheadConductorAsset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "OverheadConductorAsset" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SVCAsset" class:
#------------------------------------------------------------------------------

class SVCAsset(FACTSDeviceAsset):
    """ Physical asset performing StaticVarCompensator function.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    SvcInfo = Instance("CIM.IEC61968.Informative.InfAssets.SVCInfo",
        transient=True,
        opposite="SVCAsset",
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

    SVCAssetModel = Instance("CIM.IEC61968.Informative.InfAssetModels.SVCAssetModel",
        transient=True,
        opposite="SVCAssets",
        editor=InstanceEditor(name="_svcassetmodels"))

    def _get_svcassetmodels(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssetModels.SVCAssetModel" ]
        else:
            return []

    _svcassetmodels = Property(fget=_get_svcassetmodels)

    #--------------------------------------------------------------------------
    #  Begin "SVCAsset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "initialCondition", "category", "lotNumber", "application", "serialNumber", "installationDate", "corporateCode", "purchasePrice", "manufacturedDate", "initialLossOfLife", "utcNumber", "critical", "phaseCode", "isConnected", "kind",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "Measurements", "Hazards", "ErpOrganisationRoles", "DimensionsInfo", "ScheduledEvents", "Mediums", "AssetFunctions", "Properties", "AssetContainer", "Ratings", "ActivityRecords", "FromAssetRoles", "LocationRoles", "PowerSystemResourceRoles", "DocumentRoles", "ChangeItems", "ErpItemMaster", "ElectronicAddresses", "WorkTask", "ErpRecDeliveryItems", "ReliabilityInfos", "ToAssetRoles", "AssetPropertyCurves", "FinancialInfo", "ErpInventory", "acceptanceTest", "status", "ElectricalInfos", "ConductingEquipment", "FACTSDeviceAssetModel", "SvcInfo", "SVCAssetModel",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.SVCAsset",
        title="SVCAsset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SVCAsset" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ProtectionEquipmentAsset" class:
#------------------------------------------------------------------------------

class ProtectionEquipmentAsset(ElectricalAsset):
    """ Physical asset performing ProtectionEquipment function.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ProtectionEquipmentAssetModel = Instance("CIM.IEC61968.Informative.InfAssetModels.ProtectionEquipmentAssetModel",
        transient=True,
        opposite="ProtectionEquipmentAssets",
        editor=InstanceEditor(name="_protectionequipmentassetmodels"))

    def _get_protectionequipmentassetmodels(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssetModels.ProtectionEquipmentAssetModel" ]
        else:
            return []

    _protectionequipmentassetmodels = Property(fget=_get_protectionequipmentassetmodels)

    # Actual phase trip for this type of relay, if applicable.
    phaseTrip = CurrentFlow(desc="Actual phase trip for this type of relay, if applicable.")

    # Actual ground trip for this type of relay, if applicable.
    groundTrip = CurrentFlow(desc="Actual ground trip for this type of relay, if applicable.")

    #--------------------------------------------------------------------------
    #  Begin "ProtectionEquipmentAsset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "initialCondition", "category", "lotNumber", "application", "serialNumber", "installationDate", "corporateCode", "purchasePrice", "manufacturedDate", "initialLossOfLife", "utcNumber", "critical", "phaseCode", "isConnected", "phaseTrip", "groundTrip",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "Measurements", "Hazards", "ErpOrganisationRoles", "DimensionsInfo", "ScheduledEvents", "Mediums", "AssetFunctions", "Properties", "AssetContainer", "Ratings", "ActivityRecords", "FromAssetRoles", "LocationRoles", "PowerSystemResourceRoles", "DocumentRoles", "ChangeItems", "ErpItemMaster", "ElectronicAddresses", "WorkTask", "ErpRecDeliveryItems", "ReliabilityInfos", "ToAssetRoles", "AssetPropertyCurves", "FinancialInfo", "ErpInventory", "acceptanceTest", "status", "ElectricalInfos", "ConductingEquipment", "ProtectionEquipmentAssetModel",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.ProtectionEquipmentAsset",
        title="ProtectionEquipmentAsset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ProtectionEquipmentAsset" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Manhole" class:
#------------------------------------------------------------------------------

class Manhole(UndergroundStructure):
    """ Provides access at key locations to underground cables, equipment, etc. housed inside a protective vault.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "Manhole" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "initialCondition", "category", "lotNumber", "application", "serialNumber", "installationDate", "corporateCode", "purchasePrice", "manufacturedDate", "initialLossOfLife", "utcNumber", "critical", "materialKind", "height", "removeWeed", "weedRemovedDate", "fumigantAppliedDate", "fumigantName", "sealingWarrantyExpiresDate", "ventilation", "material",
                label="Attributes", columns=2),
            VGroup("Parent", "ModelingAuthoritySet", "Measurements", "Hazards", "ErpOrganisationRoles", "DimensionsInfo", "ScheduledEvents", "Mediums", "AssetFunctions", "Properties", "AssetContainer", "Ratings", "ActivityRecords", "FromAssetRoles", "LocationRoles", "PowerSystemResourceRoles", "DocumentRoles", "ChangeItems", "ErpItemMaster", "ElectronicAddresses", "WorkTask", "ErpRecDeliveryItems", "ReliabilityInfos", "ToAssetRoles", "AssetPropertyCurves", "FinancialInfo", "ErpInventory", "acceptanceTest", "status", "LandProperties", "Assets", "Seals", "StructureSupports",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.Manhole",
        title="Manhole",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Manhole" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "BreakerAsset" class:
#------------------------------------------------------------------------------

class BreakerAsset(ElectricalAsset):
    """ Physical asset performing Breaker role.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    BreakerInfo = Instance("CIM.IEC61968.Informative.InfAssets.BreakerInfo",
        transient=True,
        opposite="BreakerAssets",
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

    BreakerAssetModel = Instance("CIM.IEC61968.Informative.InfAssetModels.BreakerAssetModel",
        transient=True,
        opposite="BreakerAssets",
        editor=InstanceEditor(name="_breakerassetmodels"))

    def _get_breakerassetmodels(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssetModels.BreakerAssetModel" ]
        else:
            return []

    _breakerassetmodels = Property(fget=_get_breakerassetmodels)

    #--------------------------------------------------------------------------
    #  Begin "BreakerAsset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "initialCondition", "category", "lotNumber", "application", "serialNumber", "installationDate", "corporateCode", "purchasePrice", "manufacturedDate", "initialLossOfLife", "utcNumber", "critical", "phaseCode", "isConnected",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "Measurements", "Hazards", "ErpOrganisationRoles", "DimensionsInfo", "ScheduledEvents", "Mediums", "AssetFunctions", "Properties", "AssetContainer", "Ratings", "ActivityRecords", "FromAssetRoles", "LocationRoles", "PowerSystemResourceRoles", "DocumentRoles", "ChangeItems", "ErpItemMaster", "ElectronicAddresses", "WorkTask", "ErpRecDeliveryItems", "ReliabilityInfos", "ToAssetRoles", "AssetPropertyCurves", "FinancialInfo", "ErpInventory", "acceptanceTest", "status", "ElectricalInfos", "ConductingEquipment", "BreakerInfo", "BreakerAssetModel",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.BreakerAsset",
        title="BreakerAsset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "BreakerAsset" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SeriesCompensatorAsset" class:
#------------------------------------------------------------------------------

class SeriesCompensatorAsset(ElectricalAsset):
    """ For a a series capacitor or reactor, this is the physical asset performing the SeriesCompensator role (PSR).
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    SeriesCompensatorAssetModel = Instance("CIM.IEC61968.Informative.InfAssetModels.SeriesCompensatorAssetModel",
        transient=True,
        opposite="SeriesCompensatorAsset",
        editor=InstanceEditor(name="_seriescompensatorassetmodels"))

    def _get_seriescompensatorassetmodels(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssetModels.SeriesCompensatorAssetModel" ]
        else:
            return []

    _seriescompensatorassetmodels = Property(fget=_get_seriescompensatorassetmodels)

    #--------------------------------------------------------------------------
    #  Begin "SeriesCompensatorAsset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "initialCondition", "category", "lotNumber", "application", "serialNumber", "installationDate", "corporateCode", "purchasePrice", "manufacturedDate", "initialLossOfLife", "utcNumber", "critical", "phaseCode", "isConnected",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "Measurements", "Hazards", "ErpOrganisationRoles", "DimensionsInfo", "ScheduledEvents", "Mediums", "AssetFunctions", "Properties", "AssetContainer", "Ratings", "ActivityRecords", "FromAssetRoles", "LocationRoles", "PowerSystemResourceRoles", "DocumentRoles", "ChangeItems", "ErpItemMaster", "ElectronicAddresses", "WorkTask", "ErpRecDeliveryItems", "ReliabilityInfos", "ToAssetRoles", "AssetPropertyCurves", "FinancialInfo", "ErpInventory", "acceptanceTest", "status", "ElectricalInfos", "ConductingEquipment", "SeriesCompensatorAssetModel",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.SeriesCompensatorAsset",
        title="SeriesCompensatorAsset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SeriesCompensatorAsset" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Pole" class:
#------------------------------------------------------------------------------

class Pole(Structure):
    """ A long, slender piece of wood, metal, etc. usually rounded that stands vertically from the ground and is used for mounting various types of overhead equipment. Dimensions of Pole are specified in associated DimensionsInfo.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Streetlight(s) may be attached to a pole.
    SupportStreetlights = List(Instance("CIM.IEC61968.Informative.InfAssets.Streetlight"),
        desc="Streetlight(s) may be attached to a pole.")

    PoleModel = Instance("CIM.IEC61968.Informative.InfAssetModels.PoleModel",
        transient=True,
        opposite="Poles",
        editor=InstanceEditor(name="_polemodels"))

    def _get_polemodels(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssetModels.PoleModel" ]
        else:
            return []

    _polemodels = Property(fget=_get_polemodels)

    # Kind of base for this pole.
    baseKind = PoleBaseKind(desc="Kind of base for this pole.")

    # Kind of preservative for this pole.
    preservativeKind = PolePreservativeKind(desc="Kind of preservative for this pole.")

    # Kind of treatment for this pole.
    treatmentKind = PoleTreatmentKind(desc="Kind of treatment for this pole.")

    # Date and time pole was last treated with preservative.
    treatedDateTime = Date(desc="Date and time pole was last treated with preservative.")

    # The framing structure mounted on the pole.
    construction = Str(desc="The framing structure mounted on the pole.")

    # True if a block of material has been attached to base of pole in ground for stability. This technique is used primarily when anchors can not be used.
    breastBlock = Bool(desc="True if a block of material has been attached to base of pole in ground for stability. This technique is used primarily when anchors can not be used.")

    # Joint pole agreement reference number.
    jpaReference = Str(desc="Joint pole agreement reference number.")

    #--------------------------------------------------------------------------
    #  Begin "Pole" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "initialCondition", "category", "lotNumber", "application", "serialNumber", "installationDate", "corporateCode", "purchasePrice", "manufacturedDate", "initialLossOfLife", "utcNumber", "critical", "materialKind", "height", "removeWeed", "weedRemovedDate", "fumigantAppliedDate", "fumigantName", "baseKind", "preservativeKind", "treatmentKind", "treatedDateTime", "construction", "breastBlock", "jpaReference",
                label="Attributes", columns=2),
            VGroup("Parent", "ModelingAuthoritySet", "Measurements", "Hazards", "ErpOrganisationRoles", "DimensionsInfo", "ScheduledEvents", "Mediums", "AssetFunctions", "Properties", "AssetContainer", "Ratings", "ActivityRecords", "FromAssetRoles", "LocationRoles", "PowerSystemResourceRoles", "DocumentRoles", "ChangeItems", "ErpItemMaster", "ElectronicAddresses", "WorkTask", "ErpRecDeliveryItems", "ReliabilityInfos", "ToAssetRoles", "AssetPropertyCurves", "FinancialInfo", "ErpInventory", "acceptanceTest", "status", "LandProperties", "Assets", "Seals", "StructureSupports", "SupportStreetlights", "PoleModel",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.Pole",
        title="Pole",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Pole" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Anchor" class:
#------------------------------------------------------------------------------

class Anchor(StructureSupport):
    """ A type of support for structures, used to hold poles secure.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Kind of this anchor.
    kind = AnchorKind(desc="Kind of this anchor.")

    #--------------------------------------------------------------------------
    #  Begin "Anchor" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "initialCondition", "category", "lotNumber", "application", "serialNumber", "installationDate", "corporateCode", "purchasePrice", "manufacturedDate", "initialLossOfLife", "utcNumber", "critical", "length", "direction", "size", "rodLength", "rodCount", "kind",
                label="Attributes", columns=2),
            VGroup("Parent", "ModelingAuthoritySet", "Measurements", "Hazards", "ErpOrganisationRoles", "DimensionsInfo", "ScheduledEvents", "Mediums", "AssetFunctions", "Properties", "AssetContainer", "Ratings", "ActivityRecords", "FromAssetRoles", "LocationRoles", "PowerSystemResourceRoles", "DocumentRoles", "ChangeItems", "ErpItemMaster", "ElectronicAddresses", "WorkTask", "ErpRecDeliveryItems", "ReliabilityInfos", "ToAssetRoles", "AssetPropertyCurves", "FinancialInfo", "ErpInventory", "acceptanceTest", "status", "SecuredStructure",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.Anchor",
        title="Anchor",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Anchor" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "CurrentTransformerAsset" class:
#------------------------------------------------------------------------------

class CurrentTransformerAsset(ElectricalAsset):
    """ Physical asset performing Current Transformer (CT) function.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    CurrentTransformerInfo = Instance("CIM.IEC61968.Informative.InfAssets.CurrentTransformerInfo",
        transient=True,
        opposite="CurrentTransformerAssets",
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

    CurrentTransformerAssetModel = Instance("CIM.IEC61968.Informative.InfAssetModels.CurrentTransformerAssetModel",
        transient=True,
        opposite="CurrentTransformerAssets",
        editor=InstanceEditor(name="_currenttransformerassetmodels"))

    def _get_currenttransformerassetmodels(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssetModels.CurrentTransformerAssetModel" ]
        else:
            return []

    _currenttransformerassetmodels = Property(fget=_get_currenttransformerassetmodels)

    CurrentTransformer = Instance("CIM.IEC61970.Meas.CurrentTransformer",
        transient=True,
        opposite="CurrentTransformerAsset",
        editor=InstanceEditor(name="_currenttransformers"))

    def _get_currenttransformers(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Meas.CurrentTransformer" ]
        else:
            return []

    _currenttransformers = Property(fget=_get_currenttransformers)

    # Type of CT as categorized by the utility's asset management standards and practices.
    typeCT = Str(desc="Type of CT as categorized by the utility's asset management standards and practices.")

    #--------------------------------------------------------------------------
    #  Begin "CurrentTransformerAsset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "initialCondition", "category", "lotNumber", "application", "serialNumber", "installationDate", "corporateCode", "purchasePrice", "manufacturedDate", "initialLossOfLife", "utcNumber", "critical", "phaseCode", "isConnected", "typeCT",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "Measurements", "Hazards", "ErpOrganisationRoles", "DimensionsInfo", "ScheduledEvents", "Mediums", "AssetFunctions", "Properties", "AssetContainer", "Ratings", "ActivityRecords", "FromAssetRoles", "LocationRoles", "PowerSystemResourceRoles", "DocumentRoles", "ChangeItems", "ErpItemMaster", "ElectronicAddresses", "WorkTask", "ErpRecDeliveryItems", "ReliabilityInfos", "ToAssetRoles", "AssetPropertyCurves", "FinancialInfo", "ErpInventory", "acceptanceTest", "status", "ElectricalInfos", "ConductingEquipment", "CurrentTransformerInfo", "CurrentTransformerAssetModel", "CurrentTransformer",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.CurrentTransformerAsset",
        title="CurrentTransformerAsset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "CurrentTransformerAsset" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ResistorAsset" class:
#------------------------------------------------------------------------------

class ResistorAsset(ElectricalAsset):
    """ Physical asset performing Resistor function.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Resistor = Instance("CIM.IEC61970.Wires.Resistor",
        transient=True,
        opposite="ResistorAsset",
        editor=InstanceEditor(name="_resistors"))

    def _get_resistors(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Wires.Resistor" ]
        else:
            return []

    _resistors = Property(fget=_get_resistors)

    ResistorAssetModel = Instance("CIM.IEC61968.Informative.InfAssetModels.ResistorAssetModel",
        transient=True,
        opposite="ResistorAssets",
        editor=InstanceEditor(name="_resistorassetmodels"))

    def _get_resistorassetmodels(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssetModels.ResistorAssetModel" ]
        else:
            return []

    _resistorassetmodels = Property(fget=_get_resistorassetmodels)

    #--------------------------------------------------------------------------
    #  Begin "ResistorAsset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "initialCondition", "category", "lotNumber", "application", "serialNumber", "installationDate", "corporateCode", "purchasePrice", "manufacturedDate", "initialLossOfLife", "utcNumber", "critical", "phaseCode", "isConnected",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "Measurements", "Hazards", "ErpOrganisationRoles", "DimensionsInfo", "ScheduledEvents", "Mediums", "AssetFunctions", "Properties", "AssetContainer", "Ratings", "ActivityRecords", "FromAssetRoles", "LocationRoles", "PowerSystemResourceRoles", "DocumentRoles", "ChangeItems", "ErpItemMaster", "ElectronicAddresses", "WorkTask", "ErpRecDeliveryItems", "ReliabilityInfos", "ToAssetRoles", "AssetPropertyCurves", "FinancialInfo", "ErpInventory", "acceptanceTest", "status", "ElectricalInfos", "ConductingEquipment", "Resistor", "ResistorAssetModel",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.ResistorAsset",
        title="ResistorAsset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ResistorAsset" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Streetlight" class:
#------------------------------------------------------------------------------

class Streetlight(ElectricalAsset):
    """ Streetlight asset.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Streetlight(s) may be attached to a pole.
    AttachedToPole = Instance("CIM.IEC61968.Informative.InfAssets.Pole",
        desc="Streetlight(s) may be attached to a pole.",
        transient=True,
        opposite="SupportStreetlights",
        editor=InstanceEditor(name="_poles"))

    def _get_poles(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssets.Pole" ]
        else:
            return []

    _poles = Property(fget=_get_poles)

    StreetlightAssetModel = Instance("CIM.IEC61968.Informative.InfAssetModels.StreetlightAssetModel",
        transient=True,
        opposite="Streetlights",
        editor=InstanceEditor(name="_streetlightassetmodels"))

    def _get_streetlightassetmodels(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssetModels.StreetlightAssetModel" ]
        else:
            return []

    _streetlightassetmodels = Property(fget=_get_streetlightassetmodels)

    # Lamp kind currently installed.
    lampKind = StreetlightLampKind(desc="Lamp kind currently installed.")

    # Actual power rating of light.
    lightRating = ActivePower(desc="Actual power rating of light.")

    # Length of arm of this specific asset. Note that a new light may be placed on an existing arm.
    armLength = Length(desc="Length of arm of this specific asset. Note that a new light may be placed on an existing arm.")

    #--------------------------------------------------------------------------
    #  Begin "Streetlight" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "initialCondition", "category", "lotNumber", "application", "serialNumber", "installationDate", "corporateCode", "purchasePrice", "manufacturedDate", "initialLossOfLife", "utcNumber", "critical", "phaseCode", "isConnected", "lampKind", "lightRating", "armLength",
                label="Attributes", columns=2),
            VGroup("Parent", "ModelingAuthoritySet", "Measurements", "Hazards", "ErpOrganisationRoles", "DimensionsInfo", "ScheduledEvents", "Mediums", "AssetFunctions", "Properties", "AssetContainer", "Ratings", "ActivityRecords", "FromAssetRoles", "LocationRoles", "PowerSystemResourceRoles", "DocumentRoles", "ChangeItems", "ErpItemMaster", "ElectronicAddresses", "WorkTask", "ErpRecDeliveryItems", "ReliabilityInfos", "ToAssetRoles", "AssetPropertyCurves", "FinancialInfo", "ErpInventory", "acceptanceTest", "status", "ElectricalInfos", "ConductingEquipment", "AttachedToPole", "StreetlightAssetModel",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.Streetlight",
        title="Streetlight",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Streetlight" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "JointAsset" class:
#------------------------------------------------------------------------------

class JointAsset(ElectricalAsset):
    """ Physical asset connecting two or more cable assets. It includes the portion of cable under wipes, welds, or other seals.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Configuration of joint.
    configurationKind = JointConfigurationKind(desc="Configuration of joint.")

    # Material used to fill the joint.
    fillKind = JointFillKind(desc="Material used to fill the joint.")

    # The type of insulation around the joint, classified according to the utility's asset management standards and practices.
    insulation = Str(desc="The type of insulation around the joint, classified according to the utility's asset management standards and practices.")

    #--------------------------------------------------------------------------
    #  Begin "JointAsset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "initialCondition", "category", "lotNumber", "application", "serialNumber", "installationDate", "corporateCode", "purchasePrice", "manufacturedDate", "initialLossOfLife", "utcNumber", "critical", "phaseCode", "isConnected", "configurationKind", "fillKind", "insulation",
                label="Attributes", columns=2),
            VGroup("Parent", "ModelingAuthoritySet", "Measurements", "Hazards", "ErpOrganisationRoles", "DimensionsInfo", "ScheduledEvents", "Mediums", "AssetFunctions", "Properties", "AssetContainer", "Ratings", "ActivityRecords", "FromAssetRoles", "LocationRoles", "PowerSystemResourceRoles", "DocumentRoles", "ChangeItems", "ErpItemMaster", "ElectronicAddresses", "WorkTask", "ErpRecDeliveryItems", "ReliabilityInfos", "ToAssetRoles", "AssetPropertyCurves", "FinancialInfo", "ErpInventory", "acceptanceTest", "status", "ElectricalInfos", "ConductingEquipment",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.JointAsset",
        title="JointAsset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "JointAsset" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "RecloserAsset" class:
#------------------------------------------------------------------------------

class RecloserAsset(ElectricalAsset):
    """ Physical recloser performing a reclosing function, which is modeled through Breaker.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    RecloserAssetModel = Instance("CIM.IEC61968.Informative.InfAssetModels.RecloserAssetModel",
        transient=True,
        opposite="RecloserAssets",
        editor=InstanceEditor(name="_recloserassetmodels"))

    def _get_recloserassetmodels(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssetModels.RecloserAssetModel" ]
        else:
            return []

    _recloserassetmodels = Property(fget=_get_recloserassetmodels)

    RecloserInfo = Instance("CIM.IEC61968.Informative.InfAssets.RecloserInfo",
        transient=True,
        opposite="RecloserAssets",
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

    #--------------------------------------------------------------------------
    #  Begin "RecloserAsset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "initialCondition", "category", "lotNumber", "application", "serialNumber", "installationDate", "corporateCode", "purchasePrice", "manufacturedDate", "initialLossOfLife", "utcNumber", "critical", "phaseCode", "isConnected",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "Measurements", "Hazards", "ErpOrganisationRoles", "DimensionsInfo", "ScheduledEvents", "Mediums", "AssetFunctions", "Properties", "AssetContainer", "Ratings", "ActivityRecords", "FromAssetRoles", "LocationRoles", "PowerSystemResourceRoles", "DocumentRoles", "ChangeItems", "ErpItemMaster", "ElectronicAddresses", "WorkTask", "ErpRecDeliveryItems", "ReliabilityInfos", "ToAssetRoles", "AssetPropertyCurves", "FinancialInfo", "ErpInventory", "acceptanceTest", "status", "ElectricalInfos", "ConductingEquipment", "RecloserAssetModel", "RecloserInfo",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.RecloserAsset",
        title="RecloserAsset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "RecloserAsset" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Tower" class:
#------------------------------------------------------------------------------

class Tower(Structure):
    """ Large structure used to carry transmission lines, subtransmission lines, and/or other equipment/lines (e.g., communication). Dimensions of the Tower are specified in associated DimensionsInfo class.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    TowerAssetModel = Instance("CIM.IEC61968.Informative.InfAssetModels.TowerAssetModel",
        transient=True,
        opposite="Towers",
        editor=InstanceEditor(name="_towerassetmodels"))

    def _get_towerassetmodels(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssetModels.TowerAssetModel" ]
        else:
            return []

    _towerassetmodels = Property(fget=_get_towerassetmodels)

    # Construction structure on the tower.
    constructionKind = TowerConstructionKind(desc="Construction structure on the tower.")

    #--------------------------------------------------------------------------
    #  Begin "Tower" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "initialCondition", "category", "lotNumber", "application", "serialNumber", "installationDate", "corporateCode", "purchasePrice", "manufacturedDate", "initialLossOfLife", "utcNumber", "critical", "materialKind", "height", "removeWeed", "weedRemovedDate", "fumigantAppliedDate", "fumigantName", "constructionKind",
                label="Attributes", columns=2),
            VGroup("Parent", "ModelingAuthoritySet", "Measurements", "Hazards", "ErpOrganisationRoles", "DimensionsInfo", "ScheduledEvents", "Mediums", "AssetFunctions", "Properties", "AssetContainer", "Ratings", "ActivityRecords", "FromAssetRoles", "LocationRoles", "PowerSystemResourceRoles", "DocumentRoles", "ChangeItems", "ErpItemMaster", "ElectronicAddresses", "WorkTask", "ErpRecDeliveryItems", "ReliabilityInfos", "ToAssetRoles", "AssetPropertyCurves", "FinancialInfo", "ErpInventory", "acceptanceTest", "status", "LandProperties", "Assets", "Seals", "StructureSupports", "TowerAssetModel",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.Tower",
        title="Tower",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Tower" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "FaultIndicatorAsset" class:
#------------------------------------------------------------------------------

class FaultIndicatorAsset(ElectricalAsset):
    """ Physical asset performing FaultIndicator function.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    FaultIndicator = Instance("CIM.IEC61970.Protection.FaultIndicator",
        transient=True,
        opposite="FaultIndicatorAssets",
        editor=InstanceEditor(name="_faultindicators"))

    def _get_faultindicators(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Protection.FaultIndicator" ]
        else:
            return []

    _faultindicators = Property(fget=_get_faultindicators)

    FaultIndicatorAssetModel = Instance("CIM.IEC61968.Informative.InfAssetModels.FaultIndicatorAssetModel",
        transient=True,
        opposite="FaultIndicatorAssets",
        editor=InstanceEditor(name="_faultindicatorassetmodels"))

    def _get_faultindicatorassetmodels(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssetModels.FaultIndicatorAssetModel" ]
        else:
            return []

    _faultindicatorassetmodels = Property(fget=_get_faultindicatorassetmodels)

    #--------------------------------------------------------------------------
    #  Begin "FaultIndicatorAsset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "initialCondition", "category", "lotNumber", "application", "serialNumber", "installationDate", "corporateCode", "purchasePrice", "manufacturedDate", "initialLossOfLife", "utcNumber", "critical", "phaseCode", "isConnected",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "Measurements", "Hazards", "ErpOrganisationRoles", "DimensionsInfo", "ScheduledEvents", "Mediums", "AssetFunctions", "Properties", "AssetContainer", "Ratings", "ActivityRecords", "FromAssetRoles", "LocationRoles", "PowerSystemResourceRoles", "DocumentRoles", "ChangeItems", "ErpItemMaster", "ElectronicAddresses", "WorkTask", "ErpRecDeliveryItems", "ReliabilityInfos", "ToAssetRoles", "AssetPropertyCurves", "FinancialInfo", "ErpInventory", "acceptanceTest", "status", "ElectricalInfos", "ConductingEquipment", "FaultIndicator", "FaultIndicatorAssetModel",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.FaultIndicatorAsset",
        title="FaultIndicatorAsset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "FaultIndicatorAsset" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "BreakerInfo" class:
#------------------------------------------------------------------------------

class BreakerInfo(SwitchInfo):
    """ Properties of breakers.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    BreakerAssets = List(Instance("CIM.IEC61968.Informative.InfAssets.BreakerAsset"))

    BreakerAssetModels = List(Instance("CIM.IEC61968.Informative.InfAssetModels.BreakerAssetModel"))

    BreakerTypeAsset = Instance("CIM.IEC61968.Informative.InfTypeAsset.BreakerTypeAsset",
        transient=True,
        opposite="BreakerInfo",
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

    # Phase trip rating.
    phaseTrip = CurrentFlow(desc="Phase trip rating.")

    #--------------------------------------------------------------------------
    #  Begin "BreakerInfo" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "b", "wireCount", "r0", "frequency", "g", "ratedVoltage", "x", "phaseCount", "ratedCurrent", "b0", "r", "g0", "ratedApparentPower", "x0", "bil", "makingCapacity", "poleCount", "interruptingRating", "withstandCurrent", "minimumCurrent", "loadBreak", "gang", "dielectricStrength", "remote", "phaseTrip",
                label="Attributes", columns=2),
            VGroup("Parent", "ModelingAuthoritySet", "EndDeviceAssets", "ElectricalTypeAssets", "ElectricalAssets", "ElectricalAssetModels", "SwitchAssets", "SwitchAssetModel", "SwitchTypeAsset", "BreakerAssets", "BreakerAssetModels", "BreakerTypeAsset",
                label="References", columns=1),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfAssets.BreakerInfo",
        title="BreakerInfo",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "BreakerInfo" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
