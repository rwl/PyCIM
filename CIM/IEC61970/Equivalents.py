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

""" The equivalents package models equivalent networks.
"""
#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CIM.IEC61970.Core import ConductingEquipment
from CIM.IEC61970.Core import ConnectivityNodeContainer
from CIM.IEC61970.Domain import Resistance
from CIM.IEC61970.Domain import Reactance
from CIM.IEC61970.Domain import Susceptance
from CIM.IEC61970.Domain import Conductance
from CIM.IEC61970.Domain import ActivePower
from CIM.IEC61970.Domain import Voltage



from enthought.traits.api import Instance, List, Property, Bool
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
#  "EquivalentEquipment" class:
#------------------------------------------------------------------------------

class EquivalentEquipment(ConductingEquipment):
    """ The class represents equivalent objects that are the result of a network reduction. The class is the base for equivalent objects of different types.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The equivalent where the reduced model belongs.
    EquivalentNetwork = Instance("CIM.IEC61970.Equivalents.EquivalentNetwork",
        desc="The equivalent where the reduced model belongs.",
        transient=True,
        opposite="EquivalentEquipments",
        editor=InstanceEditor(name="_equivalentnetworks"))

    def _get_equivalentnetworks(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Equivalents.EquivalentNetwork" ]
        else:
            return []

    _equivalentnetworks = Property(fget=_get_equivalentnetworks)

    #--------------------------------------------------------------------------
    #  Begin "EquivalentEquipment" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "normaIlyInService", "phases",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "ContingencyEquipment", "CustomerAgreements", "OperationalLimitSet", "EquipmentContainer", "Terminals", "ClearanceTags", "OutageStepRoles", "BaseVoltage", "ElectricalAssets", "SvStatus", "ProtectionEquipments", "EquivalentNetwork",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61970.Equivalents.EquivalentEquipment",
        title="EquivalentEquipment",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "EquivalentEquipment" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "EquivalentNetwork" class:
#------------------------------------------------------------------------------

class EquivalentNetwork(ConnectivityNodeContainer):
    """ A class that represents an external meshed network that has been reduced to an electrically equivalent model. The ConnectivityNodes contained in the equivalent are intended to reflect internal nodes of the equivalent. The boundary Connectivity nodes where the equivalent connects outside itself are NOT contained by the equivalent.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The associated reduced equivalents.
    EquivalentEquipments = List(Instance("CIM.IEC61970.Equivalents.EquivalentEquipment"),
        desc="The associated reduced equivalents.")

    #--------------------------------------------------------------------------
    #  Begin "EquivalentNetwork" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "TopologicalNode", "ConnectivityNodes", "EquivalentEquipments",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61970.Equivalents.EquivalentNetwork",
        title="EquivalentNetwork",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "EquivalentNetwork" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "EquivalentBranch" class:
#------------------------------------------------------------------------------

class EquivalentBranch(EquivalentEquipment):
    """ The class represents equivalent branches.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Positive sequence series resistance of the reduced branch.
    r = Resistance(desc="Positive sequence series resistance of the reduced branch.")

    # Positive sequence series reactance of the reduced branch.
    x = Reactance(desc="Positive sequence series reactance of the reduced branch.")

    #--------------------------------------------------------------------------
    #  Begin "EquivalentBranch" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "normaIlyInService", "phases", "r", "x",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "ContingencyEquipment", "CustomerAgreements", "OperationalLimitSet", "EquipmentContainer", "Terminals", "ClearanceTags", "OutageStepRoles", "BaseVoltage", "ElectricalAssets", "SvStatus", "ProtectionEquipments", "EquivalentNetwork",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61970.Equivalents.EquivalentBranch",
        title="EquivalentBranch",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "EquivalentBranch" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "EquivalentShunt" class:
#------------------------------------------------------------------------------

class EquivalentShunt(EquivalentEquipment):
    """ The class represents equivalent shunts.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Positive sequence shunt susceptance.
    b = Susceptance(desc="Positive sequence shunt susceptance.")

    # Positive sequence shunt conductance.
    g = Conductance(desc="Positive sequence shunt conductance.")

    #--------------------------------------------------------------------------
    #  Begin "EquivalentShunt" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "normaIlyInService", "phases", "b", "g",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "ContingencyEquipment", "CustomerAgreements", "OperationalLimitSet", "EquipmentContainer", "Terminals", "ClearanceTags", "OutageStepRoles", "BaseVoltage", "ElectricalAssets", "SvStatus", "ProtectionEquipments", "EquivalentNetwork",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61970.Equivalents.EquivalentShunt",
        title="EquivalentShunt",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "EquivalentShunt" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "EquivalentInjection" class:
#------------------------------------------------------------------------------

class EquivalentInjection(EquivalentEquipment):
    """ This class represents equivalent injections (generation or load).  Voltage regulation is allowed only at the local connectivity node.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Specifies the default regulation status of the EquivalentInjection.  True is regulating.  False is not regulating.
    regulationStatus = Bool(desc="Specifies the default regulation status of the EquivalentInjection.  True is regulating.  False is not regulating.")

    # Specifies whether or not the EquivalentInjection has the capability to regulate the local voltage.
    regulationCapability = Bool(desc="Specifies whether or not the EquivalentInjection has the capability to regulate the local voltage.")

    # Maximum active power of the injection.
    minP = ActivePower(desc="Maximum active power of the injection.")

    # Minimum active power of the injection.
    maxP = ActivePower(desc="Minimum active power of the injection.")

    # The target voltage for voltage regulation.
    regulationTarget = Voltage(desc="The target voltage for voltage regulation.")

    #--------------------------------------------------------------------------
    #  Begin "EquivalentInjection" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "normaIlyInService", "phases", "regulationStatus", "regulationCapability", "minP", "maxP", "regulationTarget",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "ContingencyEquipment", "CustomerAgreements", "OperationalLimitSet", "EquipmentContainer", "Terminals", "ClearanceTags", "OutageStepRoles", "BaseVoltage", "ElectricalAssets", "SvStatus", "ProtectionEquipments", "EquivalentNetwork",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61970.Equivalents.EquivalentInjection",
        title="EquivalentInjection",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "EquivalentInjection" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
