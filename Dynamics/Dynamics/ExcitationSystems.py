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

from dynamics import Element
from dynamics.Domain import Seconds



from enthought.traits.api import Float, Bool
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
#  "ExcitationSystem" class:
#------------------------------------------------------------------------------

class ExcitationSystem(Element):
    """ An excitation system provides the field voltage (Efd) for a synchronous machine model. It is linked to a specific generator by the Bus number and Unit ID.An excitation system provides the field voltage (Efd) for a synchronous machine model. It is linked to a specific generator by the Bus number and Unit ID.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "ExcitationSystem" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.ExcitationSystems.ExcitationSystem",
        title="ExcitationSystem",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ExcitationSystem" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ExcBAS" class:
#------------------------------------------------------------------------------

class ExcBAS(ExcitationSystem):
    """ Basler static voltage regulator feeding dc or ac rotating exciter modelBasler static voltage regulator feeding dc or ac rotating exciter model
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "ExcBAS" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.ExcitationSystems.ExcBAS",
        title="ExcBAS",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ExcBAS" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ExcDC2A" class:
#------------------------------------------------------------------------------

class ExcDC2A(ExcitationSystem):
    """ IEEE (1992/2005) DC2A Model  The model is used to represent field-controlled dc commutator exciters with continuously acting voltage regulators having supplies obtained from the generator or auxiliary bus. It differs from the Type DC1A model only in the voltage regulator output limits, which are now proportional to terminal voltage <i>V</i><i><sub>T</sub></i>. It is representative of solid-state replacements for various forms of older mechanical and rotating amplifier regulating equipment connected to dc commutator exciters.IEEE (1992/2005) DC2A Model  The model is used to represent field-controlled dc commutator exciters with continuously acting voltage regulators having supplies obtained from the generator or auxiliary bus. It differs from the Type DC1A model only in the voltage regulator output limits, which are now proportional to terminal voltage <i>V</i><i><sub>T</sub></i>. It is representative of solid-state replacements for various forms of older mechanical and rotating amplifier regulating equipment connected to dc commutator exciters.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Exciter time constant (&gt; 0.)Exciter time constant (&gt; 0.)
    te = Seconds(desc="Exciter time constant (&gt; 0.)Exciter time constant (&gt; 0.)")

    # Rate feedback time constant, sec. (&gt; 0.)Rate feedback time constant, sec. (&gt; 0.)
    tf = Seconds(desc="Rate feedback time constant, sec. (&gt; 0.)Rate feedback time constant, sec. (&gt; 0.)")

    # Gain (&gt; 0.)Gain (&gt; 0.)
    ka = Float(desc="Gain (&gt; 0.)Gain (&gt; 0.)")

    # Lead time constantLead time constant
    tc = Seconds(desc="Lead time constantLead time constant")

    # Minimum controller output (&lt; 0.)Minimum controller output (&lt; 0.)
    vrmin = Float(desc="Minimum controller output (&lt; 0.)Minimum controller output (&lt; 0.)")

    # Time constant (&gt; 0.)Time constant (&gt; 0.)
    ta = Seconds(desc="Time constant (&gt; 0.)Time constant (&gt; 0.)")

    # Lag time constant (&gt;= 0.)Lag time constant (&gt;= 0.)
    tb = Seconds(desc="Lag time constant (&gt;= 0.)Lag time constant (&gt;= 0.)")

    # Maximum controller outputMaximum controller output
    vrmax = Float(desc="Maximum controller outputMaximum controller output")

    # Rate feedback gain (&gt;= 0.)Rate feedback gain (&gt;= 0.)
    kf = Float(desc="Rate feedback gain (&gt;= 0.)Rate feedback gain (&gt;= 0.)")

    # Exciter field resistance line slopeExciter field resistance line slope
    ke = Float(desc="Exciter field resistance line slopeExciter field resistance line slope")

    # UEL input: if &lt; 2, HV gate; if = 2, add to error signalUEL input: if &lt; 2, HV gate; if = 2, add to error signal
    uelin = Float(desc="UEL input: if &lt; 2, HV gate; if = 2, add to error signalUEL input: if &lt; 2, HV gate; if = 2, add to error signal")

    # Saturation factor at e1  (&gt;= 0.)Saturation factor at e1  (&gt;= 0.)
    se1 = Float(desc="Saturation factor at e1  (&gt;= 0.)Saturation factor at e1  (&gt;= 0.)")

    # Filter time constant (&gt;= 0.)Filter time constant (&gt;= 0.)
    tr = Seconds(desc="Filter time constant (&gt;= 0.)Filter time constant (&gt;= 0.)")

    # Saturation factor at e2  (&gt;= 0.)Saturation factor at e2  (&gt;= 0.)
    se2 = Float(desc="Saturation factor at e2  (&gt;= 0.)Saturation factor at e2  (&gt;= 0.)")

    # If not 0, apply lower limit of 0. to exciter outputIf not 0, apply lower limit of 0. to exciter output
    exclim = Float(desc="If not 0, apply lower limit of 0. to exciter outputIf not 0, apply lower limit of 0. to exciter output")

    # Field voltage value 2.    (&gt; 0.)Field voltage value 2.    (&gt; 0.)
    e2 = Float(desc="Field voltage value 2.    (&gt; 0.)Field voltage value 2.    (&gt; 0.)")

    # Field voltage value 1     (&gt; 0.)Field voltage value 1     (&gt; 0.)
    e1 = Float(desc="Field voltage value 1     (&gt; 0.)Field voltage value 1     (&gt; 0.)")

    #--------------------------------------------------------------------------
    #  Begin "ExcDC2A" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "te", "tf", "ka", "tc", "vrmin", "ta", "tb", "vrmax", "kf", "ke", "uelin", "se1", "tr", "se2", "exclim", "e2", "e1",
                label="Attributes", columns=1),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.ExcitationSystems.ExcDC2A",
        title="ExcDC2A",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ExcDC2A" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ExcSEXS" class:
#------------------------------------------------------------------------------

class ExcSEXS(ExcitationSystem):
    """ Simplified Excitation System ModelSimplified Excitation System Model
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Gain (&gt; 0.)Gain (&gt; 0.)
    k = Float(desc="Gain (&gt; 0.)Gain (&gt; 0.)")

    # Ta/Tb - gain reduction ratio of lag-lead elementTa/Tb - gain reduction ratio of lag-lead element
    tatb = Float(desc="Ta/Tb - gain reduction ratio of lag-lead elementTa/Tb - gain reduction ratio of lag-lead element")

    # Field voltage clipping minimum limitField voltage clipping minimum limit
    efdmin = Float(desc="Field voltage clipping minimum limitField voltage clipping minimum limit")

    # Time constant of gain block (&gt; 0.)Time constant of gain block (&gt; 0.)
    te = Seconds(desc="Time constant of gain block (&gt; 0.)Time constant of gain block (&gt; 0.)")

    # PI controller phase lead time constantPI controller phase lead time constant
    tc = Seconds(desc="PI controller phase lead time constantPI controller phase lead time constant")

    # PI controller gain (&gt; 0. if Tc &gt; 0.)PI controller gain (&gt; 0. if Tc &gt; 0.)
    kc = Float(desc="PI controller gain (&gt; 0. if Tc &gt; 0.)PI controller gain (&gt; 0. if Tc &gt; 0.)")

    # Denominator time constant of lag-lead blockDenominator time constant of lag-lead block
    tb = Seconds(desc="Denominator time constant of lag-lead blockDenominator time constant of lag-lead block")

    # Minimum field voltage outputMinimum field voltage output
    emin = Float(desc="Minimum field voltage outputMinimum field voltage output")

    # Maximum field voltage outputMaximum field voltage output
    emax = Float(desc="Maximum field voltage outputMaximum field voltage output")

    # Field voltage clipping maximum limitField voltage clipping maximum limit
    efdmax = Float(desc="Field voltage clipping maximum limitField voltage clipping maximum limit")

    #--------------------------------------------------------------------------
    #  Begin "ExcSEXS" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "k", "tatb", "efdmin", "te", "tc", "kc", "tb", "emin", "emax", "efdmax",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.ExcitationSystems.ExcSEXS",
        title="ExcSEXS",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ExcSEXS" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ExcELIN2" class:
#------------------------------------------------------------------------------

class ExcELIN2(ExcitationSystem):
    """ Detailed Excitation System Model - ELIN (VATECH)Detailed Excitation System Model - ELIN (VATECH)
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "ExcELIN2" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.ExcitationSystems.ExcELIN2",
        title="ExcELIN2",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ExcELIN2" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ExcAC4A" class:
#------------------------------------------------------------------------------

class ExcAC4A(ExcitationSystem):
    """ IEEE (1992/2005) AC4A Model  The Type AC4A alternator-supplied controlled-rectifier excitation system is quite different from the other type ac systems. This high initial response excitation system utilizes a full thyristor bridge in the exciter output circuit. The voltage regulator controls the firing of the thyristor bridges. The exciter alternator uses an independent voltage regulator to control its output voltage to a constant value. These effects are not modeled; however, transient loading effects on the exciter alternator are included.IEEE (1992/2005) AC4A Model  The Type AC4A alternator-supplied controlled-rectifier excitation system is quite different from the other type ac systems. This high initial response excitation system utilizes a full thyristor bridge in the exciter output circuit. The voltage regulator controls the firing of the thyristor bridges. The exciter alternator uses an independent voltage regulator to control its output voltage to a constant value. These effects are not modeled; however, transient loading effects on the exciter alternator are included.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Lag time constant (&gt;= 0.)Lag time constant (&gt;= 0.)
    tb = Seconds(desc="Lag time constant (&gt;= 0.)Lag time constant (&gt;= 0.)")

    # Time constant (&gt; 0.)Time constant (&gt; 0.)
    ta = Seconds(desc="Time constant (&gt; 0.)Time constant (&gt; 0.)")

    # Lead time constantLead time constant
    tc = Seconds(desc="Lead time constantLead time constant")

    # Minimum controller output (&lt; 0.)Minimum controller output (&lt; 0.)
    vrmin = Float(desc="Minimum controller output (&lt; 0.)Minimum controller output (&lt; 0.)")

    # Maximum error signal ( &gt; 0.)Maximum error signal ( &gt; 0.)
    vimax = Float(desc="Maximum error signal ( &gt; 0.)Maximum error signal ( &gt; 0.)")

    # Maximum controller output (&gt; 0.)Maximum controller output (&gt; 0.)
    vrmax = Float(desc="Maximum controller output (&gt; 0.)Maximum controller output (&gt; 0.)")

    # Filter time constant (&gt;= 0.)Filter time constant (&gt;= 0.)
    tr = Seconds(desc="Filter time constant (&gt;= 0.)Filter time constant (&gt;= 0.)")

    # Excitation system regulation (&gt;= 0.)Excitation system regulation (&gt;= 0.)
    kc = Float(desc="Excitation system regulation (&gt;= 0.)Excitation system regulation (&gt;= 0.)")

    # Minimum error signal (&lt; 0.)Minimum error signal (&lt; 0.)
    vimin = Float(desc="Minimum error signal (&lt; 0.)Minimum error signal (&lt; 0.)")

    # Gain (&gt; 0.)Gain (&gt; 0.)
    ka = Float(desc="Gain (&gt; 0.)Gain (&gt; 0.)")

    #--------------------------------------------------------------------------
    #  Begin "ExcAC4A" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "tb", "ta", "tc", "vrmin", "vimax", "vrmax", "tr", "kc", "vimin", "ka",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.ExcitationSystems.ExcAC4A",
        title="ExcAC4A",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ExcAC4A" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ExcSK" class:
#------------------------------------------------------------------------------

