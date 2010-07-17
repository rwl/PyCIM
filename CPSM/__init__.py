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




from enthought.traits.api import HasTraits, Instance, List, Property, Str, Date
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
#  "Element" class:
#------------------------------------------------------------------------------

class Element(HasTraits):
    Model = Instance("CPSM.Model", allow_none=False,
        transient=True,
        opposite="Elements",
        editor=InstanceEditor(name="_models"))

    def _get_models(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CPSM.Model" ]
        else:
            return []

    _models = Property(fget=_get_models)

    URI = Str

    #--------------------------------------------------------------------------
    #  Begin "Element" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="CPSM.Element",
        title="Element",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Element" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Model" class:
#------------------------------------------------------------------------------

class Model(HasTraits):
    Elements = List(Instance("CPSM.Element"))

    URI = Str

    #--------------------------------------------------------------------------
    #  Begin "Model" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Elements",
                label="References"),
            dock="tab"),
        id="CPSM.Model",
        title="Model",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Model" user definitions:
    #--------------------------------------------------------------------------

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
            VGroup("URI", "version", "date",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="CPSM.IEC61970CIMVersion",
        title="IEC61970CIMVersion",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "IEC61970CIMVersion" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
