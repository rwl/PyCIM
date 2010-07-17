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

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------




from enthought.traits.api import HasTraits, Instance, List, Property, Date, Str
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
    Parent = Instance("CIM.Model",
        transient=True,
        opposite="Elements",
        editor=InstanceEditor(name="_models"))

    def _get_models(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.Model" ]
        else:
            return []

    _models = Property(fget=_get_models)

    UUID = Str

    #--------------------------------------------------------------------------
    #  Begin "Element" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID",
                label="Attributes"),
            VGroup("Parent",
                label="References"),
            dock="tab"),
        id="CIM.Element",
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
    Elements = List(Instance("CIM.Element"))

    #--------------------------------------------------------------------------
    #  Begin "Model" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("Elements",
                label="References"),
            dock="tab"),
        id="CIM.Model",
        title="Model",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Model" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "CombinedVersion" class:
#------------------------------------------------------------------------------

class CombinedVersion(Element):
    """ The combined version denotes the versions of the subpackages that have been combined into the total CIIMmodel. This is a convenience instead of having to look at each subpackage.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Form is YYYY-MM-DD for example for January 5, 2009 it is 2009-01-05.
    date = Date(desc="Form is YYYY-MM-DD for example for January 5, 2009 it is 2009-01-05.")

    # Form is IEC61970CIMXXvYY_IEC61968CIMXXvYY_combined where XX is the major CIM package version and the YY is the minor version, and different packages could have different major and minor versions.   For example IEC61970CIM13v18_IEC61968CIM10v16_combined.  Additional packages might be added in the future.
    version = Str(desc="Form is IEC61970CIMXXvYY_IEC61968CIMXXvYY_combined where XX is the major CIM package version and the YY is the minor version, and different packages could have different major and minor versions.   For example IEC61970CIM13v18_IEC61968CIM10v16_combined.  Additional packages might be added in the future.")

    #--------------------------------------------------------------------------
    #  Begin "CombinedVersion" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "date", "version",
                label="Attributes"),
            VGroup("Parent",
                label="References"),
            dock="tab"),
        id="CIM.CombinedVersion",
        title="CombinedVersion",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "CombinedVersion" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "PowerROCPerMin" class:
#------------------------------------------------------------------------------

class PowerROCPerMin(Element):
    pass
    #--------------------------------------------------------------------------
    #  Begin "PowerROCPerMin" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID",
                label="Attributes"),
            VGroup("Parent",
                label="References"),
            dock="tab"),
        id="CIM.PowerROCPerMin",
        title="PowerROCPerMin",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "PowerROCPerMin" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "RateOfChange" class:
#------------------------------------------------------------------------------

class RateOfChange(Element):
    pass
    #--------------------------------------------------------------------------
    #  Begin "RateOfChange" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID",
                label="Attributes"),
            VGroup("Parent",
                label="References"),
            dock="tab"),
        id="CIM.RateOfChange",
        title="RateOfChange",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "RateOfChange" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "EnumeratedType" class:
#------------------------------------------------------------------------------

class EnumeratedType(Element):
    pass
    #--------------------------------------------------------------------------
    #  Begin "EnumeratedType" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID",
                label="Attributes"),
            VGroup("Parent",
                label="References"),
            dock="tab"),
        id="CIM.EnumeratedType",
        title="EnumeratedType",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "EnumeratedType" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "FreqBiasFactor" class:
#------------------------------------------------------------------------------

class FreqBiasFactor(Element):
    pass
    #--------------------------------------------------------------------------
    #  Begin "FreqBiasFactor" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID",
                label="Attributes"),
            VGroup("Parent",
                label="References"),
            dock="tab"),
        id="CIM.FreqBiasFactor",
        title="FreqBiasFactor",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "FreqBiasFactor" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "FlowgateIdcType" class:
#------------------------------------------------------------------------------

class FlowgateIdcType(Element):
    pass
    #--------------------------------------------------------------------------
    #  Begin "FlowgateIdcType" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID",
                label="Attributes"),
            VGroup("Parent",
                label="References"),
            dock="tab"),
        id="CIM.FlowgateIdcType",
        title="FlowgateIdcType",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "FlowgateIdcType" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Quantity" class:
#------------------------------------------------------------------------------

class Quantity(Element):
    pass
    #--------------------------------------------------------------------------
    #  Begin "Quantity" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID",
                label="Attributes"),
            VGroup("Parent",
                label="References"),
            dock="tab"),
        id="CIM.Quantity",
        title="Quantity",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Quantity" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "EnergyAsMWh" class:
#------------------------------------------------------------------------------

class EnergyAsMWh(Element):
    pass
    #--------------------------------------------------------------------------
    #  Begin "EnergyAsMWh" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID",
                label="Attributes"),
            VGroup("Parent",
                label="References"),
            dock="tab"),
        id="CIM.EnergyAsMWh",
        title="EnergyAsMWh",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "EnergyAsMWh" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "FlowgateAfcUseCode" class:
#------------------------------------------------------------------------------

class FlowgateAfcUseCode(Element):
    pass
    #--------------------------------------------------------------------------
    #  Begin "FlowgateAfcUseCode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID",
                label="Attributes"),
            VGroup("Parent",
                label="References"),
            dock="tab"),
        id="CIM.FlowgateAfcUseCode",
        title="FlowgateAfcUseCode",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "FlowgateAfcUseCode" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "PenaltyFactor" class:
#------------------------------------------------------------------------------

class PenaltyFactor(Element):
    pass
    #--------------------------------------------------------------------------
    #  Begin "PenaltyFactor" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID",
                label="Attributes"),
            VGroup("Parent",
                label="References"),
            dock="tab"),
        id="CIM.PenaltyFactor",
        title="PenaltyFactor",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "PenaltyFactor" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