class ExcSK(ExcitationSystem):
    """ Slovakian Excitation System Model (UEL, secondary voltage control)Slovakian Excitation System Model (UEL, secondary voltage control)
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "ExcSK" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.ExcitationSystems.ExcSK",
        title="ExcSK",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ExcSK" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ExcAC2A" class:
#------------------------------------------------------------------------------

class ExcAC2A(ExcitationSystem):
    """ IEEE (1992/2005) AC2A Model The model designated as Type AC2A, represents a high initial response fieldcontrolled alternator-rectifier excitation system. The alternator main exciter is used with non-controlled rectifiers. The Type AC2A model is similar to that of Type AC1A except for the inclusion of exciter time constant compensation and exciter field current limiting elements.IEEE (1992/2005) AC2A Model The model designated as Type AC2A, represents a high initial response fieldcontrolled alternator-rectifier excitation system. The alternator main exciter is used with non-controlled rectifiers. The Type AC2A model is similar to that of Type AC1A except for the inclusion of exciter time constant compensation and exciter field current limiting elements.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # TGR lag time constant (&gt;= 0.)TGR lag time constant (&gt;= 0.)
    tb = Seconds(desc="TGR lag time constant (&gt;= 0.)TGR lag time constant (&gt;= 0.)")

    # Field voltage value 1     (&gt; 0.)Field voltage value 1     (&gt; 0.)
    e1 = Float(desc="Field voltage value 1     (&gt; 0.)Field voltage value 1     (&gt; 0.)")

    # AVR time constant (&gt; 0.)AVR time constant (&gt; 0.)
    ta = Seconds(desc="AVR time constant (&gt; 0.)AVR time constant (&gt; 0.)")

    # Minimum exciter control signal (&lt; 0.)Minimum exciter control signal (&lt; 0.)
    vrmin = Float(desc="Minimum exciter control signal (&lt; 0.)Minimum exciter control signal (&lt; 0.)")

    # Field voltage value 2.    (&gt; 0.)Field voltage value 2.    (&gt; 0.)
    e2 = Float(desc="Field voltage value 2.    (&gt; 0.)Field voltage value 2.    (&gt; 0.)")

    # Exciter field current limit parameter (&gt;= 0.)Exciter field current limit parameter (&gt;= 0.)
    vfemax = Float(desc="Exciter field current limit parameter (&gt;= 0.)Exciter field current limit parameter (&gt;= 0.)")

    # Maximum exciter control signal (&gt; 0.)Maximum exciter control signal (&gt; 0.)
    vrmax = Float(desc="Maximum exciter control signal (&gt; 0.)Maximum exciter control signal (&gt; 0.)")

    # AVR gain (&gt; 0.)AVR gain (&gt; 0.)
    ka = Float(desc="AVR gain (&gt; 0.)AVR gain (&gt; 0.)")

    # Saturation factor at e1  (&gt;= 0.)Saturation factor at e1  (&gt;= 0.)
    se1 = Float(desc="Saturation factor at e1  (&gt;= 0.)Saturation factor at e1  (&gt;= 0.)")

    # Saturation factor at e2   (&gt;= 0.)Saturation factor at e2   (&gt;= 0.)
    se2 = Float(desc="Saturation factor at e2   (&gt;= 0.)Saturation factor at e2   (&gt;= 0.)")

    # Rate feedback gain (&gt;= 0.)Rate feedback gain (&gt;= 0.)
    kf = Float(desc="Rate feedback gain (&gt;= 0.)Rate feedback gain (&gt;= 0.)")

    # Exciter field current feedback gain (&gt;= 0.)Exciter field current feedback gain (&gt;= 0.)
    kh = Float(desc="Exciter field current feedback gain (&gt;= 0.)Exciter field current feedback gain (&gt;= 0.)")

    # Rectifier regulation factor (&gt;= 0.)Rectifier regulation factor (&gt;= 0.)
    kc = Float(desc="Rectifier regulation factor (&gt;= 0.)Rectifier regulation factor (&gt;= 0.)")

    # Minimum AVR output (&lt; 0.)Minimum AVR output (&lt; 0.)
    vamin = Float(desc="Minimum AVR output (&lt; 0.)Minimum AVR output (&lt; 0.)")

    # Exciter field current controller gain (&gt; 0.)Exciter field current controller gain (&gt; 0.)
    kb = Float(desc="Exciter field current controller gain (&gt; 0.)Exciter field current controller gain (&gt; 0.)")

    # Exciter field resistance constantExciter field resistance constant
    ke = Float(desc="Exciter field resistance constantExciter field resistance constant")

    # Filter time constant (&gt;= 0.)Filter time constant (&gt;= 0.)
    tr = Seconds(desc="Filter time constant (&gt;= 0.)Filter time constant (&gt;= 0.)")

    # Exciter internal reactance (&gt;= 0.)Exciter internal reactance (&gt;= 0.)
    kd = Float(desc="Exciter internal reactance (&gt;= 0.)Exciter internal reactance (&gt;= 0.)")

    # Exciter time constant (&gt; 0.)Exciter time constant (&gt; 0.)
    te = Seconds(desc="Exciter time constant (&gt; 0.)Exciter time constant (&gt; 0.)")

    # TGR lead time constantTGR lead time constant
    tc = Seconds(desc="TGR lead time constantTGR lead time constant")

    # Maximum AVR output (&gt; 0.)Maximum AVR output (&gt; 0.)
    vamax = Float(desc="Maximum AVR output (&gt; 0.)Maximum AVR output (&gt; 0.)")

    # Rate feedback time constant (&gt; 0.)Rate feedback time constant (&gt; 0.)
    tf = Seconds(desc="Rate feedback time constant (&gt; 0.)Rate feedback time constant (&gt; 0.)")

    #--------------------------------------------------------------------------
    #  Begin "ExcAC2A" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "tb", "e1", "ta", "vrmin", "e2", "vfemax", "vrmax", "ka", "se1", "se2", "kf", "kh", "kc", "vamin", "kb", "ke", "tr", "kd", "te", "tc", "vamax", "tf",
                label="Attributes", columns=1),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.ExcitationSystems.ExcAC2A",
        title="ExcAC2A",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ExcAC2A" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ExcELIN1" class:
#------------------------------------------------------------------------------

class ExcELIN1(ExcitationSystem):
    """ Simplified Excitation System Model - ELIN (VATECH)Simplified Excitation System Model - ELIN (VATECH)
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "ExcELIN1" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.ExcitationSystems.ExcELIN1",
        title="ExcELIN1",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ExcELIN1" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ExcST6B" class:
#------------------------------------------------------------------------------

class ExcST6B(ExcitationSystem):
    """ IEEE (2005) ST6B Model  The AVR consists of a PI voltage regulator with an inner loop field voltage regulator and pre-control. The field voltage regulator implements a proportional control. The pre-control and the delay in the feedback circuit increase the dynamic response.IEEE (2005) ST6B Model  The AVR consists of a PI voltage regulator with an inner loop field voltage regulator and pre-control. The field voltage regulator implements a proportional control. The pre-control and the delay in the feedback circuit increase the dynamic response.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # PI minimum output (&lt; 0.)PI minimum output (&lt; 0.)
    vamin = Float(desc="PI minimum output (&lt; 0.)PI minimum output (&lt; 0.)")

    # Minimum regulator output (&lt; 0.)Minimum regulator output (&lt; 0.)
    vrmin = Float(desc="Minimum regulator output (&lt; 0.)Minimum regulator output (&lt; 0.)")

    # Main gainMain gain
    km = Float(desc="Main gainMain gain")

    # Rectifier firing time constant (not in IEEE model) (&gt;= 0.)Rectifier firing time constant (not in IEEE model) (&gt;= 0.)
    ts = Seconds(desc="Rectifier firing time constant (not in IEEE model) (&gt;= 0.)Rectifier firing time constant (not in IEEE model) (&gt;= 0.)")

    # Feedback gain (&gt;= 0.)Feedback gain (&gt;= 0.)
    kg = Float(desc="Feedback gain (&gt;= 0.)Feedback gain (&gt;= 0.)")

    # Filter time constant (&gt;= 0.)Filter time constant (&gt;= 0.)
    tr = Seconds(desc="Filter time constant (&gt;= 0.)Filter time constant (&gt;= 0.)")

    # Field current limiter conversion factor (&gt; 0.)Field current limiter conversion factor (&gt; 0.)
    kcl = Float(desc="Field current limiter conversion factor (&gt; 0.)Field current limiter conversion factor (&gt; 0.)")

    # Field current limiter gain (&gt; 0.)Field current limiter gain (&gt; 0.)
    klr = Float(desc="Field current limiter gain (&gt; 0.)Field current limiter gain (&gt; 0.)")

    # Maximum regulator output (&gt; 0.)Maximum regulator output (&gt; 0.)
    vrmax = Float(desc="Maximum regulator output (&gt; 0.)Maximum regulator output (&gt; 0.)")

    # Field current limiter setpoint (&gt; 0.)Field current limiter setpoint (&gt; 0.)
    ilr = Float(desc="Field current limiter setpoint (&gt; 0.)Field current limiter setpoint (&gt; 0.)")

    # Regulator proportional gain (&gt; 0.)Regulator proportional gain (&gt; 0.)
    kpa = Float(desc="Regulator proportional gain (&gt; 0.)Regulator proportional gain (&gt; 0.)")

    # Feedback time constant (&gt;= 0.)Feedback time constant (&gt;= 0.)
    tg = Seconds(desc="Feedback time constant (&gt;= 0.)Feedback time constant (&gt;= 0.)")

    # PI maximum output. (&gt; 0.)PI maximum output. (&gt; 0.)
    vamax = Float(desc="PI maximum output. (&gt; 0.)PI maximum output. (&gt; 0.)")

    # OEL input selector: 1 ? before UEL, 2 ? after UEL, 0 ? no OEL inputOEL input selector: 1 ? before UEL, 2 ? after UEL, 0 ? no OEL input
    oelin = Float(desc="OEL input selector: 1 ? before UEL, 2 ? after UEL, 0 ? no OEL inputOEL input selector: 1 ? before UEL, 2 ? after UEL, 0 ? no OEL input")

    # Feedforward gainFeedforward gain
    kff = Float(desc="Feedforward gainFeedforward gain")

    # If non-zero, multiply regulator output by terminal voltageIf non-zero, multiply regulator output by terminal voltage
    vmult = Float(desc="If non-zero, multiply regulator output by terminal voltageIf non-zero, multiply regulator output by terminal voltage")

    # Regulator integral gain (&gt; 0.)Regulator integral gain (&gt; 0.)
    kia = Float(desc="Regulator integral gain (&gt; 0.)Regulator integral gain (&gt; 0.)")

    #--------------------------------------------------------------------------
    #  Begin "ExcST6B" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "vamin", "vrmin", "km", "ts", "kg", "tr", "kcl", "klr", "vrmax", "ilr", "kpa", "tg", "vamax", "oelin", "kff", "vmult", "kia",
                label="Attributes", columns=1),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.ExcitationSystems.ExcST6B",
        title="ExcST6B",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ExcST6B" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ExcST4B" class:
#------------------------------------------------------------------------------

class ExcST4B(ExcitationSystem):
    """ IEEE (2005) ST4B Model  This model is a variation of the Type ST3A model, with a proportional plus integral (PI) regulator block replacing the lag-lead regulator characteristic that was in the ST3A model. Both potential- and compoundsource rectifier excitation systems are modeled. The PI regulator blocks have nonwindup limits that are represented. The voltage regulator of this model is typically implemented digitally.IEEE (2005) ST4B Model  This model is a variation of the Type ST3A model, with a proportional plus integral (PI) regulator block replacing the lag-lead regulator characteristic that was in the ST3A model. Both potential- and compoundsource rectifier excitation systems are modeled. The PI regulator blocks have nonwindup limits that are represented. The voltage regulator of this model is typically implemented digitally.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Potential source gain (&gt; 0.)Potential source gain (&gt; 0.)
    kp = Float(desc="Potential source gain (&gt; 0.)Potential source gain (&gt; 0.)")

    # P-bar leakage reactance (&gt;= 0.)P-bar leakage reactance (&gt;= 0.)
    xl = Float(desc="P-bar leakage reactance (&gt;= 0.)P-bar leakage reactance (&gt;= 0.)")

    # Maximum excitation voltage (&gt; 0.)Maximum excitation voltage (&gt; 0.)
    vbmax = Float(desc="Maximum excitation voltage (&gt; 0.)Maximum excitation voltage (&gt; 0.)")

    # Current source gain (&gt;= 0.)Current source gain (&gt;= 0.)
    ki = Float(desc="Current source gain (&gt;= 0.)Current source gain (&gt;= 0.)")

    # AVR Integral gainAVR Integral gain
    kir = Float(desc="AVR Integral gainAVR Integral gain")

    # Minimum AVR output (&lt; 0.)Minimum AVR output (&lt; 0.)
    vrmin = Float(desc="Minimum AVR output (&lt; 0.)Minimum AVR output (&lt; 0.)")

    # Minimum inner loop regulator outputMinimum inner loop regulator output
    vmmin = Float(desc="Minimum inner loop regulator outputMinimum inner loop regulator output")

    # Integral gain of inner loop regulatorIntegral gain of inner loop regulator
    kim = Float(desc="Integral gain of inner loop regulatorIntegral gain of inner loop regulator")

    # AVR time constant (&gt;= 0.)AVR time constant (&gt;= 0.)
    ta = Seconds(desc="AVR time constant (&gt;= 0.)AVR time constant (&gt;= 0.)")

    # Inner loop feedback gain (&gt;= 0.)Inner loop feedback gain (&gt;= 0.)
    kg = Float(desc="Inner loop feedback gain (&gt;= 0.)Inner loop feedback gain (&gt;= 0.)")

    # Voltage transducer time constant (&gt;= 0.)Voltage transducer time constant (&gt;= 0.)
    tr = Seconds(desc="Voltage transducer time constant (&gt;= 0.)Voltage transducer time constant (&gt;= 0.)")

    # Exciter regulation factor (&gt;= 0.)Exciter regulation factor (&gt;= 0.)
    kc = Float(desc="Exciter regulation factor (&gt;= 0.)Exciter regulation factor (&gt;= 0.)")

    # Maximum AVR output (&gt; 0.)Maximum AVR output (&gt; 0.)
    vrmax = Float(desc="Maximum AVR output (&gt; 0.)Maximum AVR output (&gt; 0.)")

    # Phase angle of potential sourcePhase angle of potential source
    angp = Float(desc="Phase angle of potential sourcePhase angle of potential source")

    # AVR proportional gainAVR proportional gain
    kpr = Float(desc="AVR proportional gainAVR proportional gain")

    # Maximum inner loop feedback gain (&gt;= 0.)Maximum inner loop feedback gain (&gt;= 0.)
    vgmax = Float(desc="Maximum inner loop feedback gain (&gt;= 0.)Maximum inner loop feedback gain (&gt;= 0.)")

    # Prop. gain of inner loop regulatorProp. gain of inner loop regulator
    kpm = Float(desc="Prop. gain of inner loop regulatorProp. gain of inner loop regulator")

    # Maximum inner loop regulator outputMaximum inner loop regulator output
    vmmax = Float(desc="Maximum inner loop regulator outputMaximum inner loop regulator output")

    #--------------------------------------------------------------------------
    #  Begin "ExcST4B" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "kp", "xl", "vbmax", "ki", "kir", "vrmin", "vmmin", "kim", "ta", "kg", "tr", "kc", "vrmax", "angp", "kpr", "vgmax", "kpm", "vmmax",
                label="Attributes", columns=1),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.ExcitationSystems.ExcST4B",
        title="ExcST4B",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ExcST4B" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ExcWT3E" class:
#------------------------------------------------------------------------------

class ExcWT3E(ExcitationSystem):
    """ Type 3 standard wind turbine converter control modelType 3 standard wind turbine converter control model
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "ExcWT3E" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.ExcitationSystems.ExcWT3E",
        title="ExcWT3E",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ExcWT3E" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ExcPIC" class:
