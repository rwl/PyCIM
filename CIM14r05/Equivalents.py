#------------------------------------------------------------------------------
# Copyright (C) 2009 Richard W. Lincoln
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 dated June, 1991.
#
# This software is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANDABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CIM14r05.Core import ConductingEquipment
from CIM14r05.Core import ConnectivityNodeContainer



from enthought.traits.api import Instance, List, Property, Float
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

    EquivalentNetwork = Instance("CIM14r05.Equivalents.EquivalentNetwork",
        transient=True,
        opposite="EquivalentEquipments",
        editor=InstanceEditor(name="_equivalentnetworks"))

    def _get_equivalentnetworks(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM14r05.Equivalents.EquivalentNetwork" ]
        else:
            return []

    _equivalentnetworks = Property(fget=_get_equivalentnetworks)

    #--------------------------------------------------------------------------
    #  Begin "EquivalentEquipment" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("description", "mRID", "pathName", "localName", "aliasName", "name", "equivalent", "normalIlyInService", "phases",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "OperatingShare", "OperatedBy_Companies", "PSRType", "PsrLists", "ReportingGroup", "OutageSchedule", "Contains_Measurements", "MemberOf_EquipmentContainer", "OperationalLimitSet", "ContingencyEquipment", "ProtectionEquipments", "SvStatus", "Terminals", "BaseVoltage", "ClearanceTags", "EquivalentNetwork",
                label="References", columns=1),
            dock="tab"),
        id="CIM14r05.Equivalents.EquivalentEquipment",
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

    EquivalentEquipments = List(Instance("CIM14r05.Equivalents.EquivalentEquipment"))

    #--------------------------------------------------------------------------
    #  Begin "EquivalentNetwork" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("description", "mRID", "pathName", "localName", "aliasName", "name",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "OperatingShare", "OperatedBy_Companies", "PSRType", "PsrLists", "ReportingGroup", "OutageSchedule", "Contains_Measurements", "ConnectivityNodes", "TopologicalNode", "EquivalentEquipments",
                label="References", columns=1),
            dock="tab"),
        id="CIM14r05.Equivalents.EquivalentNetwork",
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

    # Positive sequence series reactance of the reduced branch.
    x = Float(desc="Positive sequence series reactance of the reduced branch.")

    # Positive sequence series resistance of the reduced branch.
    r = Float(desc="Positive sequence series resistance of the reduced branch.")

    #--------------------------------------------------------------------------
    #  Begin "EquivalentBranch" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("description", "mRID", "pathName", "localName", "aliasName", "name", "equivalent", "normalIlyInService", "phases", "x", "r",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "OperatingShare", "OperatedBy_Companies", "PSRType", "PsrLists", "ReportingGroup", "OutageSchedule", "Contains_Measurements", "MemberOf_EquipmentContainer", "OperationalLimitSet", "ContingencyEquipment", "ProtectionEquipments", "SvStatus", "Terminals", "BaseVoltage", "ClearanceTags", "EquivalentNetwork",
                label="References", columns=1),
            dock="tab"),
        id="CIM14r05.Equivalents.EquivalentBranch",
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
    b = Float(desc="Positive sequence shunt susceptance.")

    # Positive sequence shunt conductance.
    g = Float(desc="Positive sequence shunt conductance.")

    #--------------------------------------------------------------------------
    #  Begin "EquivalentShunt" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("description", "mRID", "pathName", "localName", "aliasName", "name", "equivalent", "normalIlyInService", "phases", "b", "g",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "OperatingShare", "OperatedBy_Companies", "PSRType", "PsrLists", "ReportingGroup", "OutageSchedule", "Contains_Measurements", "MemberOf_EquipmentContainer", "OperationalLimitSet", "ContingencyEquipment", "ProtectionEquipments", "SvStatus", "Terminals", "BaseVoltage", "ClearanceTags", "EquivalentNetwork",
                label="References", columns=1),
            dock="tab"),
        id="CIM14r05.Equivalents.EquivalentShunt",
        title="EquivalentShunt",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "EquivalentShunt" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
