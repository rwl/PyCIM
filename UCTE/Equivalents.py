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

""" The equivalents package models equivalent networks.The equivalents package models equivalent networks.
"""
#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from UCTE.Core import ConductingEquipment




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
    """ The class represents equivalent objects that are the result of a network reduction. The class is the base for equivalent objects of different types.The class represents equivalent objects that are the result of a network reduction. The class is the base for equivalent objects of different types.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "EquivalentEquipment" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "name", "aliasName", "equivalent",
                label="Attributes"),
            VGroup("Model", "MemberOf_EquipmentContainer", "BaseVoltage", "Terminals",
                label="References"),
            dock="tab"),
        id="UCTE.Equivalents.EquivalentEquipment",
        title="EquivalentEquipment",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "EquivalentEquipment" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