#------------------------------------------------------------------------------

class ExcPIC(ExcitationSystem):
    """ Excitation System Model with PI voltage regulatorExcitation System Model with PI voltage regulator
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "ExcPIC" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.ExcitationSystems.ExcPIC",
        title="ExcPIC",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ExcPIC" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ExcSK2" class:
#------------------------------------------------------------------------------

class ExcSK2(ExcitationSystem):
    """ Slovakian alternator-rectifier Excitation System Model (UEL, secondary voltage control)Slovakian alternator-rectifier Excitation System Model (UEL, secondary voltage control)
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "ExcSK2" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.ExcitationSystems.ExcSK2",
        title="ExcSK2",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ExcSK2" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ExcST2A" class:
#------------------------------------------------------------------------------

class ExcST2A(ExcitationSystem):
    """ IEEE (1992/2005) ST2A Model  Some static systems utilize both current and voltage sources (generator terminal quantities) to comprise the power source. These compound-source rectifier excitation systems are designated Type ST2A. The regulator controls the exciter output through controlled saturation of the power transformer components.IEEE (1992/2005) ST2A Model  Some static systems utilize both current and voltage sources (generator terminal quantities) to comprise the power source. These compound-source rectifier excitation systems are designated Type ST2A. The regulator controls the exciter output through controlled saturation of the power transformer components.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Minimum controller output (&lt; 0.)Minimum controller output (&lt; 0.)
    vrmin = Float(desc="Minimum controller output (&lt; 0.)Minimum controller output (&lt; 0.)")

    # Time constantTime constant
    tc = Seconds(desc="Time constantTime constant")

    # Time constant (&gt;=0.)Time constant (&gt;=0.)
    tb = Seconds(desc="Time constant (&gt;=0.)Time constant (&gt;=0.)")

    # Time constant (&gt; 0.)Time constant (&gt; 0.)
    ta = Seconds(desc="Time constant (&gt; 0.)Time constant (&gt; 0.)")

    # Gain (&gt; 0.)Gain (&gt; 0.)
    ka = Float(desc="Gain (&gt; 0.)Gain (&gt; 0.)")

    # Time constant feedbackTime constant feedback
    ke = Float(desc="Time constant feedbackTime constant feedback")

    # UEL input: if = 1, HV gate; if = 2, add to error signalUEL input: if = 1, HV gate; if = 2, add to error signal
    uelin = Float(desc="UEL input: if = 1, HV gate; if = 2, add to error signalUEL input: if = 1, HV gate; if = 2, add to error signal")

    # Rectifier loading factor (&gt;= 0.)Rectifier loading factor (&gt;= 0.)
    kc = Float(desc="Rectifier loading factor (&gt;= 0.)Rectifier loading factor (&gt;= 0.)")

    # Transformer saturation control time constant (&gt; 0.)Transformer saturation control time constant (&gt; 0.)
    te = Seconds(desc="Transformer saturation control time constant (&gt; 0.)Transformer saturation control time constant (&gt; 0.)")

    # Current source gain (&gt;= 0.)Current source gain (&gt;= 0.)
    ki = Float(desc="Current source gain (&gt;= 0.)Current source gain (&gt;= 0.)")

    # Rate feedback gain (&gt;= 0.)Rate feedback gain (&gt;= 0.)
    kf = Float(desc="Rate feedback gain (&gt;= 0.)Rate feedback gain (&gt;= 0.)")

    # Rate feedback time constant (&gt;= 0.)Rate feedback time constant (&gt;= 0.)
    tf = Seconds(desc="Rate feedback time constant (&gt;= 0.)Rate feedback time constant (&gt;= 0.)")

    # Maximum controller output (&gt; 0.)Maximum controller output (&gt; 0.)
    vrmax = Float(desc="Maximum controller output (&gt; 0.)Maximum controller output (&gt; 0.)")

    # Maximum field voltage (&gt;=0.)Maximum field voltage (&gt;=0.)
    efdmax = Float(desc="Maximum field voltage (&gt;=0.)Maximum field voltage (&gt;=0.)")

    # Filter time constant (&gt;= 0.)Filter time constant (&gt;= 0.)
    tr = Seconds(desc="Filter time constant (&gt;= 0.)Filter time constant (&gt;= 0.)")

    # Potential source gain (&gt;= 0.)Potential source gain (&gt;= 0.)
    kp = Float(desc="Potential source gain (&gt;= 0.)Potential source gain (&gt;= 0.)")

    #--------------------------------------------------------------------------
    #  Begin "ExcST2A" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "vrmin", "tc", "tb", "ta", "ka", "ke", "uelin", "kc", "te", "ki", "kf", "tf", "vrmax", "efdmax", "tr", "kp",
                label="Attributes", columns=1),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.ExcitationSystems.ExcST2A",
        title="ExcST2A",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ExcST2A" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ExcHU" class:
#------------------------------------------------------------------------------

class ExcHU(ExcitationSystem):
    """ Hungarian Excitation System ModelHungarian Excitation System Model
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "ExcHU" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.ExcitationSystems.ExcHU",
        title="ExcHU",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ExcHU" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ExcREXS" class:
#------------------------------------------------------------------------------

class ExcREXS(ExcitationSystem):
    """ General Purpose Rotating Excitation System ModelGeneral Purpose Rotating Excitation System Model
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "ExcREXS" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.ExcitationSystems.ExcREXS",
        title="ExcREXS",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ExcREXS" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ExcST7B" class:
#------------------------------------------------------------------------------

class ExcST7B(ExcitationSystem):
    """ IEEE (2005) ST7B Model  The model ST7B is representative of static potential-source excitation systems. In this system, the AVR consists of a PI voltage regulator. A phase lead-lag filter in series allows introduction of a derivative function, typically used with brushless excitation systems. In that case, the regulator is of the PID type. In addition, the terminal voltage channel includes a phase lead-lag filter. The AVR includes the appropriate inputs on its reference for overexcitation limiter (OEL1), underexcitation limiter (UEL), stator current limiter (SCL), and current compensator (DROOP). All these limitations, when they work at voltage reference level, keep the PSS (VS signal from Type PSS1A, PSS2A, or PSS2B) in operation. However, the UEL limitation can also be transferred to the high value (HV) gate acting on the output signal. In addition, the output signal passes through a low value (LV) gate for a ceiling overexcitation limiter (OEL2).IEEE (2005) ST7B Model  The model ST7B is representative of static potential-source excitation systems. In this system, the AVR consists of a PI voltage regulator. A phase lead-lag filter in series allows introduction of a derivative function, typically used with brushless excitation systems. In that case, the regulator is of the PID type. In addition, the terminal voltage channel includes a phase lead-lag filter. The AVR includes the appropriate inputs on its reference for overexcitation limiter (OEL1), underexcitation limiter (UEL), stator current limiter (SCL), and current compensator (DROOP). All these limitations, when they work at voltage reference level, keep the PSS (VS signal from Type PSS1A, PSS2A, or PSS2B) in operation. However, the UEL limitation can also be transferred to the high value (HV) gate acting on the output signal. In addition, the output signal passes through a low value (LV) gate for a ceiling overexcitation limiter (OEL2).
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Input lead-lag numerator time constant (&gt;= 0.)Input lead-lag numerator time constant (&gt;= 0.)
    tg = Seconds(desc="Input lead-lag numerator time constant (&gt;= 0.)Input lead-lag numerator time constant (&gt;= 0.)")

    # Regulator proportional gain (&gt; 0.)Regulator proportional gain (&gt; 0.)
    kpa = Float(desc="Regulator proportional gain (&gt; 0.)Regulator proportional gain (&gt; 0.)")

    # Minimum voltage reference signal (&gt; 0.)Minimum voltage reference signal (&gt; 0.)
    vmin = Float(desc="Minimum voltage reference signal (&gt; 0.)Minimum voltage reference signal (&gt; 0.)")

    # Maximum field voltage output (&gt; 0.)Maximum field voltage output (&gt; 0.)
    vrmax = Float(desc="Maximum field voltage output (&gt; 0.)Maximum field voltage output (&gt; 0.)")

    # Low-value gate feedback gain (&gt;= 0.)Low-value gate feedback gain (&gt;= 0.)
    kl = Float(desc="Low-value gate feedback gain (&gt;= 0.)Low-value gate feedback gain (&gt;= 0.)")

    # Filter time constantFilter time constant
    tr = Seconds(desc="Filter time constantFilter time constant")

    # High-value gate feedback gain (&gt;= 0.)High-value gate feedback gain (&gt;= 0.)
    kh = Float(desc="High-value gate feedback gain (&gt;= 0.)High-value gate feedback gain (&gt;= 0.)")

    # Rectifier firing time constant (&gt;= 0.) (not in IEEE model)Rectifier firing time constant (&gt;= 0.) (not in IEEE model)
    ts = Seconds(desc="Rectifier firing time constant (&gt;= 0.) (not in IEEE model)Rectifier firing time constant (&gt;= 0.) (not in IEEE model)")

    # Minimum field voltage output (&lt; 0.)Minimum field voltage output (&lt; 0.)
    vrmin = Float(desc="Minimum field voltage output (&lt; 0.)Minimum field voltage output (&lt; 0.)")

    # OEL input selector: 1 ? add to Vref, 2 ? input LV gate,  2 ? output LV gate, 0 ? no OEL inputOEL input selector: 1 ? add to Vref, 2 ? input LV gate,  2 ? output LV gate, 0 ? no OEL input
    oelin = Float(desc="OEL input selector: 1 ? add to Vref, 2 ? input LV gate,  2 ? output LV gate, 0 ? no OEL inputOEL input selector: 1 ? add to Vref, 2 ? input LV gate,  2 ? output LV gate, 0 ? no OEL input")

    # UEL input selector: 1 ? add to Vref, 2 ? input HV gate,  3 ? output HV gate, 0 ? no UEL inputUEL input selector: 1 ? add to Vref, 2 ? input HV gate,  3 ? output HV gate, 0 ? no UEL input
    uelin = Float(desc="UEL input selector: 1 ? add to Vref, 2 ? input HV gate,  3 ? output HV gate, 0 ? no UEL inputUEL input selector: 1 ? add to Vref, 2 ? input HV gate,  3 ? output HV gate, 0 ? no UEL input")

    # Feedback time constant (&gt;= 0.)Feedback time constant (&gt;= 0.)
    tia = Seconds(desc="Feedback time constant (&gt;= 0.)Feedback time constant (&gt;= 0.)")

    # Lead-lag denominator time constant (&gt;= 0.)Lead-lag denominator time constant (&gt;= 0.)
    tb = Seconds(desc="Lead-lag denominator time constant (&gt;= 0.)Lead-lag denominator time constant (&gt;= 0.)")

    # Lead-lag numerator time constant (&gt;= 0.)Lead-lag numerator time constant (&gt;= 0.)
    tc = Seconds(desc="Lead-lag numerator time constant (&gt;= 0.)Lead-lag numerator time constant (&gt;= 0.)")

    # Input lead-lag denominator time constant (&gt;= 0.)Input lead-lag denominator time constant (&gt;= 0.)
    tf = Seconds(desc="Input lead-lag denominator time constant (&gt;= 0.)Input lead-lag denominator time constant (&gt;= 0.)")

    # Feedback gain (&gt;= 0.)Feedback gain (&gt;= 0.)
    kia = Float(desc="Feedback gain (&gt;= 0.)Feedback gain (&gt;= 0.)")

    # Maximum voltage reference signal (&gt; 0.)Maximum voltage reference signal (&gt; 0.)
    vmax = Float(desc="Maximum voltage reference signal (&gt; 0.)Maximum voltage reference signal (&gt; 0.)")

    #--------------------------------------------------------------------------
    #  Begin "ExcST7B" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "tg", "kpa", "vmin", "vrmax", "kl", "tr", "kh", "ts", "vrmin", "oelin", "uelin", "tia", "tb", "tc", "tf", "kia", "vmax",
                label="Attributes", columns=1),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.ExcitationSystems.ExcST7B",
        title="ExcST7B",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ExcST7B" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ExcAC1A" class:
#------------------------------------------------------------------------------

