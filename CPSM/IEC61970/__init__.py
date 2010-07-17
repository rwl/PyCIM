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

""" An extension to the Core and Wires packages that models information on the current and planned network configuration. These entities are optional within typical network applications.An extension to the Core and Wires packages that models information on the current and planned network configuration. These entities are optional within typical network applications.
"""
#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CPSM import Element



from enthought.traits.api import Str, Date
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
#  "IEC61970CIMVersion" class:
#------------------------------------------------------------------------------

class IEC61970CIMVersion(Element):
    """ This is the IEC 61970 CIM version number assigned to this UML model file.This is the IEC 61970 CIM version number assigned to this UML model file.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    version = Str

    date = Date

    #--------------------------------------------------------------------------
    #  Begin "IEC61970CIMVersion" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "version", "date",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="CPSM.IEC61970.IEC61970CIMVersion",
        title="IEC61970CIMVersion",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "IEC61970CIMVersion" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
