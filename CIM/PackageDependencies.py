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

""" This package shows all the root level subpackage dependencies of the combined CIM model.
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
#  "PackageDependenciesCIMVeresion" class:
#------------------------------------------------------------------------------

class PackageDependenciesCIMVeresion(Element):
    """ The version of dependencies description among top level subpackages of the combined CIM model.  This is not the same as the combined packages version.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Date of last change to the main package dependencies in format YYYY-MM-DD.   This is updated when the version attribute is updated.
    date = Date(desc="Date of last change to the main package dependencies in format YYYY-MM-DD.   This is updated when the version attribute is updated.")

    # The version of the main subpackages of the combined CIM model.  The format is simply an integer.  The version (and date) initial values should be updated any time the dependencies in the model change and require an actual change to the diagrams within this package.
    vesion = Str(desc="The version of the main subpackages of the combined CIM model.  The format is simply an integer.  The version (and date) initial values should be updated any time the dependencies in the model change and require an actual change to the diagrams within this package.")

    #--------------------------------------------------------------------------
    #  Begin "PackageDependenciesCIMVeresion" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "date", "vesion",
                label="Attributes"),
            VGroup("Parent",
                label="References"),
            dock="tab"),
        id="CIM.PackageDependencies.PackageDependenciesCIMVeresion",
        title="PackageDependenciesCIMVeresion",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "PackageDependenciesCIMVeresion" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