class ExcAC1A(ExcitationSystem):
    """ IEEE (1992/2005) AC1A Model The model represents the field-controlled alternator-rectifier excitation systems designated Type AC1A. These excitation systems consist of an alternator main exciter with non-controlled rectifiers.IEEE (1992/2005) AC1A Model The model represents the field-controlled alternator-rectifier excitation systems designated Type AC1A. These excitation systems consist of an alternator main exciter with non-controlled rectifiers.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Saturation factor at e1  (&gt;= 0.)Saturation factor at e1  (&gt;= 0.)
    se1 = Float(desc="Saturation factor at e1  (&gt;= 0.)Saturation factor at e1  (&gt;= 0.)")

    # Saturation factor at e2   (&gt;= 0.)Saturation factor at e2   (&gt;= 0.)
    se2 = Float(desc="Saturation factor at e2   (&gt;= 0.)Saturation factor at e2   (&gt;= 0.)")

    # Field voltage value 2.   (&gt; 0.)Field voltage value 2.   (&gt; 0.)
    e2 = Float(desc="Field voltage value 2.   (&gt; 0.)Field voltage value 2.   (&gt; 0.)")

    # Field voltage value 1    (&gt; 0.)Field voltage value 1    (&gt; 0.)
    e1 = Float(desc="Field voltage value 1    (&gt; 0.)Field voltage value 1    (&gt; 0.)")

    # Filter time constant (&gt;= 0.)Filter time constant (&gt;= 0.)
    tr = Seconds(desc="Filter time constant (&gt;= 0.)Filter time constant (&gt;= 0.)")

    # Minimum AVR output (&lt; 0.)Minimum AVR output (&lt; 0.)
    vamin = Float(desc="Minimum AVR output (&lt; 0.)Minimum AVR output (&lt; 0.)")

    # Maximum AVR output (&gt; 0.)Maximum AVR output (&gt; 0.)
    vamax = Float(desc="Maximum AVR output (&gt; 0.)Maximum AVR output (&gt; 0.)")

    # Maximum exciter control signal (&gt; 0.)Maximum exciter control signal (&gt; 0.)
    vrmax = Float(desc="Maximum exciter control signal (&gt; 0.)Maximum exciter control signal (&gt; 0.)")

    # TGR lag time constant (&gt;= 0.)TGR lag time constant (&gt;= 0.)
    tb = Seconds(desc="TGR lag time constant (&gt;= 0.)TGR lag time constant (&gt;= 0.)")

    # Exciter internal reactance  (&gt;= 0.)Exciter internal reactance  (&gt;= 0.)
    kd = Float(desc="Exciter internal reactance  (&gt;= 0.)Exciter internal reactance  (&gt;= 0.)")

    # TGR lead time constantTGR lead time constant
    tc = Seconds(desc="TGR lead time constantTGR lead time constant")

    # Rectifier regulation factor (&gt;= 0.)Rectifier regulation factor (&gt;= 0.)
    kc = Float(desc="Rectifier regulation factor (&gt;= 0.)Rectifier regulation factor (&gt;= 0.)")

    # Rate feedback gain (&gt;= 0.)Rate feedback gain (&gt;= 0.)
    kf = Float(desc="Rate feedback gain (&gt;= 0.)Rate feedback gain (&gt;= 0.)")

    # AVR time constant (&gt; 0.)AVR time constant (&gt; 0.)
    ta = Seconds(desc="AVR time constant (&gt; 0.)AVR time constant (&gt; 0.)")

    # Minimum exciter control signal  (&lt; 0.)Minimum exciter control signal  (&lt; 0.)
    vrmin = Float(desc="Minimum exciter control signal  (&lt; 0.)Minimum exciter control signal  (&lt; 0.)")

    # Exciter field resistance constantExciter field resistance constant
    ke = Float(desc="Exciter field resistance constantExciter field resistance constant")

    # Exciter time constant (&gt; 0.)Exciter time constant (&gt; 0.)
    te = Seconds(desc="Exciter time constant (&gt; 0.)Exciter time constant (&gt; 0.)")

    # Rate feedback time constant (&gt; 0.)Rate feedback time constant (&gt; 0.)
    tf = Seconds(desc="Rate feedback time constant (&gt; 0.)Rate feedback time constant (&gt; 0.)")

    # AVR gain (&gt; 0.)AVR gain (&gt; 0.)
    ka = Float(desc="AVR gain (&gt; 0.)AVR gain (&gt; 0.)")

    #--------------------------------------------------------------------------
    #  Begin "ExcAC1A" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "se1", "se2", "e2", "e1", "tr", "vamin", "vamax", "vrmax", "tb", "kd", "tc", "kc", "kf", "ta", "vrmin", "ke", "te", "tf", "ka",
                label="Attributes", columns=1),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.ExcitationSystems.ExcAC1A",
        title="ExcAC1A",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ExcAC1A" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ExcDC4B" class:
#------------------------------------------------------------------------------

class ExcDC4B(ExcitationSystem):
    """ IEEE (2005) DC4B Model  These excitation systems utilize a field-controlled dc commutator exciter with a continuously acting voltage regulator having supplies obtained from the generator or auxiliary bus. The replacement of the controls only as an upgrade (retaining the dc commutator exciter) has resulted in a new model. This excitation system typically includes a proportional, integral, and differential (PID) generator voltage regulator (AVR). An alternative rate feedback loop (<i>kf</i>, <i>tf</i>) for stabilization is also shown in the model if the AVR does not include a derivative term. If a PSS control is supplied, the appropriate model is the Type PSS2B model.IEEE (2005) DC4B Model  These excitation systems utilize a field-controlled dc commutator exciter with a continuously acting voltage regulator having supplies obtained from the generator or auxiliary bus. The replacement of the controls only as an upgrade (retaining the dc commutator exciter) has resulted in a new model. This excitation system typically includes a proportional, integral, and differential (PID) generator voltage regulator (AVR). An alternative rate feedback loop (<i>kf</i>, <i>tf</i>) for stabilization is also shown in the model if the AVR does not include a derivative term. If a PSS control is supplied, the appropriate model is the Type PSS2B model.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Minimum controller output (&lt;= 0.)Minimum controller output (&lt;= 0.)
    vrmin = Float(desc="Minimum controller output (&lt;= 0.)Minimum controller output (&lt;= 0.)")

    # UEL input: if &lt; 2, HV gate; if = 2, add to error signalUEL input: if &lt; 2, HV gate; if = 2, add to error signal
    uelin = Float(desc="UEL input: if &lt; 2, HV gate; if = 2, add to error signalUEL input: if &lt; 2, HV gate; if = 2, add to error signal")

    # Integral gain (&gt;= 0.)Integral gain (&gt;= 0.)
    ki = Float(desc="Integral gain (&gt;= 0.)Integral gain (&gt;= 0.)")

    # Proportional gain (&gt;= 0.)Proportional gain (&gt;= 0.)
    kp = Float(desc="Proportional gain (&gt;= 0.)Proportional gain (&gt;= 0.)")

    # Field voltage value 2.   (&gt; 0.)Field voltage value 2.   (&gt; 0.)
    e2 = Float(desc="Field voltage value 2.   (&gt; 0.)Field voltage value 2.   (&gt; 0.)")

    # OEL input: if &lt; 2, LV gate; if = 2, subtract from error signalOEL input: if &lt; 2, LV gate; if = 2, subtract from error signal
    oelin = Float(desc="OEL input: if &lt; 2, LV gate; if = 2, subtract from error signalOEL input: if &lt; 2, LV gate; if = 2, subtract from error signal")

    # Maximum controller outputMaximum controller output
    vrmax = Float(desc="Maximum controller outputMaximum controller output")

    # Rate feedback gain (&gt;= 0.)Rate feedback gain (&gt;= 0.)
    kf = Float(desc="Rate feedback gain (&gt;= 0.)Rate feedback gain (&gt;= 0.)")

    # Exciter time constant (&gt; 0.)Exciter time constant (&gt; 0.)
    te = Seconds(desc="Exciter time constant (&gt; 0.)Exciter time constant (&gt; 0.)")

    # Exciter field resistance line slopeExciter field resistance line slope
    ke = Float(desc="Exciter field resistance line slopeExciter field resistance line slope")

    # Exciter minimum output  (&lt;= 0.)Exciter minimum output  (&lt;= 0.)
    vemin = Float(desc="Exciter minimum output  (&lt;= 0.)Exciter minimum output  (&lt;= 0.)")

    # Rate feedback time constant (&gt;= 0.)Rate feedback time constant (&gt;= 0.)
    tf = Seconds(desc="Rate feedback time constant (&gt;= 0.)Rate feedback time constant (&gt;= 0.)")

    # Derivative gain (&gt;= 0.)Derivative gain (&gt;= 0.)
    kd = Float(desc="Derivative gain (&gt;= 0.)Derivative gain (&gt;= 0.)")

    # Saturation factor at e2 (&gt;= 0.)Saturation factor at e2 (&gt;= 0.)
    se2 = Float(desc="Saturation factor at e2 (&gt;= 0.)Saturation factor at e2 (&gt;= 0.)")

    # Time constant (&gt; 0.)Time constant (&gt; 0.)
    ta = Seconds(desc="Time constant (&gt; 0.)Time constant (&gt; 0.)")

    # Filter time constant (&gt;= 0.)Filter time constant (&gt;= 0.)
    tr = Seconds(desc="Filter time constant (&gt;= 0.)Filter time constant (&gt;= 0.)")

    # Gain (&gt; 0.)Gain (&gt; 0.)
    ka = Float(desc="Gain (&gt; 0.)Gain (&gt; 0.)")

    # Saturation factor at e1   (&gt;= 0.)Saturation factor at e1   (&gt;= 0.)
    se1 = Float(desc="Saturation factor at e1   (&gt;= 0.)Saturation factor at e1   (&gt;= 0.)")

    # Derivative time constant (&gt; 0. If kd &gt; 0.)Derivative time constant (&gt; 0. If kd &gt; 0.)
    td = Seconds(desc="Derivative time constant (&gt; 0. If kd &gt; 0.)Derivative time constant (&gt; 0. If kd &gt; 0.)")

    # Field voltage value 1     (&gt; 0.)Field voltage value 1     (&gt; 0.)
    e1 = Float(desc="Field voltage value 1     (&gt; 0.)Field voltage value 1     (&gt; 0.)")

    #--------------------------------------------------------------------------
    #  Begin "ExcDC4B" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "vrmin", "uelin", "ki", "kp", "e2", "oelin", "vrmax", "kf", "te", "ke", "vemin", "tf", "kd", "se2", "ta", "tr", "ka", "se1", "td", "e1",
                label="Attributes", columns=1),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.ExcitationSystems.ExcDC4B",
        title="ExcDC4B",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ExcDC4B" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ExcDC1A" class:
#------------------------------------------------------------------------------

