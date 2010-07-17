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

from CIM.Core import ConductingEquipment
from CIM.Core import ConnectivityNodeContainer
from CIM.Domain import Conductance
from CIM.Domain import Susceptance
from CIM.Domain import Resistance
from CIM.Domain import Reactance



from enthought.traits.api import Instance, List, Property
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
    EquivalentNetwork = Instance("CIM.Equivalents.EquivalentNetwork",
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
                    "CIM.Equivalents.EquivalentNetwork" ]
        else:
            return []

    _equivalentnetworks = Property(fget=_get_equivalentnetworks)

    #--------------------------------------------------------------------------
    #  Begin "EquivalentEquipment" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "equivalent", "normalIlyInService", "phases",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "OperatedBy_Companies", "PsrLists", "Contains_Measurements", "OperatingShare", "OutageSchedule", "ReportingGroup", "PSRType", "OperationalLimitSet", "MemberOf_EquipmentContainer", "ContingencyEquipment", "SvStatus", "BaseVoltage", "ProtectionEquipments", "Terminals", "ClearanceTags", "EquivalentNetwork",
                label="References", columns=1),
            dock="tab"),
        id="CIM.Equivalents.EquivalentEquipment",
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
    EquivalentEquipments = List(Instance("CIM.Equivalents.EquivalentEquipment"),
        desc="The associated reduced equivalents.")

    #--------------------------------------------------------------------------
    #  Begin "EquivalentNetwork" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "OperatedBy_Companies", "PsrLists", "Contains_Measurements", "OperatingShare", "OutageSchedule", "ReportingGroup", "PSRType", "TopologicalNode", "ConnectivityNodes", "EquivalentEquipments",
                label="References", columns=1),
            dock="tab"),
        id="CIM.Equivalents.EquivalentNetwork",
        title="EquivalentNetwork",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "EquivalentNetwork" user definitions:
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

    # Positive sequence shunt conductance.
    g = Conductance(desc="Positive sequence shunt conductance.")

    # Positive sequence shunt susceptance.
    b = Susceptance(desc="Positive sequence shunt susceptance.")

    #--------------------------------------------------------------------------
    #  Begin "EquivalentShunt" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "equivalent", "normalIlyInService", "phases", "g", "b",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "OperatedBy_Companies", "PsrLists", "Contains_Measurements", "OperatingShare", "OutageSchedule", "ReportingGroup", "PSRType", "OperationalLimitSet", "MemberOf_EquipmentContainer", "ContingencyEquipment", "SvStatus", "BaseVoltage", "ProtectionEquipments", "Terminals", "ClearanceTags", "EquivalentNetwork",
                label="References", columns=1),
            dock="tab"),
        id="CIM.Equivalents.EquivalentShunt",
        title="EquivalentShunt",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "EquivalentShunt" user definitions:
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
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "equivalent", "normalIlyInService", "phases", "r", "x",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "OperatedBy_Companies", "PsrLists", "Contains_Measurements", "OperatingShare", "OutageSchedule", "ReportingGroup", "PSRType", "OperationalLimitSet", "MemberOf_EquipmentContainer", "ContingencyEquipment", "SvStatus", "BaseVoltage", "ProtectionEquipments", "Terminals", "ClearanceTags", "EquivalentNetwork",
                label="References", columns=1),
            dock="tab"),
        id="CIM.Equivalents.EquivalentBranch",
        title="EquivalentBranch",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "EquivalentBranch" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
