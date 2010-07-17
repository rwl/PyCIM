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

""" State variables for analysis solutions such as powerflow.State variables for analysis solutions such as powerflow.
"""
#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CDPSM import Element



from enthought.traits.api import Instance, List, Property, Float, Int
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
#  "SvTapStep" class:
#------------------------------------------------------------------------------

class SvTapStep(Element):
    """ State variable for transformer tap step.     This class is to be used for taps of LTC (load tap changing) transformers, not fixed tap transformers.  Normally a profile specifies only one of the attributes 'position'or 'tapRatio'.State variable for transformer tap step.     This class is to be used for taps of LTC (load tap changing) transformers, not fixed tap transformers.  Normally a profile specifies only one of the attributes 'position'or 'tapRatio'.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The tap changer associated with the tap step state.The tap changer associated with the tap step state.
    TapChanger = Instance("CDPSM.IEC61970.Wires.TapChanger", allow_none=False,
        desc="The tap changer associated with the tap step state.The tap changer associated with the tap step state.",
        transient=True,
        opposite="SvTapStep",
        editor=InstanceEditor(name="_tapchangers"))

    def _get_tapchangers(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CDPSM.IEC61970.Wires.TapChanger" ]
        else:
            return []

    _tapchangers = Property(fget=_get_tapchangers)

    # The floating point tap position.The floating point tap position.
    continuousPosition = Float(desc="The floating point tap position.The floating point tap position.")

    # The integer tap position.The integer tap position.
    position = Int(desc="The integer tap position.The integer tap position.")

    #--------------------------------------------------------------------------
    #  Begin "SvTapStep" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "continuousPosition", "position",
                label="Attributes"),
            VGroup("Model", "TapChanger",
                label="References"),
            dock="tab"),
        id="CDPSM.IEC61970.StateVariables.SvTapStep",
        title="SvTapStep",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SvTapStep" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