class ExcDC1A(ExcitationSystem):
    """ IEEE (1992/2005) DC1A Model  This model is used to represent field-controlled dc commutator exciters with continuously acting voltage regulators (especially the direct-acting rheostatic, rotating amplifier, and magnetic amplifier types). Because this model has been widely implemented by the industry, it is sometimes used to represent other types of systems when detailed data for them are not available or when a simplified model is required.IEEE (1992/2005) DC1A Model  This model is used to represent field-controlled dc commutator exciters with continuously acting voltage regulators (especially the direct-acting rheostatic, rotating amplifier, and magnetic amplifier types). Because this model has been widely implemented by the industry, it is sometimes used to represent other types of systems when detailed data for them are not available or when a simplified model is required.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # If not 0, apply lower limit of 0. to exciter outputIf not 0, apply lower limit of 0. to exciter output
    exclim = Float(desc="If not 0, apply lower limit of 0. to exciter outputIf not 0, apply lower limit of 0. to exciter output")

    # Minimum controller output (&lt; 0.)Minimum controller output (&lt; 0.)
    vrmin = Float(desc="Minimum controller output (&lt; 0.)Minimum controller output (&lt; 0.)")

    # Lead time constantLead time constant
    tc = Seconds(desc="Lead time constantLead time constant")

    # Time constant (&gt; 0.)Time constant (&gt; 0.)
    ta = Seconds(desc="Time constant (&gt; 0.)Time constant (&gt; 0.)")

    # Lag time constant (&gt;= 0.)Lag time constant (&gt;= 0.)
    tb = Seconds(desc="Lag time constant (&gt;= 0.)Lag time constant (&gt;= 0.)")

    # Gain (&gt; 0.)Gain (&gt; 0.)
    ka = Float(desc="Gain (&gt; 0.)Gain (&gt; 0.)")

    # Exciter field resistance line slopeExciter field resistance line slope
    ke = Float(desc="Exciter field resistance line slopeExciter field resistance line slope")

    # Saturation factor at e2  (&gt;= 0.)Saturation factor at e2  (&gt;= 0.)
    se2 = Float(desc="Saturation factor at e2  (&gt;= 0.)Saturation factor at e2  (&gt;= 0.)")

    # Exciter time constant (&gt; 0.)Exciter time constant (&gt; 0.)
    te = Seconds(desc="Exciter time constant (&gt; 0.)Exciter time constant (&gt; 0.)")

    # Saturation factor at e1  (&gt;= 0.)Saturation factor at e1  (&gt;= 0.)
    se1 = Float(desc="Saturation factor at e1  (&gt;= 0.)Saturation factor at e1  (&gt;= 0.)")

    # Rate feedback time constant, sec. (&gt; 0.)Rate feedback time constant, sec. (&gt; 0.)
    tf = Seconds(desc="Rate feedback time constant, sec. (&gt; 0.)Rate feedback time constant, sec. (&gt; 0.)")

    # Rate feedback gain (&gt;= 0.)Rate feedback gain (&gt;= 0.)
    kf = Float(desc="Rate feedback gain (&gt;= 0.)Rate feedback gain (&gt;= 0.)")

    # UEL input: if &lt; 2, HV gate; if = 2, add to error signalUEL input: if &lt; 2, HV gate; if = 2, add to error signal
    uelin = Float(desc="UEL input: if &lt; 2, HV gate; if = 2, add to error signalUEL input: if &lt; 2, HV gate; if = 2, add to error signal")

    # Filter time constant (&gt;= 0.)Filter time constant (&gt;= 0.)
    tr = Seconds(desc="Filter time constant (&gt;= 0.)Filter time constant (&gt;= 0.)")

    # Field voltage value 1    (&gt; 0.)Field voltage value 1    (&gt; 0.)
    e1 = Float(desc="Field voltage value 1    (&gt; 0.)Field voltage value 1    (&gt; 0.)")

    # Maximum controller outputMaximum controller output
    vrmax = Float(desc="Maximum controller outputMaximum controller output")

    # Field voltage value 2.   (&gt; 0.)Field voltage value 2.   (&gt; 0.)
    e2 = Float(desc="Field voltage value 2.   (&gt; 0.)Field voltage value 2.   (&gt; 0.)")

    #--------------------------------------------------------------------------
    #  Begin "ExcDC1A" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "exclim", "vrmin", "tc", "ta", "tb", "ka", "ke", "se2", "te", "se1", "tf", "kf", "uelin", "tr", "e1", "vrmax", "e2",
                label="Attributes", columns=1),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.ExcitationSystems.ExcDC1A",
        title="ExcDC1A",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ExcDC1A" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ExcAC3A" class:
#------------------------------------------------------------------------------

class ExcAC3A(ExcitationSystem):
    """ IEEE (1992/2005) AC3A Model  The model represents the field-controlled alternator-rectifier excitation systems designated Type AC3A. These excitation systems include an alternator main exciter with non-controlled rectifiers. The exciter employs self-excitation, and the voltage regulator power is derived from the exciter output voltage. Therefore, this system has an additional nonlinearity, simulated by the use of a multiplier whose inputs are the voltage regulator command signal, <i>VA</i>, and the exciter output voltage, <i>EFD</i>, times <i>KR</i>. This model is applicable to excitation systems employing static voltage regulators.IEEE (1992/2005) AC3A Model  The model represents the field-controlled alternator-rectifier excitation systems designated Type AC3A. These excitation systems include an alternator main exciter with non-controlled rectifiers. The exciter employs self-excitation, and the voltage regulator power is derived from the exciter output voltage. Therefore, this system has an additional nonlinearity, simulated by the use of a multiplier whose inputs are the voltage regulator command signal, <i>VA</i>, and the exciter output voltage, <i>EFD</i>, times <i>KR</i>. This model is applicable to excitation systems employing static voltage regulators.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # AVR time constant (&gt; 0.)AVR time constant (&gt; 0.)
    ta = Seconds(desc="AVR time constant (&gt; 0.)AVR time constant (&gt; 0.)")

    # AVR gain (&gt; 0.)AVR gain (&gt; 0.)
    ka = Float(desc="AVR gain (&gt; 0.)AVR gain (&gt; 0.)")

    # Exciter internal reactance (&gt;= 0.)Exciter internal reactance (&gt;= 0.)
    kd = Float(desc="Exciter internal reactance (&gt;= 0.)Exciter internal reactance (&gt;= 0.)")

    # Saturation factor at e1   (&gt;= 0.)Saturation factor at e1   (&gt;= 0.)
    se1 = Float(desc="Saturation factor at e1   (&gt;= 0.)Saturation factor at e1   (&gt;= 0.)")

    # Rectifier regulation factor (&gt;= 0.)Rectifier regulation factor (&gt;= 0.)
    kc = Float(desc="Rectifier regulation factor (&gt;= 0.)Rectifier regulation factor (&gt;= 0.)")

    # Saturation factor at e2   (&gt;= 0.)Saturation factor at e2   (&gt;= 0.)
    se2 = Float(desc="Saturation factor at e2   (&gt;= 0.)Saturation factor at e2   (&gt;= 0.)")

    # Exciter time constant (&gt; 0.)Exciter time constant (&gt; 0.)
    te = Seconds(desc="Exciter time constant (&gt; 0.)Exciter time constant (&gt; 0.)")

    # Rate feedback time constant (&gt; 0.)Rate feedback time constant (&gt; 0.)
    tf = Seconds(desc="Rate feedback time constant (&gt; 0.)Rate feedback time constant (&gt; 0.)")

    # TGR lag time constant (&gt;= 0.)TGR lag time constant (&gt;= 0.)
    tb = Seconds(desc="TGR lag time constant (&gt;= 0.)TGR lag time constant (&gt;= 0.)")

    # TGR lead time constantTGR lead time constant
    tc = Seconds(desc="TGR lead time constantTGR lead time constant")

    # Maximum AVR output (&gt; 0.)Maximum AVR output (&gt; 0.)
    vamax = Float(desc="Maximum AVR output (&gt; 0.)Maximum AVR output (&gt; 0.)")

    # Low level rate feedback gain (&gt;= 0.)Low level rate feedback gain (&gt;= 0.)
    kf = Float(desc="Low level rate feedback gain (&gt;= 0.)Low level rate feedback gain (&gt;= 0.)")

    # Minimum field voltage limit (&lt;= 0.)Minimum field voltage limit (&lt;= 0.)
    vemin = Float(desc="Minimum field voltage limit (&lt;= 0.)Minimum field voltage limit (&lt;= 0.)")

    # Exciter field resistance constantExciter field resistance constant
    ke = Float(desc="Exciter field resistance constantExciter field resistance constant")

    # Exciter field current limit parameter (&gt;= 0.)Exciter field current limit parameter (&gt;= 0.)
    vfemax = Float(desc="Exciter field current limit parameter (&gt;= 0.)Exciter field current limit parameter (&gt;= 0.)")

    # Filter time constant (&gt;= 0.)Filter time constant (&gt;= 0.)
    tr = Seconds(desc="Filter time constant (&gt;= 0.)Filter time constant (&gt;= 0.)")

    # Field voltage value 2.     (&gt; 0.)Field voltage value 2.     (&gt; 0.)
    e2 = Float(desc="Field voltage value 2.     (&gt; 0.)Field voltage value 2.     (&gt; 0.)")

    # Field voltage value 1     (&gt; 0.)Field voltage value 1     (&gt; 0.)
    e1 = Float(desc="Field voltage value 1     (&gt; 0.)Field voltage value 1     (&gt; 0.)")

    # High level rate feedback gain (&gt;= 0.)High level rate feedback gain (&gt;= 0.)
    kn = Float(desc="High level rate feedback gain (&gt;= 0.)High level rate feedback gain (&gt;= 0.)")

    # Minimum AVR output (&lt; 0.)Minimum AVR output (&lt; 0.)
    vamin = Float(desc="Minimum AVR output (&lt; 0.)Minimum AVR output (&lt; 0.)")

    # Field self-excitation feedback gain (&gt; 0.)Field self-excitation feedback gain (&gt; 0.)
    kr = Float(desc="Field self-excitation feedback gain (&gt; 0.)Field self-excitation feedback gain (&gt; 0.)")

    # Rate feedback gain break level (&gt; 0.)Rate feedback gain break level (&gt; 0.)
    efdn = Float(desc="Rate feedback gain break level (&gt; 0.)Rate feedback gain break level (&gt; 0.)")

    #--------------------------------------------------------------------------
    #  Begin "ExcAC3A" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "ta", "ka", "kd", "se1", "kc", "se2", "te", "tf", "tb", "tc", "vamax", "kf", "vemin", "ke", "vfemax", "tr", "e2", "e1", "kn", "vamin", "kr", "efdn",
                label="Attributes", columns=1),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.ExcitationSystems.ExcAC3A",
        title="ExcAC3A",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ExcAC3A" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ExcAC6A" class:
#------------------------------------------------------------------------------

class ExcAC6A(ExcitationSystem):
    """ IEEE (1992/2005) AC6A Model  The model is used to represent field-controlled alternator-rectifier excitation systems with system-supplied electronic voltage regulators. The maximum output of the regulator, <i>V</i><i><sub>R</sub></i>, is a function of terminal voltage, <i>V</i><i><sub>T</sub></i>. The field current limiter included in the original model AC6A remains in the 2005 update.IEEE (1992/2005) AC6A Model  The model is used to represent field-controlled alternator-rectifier excitation systems with system-supplied electronic voltage regulators. The maximum output of the regulator, <i>V</i><i><sub>R</sub></i>, is a function of terminal voltage, <i>V</i><i><sub>T</sub></i>. The field current limiter included in the original model AC6A remains in the 2005 update.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Maximum controller element output (&gt; 0.)Maximum controller element output (&gt; 0.)
    vamax = Float(desc="Maximum controller element output (&gt; 0.)Maximum controller element output (&gt; 0.)")

    # Exciter field current limit reference (&gt; 0.)Exciter field current limit reference (&gt; 0.)
    vfelim = Float(desc="Exciter field current limit reference (&gt; 0.)Exciter field current limit reference (&gt; 0.)")

    # Filter time constantFilter time constant
    tr = Seconds(desc="Filter time constantFilter time constant")

    # Field voltage value 2.    (&gt; 0.)Field voltage value 2.    (&gt; 0.)
    e2 = Float(desc="Field voltage value 2.    (&gt; 0.)Field voltage value 2.    (&gt; 0.)")

    # Field voltage value 1     (&gt; 0.)Field voltage value 1     (&gt; 0.)
    e1 = Float(desc="Field voltage value 1     (&gt; 0.)Field voltage value 1     (&gt; 0.)")

    # Minimum controller element output (&lt; 0.)Minimum controller element output (&lt; 0.)
    vamin = Float(desc="Minimum controller element output (&lt; 0.)Minimum controller element output (&lt; 0.)")

    # Maximum field current limiter signal (&gt; 0.)Maximum field current limiter signal (&gt; 0.)
    vhmax = Float(desc="Maximum field current limiter signal (&gt; 0.)Maximum field current limiter signal (&gt; 0.)")

    # Maximum exciter control signal (&gt; 0.)Maximum exciter control signal (&gt; 0.)
    vrmax = Float(desc="Maximum exciter control signal (&gt; 0.)Maximum exciter control signal (&gt; 0.)")

    # Saturation factor at e1 (&gt;= 0.)Saturation factor at e1 (&gt;= 0.)
    se1 = Float(desc="Saturation factor at e1 (&gt;= 0.)Saturation factor at e1 (&gt;= 0.)")

    # Saturation factor at e2  (&gt;= 0.)Saturation factor at e2  (&gt;= 0.)
    se2 = Float(desc="Saturation factor at e2  (&gt;= 0.)Saturation factor at e2  (&gt;= 0.)")

    # Minimum exciter control signal (&lt; 0.)Minimum exciter control signal (&lt; 0.)
    vrmin = Float(desc="Minimum exciter control signal (&lt; 0.)Minimum exciter control signal (&lt; 0.)")

    # Exciter time constant (&gt; 0.)Exciter time constant (&gt; 0.)
    te = Seconds(desc="Exciter time constant (&gt; 0.)Exciter time constant (&gt; 0.)")

    # Exciter field current limiter gain (&gt;= 0.)Exciter field current limiter gain (&gt;= 0.)
    kh = Float(desc="Exciter field current limiter gain (&gt;= 0.)Exciter field current limiter gain (&gt;= 0.)")

    # Time constant (&gt;= 0.)Time constant (&gt;= 0.)
    tb = Seconds(desc="Time constant (&gt;= 0.)Time constant (&gt;= 0.)")

    # Lead time constantLead time constant
    tc = Seconds(desc="Lead time constantLead time constant")

    # Time constant (&gt;= 0.)Time constant (&gt;= 0.)
    ta = Seconds(desc="Time constant (&gt;= 0.)Time constant (&gt;= 0.)")

    # Gain (&gt; 0.)Gain (&gt; 0.)
    ka = Float(desc="Gain (&gt; 0.)Gain (&gt; 0.)")

    # Rectifier regulation factor (&gt;= 0.)Rectifier regulation factor (&gt;= 0.)
    kc = Float(desc="Rectifier regulation factor (&gt;= 0.)Rectifier regulation factor (&gt;= 0.)")

    # Field current limiter time constant (&gt;= 0.)Field current limiter time constant (&gt;= 0.)
    tj = Seconds(desc="Field current limiter time constant (&gt;= 0.)Field current limiter time constant (&gt;= 0.)")

    # Lag time constant (&gt;= 0.)Lag time constant (&gt;= 0.)
    tk = Seconds(desc="Lag time constant (&gt;= 0.)Lag time constant (&gt;= 0.)")

    # Exciter field resistance constantExciter field resistance constant
    ke = Float(desc="Exciter field resistance constantExciter field resistance constant")

    # Field current limiter time constant (&gt; 0.)Field current limiter time constant (&gt; 0.)
    th = Seconds(desc="Field current limiter time constant (&gt; 0.)Field current limiter time constant (&gt; 0.)")

    # Exciter internal reactance (&gt;= 0.)Exciter internal reactance (&gt;= 0.)
    kd = Float(desc="Exciter internal reactance (&gt;= 0.)Exciter internal reactance (&gt;= 0.)")

    #--------------------------------------------------------------------------
    #  Begin "ExcAC6A" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "vamax", "vfelim", "tr", "e2", "e1", "vamin", "vhmax", "vrmax", "se1", "se2", "vrmin", "te", "kh", "tb", "tc", "ta", "ka", "kc", "tj", "tk", "ke", "th", "kd",
                label="Attributes", columns=2),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.ExcitationSystems.ExcAC6A",
        title="ExcAC6A",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ExcAC6A" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ExcAC5A" class:
#------------------------------------------------------------------------------

class ExcAC5A(ExcitationSystem):
    """ IEEE (1992/2005) AC5A Model  The model designated as Type AC5A, is a simplified model for brushless excitation systems. The regulator is supplied from a source, such as a permanent magnet generator, which is not affected by system disturbances. Unlike other ac models, this model uses loaded rather than open circuit exciter saturation data in the same way as it is used for the dc models. Because the model has been widely implemented by the industry, it is sometimes used to represent other types of systems when either detailed data for them are not available or simplified models are required.IEEE (1992/2005) AC5A Model  The model designated as Type AC5A, is a simplified model for brushless excitation systems. The regulator is supplied from a source, such as a permanent magnet generator, which is not affected by system disturbances. Unlike other ac models, this model uses loaded rather than open circuit exciter saturation data in the same way as it is used for the dc models. Because the model has been widely implemented by the industry, it is sometimes used to represent other types of systems when either detailed data for them are not available or simplified models are required.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Time constant (&gt; 0.)Time constant (&gt; 0.)
    ta = Seconds(desc="Time constant (&gt; 0.)Time constant (&gt; 0.)")

    # Maximum controller output (&gt; 0.)Maximum controller output (&gt; 0.)
    vrmax = Float(desc="Maximum controller output (&gt; 0.)Maximum controller output (&gt; 0.)")

    # Gain  (&gt; 0.)Gain  (&gt; 0.)
    ka = Float(desc="Gain  (&gt; 0.)Gain  (&gt; 0.)")

    # Minimum controller output (&lt;  0.)Minimum controller output (&lt;  0.)
    vrmin = Float(desc="Minimum controller output (&lt;  0.)Minimum controller output (&lt;  0.)")

    # Filter time constant (&gt;= 0.)Filter time constant (&gt;= 0.)
    tr = Seconds(desc="Filter time constant (&gt;= 0.)Filter time constant (&gt;= 0.)")

    # Rate feedback lag time constant (&gt; 0.)Rate feedback lag time constant (&gt; 0.)
    tf1 = Seconds(desc="Rate feedback lag time constant (&gt; 0.)Rate feedback lag time constant (&gt; 0.)")

    # Exciter field resistance line slopeExciter field resistance line slope
    ke = Float(desc="Exciter field resistance line slopeExciter field resistance line slope")

    # Rate feedback lag time constant (&gt;= 0.)Rate feedback lag time constant (&gt;= 0.)
    tf2 = Seconds(desc="Rate feedback lag time constant (&gt;= 0.)Rate feedback lag time constant (&gt;= 0.)")

    # Exciter time constant, sec. (&gt; 0.)Exciter time constant, sec. (&gt; 0.)
    te = Seconds(desc="Exciter time constant, sec. (&gt; 0.)Exciter time constant, sec. (&gt; 0.)")

    # Rate feedback gain (&gt;= 0.)Rate feedback gain (&gt;= 0.)
    kf = Float(desc="Rate feedback gain (&gt;= 0.)Rate feedback gain (&gt;= 0.)")

    # Field voltage value 1      (&gt; 0.)Field voltage value 1      (&gt; 0.)
    e1 = Float(desc="Field voltage value 1      (&gt; 0.)Field voltage value 1      (&gt; 0.)")

    # Rate feedback lead time constantRate feedback lead time constant
    tf3 = Seconds(desc="Rate feedback lead time constantRate feedback lead time constant")

    # Field voltage value 2.  (&gt; 0.)Field voltage value 2.  (&gt; 0.)
    e2 = Float(desc="Field voltage value 2.  (&gt; 0.)Field voltage value 2.  (&gt; 0.)")

    # Saturation factor at e1  (&gt;= 0.)Saturation factor at e1  (&gt;= 0.)
    se1 = Float(desc="Saturation factor at e1  (&gt;= 0.)Saturation factor at e1  (&gt;= 0.)")

    # Saturation factor at e2 (&gt;= 0.)Saturation factor at e2 (&gt;= 0.)
    se2 = Float(desc="Saturation factor at e2 (&gt;= 0.)Saturation factor at e2 (&gt;= 0.)")

    #--------------------------------------------------------------------------
    #  Begin "ExcAC5A" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "ta", "vrmax", "ka", "vrmin", "tr", "tf1", "ke", "tf2", "te", "kf", "e1", "tf3", "e2", "se1", "se2",
                label="Attributes", columns=1),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.ExcitationSystems.ExcAC5A",
        title="ExcAC5A",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ExcAC5A" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ExcST5B" class:
