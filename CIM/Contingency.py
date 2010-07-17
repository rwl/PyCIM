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

""" Contingencies to be studied.
"""
#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CIM.Core import IdentifiedObject



from enthought.traits.api import Instance, List, Property, Enum, Bool
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------

# Indicates the state which the contingency equipment is to be in when the contingency is applied.
ContingencyEquipmentStatusKind = Enum("outOfService", "inService", desc="Indicates the state which the contingency equipment is to be in when the contingency is applied.")

#------------------------------------------------------------------------------
#  "ContingencyElement" class:
#------------------------------------------------------------------------------

class ContingencyElement(IdentifiedObject):
    """ An element of a system event to be studied by contingency analysis, representing a change in status of a single piece of equipment.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A contingency element belongs to one contingency.
    Contingency = Instance("CIM.Contingency.Contingency",
        desc="A contingency element belongs to one contingency.",
        transient=True,
        opposite="ContingencyElement",
        editor=InstanceEditor(name="_contingencys"))

    def _get_contingencys(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.Contingency.Contingency" ]
        else:
            return []

    _contingencys = Property(fget=_get_contingencys)

    #--------------------------------------------------------------------------
    #  Begin "ContingencyElement" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "Contingency",
                label="References"),
            dock="tab"),
        id="CIM.Contingency.ContingencyElement",
        title="ContingencyElement",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ContingencyElement" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Contingency" class:
#------------------------------------------------------------------------------

class Contingency(IdentifiedObject):
    """ An event threatening system reliability, consisting of one or more contingency elements.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A contingency can have any number of contingency elements.
    ContingencyElement = List(Instance("CIM.Contingency.ContingencyElement"),
        desc="A contingency can have any number of contingency elements.")

    # Set true if must study this contingency.
    mustStudy = Bool(desc="Set true if must study this contingency.")

    #--------------------------------------------------------------------------
    #  Begin "Contingency" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "mustStudy",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "ContingencyElement",
                label="References"),
            dock="tab"),
        id="CIM.Contingency.Contingency",
        title="Contingency",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Contingency" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ContingencyEquipment" class:
#------------------------------------------------------------------------------

class ContingencyEquipment(ContingencyElement):
    """ A equipment to which the in service status is to change such as a power transformer or AC line segment.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The single piece of equipment to which to apply the contingency.
    Equipment = Instance("CIM.Core.Equipment",
        desc="The single piece of equipment to which to apply the contingency.",
        transient=True,
        opposite="ContingencyEquipment",
        editor=InstanceEditor(name="_equipments"))

    def _get_equipments(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.Core.Equipment" ]
        else:
            return []

    _equipments = Property(fget=_get_equipments)

    # The status for the associated equipment when in the contingency state.   This status is independent of the case to which the contingency is originally applied, but defines the equipment status when the contingency is applied.
    contingentStatus = ContingencyEquipmentStatusKind(desc="The status for the associated equipment when in the contingency state.   This status is independent of the case to which the contingency is originally applied, but defines the equipment status when the contingency is applied.")

    #--------------------------------------------------------------------------
    #  Begin "ContingencyEquipment" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "contingentStatus",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "Contingency", "Equipment",
                label="References"),
            dock="tab"),
        id="CIM.Contingency.ContingencyEquipment",
        title="ContingencyEquipment",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ContingencyEquipment" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
