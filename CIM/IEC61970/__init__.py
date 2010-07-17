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

""" Contains the core PowerSystemResource and ConductingEquipment entities shared by all applications plus common collections of those entities. Not all applications require all the Core entities.  This package does not depend on any other package except the Domain package, but most of the other packages have associations and generalizations that depend on it.
"""
#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CIM import Element



from enthought.traits.api import Date, Str
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
    """ This is the IEC 61970 CIM version number assigned to this UML model file.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Form is YYYY-MM-DD for example for January 5, 2009 it is 2009-01-05.
    date = Date(desc="Form is YYYY-MM-DD for example for January 5, 2009 it is 2009-01-05.")

    # Form is IEC61970CIMXXvYY where XX is the major CIM package version and the YY is the minor version.   For ecample IEC61970CIM13v18.
    version = Str(desc="Form is IEC61970CIMXXvYY where XX is the major CIM package version and the YY is the minor version.   For ecample IEC61970CIM13v18.")

    #--------------------------------------------------------------------------
    #  Begin "IEC61970CIMVersion" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "date", "version",
                label="Attributes"),
            VGroup("Parent",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.IEC61970CIMVersion",
        title="IEC61970CIMVersion",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "IEC61970CIMVersion" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