#------------------------------------------------------------------------------

class ExcST5B(ExcitationSystem):
    """ IEEE (2005) ST5B Model  The Type ST5B excitation system is a variation of the Type ST1A model, with alternative overexcitation and underexcitation inputs and additional limits. The corresponding stabilizer models that can be used with these models are the Type PSS2B, PSS3B, or PSS4B.IEEE (2005) ST5B Model  The Type ST5B excitation system is a variation of the Type ST1A model, with alternative overexcitation and underexcitation inputs and additional limits. The corresponding stabilizer models that can be used with these models are the Type PSS2B, PSS3B, or PSS4B.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # OEL lead time constantOEL lead time constant
    toc2 = Seconds(desc="OEL lead time constantOEL lead time constant")

    # OEL lead time constantOEL lead time constant
    toc1 = Seconds(desc="OEL lead time constantOEL lead time constant")

    # Regulator lead time constantRegulator lead time constant
    tc1 = Seconds(desc="Regulator lead time constantRegulator lead time constant")

    # Minimum regulator output (&lt; 0.)Minimum regulator output (&lt; 0.)
    vrmin = Float(desc="Minimum regulator output (&lt; 0.)Minimum regulator output (&lt; 0.)")

    # Regulator lead time constant.Regulator lead time constant.
    tc2 = Seconds(desc="Regulator lead time constant.Regulator lead time constant.")

    # Rectifier regulation factor (&gt;= 0.)Rectifier regulation factor (&gt;= 0.)
    kc = Float(desc="Rectifier regulation factor (&gt;= 0.)Rectifier regulation factor (&gt;= 0.)")

    # Regulator lag time constant (&gt;= 0.)Regulator lag time constant (&gt;= 0.)
    tb2 = Seconds(desc="Regulator lag time constant (&gt;= 0.)Regulator lag time constant (&gt;= 0.)")

    # OEL lag time constant (&gt;= 0.)OEL lag time constant (&gt;= 0.)
    tob1 = Seconds(desc="OEL lag time constant (&gt;= 0.)OEL lag time constant (&gt;= 0.)")

    # Maximum regulator output (&gt; 0.)Maximum regulator output (&gt; 0.)
    vrmax = Float(desc="Maximum regulator output (&gt; 0.)Maximum regulator output (&gt; 0.)")

    # OEL lag time constant (&gt;= 0.)OEL lag time constant (&gt;= 0.)
    tob2 = Seconds(desc="OEL lag time constant (&gt;= 0.)OEL lag time constant (&gt;= 0.)")

    # Regulator lag time constant (&gt;= 0.)Regulator lag time constant (&gt;= 0.)
    tb1 = Seconds(desc="Regulator lag time constant (&gt;= 0.)Regulator lag time constant (&gt;= 0.)")

    # UEL lag time constant (&gt;= 0.)UEL lag time constant (&gt;= 0.)
    tub1 = Seconds(desc="UEL lag time constant (&gt;= 0.)UEL lag time constant (&gt;= 0.)")

    # UEL lag time constant (&gt;= 0.)UEL lag time constant (&gt;= 0.)
    tub2 = Seconds(desc="UEL lag time constant (&gt;= 0.)UEL lag time constant (&gt;= 0.)")

    # UEL lead time constant.UEL lead time constant.
    tuc1 = Seconds(desc="UEL lead time constant.UEL lead time constant.")

    # UEL lead time constantUEL lead time constant
    tuc2 = Seconds(desc="UEL lead time constantUEL lead time constant")

    # Regulator gain (&gt; 0.)Regulator gain (&gt; 0.)
    kr = Float(desc="Regulator gain (&gt; 0.)Regulator gain (&gt; 0.)")

    # Filter time constant (&gt;= 0.)Filter time constant (&gt;= 0.)
    tr = Seconds(desc="Filter time constant (&gt;= 0.)Filter time constant (&gt;= 0.)")

    # Firing circuit time constant (&gt;= 0.)Firing circuit time constant (&gt;= 0.)
    t1 = Seconds(desc="Firing circuit time constant (&gt;= 0.)Firing circuit time constant (&gt;= 0.)")

    #--------------------------------------------------------------------------
    #  Begin "ExcST5B" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "toc2", "toc1", "tc1", "vrmin", "tc2", "kc", "tb2", "tob1", "vrmax", "tob2", "tb1", "tub1", "tub2", "tuc1", "tuc2", "kr", "tr", "t1",
                label="Attributes", columns=1),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.ExcitationSystems.ExcST5B",
        title="ExcST5B",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ExcST5B" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ExcSCRX" class:
#------------------------------------------------------------------------------

class ExcSCRX(ExcitationSystem):
    """ Simple excitation system model representing generic characteristics of many excitation systems; intended for use where negative field current may be a problemSimple excitation system model representing generic characteristics of many excitation systems; intended for use where negative field current may be a problem
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Time constant of gain block (&gt; 0.)Time constant of gain block (&gt; 0.)
    te = Seconds(desc="Time constant of gain block (&gt; 0.)Time constant of gain block (&gt; 0.)")

    # Denominator time constant of lag-lead blockDenominator time constant of lag-lead block
    tb = Seconds(desc="Denominator time constant of lag-lead blockDenominator time constant of lag-lead block")

    # Maximum field voltage outputMaximum field voltage output
    emax = Float(desc="Maximum field voltage outputMaximum field voltage output")

    # Power source switch:     1 ? fixed voltage     0 ? generator terminal voltagePower source switch:     1 ? fixed voltage     0 ? generator terminal voltage
    cswitch = Bool(desc="Power source switch:     1 ? fixed voltage     0 ? generator terminal voltagePower source switch:     1 ? fixed voltage     0 ? generator terminal voltage")

    # Rc/Rfd - ratio of field discharge resistance to field winding resistanceRc/Rfd - ratio of field discharge resistance to field winding resistance
    rcrfd = Float(desc="Rc/Rfd - ratio of field discharge resistance to field winding resistanceRc/Rfd - ratio of field discharge resistance to field winding resistance")

    # Ta/Tb - gain reduction ratio of lag-lead elementTa/Tb - gain reduction ratio of lag-lead element
    tatb = Float(desc="Ta/Tb - gain reduction ratio of lag-lead elementTa/Tb - gain reduction ratio of lag-lead element")

    # Gain (&gt; 0.)Gain (&gt; 0.)
    k = Float(desc="Gain (&gt; 0.)Gain (&gt; 0.)")

    # Minimum field voltage outputMinimum field voltage output
    emin = Float(desc="Minimum field voltage outputMinimum field voltage output")

    #--------------------------------------------------------------------------
    #  Begin "ExcSCRX" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "te", "tb", "emax", "cswitch", "rcrfd", "tatb", "k", "emin",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.ExcitationSystems.ExcSCRX",
        title="ExcSCRX",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ExcSCRX" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ExcAC8B" class:
#------------------------------------------------------------------------------

class ExcAC8B(ExcitationSystem):
    """ IEEE (2005) AC8B Model  The AVR in this model consists of PID control, with separate constants for the proportional (<i>KPR</i>), integral (<i>KIR</i>), and derivative (<i>KDR</i>) gains. The representation of the brushless exciter (<i>TE</i>, <i>KE</i>, <i>SE</i>, <i>KC</i>, <i>KD</i>) is similar to the model Type AC2A. The Type AC8B model can be used to represent static voltage regulators applied to brushless excitation systems. Digitally based voltage regulators feeding dc rotating main exciters can be represented with the AC Type AC8B model with the parameters <i>KC </i>and <i>KD </i>set to 0. For thyristor power stages fed from the generator terminals, the limits <i>VRMAX </i>and <i>VRMIN </i>should be a function of terminal voltage: <i>VT </i>x <i>VRMAX </i>and <i>VT </i>x <i>VRMIN</i>.IEEE (2005) AC8B Model  The AVR in this model consists of PID control, with separate constants for the proportional (<i>KPR</i>), integral (<i>KIR</i>), and derivative (<i>KDR</i>) gains. The representation of the brushless exciter (<i>TE</i>, <i>KE</i>, <i>SE</i>, <i>KC</i>, <i>KD</i>) is similar to the model Type AC2A. The Type AC8B model can be used to represent static voltage regulators applied to brushless excitation systems. Digitally based voltage regulators feeding dc rotating main exciters can be represented with the AC Type AC8B model with the parameters <i>KC </i>and <i>KD </i>set to 0. For thyristor power stages fed from the generator terminals, the limits <i>VRMAX </i>and <i>VRMIN </i>should be a function of terminal voltage: <i>VT </i>x <i>VRMAX </i>and <i>VT </i>x <i>VRMIN</i>.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Voltage Regulator Derivative Gain (&gt;= 0.)Voltage Regulator Derivative Gain (&gt;= 0.)
    kdr = Float(desc="Voltage Regulator Derivative Gain (&gt;= 0.)Voltage Regulator Derivative Gain (&gt;= 0.)")

    # Voltage transducer time constant (&gt;= 0.)Voltage transducer time constant (&gt;= 0.)
    tr = Seconds(desc="Voltage transducer time constant (&gt;= 0.)Voltage transducer time constant (&gt;= 0.)")

    # Field voltage value 1     (&gt; 0.)Field voltage value 1     (&gt; 0.)
    e1 = Float(desc="Field voltage value 1     (&gt; 0.)Field voltage value 1     (&gt; 0.)")

    # Field voltage value 2.    (&gt; 0.)Field voltage value 2.    (&gt; 0.)
    e2 = Float(desc="Field voltage value 2.    (&gt; 0.)Field voltage value 2.    (&gt; 0.)")

    # Voltage Regulator Integral Gain (&gt;= 0.)Voltage Regulator Integral Gain (&gt;= 0.)
    kir = Float(desc="Voltage Regulator Integral Gain (&gt;= 0.)Voltage Regulator Integral Gain (&gt;= 0.)")

    # Rectifier regulation factor (&gt;= 0.)Rectifier regulation factor (&gt;= 0.)
    kc = Float(desc="Rectifier regulation factor (&gt;= 0.)Rectifier regulation factor (&gt;= 0.)")

    # Maximum controller output (&gt; 0.)Maximum controller output (&gt; 0.)
    vrmax = Float(desc="Maximum controller output (&gt; 0.)Maximum controller output (&gt; 0.)")

    # Amplifier gain (&gt; 0.)Amplifier gain (&gt; 0.)
    ka = Float(desc="Amplifier gain (&gt; 0.)Amplifier gain (&gt; 0.)")

    # Saturation factor at e2  (&gt;= 0.)Saturation factor at e2  (&gt;= 0.)
    se2 = Float(desc="Saturation factor at e2  (&gt;= 0.)Saturation factor at e2  (&gt;= 0.)")

    # Voltage Regulator Derivative Time Constant (&gt; 0. if kdr &gt; 0.)Voltage Regulator Derivative Time Constant (&gt; 0. if kdr &gt; 0.)
    tdr = Seconds(desc="Voltage Regulator Derivative Time Constant (&gt; 0. if kdr &gt; 0.)Voltage Regulator Derivative Time Constant (&gt; 0. if kdr &gt; 0.)")

    # Voltage Regulator Proportional Gain (&gt; 0. if kir = 0.)Voltage Regulator Proportional Gain (&gt; 0. if kir = 0.)
    kpr = Float(desc="Voltage Regulator Proportional Gain (&gt; 0. if kir = 0.)Voltage Regulator Proportional Gain (&gt; 0. if kir = 0.)")

    # Minimum exciter ouput voltage (&lt;= 0.)Minimum exciter ouput voltage (&lt;= 0.)
    vemin = Float(desc="Minimum exciter ouput voltage (&lt;= 0.)Minimum exciter ouput voltage (&lt;= 0.)")

    # Exciter regulation factor (&gt;= 0.)Exciter regulation factor (&gt;= 0.)
    kd = Float(desc="Exciter regulation factor (&gt;= 0.)Exciter regulation factor (&gt;= 0.)")

    # Exciter field time constant (&gt; 0.)Exciter field time constant (&gt; 0.)
    te = Seconds(desc="Exciter field time constant (&gt; 0.)Exciter field time constant (&gt; 0.)")

    # Saturation factor at e1 (&gt;= 0.)Saturation factor at e1 (&gt;= 0.)
    se1 = Float(desc="Saturation factor at e1 (&gt;= 0.)Saturation factor at e1 (&gt;= 0.)")

    # Exciter field proportional constantExciter field proportional constant
    ke = Float(desc="Exciter field proportional constantExciter field proportional constant")

    # Exciter field current limit parameterExciter field current limit parameter
    vfemax = Float(desc="Exciter field current limit parameterExciter field current limit parameter")

    # Amplifier time constant  (&gt;= 0.)Amplifier time constant  (&gt;= 0.)
    ta = Seconds(desc="Amplifier time constant  (&gt;= 0.)Amplifier time constant  (&gt;= 0.)")

    # Minimum controller output (&lt;= 0.)Minimum controller output (&lt;= 0.)
    vrmin = Float(desc="Minimum controller output (&lt;= 0.)Minimum controller output (&lt;= 0.)")

    # if not 0, multiply vrmax and vrmin by terminal voltageif not 0, multiply vrmax and vrmin by terminal voltage
    vtmult = Float(desc="if not 0, multiply vrmax and vrmin by terminal voltageif not 0, multiply vrmax and vrmin by terminal voltage")

    #--------------------------------------------------------------------------
    #  Begin "ExcAC8B" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "kdr", "tr", "e1", "e2", "kir", "kc", "vrmax", "ka", "se2", "tdr", "kpr", "vemin", "kd", "te", "se1", "ke", "vfemax", "ta", "vrmin", "vtmult",
                label="Attributes", columns=1),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.ExcitationSystems.ExcAC8B",
        title="ExcAC8B",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ExcAC8B" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ExcWT2E" class:
#------------------------------------------------------------------------------

class ExcWT2E(ExcitationSystem):
    """ Type 2 standard wind turbine field resistance control modelType 2 standard wind turbine field resistance control model
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "ExcWT2E" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.ExcitationSystems.ExcWT2E",
        title="ExcWT2E",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ExcWT2E" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ExcAC7B" class:
