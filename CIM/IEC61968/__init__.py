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

""" This package contains the core information classes that support work management and network extension planning applications.
"""
#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CIM import Element



from enthought.traits.api import Str, Date
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
#  "IEC61968CIMVersion" class:
#------------------------------------------------------------------------------

class IEC61968CIMVersion(Element):
    """ IEC 61968 version number assigned to this UML model.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Form is IEC61968CIMXXvYY where XX is the major CIM package version and the YY is the minor version.  For example IEC61968CIM10v17.
    version = Str(desc="Form is IEC61968CIMXXvYY where XX is the major CIM package version and the YY is the minor version.  For example IEC61968CIM10v17.")

    # Form is YYYY-MM-DD for example for January 5, 2009 it is 2009-01-05.
    date = Date(desc="Form is YYYY-MM-DD for example for January 5, 2009 it is 2009-01-05.")

    #--------------------------------------------------------------------------
    #  Begin "IEC61968CIMVersion" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "version", "date",
                label="Attributes"),
            VGroup("Parent",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.IEC61968CIMVersion",
        title="IEC61968CIMVersion",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "IEC61968CIMVersion" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