#------------------------------------------------------------------------------

class ExcAC7B(ExcitationSystem):
    """ IEEE (2005) AC7B Model  These excitation systems consist of an ac alternator with either stationary or rotating rectifiers to produce the dc field requirements. Upgrades to earlier ac excitation systems, which replace only the controls but retain the ac alternator and diode rectifier bridge, have resulted in this new model. Some of the features of this excitation system include a high bandwidth inner loop regulating generator field voltage or exciter current (<i>KF</i>2, <i>KF</i>1), a fast exciter current limit, <i>VFEMAX</i>, to protect the field of the ac alternator, and the PID generator voltage regulator (AVR). An alternative rate feedback loop (<i>KF</i>, <i>TF</i>) is provided for stabilization if the AVR does not include a derivative term. If a PSS control is supplied, the Type PSS2B or PSS3B models are appropriate.IEEE (2005) AC7B Model  These excitation systems consist of an ac alternator with either stationary or rotating rectifiers to produce the dc field requirements. Upgrades to earlier ac excitation systems, which replace only the controls but retain the ac alternator and diode rectifier bridge, have resulted in this new model. Some of the features of this excitation system include a high bandwidth inner loop regulating generator field voltage or exciter current (<i>KF</i>2, <i>KF</i>1), a fast exciter current limit, <i>VFEMAX</i>, to protect the field of the ac alternator, and the PID generator voltage regulator (AVR). An alternative rate feedback loop (<i>KF</i>, <i>TF</i>) is provided for stabilization if the AVR does not include a derivative term. If a PSS control is supplied, the Type PSS2B or PSS3B models are appropriate.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Exciter internal reactance (&gt;= 0.)Exciter internal reactance (&gt;= 0.)
    kd = Float(desc="Exciter internal reactance (&gt;= 0.)Exciter internal reactance (&gt;= 0.)")

    # Rectifier regulation factor (&gt;= 0.)Rectifier regulation factor (&gt;= 0.)
    kc = Float(desc="Rectifier regulation factor (&gt;= 0.)Rectifier regulation factor (&gt;= 0.)")

    # Minimum regulator output (&lt; 0.)Minimum regulator output (&lt; 0.)
    vrmin = Float(desc="Minimum regulator output (&lt; 0.)Minimum regulator output (&lt; 0.)")

    # Regulator derivative gain (&gt;= 0.)Regulator derivative gain (&gt;= 0.)
    kdr = Float(desc="Regulator derivative gain (&gt;= 0.)Regulator derivative gain (&gt;= 0.)")

    # Maximum regulator output (&gt; 0.)Maximum regulator output (&gt; 0.)
    vrmax = Float(desc="Maximum regulator output (&gt; 0.)Maximum regulator output (&gt; 0.)")

    # Regulator proportional gain (&gt; 0. if kir = 0.)Regulator proportional gain (&gt; 0. if kir = 0.)
    kpr = Float(desc="Regulator proportional gain (&gt; 0. if kir = 0.)Regulator proportional gain (&gt; 0. if kir = 0.)")

    # Minimum exciter ouput voltage (&lt;= 0.)Minimum exciter ouput voltage (&lt;= 0.)
    vemin = Float(desc="Minimum exciter ouput voltage (&lt;= 0.)Minimum exciter ouput voltage (&lt;= 0.)")

    # Exciter field voltage lower limit parameterExciter field voltage lower limit parameter
    kl = Float(desc="Exciter field voltage lower limit parameterExciter field voltage lower limit parameter")

    # Field voltage feedback gain (&gt;= 0.)Field voltage feedback gain (&gt;= 0.)
    kf1 = Float(desc="Field voltage feedback gain (&gt;= 0.)Field voltage feedback gain (&gt;= 0.)")

    # Amplifier integral gain (&gt;= 0.)Amplifier integral gain (&gt;= 0.)
    kia = Float(desc="Amplifier integral gain (&gt;= 0.)Amplifier integral gain (&gt;= 0.)")

    # Rate feedback gain (&gt;= 0.)Rate feedback gain (&gt;= 0.)
    kf3 = Float(desc="Rate feedback gain (&gt;= 0.)Rate feedback gain (&gt;= 0.)")

    # Saturation factor at e1  (&gt;= 0.)Saturation factor at e1  (&gt;= 0.)
    se1 = Float(desc="Saturation factor at e1  (&gt;= 0.)Saturation factor at e1  (&gt;= 0.)")

    # Exciter field current limit parameterExciter field current limit parameter
    vfemax = Float(desc="Exciter field current limit parameterExciter field current limit parameter")

    # Exciter field current feedback gain (&gt;= 0.)Exciter field current feedback gain (&gt;= 0.)
    kf2 = Float(desc="Exciter field current feedback gain (&gt;= 0.)Exciter field current feedback gain (&gt;= 0.)")

    # Exciter time constant, sec. (&gt; 0.)Exciter time constant, sec. (&gt; 0.)
    te = Seconds(desc="Exciter time constant, sec. (&gt; 0.)Exciter time constant, sec. (&gt; 0.)")

    # Rate feedback time constant (&gt; 0.)Rate feedback time constant (&gt; 0.)
    tf = Seconds(desc="Rate feedback time constant (&gt; 0.)Rate feedback time constant (&gt; 0.)")

    # Exciter field resistance constantExciter field resistance constant
    ke = Float(desc="Exciter field resistance constantExciter field resistance constant")

    # Amplifier proportional gain (&gt; 0. if kia = 0.)Amplifier proportional gain (&gt; 0. if kia = 0.)
    kpa = Float(desc="Amplifier proportional gain (&gt; 0. if kia = 0.)Amplifier proportional gain (&gt; 0. if kia = 0.)")

    # Field voltage value 2.    (&gt; 0.)Field voltage value 2.    (&gt; 0.)
    e2 = Float(desc="Field voltage value 2.    (&gt; 0.)Field voltage value 2.    (&gt; 0.)")

    # Saturation factor at e2   (&gt;= 0.)Saturation factor at e2   (&gt;= 0.)
    se2 = Float(desc="Saturation factor at e2   (&gt;= 0.)Saturation factor at e2   (&gt;= 0.)")

    # Exciter field voltage source gain (&gt; 0.)Exciter field voltage source gain (&gt; 0.)
    kp = Float(desc="Exciter field voltage source gain (&gt; 0.)Exciter field voltage source gain (&gt; 0.)")

    # Field voltage value 1   (&gt; 0.)Field voltage value 1   (&gt; 0.)
    e1 = Float(desc="Field voltage value 1   (&gt; 0.)Field voltage value 1   (&gt; 0.)")

    # Regulator integral gain (&gt;= 0.)Regulator integral gain (&gt;= 0.)
    kir = Float(desc="Regulator integral gain (&gt;= 0.)Regulator integral gain (&gt;= 0.)")

    # Filter time constant (&gt;= 0.)Filter time constant (&gt;= 0.)
    tr = Seconds(desc="Filter time constant (&gt;= 0.)Filter time constant (&gt;= 0.)")

    # Derivative gain washout time constant (&gt;= 0.)Derivative gain washout time constant (&gt;= 0.)
    tdr = Seconds(desc="Derivative gain washout time constant (&gt;= 0.)Derivative gain washout time constant (&gt;= 0.)")

    # Minimum amplifier output (&lt; 0.)Minimum amplifier output (&lt; 0.)
    vamin = Float(desc="Minimum amplifier output (&lt; 0.)Minimum amplifier output (&lt; 0.)")

    # Maximum amplifier output (&gt; 0.)Maximum amplifier output (&gt; 0.)
    vamax = Float(desc="Maximum amplifier output (&gt; 0.)Maximum amplifier output (&gt; 0.)")

    #--------------------------------------------------------------------------
    #  Begin "ExcAC7B" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "kd", "kc", "vrmin", "kdr", "vrmax", "kpr", "vemin", "kl", "kf1", "kia", "kf3", "se1", "vfemax", "kf2", "te", "tf", "ke", "kpa", "e2", "se2", "kp", "e1", "kir", "tr", "tdr", "vamin", "vamax",
                label="Attributes", columns=2),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.ExcitationSystems.ExcAC7B",
        title="ExcAC7B",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ExcAC7B" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ExcWT4E" class:
#------------------------------------------------------------------------------

class ExcWT4E(ExcitationSystem):
    """ Type 4 standard wind turbine convertor control modelType 4 standard wind turbine convertor control model
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "ExcWT4E" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.ExcitationSystems.ExcWT4E",
        title="ExcWT4E",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ExcWT4E" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ExcST1A" class:
#------------------------------------------------------------------------------

class ExcST1A(ExcitationSystem):
    """ IEEE (1992/2005) ST1A Model  The computer model of the Type ST1A potential-source controlled-rectifier excitation system represents systems in which excitation power is supplied through a transformer from the generator terminals (or the unit's auxiliary bus) and is regulated by a controlled rectifier. The maximum exciter voltage available from such systems is directly related to the generator terminal voltage.IEEE (1992/2005) ST1A Model  The computer model of the Type ST1A potential-source controlled-rectifier excitation system represents systems in which excitation power is supplied through a transformer from the generator terminals (or the unit's auxiliary bus) and is regulated by a controlled rectifier. The maximum exciter voltage available from such systems is directly related to the generator terminal voltage.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Excitation voltage lower limit (&lt; 0.)Excitation voltage lower limit (&lt; 0.)
    vrmin = Float(desc="Excitation voltage lower limit (&lt; 0.)Excitation voltage lower limit (&lt; 0.)")

    # Excitation system regulation factor (&gt;= 0.)Excitation system regulation factor (&gt;= 0.)
    kc = Float(desc="Excitation system regulation factor (&gt;= 0.)Excitation system regulation factor (&gt;= 0.)")

    # Minimum error (&lt; 0.)Minimum error (&lt; 0.)
    vimin = Float(desc="Minimum error (&lt; 0.)Minimum error (&lt; 0.)")

    # = 2 ? UEL input added to error signal = 1 ? UEL input HV gate with error signal = -1 ? UEL input HV gate with volt. reg. output = 0 ? ignore UEL signal= 2 ? UEL input added to error signal = 1 ? UEL input HV gate with error signal = -1 ? UEL input HV gate with volt. reg. output = 0 ? ignore UEL signal
    uelin = Float(desc="= 2 ? UEL input added to error signal = 1 ? UEL input HV gate with error signal = -1 ? UEL input HV gate with volt. reg. output = 0 ? ignore UEL signal= 2 ? UEL input added to error signal = 1 ? UEL input HV gate with error signal = -1 ? UEL input HV gate with volt. reg. output = 0 ? ignore UEL signal")

    # Rate feedback time constant (&gt;= 0.)Rate feedback time constant (&gt;= 0.)
    tf = Seconds(desc="Rate feedback time constant (&gt;= 0.)Rate feedback time constant (&gt;= 0.)")

    # Rate feedback gain (&gt;= 0.)Rate feedback gain (&gt;= 0.)
    kf = Float(desc="Rate feedback gain (&gt;= 0.)Rate feedback gain (&gt;= 0.)")

    # Lead time constantLead time constant
    tc1 = Seconds(desc="Lead time constantLead time constant")

    # = 0 ? PSS input (Vs) added to error signal not 0 ? PSS input (Vs) added to voltage regulator output= 0 ? PSS input (Vs) added to error signal not 0 ? PSS input (Vs) added to voltage regulator output
    pssin = Float(desc="= 0 ? PSS input (Vs) added to error signal not 0 ? PSS input (Vs) added to voltage regulator output= 0 ? PSS input (Vs) added to error signal not 0 ? PSS input (Vs) added to voltage regulator output")

    # Lead time constantLead time constant
    tc = Seconds(desc="Lead time constantLead time constant")

    # Lag time constant (&gt;= 0.)Lag time constant (&gt;= 0.)
    tb = Seconds(desc="Lag time constant (&gt;= 0.)Lag time constant (&gt;= 0.)")

    # Gain (&gt; 0.)Gain (&gt; 0.)
    ka = Float(desc="Gain (&gt; 0.)Gain (&gt; 0.)")

    # Time constant (&gt;= 0.)Time constant (&gt;= 0.)
    ta = Seconds(desc="Time constant (&gt;= 0.)Time constant (&gt;= 0.)")

    # Voltage transducer time constant (&gt;= 0.)Voltage transducer time constant (&gt;= 0.)
    tr = Seconds(desc="Voltage transducer time constant (&gt;= 0.)Voltage transducer time constant (&gt;= 0.)")

    # Maximum field currentMaximum field current
    ilr = Float(desc="Maximum field currentMaximum field current")

    # Minimum control element output (&lt; 0.)Minimum control element output (&lt; 0.)
    vamin = Float(desc="Minimum control element output (&lt; 0.)Minimum control element output (&lt; 0.)")

    # Gain on field current limitGain on field current limit
    klr = Float(desc="Gain on field current limitGain on field current limit")

    # Lag time constant (&gt;= 0.)Lag time constant (&gt;= 0.)
    tb1 = Seconds(desc="Lag time constant (&gt;= 0.)Lag time constant (&gt;= 0.)")

    # Maximum control element output (&gt; 0.)Maximum control element output (&gt; 0.)
    vamax = Float(desc="Maximum control element output (&gt; 0.)Maximum control element output (&gt; 0.)")

    # Excitation voltage upper limit (&gt; 0.)Excitation voltage upper limit (&gt; 0.)
    vrmax = Float(desc="Excitation voltage upper limit (&gt; 0.)Excitation voltage upper limit (&gt; 0.)")

    # Maximum error (&gt; 0.)Maximum error (&gt; 0.)
    vimax = Float(desc="Maximum error (&gt; 0.)Maximum error (&gt; 0.)")

    #--------------------------------------------------------------------------
    #  Begin "ExcST1A" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "vrmin", "kc", "vimin", "uelin", "tf", "kf", "tc1", "pssin", "tc", "tb", "ka", "ta", "tr", "ilr", "vamin", "klr", "tb1", "vamax", "vrmax", "vimax",
                label="Attributes", columns=1),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.ExcitationSystems.ExcST1A",
        title="ExcST1A",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ExcST1A" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ExcBBC" class:
#------------------------------------------------------------------------------

class ExcBBC(ExcitationSystem):
    """ Static Excitation System Model with ABB regulatorStatic Excitation System Model with ABB regulator
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "ExcBBC" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.ExcitationSystems.ExcBBC",
        title="ExcBBC",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ExcBBC" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ExcDC3A" class:
#------------------------------------------------------------------------------

class ExcDC3A(ExcitationSystem):
    """ IEEE (1992/2005) DC3A Model  The Type DC3A model is used to represent older systems, in particular those dc commutator exciters with non-continuously acting regulators that were commonly used before the development of the continuously acting varieties. These systems respond at basically two different rates, depending upon the magnitude of voltage error. For small errors, adjustment is made periodically with a signal to a motor-operated rheostat. Larger errors cause resistors to be quickly shorted or inserted and a strong forcing signal applied to the exciter. Continuous motion of the motor-operated rheostat occurs for these larger error signals, even though it is bypassed by contactor action.IEEE (1992/2005) DC3A Model  The Type DC3A model is used to represent older systems, in particular those dc commutator exciters with non-continuously acting regulators that were commonly used before the development of the continuously acting varieties. These systems respond at basically two different rates, depending upon the magnitude of voltage error. For small errors, adjustment is made periodically with a signal to a motor-operated rheostat. Larger errors cause resistors to be quickly shorted or inserted and a strong forcing signal applied to the exciter. Continuous motion of the motor-operated rheostat occurs for these larger error signals, even though it is bypassed by contactor action.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Maximum control element output (&gt; 0.)Maximum control element output (&gt; 0.)
    vrmax = Float(desc="Maximum control element output (&gt; 0.)Maximum control element output (&gt; 0.)")

    # Exciter field resistance line slopeExciter field resistance line slope
    ke = Float(desc="Exciter field resistance line slopeExciter field resistance line slope")

    # Exciter field time constant (&gt; 0.)Exciter field time constant (&gt; 0.)
    te = Seconds(desc="Exciter field time constant (&gt; 0.)Exciter field time constant (&gt; 0.)")

    # If not 0, apply lower limit of 0. to exciter outputIf not 0, apply lower limit of 0. to exciter output
    exclim = Float(desc="If not 0, apply lower limit of 0. to exciter outputIf not 0, apply lower limit of 0. to exciter output")

    # Saturation factor at e1 (&gt;= 0.)Saturation factor at e1 (&gt;= 0.)
    se1 = Float(desc="Saturation factor at e1 (&gt;= 0.)Saturation factor at e1 (&gt;= 0.)")

    # Saturation factor at e2  (&gt;= 0.)Saturation factor at e2  (&gt;= 0.)
    se2 = Float(desc="Saturation factor at e2  (&gt;= 0.)Saturation factor at e2  (&gt;= 0.)")

    # Rheostat full range travel time (&gt; 0.)Rheostat full range travel time (&gt; 0.)
    trh = Seconds(desc="Rheostat full range travel time (&gt; 0.)Rheostat full range travel time (&gt; 0.)")

    # Voltage error threshold min/max control action (&gt; 0.)Voltage error threshold min/max control action (&gt; 0.)
    kv = Float(desc="Voltage error threshold min/max control action (&gt; 0.)Voltage error threshold min/max control action (&gt; 0.)")

    # Field voltage value 1    (&gt; 0.)Field voltage value 1    (&gt; 0.)
    e1 = Float(desc="Field voltage value 1    (&gt; 0.)Field voltage value 1    (&gt; 0.)")

    # Field voltage value 2.     (&gt; 0.)Field voltage value 2.     (&gt; 0.)
    e2 = Float(desc="Field voltage value 2.     (&gt; 0.)Field voltage value 2.     (&gt; 0.)")

    # Minimum control element output (&lt;= 0.)Minimum control element output (&lt;= 0.)
    vrmin = Float(desc="Minimum control element output (&lt;= 0.)Minimum control element output (&lt;= 0.)")

    # Filter  time constant (&gt;= 0.)Filter  time constant (&gt;= 0.)
    tr = Seconds(desc="Filter  time constant (&gt;= 0.)Filter  time constant (&gt;= 0.)")

    #--------------------------------------------------------------------------
    #  Begin "ExcDC3A" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "vrmax", "ke", "te", "exclim", "se1", "se2", "trh", "kv", "e1", "e2", "vrmin", "tr",
                label="Attributes", columns=1),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.ExcitationSystems.ExcDC3A",
        title="ExcDC3A",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ExcDC3A" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ExcST3A" class:
#------------------------------------------------------------------------------

class ExcST3A(ExcitationSystem):
    """ IEEE (1992/2005) ST3A Model  Some static systems utilize a field voltage control loop to linearize the exciter control characteristic. This also makes the output independent of supply source variations until supply limitations are reached. These systems utilize a variety of controlled-rectifier designs: full thyristor complements or hybrid bridges in either series or shunt configurations. The power source may consist of only a potential source, either fed from the machine terminals or from internal windings. Some designs may have compound power sources utilizing both machine potential and current. These power sources are represented as phasor combinations of machine terminal current and voltage and are accommodated by suitable parameters in the model Type ST3A.IEEE (1992/2005) ST3A Model  Some static systems utilize a field voltage control loop to linearize the exciter control characteristic. This also makes the output independent of supply source variations until supply limitations are reached. These systems utilize a variety of controlled-rectifier designs: full thyristor complements or hybrid bridges in either series or shunt configurations. The power source may consist of only a potential source, either fed from the machine terminals or from internal windings. Some designs may have compound power sources utilizing both machine potential and current. These power sources are represented as phasor combinations of machine terminal current and voltage and are accommodated by suitable parameters in the model Type ST3A.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Minimum AVR output (&lt; 0.)Minimum AVR output (&lt; 0.)
    vrmin = Float(desc="Minimum AVR output (&lt; 0.)Minimum AVR output (&lt; 0.)")

    # Exciter regulation factor (&gt;= 0.)Exciter regulation factor (&gt;= 0.)
    kc = Float(desc="Exciter regulation factor (&gt;= 0.)Exciter regulation factor (&gt;= 0.)")

    # AVR gain (&gt; 0.)AVR gain (&gt; 0.)
    ka = Float(desc="AVR gain (&gt; 0.)AVR gain (&gt; 0.)")

    # Maximum excitation voltage (&gt; 0.)Maximum excitation voltage (&gt; 0.)
    vbmax = Float(desc="Maximum excitation voltage (&gt; 0.)Maximum excitation voltage (&gt; 0.)")

    # Minimum error (&lt; 0.)Minimum error (&lt; 0.)
    vimin = Float(desc="Minimum error (&lt; 0.)Minimum error (&lt; 0.)")

    # P-bar reactance (&gt;= 0.)P-bar reactance (&gt;= 0.)
    xl = Float(desc="P-bar reactance (&gt;= 0.)P-bar reactance (&gt;= 0.)")

    # Maximum inner loop feedback voltage (&gt;= 0.)Maximum inner loop feedback voltage (&gt;= 0.)
    vgmax = Float(desc="Maximum inner loop feedback voltage (&gt;= 0.)Maximum inner loop feedback voltage (&gt;= 0.)")

    # Phase angle of potential sourcePhase angle of potential source
    angp = Float(desc="Phase angle of potential sourcePhase angle of potential source")

    # Minimum inner loop output (&lt;= 0.)Minimum inner loop output (&lt;= 0.)
    vmmin = Float(desc="Minimum inner loop output (&lt;= 0.)Minimum inner loop output (&lt;= 0.)")

    # Maximum AVR output (&gt; 0.)Maximum AVR output (&gt; 0.)
    vrmax = Float(desc="Maximum AVR output (&gt; 0.)Maximum AVR output (&gt; 0.)")

    # Potential source gain (&gt; 0.)Potential source gain (&gt; 0.)
    kp = Float(desc="Potential source gain (&gt; 0.)Potential source gain (&gt; 0.)")

    # Inner loop forward gain (&gt; 0.)Inner loop forward gain (&gt; 0.)
    km = Float(desc="Inner loop forward gain (&gt; 0.)Inner loop forward gain (&gt; 0.)")

    # Maximum error (&gt; 0.)Maximum error (&gt; 0.)
    vimax = Float(desc="Maximum error (&gt; 0.)Maximum error (&gt; 0.)")

    # Voltage transducer time constant (&gt;= 0.)Voltage transducer time constant (&gt;= 0.)
    tr = Seconds(desc="Voltage transducer time constant (&gt;= 0.)Voltage transducer time constant (&gt;= 0.)")

    # Maximum inner loop output (&gt; 0.)Maximum inner loop output (&gt; 0.)
    vmmax = Float(desc="Maximum inner loop output (&gt; 0.)Maximum inner loop output (&gt; 0.)")

    # Current source gain (&gt;= 0.)Current source gain (&gt;= 0.)
    ki = Float(desc="Current source gain (&gt;= 0.)Current source gain (&gt;= 0.)")

    # Inner loop time constant (&gt; 0.)Inner loop time constant (&gt; 0.)
    tm = Seconds(desc="Inner loop time constant (&gt; 0.)Inner loop time constant (&gt; 0.)")

    # AVR time constant (&gt;= 0.)AVR time constant (&gt;= 0.)
    ta = Seconds(desc="AVR time constant (&gt;= 0.)AVR time constant (&gt;= 0.)")

    # AVR lag time constant (&gt;= 0.)AVR lag time constant (&gt;= 0.)
    tb = Seconds(desc="AVR lag time constant (&gt;= 0.)AVR lag time constant (&gt;= 0.)")

    # Inner loop feedback gain (&gt;= 0.)Inner loop feedback gain (&gt;= 0.)
    kg = Float(desc="Inner loop feedback gain (&gt;= 0.)Inner loop feedback gain (&gt;= 0.)")

    # AVR lead time constantAVR lead time constant
    tc = Seconds(desc="AVR lead time constantAVR lead time constant")

    #--------------------------------------------------------------------------
    #  Begin "ExcST3A" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "vrmin", "kc", "ka", "vbmax", "vimin", "xl", "vgmax", "angp", "vmmin", "vrmax", "kp", "km", "vimax", "tr", "vmmax", "ki", "tm", "ta", "tb", "kg", "tc",
                label="Attributes", columns=1),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.ExcitationSystems.ExcST3A",
        title="ExcST3A",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ExcST3A" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ExcCZ" class:
#------------------------------------------------------------------------------

class ExcCZ(ExcitationSystem):
    """ Czech proportional/integral excitation system model.Czech proportional/integral excitation system model.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "ExcCZ" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.ExcitationSystems.ExcCZ",
        title="ExcCZ",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ExcCZ" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
