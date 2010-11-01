# Copyright (C) 2010 Richard Lincoln
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA, USA


from dynamics import Element

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim"

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#Package_ExcitationSystems"

class ExcitationSystem(Element):
    """ An excitation system provides the field voltage (Efd) for a synchronous machine model. It is linked to a specific generator by the Bus number and Unit ID.
    """
    pass
    # <<< excitation_system
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'ExcitationSystem' instance.

        """


        super(ExcitationSystem, self).__init__(*args, **kw_args)
    # >>> excitation_system



class ExcBAS(ExcitationSystem):
    """ Basler static voltage regulator feeding dc or ac rotating exciter model
    """
    pass
    # <<< exc_bas
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'ExcBAS' instance.

        """


        super(ExcBAS, self).__init__(*args, **kw_args)
    # >>> exc_bas



class ExcDC2A(ExcitationSystem):
    """ IEEE (1992/2005) DC2A Model  The model is used to represent field-controlled dc commutator exciters with continuously acting voltage regulators having supplies obtained from the generator or auxiliary bus. It differs from the Type DC1A model only in the voltage regulator output limits, which are now proportional to terminal voltage <i>V</i><i><sub>T</sub></i>. It is representative of solid-state replacements for various forms of older mechanical and rotating amplifier regulating equipment connected to dc commutator exciters.
    """
    # <<< exc_dc2_a
    # @generated
    def __init__(self, te=0.0, tf=0.0, ka=0.0, tc=0.0, vrmin=0.0, ta=0.0, tb=0.0, vrmax=0.0, kf=0.0, ke=0.0, uelin=0.0, se1=0.0, tr=0.0, se2=0.0, exclim=0.0, e2=0.0, e1=0.0, *args, **kw_args):
        """ Initialises a new 'ExcDC2A' instance.

        @param te: Exciter time constant (&gt; 0.) 
        @param tf: Rate feedback time constant, sec. (&gt; 0.) 
        @param ka: Gain (&gt; 0.) 
        @param tc: Lead time constant 
        @param vrmin: Minimum controller output (&lt; 0.) 
        @param ta: Time constant (&gt; 0.) 
        @param tb: Lag time constant (&gt;= 0.) 
        @param vrmax: Maximum controller output 
        @param kf: Rate feedback gain (&gt;= 0.) 
        @param ke: Exciter field resistance line slope 
        @param uelin: UEL input: if &lt; 2, HV gate; if = 2, add to error signal 
        @param se1: Saturation factor at e1  (&gt;= 0.) 
        @param tr: Filter time constant (&gt;= 0.) 
        @param se2: Saturation factor at e2  (&gt;= 0.) 
        @param exclim: If not 0, apply lower limit of 0. to exciter output 
        @param e2: Field voltage value 2.    (&gt; 0.) 
        @param e1: Field voltage value 1     (&gt; 0.) 
        """
        # Exciter time constant (&gt; 0.) 
        self.te = te

        # Rate feedback time constant, sec. (&gt; 0.) 
        self.tf = tf

        # Gain (&gt; 0.) 
        self.ka = ka

        # Lead time constant 
        self.tc = tc

        # Minimum controller output (&lt; 0.) 
        self.vrmin = vrmin

        # Time constant (&gt; 0.) 
        self.ta = ta

        # Lag time constant (&gt;= 0.) 
        self.tb = tb

        # Maximum controller output 
        self.vrmax = vrmax

        # Rate feedback gain (&gt;= 0.) 
        self.kf = kf

        # Exciter field resistance line slope 
        self.ke = ke

        # UEL input: if &lt; 2, HV gate; if = 2, add to error signal 
        self.uelin = uelin

        # Saturation factor at e1  (&gt;= 0.) 
        self.se1 = se1

        # Filter time constant (&gt;= 0.) 
        self.tr = tr

        # Saturation factor at e2  (&gt;= 0.) 
        self.se2 = se2

        # If not 0, apply lower limit of 0. to exciter output 
        self.exclim = exclim

        # Field voltage value 2.    (&gt; 0.) 
        self.e2 = e2

        # Field voltage value 1     (&gt; 0.) 
        self.e1 = e1



        super(ExcDC2A, self).__init__(*args, **kw_args)
    # >>> exc_dc2_a



class ExcSEXS(ExcitationSystem):
    """ Simplified Excitation System Model
    """
    # <<< exc_sexs
    # @generated
    def __init__(self, k=0.0, tatb=0.0, efdmin=0.0, te=0.0, tc=0.0, kc=0.0, tb=0.0, emin=0.0, emax=0.0, efdmax=0.0, *args, **kw_args):
        """ Initialises a new 'ExcSEXS' instance.

        @param k: Gain (&gt; 0.) 
        @param tatb: Ta/Tb - gain reduction ratio of lag-lead element 
        @param efdmin: Field voltage clipping minimum limit 
        @param te: Time constant of gain block (&gt; 0.) 
        @param tc: PI controller phase lead time constant 
        @param kc: PI controller gain (&gt; 0. if Tc &gt; 0.) 
        @param tb: Denominator time constant of lag-lead block 
        @param emin: Minimum field voltage output 
        @param emax: Maximum field voltage output 
        @param efdmax: Field voltage clipping maximum limit 
        """
        # Gain (&gt; 0.) 
        self.k = k

        # Ta/Tb - gain reduction ratio of lag-lead element 
        self.tatb = tatb

        # Field voltage clipping minimum limit 
        self.efdmin = efdmin

        # Time constant of gain block (&gt; 0.) 
        self.te = te

        # PI controller phase lead time constant 
        self.tc = tc

        # PI controller gain (&gt; 0. if Tc &gt; 0.) 
        self.kc = kc

        # Denominator time constant of lag-lead block 
        self.tb = tb

        # Minimum field voltage output 
        self.emin = emin

        # Maximum field voltage output 
        self.emax = emax

        # Field voltage clipping maximum limit 
        self.efdmax = efdmax



        super(ExcSEXS, self).__init__(*args, **kw_args)
    # >>> exc_sexs



class ExcELIN2(ExcitationSystem):
    """ Detailed Excitation System Model - ELIN (VATECH)
    """
    pass
    # <<< exc_elin2
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'ExcELIN2' instance.

        """


        super(ExcELIN2, self).__init__(*args, **kw_args)
    # >>> exc_elin2



class ExcAC4A(ExcitationSystem):
    """ IEEE (1992/2005) AC4A Model  The Type AC4A alternator-supplied controlled-rectifier excitation system is quite different from the other type ac systems. This high initial response excitation system utilizes a full thyristor bridge in the exciter output circuit. The voltage regulator controls the firing of the thyristor bridges. The exciter alternator uses an independent voltage regulator to control its output voltage to a constant value. These effects are not modeled; however, transient loading effects on the exciter alternator are included.
    """
    # <<< exc_ac4_a
    # @generated
    def __init__(self, tb=0.0, ta=0.0, tc=0.0, vrmin=0.0, vimax=0.0, vrmax=0.0, tr=0.0, kc=0.0, vimin=0.0, ka=0.0, *args, **kw_args):
        """ Initialises a new 'ExcAC4A' instance.

        @param tb: Lag time constant (&gt;= 0.) 
        @param ta: Time constant (&gt; 0.) 
        @param tc: Lead time constant 
        @param vrmin: Minimum controller output (&lt; 0.) 
        @param vimax: Maximum error signal ( &gt; 0.) 
        @param vrmax: Maximum controller output (&gt; 0.) 
        @param tr: Filter time constant (&gt;= 0.) 
        @param kc: Excitation system regulation (&gt;= 0.) 
        @param vimin: Minimum error signal (&lt; 0.) 
        @param ka: Gain (&gt; 0.) 
        """
        # Lag time constant (&gt;= 0.) 
        self.tb = tb

        # Time constant (&gt; 0.) 
        self.ta = ta

        # Lead time constant 
        self.tc = tc

        # Minimum controller output (&lt; 0.) 
        self.vrmin = vrmin

        # Maximum error signal ( &gt; 0.) 
        self.vimax = vimax

        # Maximum controller output (&gt; 0.) 
        self.vrmax = vrmax

        # Filter time constant (&gt;= 0.) 
        self.tr = tr

        # Excitation system regulation (&gt;= 0.) 
        self.kc = kc

        # Minimum error signal (&lt; 0.) 
        self.vimin = vimin

        # Gain (&gt; 0.) 
        self.ka = ka



        super(ExcAC4A, self).__init__(*args, **kw_args)
    # >>> exc_ac4_a



class ExcSK(ExcitationSystem):
    """ Slovakian Excitation System Model (UEL, secondary voltage control)
    """
    pass
    # <<< exc_sk
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'ExcSK' instance.

        """


        super(ExcSK, self).__init__(*args, **kw_args)
    # >>> exc_sk



class ExcAC2A(ExcitationSystem):
    """ IEEE (1992/2005) AC2A Model The model designated as Type AC2A, represents a high initial response fieldcontrolled alternator-rectifier excitation system. The alternator main exciter is used with non-controlled rectifiers. The Type AC2A model is similar to that of Type AC1A except for the inclusion of exciter time constant compensation and exciter field current limiting elements.
    """
    # <<< exc_ac2_a
    # @generated
    def __init__(self, tb=0.0, e1=0.0, ta=0.0, vrmin=0.0, e2=0.0, vfemax=0.0, vrmax=0.0, ka=0.0, se1=0.0, se2=0.0, kf=0.0, kh=0.0, kc=0.0, vamin=0.0, kb=0.0, ke=0.0, tr=0.0, kd=0.0, te=0.0, tc=0.0, vamax=0.0, tf=0.0, *args, **kw_args):
        """ Initialises a new 'ExcAC2A' instance.

        @param tb: TGR lag time constant (&gt;= 0.) 
        @param e1: Field voltage value 1     (&gt; 0.) 
        @param ta: AVR time constant (&gt; 0.) 
        @param vrmin: Minimum exciter control signal (&lt; 0.) 
        @param e2: Field voltage value 2.    (&gt; 0.) 
        @param vfemax: Exciter field current limit parameter (&gt;= 0.) 
        @param vrmax: Maximum exciter control signal (&gt; 0.) 
        @param ka: AVR gain (&gt; 0.) 
        @param se1: Saturation factor at e1  (&gt;= 0.) 
        @param se2: Saturation factor at e2   (&gt;= 0.) 
        @param kf: Rate feedback gain (&gt;= 0.) 
        @param kh: Exciter field current feedback gain (&gt;= 0.) 
        @param kc: Rectifier regulation factor (&gt;= 0.) 
        @param vamin: Minimum AVR output (&lt; 0.) 
        @param kb: Exciter field current controller gain (&gt; 0.) 
        @param ke: Exciter field resistance constant 
        @param tr: Filter time constant (&gt;= 0.) 
        @param kd: Exciter internal reactance (&gt;= 0.) 
        @param te: Exciter time constant (&gt; 0.) 
        @param tc: TGR lead time constant 
        @param vamax: Maximum AVR output (&gt; 0.) 
        @param tf: Rate feedback time constant (&gt; 0.) 
        """
        # TGR lag time constant (&gt;= 0.) 
        self.tb = tb

        # Field voltage value 1     (&gt; 0.) 
        self.e1 = e1

        # AVR time constant (&gt; 0.) 
        self.ta = ta

        # Minimum exciter control signal (&lt; 0.) 
        self.vrmin = vrmin

        # Field voltage value 2.    (&gt; 0.) 
        self.e2 = e2

        # Exciter field current limit parameter (&gt;= 0.) 
        self.vfemax = vfemax

        # Maximum exciter control signal (&gt; 0.) 
        self.vrmax = vrmax

        # AVR gain (&gt; 0.) 
        self.ka = ka

        # Saturation factor at e1  (&gt;= 0.) 
        self.se1 = se1

        # Saturation factor at e2   (&gt;= 0.) 
        self.se2 = se2

        # Rate feedback gain (&gt;= 0.) 
        self.kf = kf

        # Exciter field current feedback gain (&gt;= 0.) 
        self.kh = kh

        # Rectifier regulation factor (&gt;= 0.) 
        self.kc = kc

        # Minimum AVR output (&lt; 0.) 
        self.vamin = vamin

        # Exciter field current controller gain (&gt; 0.) 
        self.kb = kb

        # Exciter field resistance constant 
        self.ke = ke

        # Filter time constant (&gt;= 0.) 
        self.tr = tr

        # Exciter internal reactance (&gt;= 0.) 
        self.kd = kd

        # Exciter time constant (&gt; 0.) 
        self.te = te

        # TGR lead time constant 
        self.tc = tc

        # Maximum AVR output (&gt; 0.) 
        self.vamax = vamax

        # Rate feedback time constant (&gt; 0.) 
        self.tf = tf



        super(ExcAC2A, self).__init__(*args, **kw_args)
    # >>> exc_ac2_a



class ExcELIN1(ExcitationSystem):
    """ Simplified Excitation System Model - ELIN (VATECH)
    """
    pass
    # <<< exc_elin1
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'ExcELIN1' instance.

        """


        super(ExcELIN1, self).__init__(*args, **kw_args)
    # >>> exc_elin1



class ExcST6B(ExcitationSystem):
    """ IEEE (2005) ST6B Model  The AVR consists of a PI voltage regulator with an inner loop field voltage regulator and pre-control. The field voltage regulator implements a proportional control. The pre-control and the delay in the feedback circuit increase the dynamic response.
    """
    # <<< exc_st6_b
    # @generated
    def __init__(self, vamin=0.0, vrmin=0.0, km=0.0, ts=0.0, kg=0.0, tr=0.0, kcl=0.0, klr=0.0, vrmax=0.0, ilr=0.0, kpa=0.0, tg=0.0, vamax=0.0, oelin=0.0, kff=0.0, vmult=0.0, kia=0.0, *args, **kw_args):
        """ Initialises a new 'ExcST6B' instance.

        @param vamin: PI minimum output (&lt; 0.) 
        @param vrmin: Minimum regulator output (&lt; 0.) 
        @param km: Main gain 
        @param ts: Rectifier firing time constant (not in IEEE model) (&gt;= 0.) 
        @param kg: Feedback gain (&gt;= 0.) 
        @param tr: Filter time constant (&gt;= 0.) 
        @param kcl: Field current limiter conversion factor (&gt; 0.) 
        @param klr: Field current limiter gain (&gt; 0.) 
        @param vrmax: Maximum regulator output (&gt; 0.) 
        @param ilr: Field current limiter setpoint (&gt; 0.) 
        @param kpa: Regulator proportional gain (&gt; 0.) 
        @param tg: Feedback time constant (&gt;= 0.) 
        @param vamax: PI maximum output. (&gt; 0.) 
        @param oelin: OEL input selector: 1 ? before UEL, 2 ? after UEL, 0 ? no OEL input 
        @param kff: Feedforward gain 
        @param vmult: If non-zero, multiply regulator output by terminal voltage 
        @param kia: Regulator integral gain (&gt; 0.) 
        """
        # PI minimum output (&lt; 0.) 
        self.vamin = vamin

        # Minimum regulator output (&lt; 0.) 
        self.vrmin = vrmin

        # Main gain 
        self.km = km

        # Rectifier firing time constant (not in IEEE model) (&gt;= 0.) 
        self.ts = ts

        # Feedback gain (&gt;= 0.) 
        self.kg = kg

        # Filter time constant (&gt;= 0.) 
        self.tr = tr

        # Field current limiter conversion factor (&gt; 0.) 
        self.kcl = kcl

        # Field current limiter gain (&gt; 0.) 
        self.klr = klr

        # Maximum regulator output (&gt; 0.) 
        self.vrmax = vrmax

        # Field current limiter setpoint (&gt; 0.) 
        self.ilr = ilr

        # Regulator proportional gain (&gt; 0.) 
        self.kpa = kpa

        # Feedback time constant (&gt;= 0.) 
        self.tg = tg

        # PI maximum output. (&gt; 0.) 
        self.vamax = vamax

        # OEL input selector: 1 ? before UEL, 2 ? after UEL, 0 ? no OEL input 
        self.oelin = oelin

        # Feedforward gain 
        self.kff = kff

        # If non-zero, multiply regulator output by terminal voltage 
        self.vmult = vmult

        # Regulator integral gain (&gt; 0.) 
        self.kia = kia



        super(ExcST6B, self).__init__(*args, **kw_args)
    # >>> exc_st6_b



class ExcST4B(ExcitationSystem):
    """ IEEE (2005) ST4B Model  This model is a variation of the Type ST3A model, with a proportional plus integral (PI) regulator block replacing the lag-lead regulator characteristic that was in the ST3A model. Both potential- and compoundsource rectifier excitation systems are modeled. The PI regulator blocks have nonwindup limits that are represented. The voltage regulator of this model is typically implemented digitally.
    """
    # <<< exc_st4_b
    # @generated
    def __init__(self, kp=0.0, xl=0.0, vbmax=0.0, ki=0.0, kir=0.0, vrmin=0.0, vmmin=0.0, kim=0.0, ta=0.0, kg=0.0, tr=0.0, kc=0.0, vrmax=0.0, angp=0.0, kpr=0.0, vgmax=0.0, kpm=0.0, vmmax=0.0, *args, **kw_args):
        """ Initialises a new 'ExcST4B' instance.

        @param kp: Potential source gain (&gt; 0.) 
        @param xl: P-bar leakage reactance (&gt;= 0.) 
        @param vbmax: Maximum excitation voltage (&gt; 0.) 
        @param ki: Current source gain (&gt;= 0.) 
        @param kir: AVR Integral gain 
        @param vrmin: Minimum AVR output (&lt; 0.) 
        @param vmmin: Minimum inner loop regulator output 
        @param kim: Integral gain of inner loop regulator 
        @param ta: AVR time constant (&gt;= 0.) 
        @param kg: Inner loop feedback gain (&gt;= 0.) 
        @param tr: Voltage transducer time constant (&gt;= 0.) 
        @param kc: Exciter regulation factor (&gt;= 0.) 
        @param vrmax: Maximum AVR output (&gt; 0.) 
        @param angp: Phase angle of potential source 
        @param kpr: AVR proportional gain 
        @param vgmax: Maximum inner loop feedback gain (&gt;= 0.) 
        @param kpm: Prop. gain of inner loop regulator 
        @param vmmax: Maximum inner loop regulator output 
        """
        # Potential source gain (&gt; 0.) 
        self.kp = kp

        # P-bar leakage reactance (&gt;= 0.) 
        self.xl = xl

        # Maximum excitation voltage (&gt; 0.) 
        self.vbmax = vbmax

        # Current source gain (&gt;= 0.) 
        self.ki = ki

        # AVR Integral gain 
        self.kir = kir

        # Minimum AVR output (&lt; 0.) 
        self.vrmin = vrmin

        # Minimum inner loop regulator output 
        self.vmmin = vmmin

        # Integral gain of inner loop regulator 
        self.kim = kim

        # AVR time constant (&gt;= 0.) 
        self.ta = ta

        # Inner loop feedback gain (&gt;= 0.) 
        self.kg = kg

        # Voltage transducer time constant (&gt;= 0.) 
        self.tr = tr

        # Exciter regulation factor (&gt;= 0.) 
        self.kc = kc

        # Maximum AVR output (&gt; 0.) 
        self.vrmax = vrmax

        # Phase angle of potential source 
        self.angp = angp

        # AVR proportional gain 
        self.kpr = kpr

        # Maximum inner loop feedback gain (&gt;= 0.) 
        self.vgmax = vgmax

        # Prop. gain of inner loop regulator 
        self.kpm = kpm

        # Maximum inner loop regulator output 
        self.vmmax = vmmax



        super(ExcST4B, self).__init__(*args, **kw_args)
    # >>> exc_st4_b



class ExcWT3E(ExcitationSystem):
    """ Type 3 standard wind turbine converter control model
    """
    pass
    # <<< exc_wt3_e
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'ExcWT3E' instance.

        """


        super(ExcWT3E, self).__init__(*args, **kw_args)
    # >>> exc_wt3_e



class ExcPIC(ExcitationSystem):
    """ Excitation System Model with PI voltage regulator
    """
    pass
    # <<< exc_pic
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'ExcPIC' instance.

        """


        super(ExcPIC, self).__init__(*args, **kw_args)
    # >>> exc_pic



class ExcSK2(ExcitationSystem):
    """ Slovakian alternator-rectifier Excitation System Model (UEL, secondary voltage control)
    """
    pass
    # <<< exc_sk2
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'ExcSK2' instance.

        """


        super(ExcSK2, self).__init__(*args, **kw_args)
    # >>> exc_sk2



class ExcST2A(ExcitationSystem):
    """ IEEE (1992/2005) ST2A Model  Some static systems utilize both current and voltage sources (generator terminal quantities) to comprise the power source. These compound-source rectifier excitation systems are designated Type ST2A. The regulator controls the exciter output through controlled saturation of the power transformer components.
    """
    # <<< exc_st2_a
    # @generated
    def __init__(self, vrmin=0.0, tc=0.0, tb=0.0, ta=0.0, ka=0.0, ke=0.0, uelin=0.0, kc=0.0, te=0.0, ki=0.0, kf=0.0, tf=0.0, vrmax=0.0, efdmax=0.0, tr=0.0, kp=0.0, *args, **kw_args):
        """ Initialises a new 'ExcST2A' instance.

        @param vrmin: Minimum controller output (&lt; 0.) 
        @param tc: Time constant 
        @param tb: Time constant (&gt;=0.) 
        @param ta: Time constant (&gt; 0.) 
        @param ka: Gain (&gt; 0.) 
        @param ke: Time constant feedback 
        @param uelin: UEL input: if = 1, HV gate; if = 2, add to error signal 
        @param kc: Rectifier loading factor (&gt;= 0.) 
        @param te: Transformer saturation control time constant (&gt; 0.) 
        @param ki: Current source gain (&gt;= 0.) 
        @param kf: Rate feedback gain (&gt;= 0.) 
        @param tf: Rate feedback time constant (&gt;= 0.) 
        @param vrmax: Maximum controller output (&gt; 0.) 
        @param efdmax: Maximum field voltage (&gt;=0.) 
        @param tr: Filter time constant (&gt;= 0.) 
        @param kp: Potential source gain (&gt;= 0.) 
        """
        # Minimum controller output (&lt; 0.) 
        self.vrmin = vrmin

        # Time constant 
        self.tc = tc

        # Time constant (&gt;=0.) 
        self.tb = tb

        # Time constant (&gt; 0.) 
        self.ta = ta

        # Gain (&gt; 0.) 
        self.ka = ka

        # Time constant feedback 
        self.ke = ke

        # UEL input: if = 1, HV gate; if = 2, add to error signal 
        self.uelin = uelin

        # Rectifier loading factor (&gt;= 0.) 
        self.kc = kc

        # Transformer saturation control time constant (&gt; 0.) 
        self.te = te

        # Current source gain (&gt;= 0.) 
        self.ki = ki

        # Rate feedback gain (&gt;= 0.) 
        self.kf = kf

        # Rate feedback time constant (&gt;= 0.) 
        self.tf = tf

        # Maximum controller output (&gt; 0.) 
        self.vrmax = vrmax

        # Maximum field voltage (&gt;=0.) 
        self.efdmax = efdmax

        # Filter time constant (&gt;= 0.) 
        self.tr = tr

        # Potential source gain (&gt;= 0.) 
        self.kp = kp



        super(ExcST2A, self).__init__(*args, **kw_args)
    # >>> exc_st2_a



class ExcHU(ExcitationSystem):
    """ Hungarian Excitation System Model
    """
    pass
    # <<< exc_hu
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'ExcHU' instance.

        """


        super(ExcHU, self).__init__(*args, **kw_args)
    # >>> exc_hu



class ExcREXS(ExcitationSystem):
    """ General Purpose Rotating Excitation System Model
    """
    pass
    # <<< exc_rexs
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'ExcREXS' instance.

        """


        super(ExcREXS, self).__init__(*args, **kw_args)
    # >>> exc_rexs



class ExcST7B(ExcitationSystem):
    """ IEEE (2005) ST7B Model  The model ST7B is representative of static potential-source excitation systems. In this system, the AVR consists of a PI voltage regulator. A phase lead-lag filter in series allows introduction of a derivative function, typically used with brushless excitation systems. In that case, the regulator is of the PID type. In addition, the terminal voltage channel includes a phase lead-lag filter. The AVR includes the appropriate inputs on its reference for overexcitation limiter (OEL1), underexcitation limiter (UEL), stator current limiter (SCL), and current compensator (DROOP). All these limitations, when they work at voltage reference level, keep the PSS (VS signal from Type PSS1A, PSS2A, or PSS2B) in operation. However, the UEL limitation can also be transferred to the high value (HV) gate acting on the output signal. In addition, the output signal passes through a low value (LV) gate for a ceiling overexcitation limiter (OEL2).
    """
    # <<< exc_st7_b
    # @generated
    def __init__(self, tg=0.0, kpa=0.0, vmin=0.0, vrmax=0.0, kl=0.0, tr=0.0, kh=0.0, ts=0.0, vrmin=0.0, oelin=0.0, uelin=0.0, tia=0.0, tb=0.0, tc=0.0, tf=0.0, kia=0.0, vmax=0.0, *args, **kw_args):
        """ Initialises a new 'ExcST7B' instance.

        @param tg: Input lead-lag numerator time constant (&gt;= 0.) 
        @param kpa: Regulator proportional gain (&gt; 0.) 
        @param vmin: Minimum voltage reference signal (&gt; 0.) 
        @param vrmax: Maximum field voltage output (&gt; 0.) 
        @param kl: Low-value gate feedback gain (&gt;= 0.) 
        @param tr: Filter time constant 
        @param kh: High-value gate feedback gain (&gt;= 0.) 
        @param ts: Rectifier firing time constant (&gt;= 0.) (not in IEEE model) 
        @param vrmin: Minimum field voltage output (&lt; 0.) 
        @param oelin: OEL input selector: 1 ? add to Vref, 2 ? input LV gate,  2 ? output LV gate, 0 ? no OEL input 
        @param uelin: UEL input selector: 1 ? add to Vref, 2 ? input HV gate,  3 ? output HV gate, 0 ? no UEL input 
        @param tia: Feedback time constant (&gt;= 0.) 
        @param tb: Lead-lag denominator time constant (&gt;= 0.) 
        @param tc: Lead-lag numerator time constant (&gt;= 0.) 
        @param tf: Input lead-lag denominator time constant (&gt;= 0.) 
        @param kia: Feedback gain (&gt;= 0.) 
        @param vmax: Maximum voltage reference signal (&gt; 0.) 
        """
        # Input lead-lag numerator time constant (&gt;= 0.) 
        self.tg = tg

        # Regulator proportional gain (&gt; 0.) 
        self.kpa = kpa

        # Minimum voltage reference signal (&gt; 0.) 
        self.vmin = vmin

        # Maximum field voltage output (&gt; 0.) 
        self.vrmax = vrmax

        # Low-value gate feedback gain (&gt;= 0.) 
        self.kl = kl

        # Filter time constant 
        self.tr = tr

        # High-value gate feedback gain (&gt;= 0.) 
        self.kh = kh

        # Rectifier firing time constant (&gt;= 0.) (not in IEEE model) 
        self.ts = ts

        # Minimum field voltage output (&lt; 0.) 
        self.vrmin = vrmin

        # OEL input selector: 1 ? add to Vref, 2 ? input LV gate,  2 ? output LV gate, 0 ? no OEL input 
        self.oelin = oelin

        # UEL input selector: 1 ? add to Vref, 2 ? input HV gate,  3 ? output HV gate, 0 ? no UEL input 
        self.uelin = uelin

        # Feedback time constant (&gt;= 0.) 
        self.tia = tia

        # Lead-lag denominator time constant (&gt;= 0.) 
        self.tb = tb

        # Lead-lag numerator time constant (&gt;= 0.) 
        self.tc = tc

        # Input lead-lag denominator time constant (&gt;= 0.) 
        self.tf = tf

        # Feedback gain (&gt;= 0.) 
        self.kia = kia

        # Maximum voltage reference signal (&gt; 0.) 
        self.vmax = vmax



        super(ExcST7B, self).__init__(*args, **kw_args)
    # >>> exc_st7_b



class ExcAC1A(ExcitationSystem):
    """ IEEE (1992/2005) AC1A Model The model represents the field-controlled alternator-rectifier excitation systems designated Type AC1A. These excitation systems consist of an alternator main exciter with non-controlled rectifiers.
    """
    # <<< exc_ac1_a
    # @generated
    def __init__(self, se1=0.0, se2=0.0, e2=0.0, e1=0.0, tr=0.0, vamin=0.0, vamax=0.0, vrmax=0.0, tb=0.0, kd=0.0, tc=0.0, kc=0.0, kf=0.0, ta=0.0, vrmin=0.0, ke=0.0, te=0.0, tf=0.0, ka=0.0, *args, **kw_args):
        """ Initialises a new 'ExcAC1A' instance.

        @param se1: Saturation factor at e1  (&gt;= 0.) 
        @param se2: Saturation factor at e2   (&gt;= 0.) 
        @param e2: Field voltage value 2.   (&gt; 0.) 
        @param e1: Field voltage value 1    (&gt; 0.) 
        @param tr: Filter time constant (&gt;= 0.) 
        @param vamin: Minimum AVR output (&lt; 0.) 
        @param vamax: Maximum AVR output (&gt; 0.) 
        @param vrmax: Maximum exciter control signal (&gt; 0.) 
        @param tb: TGR lag time constant (&gt;= 0.) 
        @param kd: Exciter internal reactance  (&gt;= 0.) 
        @param tc: TGR lead time constant 
        @param kc: Rectifier regulation factor (&gt;= 0.) 
        @param kf: Rate feedback gain (&gt;= 0.) 
        @param ta: AVR time constant (&gt; 0.) 
        @param vrmin: Minimum exciter control signal  (&lt; 0.) 
        @param ke: Exciter field resistance constant 
        @param te: Exciter time constant (&gt; 0.) 
        @param tf: Rate feedback time constant (&gt; 0.) 
        @param ka: AVR gain (&gt; 0.) 
        """
        # Saturation factor at e1  (&gt;= 0.) 
        self.se1 = se1

        # Saturation factor at e2   (&gt;= 0.) 
        self.se2 = se2

        # Field voltage value 2.   (&gt; 0.) 
        self.e2 = e2

        # Field voltage value 1    (&gt; 0.) 
        self.e1 = e1

        # Filter time constant (&gt;= 0.) 
        self.tr = tr

        # Minimum AVR output (&lt; 0.) 
        self.vamin = vamin

        # Maximum AVR output (&gt; 0.) 
        self.vamax = vamax

        # Maximum exciter control signal (&gt; 0.) 
        self.vrmax = vrmax

        # TGR lag time constant (&gt;= 0.) 
        self.tb = tb

        # Exciter internal reactance  (&gt;= 0.) 
        self.kd = kd

        # TGR lead time constant 
        self.tc = tc

        # Rectifier regulation factor (&gt;= 0.) 
        self.kc = kc

        # Rate feedback gain (&gt;= 0.) 
        self.kf = kf

        # AVR time constant (&gt; 0.) 
        self.ta = ta

        # Minimum exciter control signal  (&lt; 0.) 
        self.vrmin = vrmin

        # Exciter field resistance constant 
        self.ke = ke

        # Exciter time constant (&gt; 0.) 
        self.te = te

        # Rate feedback time constant (&gt; 0.) 
        self.tf = tf

        # AVR gain (&gt; 0.) 
        self.ka = ka



        super(ExcAC1A, self).__init__(*args, **kw_args)
    # >>> exc_ac1_a



class ExcDC4B(ExcitationSystem):
    """ IEEE (2005) DC4B Model  These excitation systems utilize a field-controlled dc commutator exciter with a continuously acting voltage regulator having supplies obtained from the generator or auxiliary bus. The replacement of the controls only as an upgrade (retaining the dc commutator exciter) has resulted in a new model. This excitation system typically includes a proportional, integral, and differential (PID) generator voltage regulator (AVR). An alternative rate feedback loop (<i>kf</i>, <i>tf</i>) for stabilization is also shown in the model if the AVR does not include a derivative term. If a PSS control is supplied, the appropriate model is the Type PSS2B model.
    """
    # <<< exc_dc4_b
    # @generated
    def __init__(self, vrmin=0.0, uelin=0.0, ki=0.0, kp=0.0, e2=0.0, oelin=0.0, vrmax=0.0, kf=0.0, te=0.0, ke=0.0, vemin=0.0, tf=0.0, kd=0.0, se2=0.0, ta=0.0, tr=0.0, ka=0.0, se1=0.0, td=0.0, e1=0.0, *args, **kw_args):
        """ Initialises a new 'ExcDC4B' instance.

        @param vrmin: Minimum controller output (&lt;= 0.) 
        @param uelin: UEL input: if &lt; 2, HV gate; if = 2, add to error signal 
        @param ki: Integral gain (&gt;= 0.) 
        @param kp: Proportional gain (&gt;= 0.) 
        @param e2: Field voltage value 2.   (&gt; 0.) 
        @param oelin: OEL input: if &lt; 2, LV gate; if = 2, subtract from error signal 
        @param vrmax: Maximum controller output 
        @param kf: Rate feedback gain (&gt;= 0.) 
        @param te: Exciter time constant (&gt; 0.) 
        @param ke: Exciter field resistance line slope 
        @param vemin: Exciter minimum output  (&lt;= 0.) 
        @param tf: Rate feedback time constant (&gt;= 0.) 
        @param kd: Derivative gain (&gt;= 0.) 
        @param se2: Saturation factor at e2 (&gt;= 0.) 
        @param ta: Time constant (&gt; 0.) 
        @param tr: Filter time constant (&gt;= 0.) 
        @param ka: Gain (&gt; 0.) 
        @param se1: Saturation factor at e1   (&gt;= 0.) 
        @param td: Derivative time constant (&gt; 0. If kd &gt; 0.) 
        @param e1: Field voltage value 1     (&gt; 0.) 
        """
        # Minimum controller output (&lt;= 0.) 
        self.vrmin = vrmin

        # UEL input: if &lt; 2, HV gate; if = 2, add to error signal 
        self.uelin = uelin

        # Integral gain (&gt;= 0.) 
        self.ki = ki

        # Proportional gain (&gt;= 0.) 
        self.kp = kp

        # Field voltage value 2.   (&gt; 0.) 
        self.e2 = e2

        # OEL input: if &lt; 2, LV gate; if = 2, subtract from error signal 
        self.oelin = oelin

        # Maximum controller output 
        self.vrmax = vrmax

        # Rate feedback gain (&gt;= 0.) 
        self.kf = kf

        # Exciter time constant (&gt; 0.) 
        self.te = te

        # Exciter field resistance line slope 
        self.ke = ke

        # Exciter minimum output  (&lt;= 0.) 
        self.vemin = vemin

        # Rate feedback time constant (&gt;= 0.) 
        self.tf = tf

        # Derivative gain (&gt;= 0.) 
        self.kd = kd

        # Saturation factor at e2 (&gt;= 0.) 
        self.se2 = se2

        # Time constant (&gt; 0.) 
        self.ta = ta

        # Filter time constant (&gt;= 0.) 
        self.tr = tr

        # Gain (&gt; 0.) 
        self.ka = ka

        # Saturation factor at e1   (&gt;= 0.) 
        self.se1 = se1

        # Derivative time constant (&gt; 0. If kd &gt; 0.) 
        self.td = td

        # Field voltage value 1     (&gt; 0.) 
        self.e1 = e1



        super(ExcDC4B, self).__init__(*args, **kw_args)
    # >>> exc_dc4_b



class ExcDC1A(ExcitationSystem):
    """ IEEE (1992/2005) DC1A Model  This model is used to represent field-controlled dc commutator exciters with continuously acting voltage regulators (especially the direct-acting rheostatic, rotating amplifier, and magnetic amplifier types). Because this model has been widely implemented by the industry, it is sometimes used to represent other types of systems when detailed data for them are not available or when a simplified model is required.
    """
    # <<< exc_dc1_a
    # @generated
    def __init__(self, exclim=0.0, vrmin=0.0, tc=0.0, ta=0.0, tb=0.0, ka=0.0, ke=0.0, se2=0.0, te=0.0, se1=0.0, tf=0.0, kf=0.0, uelin=0.0, tr=0.0, e1=0.0, vrmax=0.0, e2=0.0, *args, **kw_args):
        """ Initialises a new 'ExcDC1A' instance.

        @param exclim: If not 0, apply lower limit of 0. to exciter output 
        @param vrmin: Minimum controller output (&lt; 0.) 
        @param tc: Lead time constant 
        @param ta: Time constant (&gt; 0.) 
        @param tb: Lag time constant (&gt;= 0.) 
        @param ka: Gain (&gt; 0.) 
        @param ke: Exciter field resistance line slope 
        @param se2: Saturation factor at e2  (&gt;= 0.) 
        @param te: Exciter time constant (&gt; 0.) 
        @param se1: Saturation factor at e1  (&gt;= 0.) 
        @param tf: Rate feedback time constant, sec. (&gt; 0.) 
        @param kf: Rate feedback gain (&gt;= 0.) 
        @param uelin: UEL input: if &lt; 2, HV gate; if = 2, add to error signal 
        @param tr: Filter time constant (&gt;= 0.) 
        @param e1: Field voltage value 1    (&gt; 0.) 
        @param vrmax: Maximum controller output 
        @param e2: Field voltage value 2.   (&gt; 0.) 
        """
        # If not 0, apply lower limit of 0. to exciter output 
        self.exclim = exclim

        # Minimum controller output (&lt; 0.) 
        self.vrmin = vrmin

        # Lead time constant 
        self.tc = tc

        # Time constant (&gt; 0.) 
        self.ta = ta

        # Lag time constant (&gt;= 0.) 
        self.tb = tb

        # Gain (&gt; 0.) 
        self.ka = ka

        # Exciter field resistance line slope 
        self.ke = ke

        # Saturation factor at e2  (&gt;= 0.) 
        self.se2 = se2

        # Exciter time constant (&gt; 0.) 
        self.te = te

        # Saturation factor at e1  (&gt;= 0.) 
        self.se1 = se1

        # Rate feedback time constant, sec. (&gt; 0.) 
        self.tf = tf

        # Rate feedback gain (&gt;= 0.) 
        self.kf = kf

        # UEL input: if &lt; 2, HV gate; if = 2, add to error signal 
        self.uelin = uelin

        # Filter time constant (&gt;= 0.) 
        self.tr = tr

        # Field voltage value 1    (&gt; 0.) 
        self.e1 = e1

        # Maximum controller output 
        self.vrmax = vrmax

        # Field voltage value 2.   (&gt; 0.) 
        self.e2 = e2



        super(ExcDC1A, self).__init__(*args, **kw_args)
    # >>> exc_dc1_a



class ExcAC3A(ExcitationSystem):
    """ IEEE (1992/2005) AC3A Model  The model represents the field-controlled alternator-rectifier excitation systems designated Type AC3A. These excitation systems include an alternator main exciter with non-controlled rectifiers. The exciter employs self-excitation, and the voltage regulator power is derived from the exciter output voltage. Therefore, this system has an additional nonlinearity, simulated by the use of a multiplier whose inputs are the voltage regulator command signal, <i>VA</i>, and the exciter output voltage, <i>EFD</i>, times <i>KR</i>. This model is applicable to excitation systems employing static voltage regulators.
    """
    # <<< exc_ac3_a
    # @generated
    def __init__(self, ta=0.0, ka=0.0, kd=0.0, se1=0.0, kc=0.0, se2=0.0, te=0.0, tf=0.0, tb=0.0, tc=0.0, vamax=0.0, kf=0.0, vemin=0.0, ke=0.0, vfemax=0.0, tr=0.0, e2=0.0, e1=0.0, kn=0.0, vamin=0.0, kr=0.0, efdn=0.0, *args, **kw_args):
        """ Initialises a new 'ExcAC3A' instance.

        @param ta: AVR time constant (&gt; 0.) 
        @param ka: AVR gain (&gt; 0.) 
        @param kd: Exciter internal reactance (&gt;= 0.) 
        @param se1: Saturation factor at e1   (&gt;= 0.) 
        @param kc: Rectifier regulation factor (&gt;= 0.) 
        @param se2: Saturation factor at e2   (&gt;= 0.) 
        @param te: Exciter time constant (&gt; 0.) 
        @param tf: Rate feedback time constant (&gt; 0.) 
        @param tb: TGR lag time constant (&gt;= 0.) 
        @param tc: TGR lead time constant 
        @param vamax: Maximum AVR output (&gt; 0.) 
        @param kf: Low level rate feedback gain (&gt;= 0.) 
        @param vemin: Minimum field voltage limit (&lt;= 0.) 
        @param ke: Exciter field resistance constant 
        @param vfemax: Exciter field current limit parameter (&gt;= 0.) 
        @param tr: Filter time constant (&gt;= 0.) 
        @param e2: Field voltage value 2.     (&gt; 0.) 
        @param e1: Field voltage value 1     (&gt; 0.) 
        @param kn: High level rate feedback gain (&gt;= 0.) 
        @param vamin: Minimum AVR output (&lt; 0.) 
        @param kr: Field self-excitation feedback gain (&gt; 0.) 
        @param efdn: Rate feedback gain break level (&gt; 0.) 
        """
        # AVR time constant (&gt; 0.) 
        self.ta = ta

        # AVR gain (&gt; 0.) 
        self.ka = ka

        # Exciter internal reactance (&gt;= 0.) 
        self.kd = kd

        # Saturation factor at e1   (&gt;= 0.) 
        self.se1 = se1

        # Rectifier regulation factor (&gt;= 0.) 
        self.kc = kc

        # Saturation factor at e2   (&gt;= 0.) 
        self.se2 = se2

        # Exciter time constant (&gt; 0.) 
        self.te = te

        # Rate feedback time constant (&gt; 0.) 
        self.tf = tf

        # TGR lag time constant (&gt;= 0.) 
        self.tb = tb

        # TGR lead time constant 
        self.tc = tc

        # Maximum AVR output (&gt; 0.) 
        self.vamax = vamax

        # Low level rate feedback gain (&gt;= 0.) 
        self.kf = kf

        # Minimum field voltage limit (&lt;= 0.) 
        self.vemin = vemin

        # Exciter field resistance constant 
        self.ke = ke

        # Exciter field current limit parameter (&gt;= 0.) 
        self.vfemax = vfemax

        # Filter time constant (&gt;= 0.) 
        self.tr = tr

        # Field voltage value 2.     (&gt; 0.) 
        self.e2 = e2

        # Field voltage value 1     (&gt; 0.) 
        self.e1 = e1

        # High level rate feedback gain (&gt;= 0.) 
        self.kn = kn

        # Minimum AVR output (&lt; 0.) 
        self.vamin = vamin

        # Field self-excitation feedback gain (&gt; 0.) 
        self.kr = kr

        # Rate feedback gain break level (&gt; 0.) 
        self.efdn = efdn



        super(ExcAC3A, self).__init__(*args, **kw_args)
    # >>> exc_ac3_a



class ExcAC6A(ExcitationSystem):
    """ IEEE (1992/2005) AC6A Model  The model is used to represent field-controlled alternator-rectifier excitation systems with system-supplied electronic voltage regulators. The maximum output of the regulator, <i>V</i><i><sub>R</sub></i>, is a function of terminal voltage, <i>V</i><i><sub>T</sub></i>. The field current limiter included in the original model AC6A remains in the 2005 update.
    """
    # <<< exc_ac6_a
    # @generated
    def __init__(self, vamax=0.0, vfelim=0.0, tr=0.0, e2=0.0, e1=0.0, vamin=0.0, vhmax=0.0, vrmax=0.0, se1=0.0, se2=0.0, vrmin=0.0, te=0.0, kh=0.0, tb=0.0, tc=0.0, ta=0.0, ka=0.0, kc=0.0, tj=0.0, tk=0.0, ke=0.0, th=0.0, kd=0.0, *args, **kw_args):
        """ Initialises a new 'ExcAC6A' instance.

        @param vamax: Maximum controller element output (&gt; 0.) 
        @param vfelim: Exciter field current limit reference (&gt; 0.) 
        @param tr: Filter time constant 
        @param e2: Field voltage value 2.    (&gt; 0.) 
        @param e1: Field voltage value 1     (&gt; 0.) 
        @param vamin: Minimum controller element output (&lt; 0.) 
        @param vhmax: Maximum field current limiter signal (&gt; 0.) 
        @param vrmax: Maximum exciter control signal (&gt; 0.) 
        @param se1: Saturation factor at e1 (&gt;= 0.) 
        @param se2: Saturation factor at e2  (&gt;= 0.) 
        @param vrmin: Minimum exciter control signal (&lt; 0.) 
        @param te: Exciter time constant (&gt; 0.) 
        @param kh: Exciter field current limiter gain (&gt;= 0.) 
        @param tb: Time constant (&gt;= 0.) 
        @param tc: Lead time constant 
        @param ta: Time constant (&gt;= 0.) 
        @param ka: Gain (&gt; 0.) 
        @param kc: Rectifier regulation factor (&gt;= 0.) 
        @param tj: Field current limiter time constant (&gt;= 0.) 
        @param tk: Lag time constant (&gt;= 0.) 
        @param ke: Exciter field resistance constant 
        @param th: Field current limiter time constant (&gt; 0.) 
        @param kd: Exciter internal reactance (&gt;= 0.) 
        """
        # Maximum controller element output (&gt; 0.) 
        self.vamax = vamax

        # Exciter field current limit reference (&gt; 0.) 
        self.vfelim = vfelim

        # Filter time constant 
        self.tr = tr

        # Field voltage value 2.    (&gt; 0.) 
        self.e2 = e2

        # Field voltage value 1     (&gt; 0.) 
        self.e1 = e1

        # Minimum controller element output (&lt; 0.) 
        self.vamin = vamin

        # Maximum field current limiter signal (&gt; 0.) 
        self.vhmax = vhmax

        # Maximum exciter control signal (&gt; 0.) 
        self.vrmax = vrmax

        # Saturation factor at e1 (&gt;= 0.) 
        self.se1 = se1

        # Saturation factor at e2  (&gt;= 0.) 
        self.se2 = se2

        # Minimum exciter control signal (&lt; 0.) 
        self.vrmin = vrmin

        # Exciter time constant (&gt; 0.) 
        self.te = te

        # Exciter field current limiter gain (&gt;= 0.) 
        self.kh = kh

        # Time constant (&gt;= 0.) 
        self.tb = tb

        # Lead time constant 
        self.tc = tc

        # Time constant (&gt;= 0.) 
        self.ta = ta

        # Gain (&gt; 0.) 
        self.ka = ka

        # Rectifier regulation factor (&gt;= 0.) 
        self.kc = kc

        # Field current limiter time constant (&gt;= 0.) 
        self.tj = tj

        # Lag time constant (&gt;= 0.) 
        self.tk = tk

        # Exciter field resistance constant 
        self.ke = ke

        # Field current limiter time constant (&gt; 0.) 
        self.th = th

        # Exciter internal reactance (&gt;= 0.) 
        self.kd = kd



        super(ExcAC6A, self).__init__(*args, **kw_args)
    # >>> exc_ac6_a



class ExcAC5A(ExcitationSystem):
    """ IEEE (1992/2005) AC5A Model  The model designated as Type AC5A, is a simplified model for brushless excitation systems. The regulator is supplied from a source, such as a permanent magnet generator, which is not affected by system disturbances. Unlike other ac models, this model uses loaded rather than open circuit exciter saturation data in the same way as it is used for the dc models. Because the model has been widely implemented by the industry, it is sometimes used to represent other types of systems when either detailed data for them are not available or simplified models are required.
    """
    # <<< exc_ac5_a
    # @generated
    def __init__(self, ta=0.0, vrmax=0.0, ka=0.0, vrmin=0.0, tr=0.0, tf1=0.0, ke=0.0, tf2=0.0, te=0.0, kf=0.0, e1=0.0, e2=0.0, tf3=0.0, se1=0.0, se2=0.0, *args, **kw_args):
        """ Initialises a new 'ExcAC5A' instance.

        @param ta: Time constant (&gt; 0.) 
        @param vrmax: Maximum controller output (&gt; 0.) 
        @param ka: Gain  (&gt; 0.) 
        @param vrmin: Minimum controller output (&lt;  0.) 
        @param tr: Filter time constant (&gt;= 0.) 
        @param tf1: Rate feedback lag time constant (&gt; 0.) 
        @param ke: Exciter field resistance line slope 
        @param tf2: Rate feedback lag time constant (&gt;= 0.) 
        @param te: Exciter time constant, sec. (&gt; 0.) 
        @param kf: Rate feedback gain (&gt;= 0.) 
        @param e1: Field voltage value 1      (&gt; 0.) 
        @param e2: Field voltage value 2.  (&gt; 0.) 
        @param tf3: Rate feedback lead time constant 
        @param se1: Saturation factor at e1  (&gt;= 0.) 
        @param se2: Saturation factor at e2 (&gt;= 0.) 
        """
        # Time constant (&gt; 0.) 
        self.ta = ta

        # Maximum controller output (&gt; 0.) 
        self.vrmax = vrmax

        # Gain  (&gt; 0.) 
        self.ka = ka

        # Minimum controller output (&lt;  0.) 
        self.vrmin = vrmin

        # Filter time constant (&gt;= 0.) 
        self.tr = tr

        # Rate feedback lag time constant (&gt; 0.) 
        self.tf1 = tf1

        # Exciter field resistance line slope 
        self.ke = ke

        # Rate feedback lag time constant (&gt;= 0.) 
        self.tf2 = tf2

        # Exciter time constant, sec. (&gt; 0.) 
        self.te = te

        # Rate feedback gain (&gt;= 0.) 
        self.kf = kf

        # Field voltage value 1      (&gt; 0.) 
        self.e1 = e1

        # Field voltage value 2.  (&gt; 0.) 
        self.e2 = e2

        # Rate feedback lead time constant 
        self.tf3 = tf3

        # Saturation factor at e1  (&gt;= 0.) 
        self.se1 = se1

        # Saturation factor at e2 (&gt;= 0.) 
        self.se2 = se2



        super(ExcAC5A, self).__init__(*args, **kw_args)
    # >>> exc_ac5_a



class ExcST5B(ExcitationSystem):
    """ IEEE (2005) ST5B Model  The Type ST5B excitation system is a variation of the Type ST1A model, with alternative overexcitation and underexcitation inputs and additional limits. The corresponding stabilizer models that can be used with these models are the Type PSS2B, PSS3B, or PSS4B.
    """
    # <<< exc_st5_b
    # @generated
    def __init__(self, toc2=0.0, toc1=0.0, tc1=0.0, vrmin=0.0, tc2=0.0, kc=0.0, tb2=0.0, tob1=0.0, vrmax=0.0, tob2=0.0, tb1=0.0, tub1=0.0, tub2=0.0, tuc1=0.0, tuc2=0.0, kr=0.0, tr=0.0, t1=0.0, *args, **kw_args):
        """ Initialises a new 'ExcST5B' instance.

        @param toc2: OEL lead time constant 
        @param toc1: OEL lead time constant 
        @param tc1: Regulator lead time constant 
        @param vrmin: Minimum regulator output (&lt; 0.) 
        @param tc2: Regulator lead time constant. 
        @param kc: Rectifier regulation factor (&gt;= 0.) 
        @param tb2: Regulator lag time constant (&gt;= 0.) 
        @param tob1: OEL lag time constant (&gt;= 0.) 
        @param vrmax: Maximum regulator output (&gt; 0.) 
        @param tob2: OEL lag time constant (&gt;= 0.) 
        @param tb1: Regulator lag time constant (&gt;= 0.) 
        @param tub1: UEL lag time constant (&gt;= 0.) 
        @param tub2: UEL lag time constant (&gt;= 0.) 
        @param tuc1: UEL lead time constant. 
        @param tuc2: UEL lead time constant 
        @param kr: Regulator gain (&gt; 0.) 
        @param tr: Filter time constant (&gt;= 0.) 
        @param t1: Firing circuit time constant (&gt;= 0.) 
        """
        # OEL lead time constant 
        self.toc2 = toc2

        # OEL lead time constant 
        self.toc1 = toc1

        # Regulator lead time constant 
        self.tc1 = tc1

        # Minimum regulator output (&lt; 0.) 
        self.vrmin = vrmin

        # Regulator lead time constant. 
        self.tc2 = tc2

        # Rectifier regulation factor (&gt;= 0.) 
        self.kc = kc

        # Regulator lag time constant (&gt;= 0.) 
        self.tb2 = tb2

        # OEL lag time constant (&gt;= 0.) 
        self.tob1 = tob1

        # Maximum regulator output (&gt; 0.) 
        self.vrmax = vrmax

        # OEL lag time constant (&gt;= 0.) 
        self.tob2 = tob2

        # Regulator lag time constant (&gt;= 0.) 
        self.tb1 = tb1

        # UEL lag time constant (&gt;= 0.) 
        self.tub1 = tub1

        # UEL lag time constant (&gt;= 0.) 
        self.tub2 = tub2

        # UEL lead time constant. 
        self.tuc1 = tuc1

        # UEL lead time constant 
        self.tuc2 = tuc2

        # Regulator gain (&gt; 0.) 
        self.kr = kr

        # Filter time constant (&gt;= 0.) 
        self.tr = tr

        # Firing circuit time constant (&gt;= 0.) 
        self.t1 = t1



        super(ExcST5B, self).__init__(*args, **kw_args)
    # >>> exc_st5_b



class ExcSCRX(ExcitationSystem):
    """ Simple excitation system model representing generic characteristics of many excitation systems; intended for use where negative field current may be a problem
    """
    # <<< exc_scrx
    # @generated
    def __init__(self, te=0.0, tb=0.0, emax=0.0, cswitch=False, rcrfd=0.0, tatb=0.0, k=0.0, emin=0.0, *args, **kw_args):
        """ Initialises a new 'ExcSCRX' instance.

        @param te: Time constant of gain block (&gt; 0.) 
        @param tb: Denominator time constant of lag-lead block 
        @param emax: Maximum field voltage output 
        @param cswitch: Power source switch:     1 ? fixed voltage     0 ? generator terminal voltage 
        @param rcrfd: Rc/Rfd - ratio of field discharge resistance to field winding resistance 
        @param tatb: Ta/Tb - gain reduction ratio of lag-lead element 
        @param k: Gain (&gt; 0.) 
        @param emin: Minimum field voltage output 
        """
        # Time constant of gain block (&gt; 0.) 
        self.te = te

        # Denominator time constant of lag-lead block 
        self.tb = tb

        # Maximum field voltage output 
        self.emax = emax

        # Power source switch:     1 ? fixed voltage     0 ? generator terminal voltage 
        self.cswitch = cswitch

        # Rc/Rfd - ratio of field discharge resistance to field winding resistance 
        self.rcrfd = rcrfd

        # Ta/Tb - gain reduction ratio of lag-lead element 
        self.tatb = tatb

        # Gain (&gt; 0.) 
        self.k = k

        # Minimum field voltage output 
        self.emin = emin



        super(ExcSCRX, self).__init__(*args, **kw_args)
    # >>> exc_scrx



class ExcAC8B(ExcitationSystem):
    """ IEEE (2005) AC8B Model  The AVR in this model consists of PID control, with separate constants for the proportional (<i>KPR</i>), integral (<i>KIR</i>), and derivative (<i>KDR</i>) gains. The representation of the brushless exciter (<i>TE</i>, <i>KE</i>, <i>SE</i>, <i>KC</i>, <i>KD</i>) is similar to the model Type AC2A. The Type AC8B model can be used to represent static voltage regulators applied to brushless excitation systems. Digitally based voltage regulators feeding dc rotating main exciters can be represented with the AC Type AC8B model with the parameters <i>KC </i>and <i>KD </i>set to 0. For thyristor power stages fed from the generator terminals, the limits <i>VRMAX </i>and <i>VRMIN </i>should be a function of terminal voltage: <i>VT </i>x <i>VRMAX </i>and <i>VT </i>x <i>VRMIN</i>.
    """
    # <<< exc_ac8_b
    # @generated
    def __init__(self, kdr=0.0, tr=0.0, e1=0.0, e2=0.0, kir=0.0, kc=0.0, vrmax=0.0, ka=0.0, se2=0.0, tdr=0.0, kpr=0.0, vemin=0.0, kd=0.0, te=0.0, se1=0.0, ke=0.0, vfemax=0.0, ta=0.0, vrmin=0.0, vtmult=0.0, *args, **kw_args):
        """ Initialises a new 'ExcAC8B' instance.

        @param kdr: Voltage Regulator Derivative Gain (&gt;= 0.) 
        @param tr: Voltage transducer time constant (&gt;= 0.) 
        @param e1: Field voltage value 1     (&gt; 0.) 
        @param e2: Field voltage value 2.    (&gt; 0.) 
        @param kir: Voltage Regulator Integral Gain (&gt;= 0.) 
        @param kc: Rectifier regulation factor (&gt;= 0.) 
        @param vrmax: Maximum controller output (&gt; 0.) 
        @param ka: Amplifier gain (&gt; 0.) 
        @param se2: Saturation factor at e2  (&gt;= 0.) 
        @param tdr: Voltage Regulator Derivative Time Constant (&gt; 0. if kdr &gt; 0.) 
        @param kpr: Voltage Regulator Proportional Gain (&gt; 0. if kir = 0.) 
        @param vemin: Minimum exciter ouput voltage (&lt;= 0.) 
        @param kd: Exciter regulation factor (&gt;= 0.) 
        @param te: Exciter field time constant (&gt; 0.) 
        @param se1: Saturation factor at e1 (&gt;= 0.) 
        @param ke: Exciter field proportional constant 
        @param vfemax: Exciter field current limit parameter 
        @param ta: Amplifier time constant  (&gt;= 0.) 
        @param vrmin: Minimum controller output (&lt;= 0.) 
        @param vtmult: if not 0, multiply vrmax and vrmin by terminal voltage 
        """
        # Voltage Regulator Derivative Gain (&gt;= 0.) 
        self.kdr = kdr

        # Voltage transducer time constant (&gt;= 0.) 
        self.tr = tr

        # Field voltage value 1     (&gt; 0.) 
        self.e1 = e1

        # Field voltage value 2.    (&gt; 0.) 
        self.e2 = e2

        # Voltage Regulator Integral Gain (&gt;= 0.) 
        self.kir = kir

        # Rectifier regulation factor (&gt;= 0.) 
        self.kc = kc

        # Maximum controller output (&gt; 0.) 
        self.vrmax = vrmax

        # Amplifier gain (&gt; 0.) 
        self.ka = ka

        # Saturation factor at e2  (&gt;= 0.) 
        self.se2 = se2

        # Voltage Regulator Derivative Time Constant (&gt; 0. if kdr &gt; 0.) 
        self.tdr = tdr

        # Voltage Regulator Proportional Gain (&gt; 0. if kir = 0.) 
        self.kpr = kpr

        # Minimum exciter ouput voltage (&lt;= 0.) 
        self.vemin = vemin

        # Exciter regulation factor (&gt;= 0.) 
        self.kd = kd

        # Exciter field time constant (&gt; 0.) 
        self.te = te

        # Saturation factor at e1 (&gt;= 0.) 
        self.se1 = se1

        # Exciter field proportional constant 
        self.ke = ke

        # Exciter field current limit parameter 
        self.vfemax = vfemax

        # Amplifier time constant  (&gt;= 0.) 
        self.ta = ta

        # Minimum controller output (&lt;= 0.) 
        self.vrmin = vrmin

        # if not 0, multiply vrmax and vrmin by terminal voltage 
        self.vtmult = vtmult



        super(ExcAC8B, self).__init__(*args, **kw_args)
    # >>> exc_ac8_b



class ExcWT2E(ExcitationSystem):
    """ Type 2 standard wind turbine field resistance control model
    """
    pass
    # <<< exc_wt2_e
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'ExcWT2E' instance.

        """


        super(ExcWT2E, self).__init__(*args, **kw_args)
    # >>> exc_wt2_e



class ExcAC7B(ExcitationSystem):
    """ IEEE (2005) AC7B Model  These excitation systems consist of an ac alternator with either stationary or rotating rectifiers to produce the dc field requirements. Upgrades to earlier ac excitation systems, which replace only the controls but retain the ac alternator and diode rectifier bridge, have resulted in this new model. Some of the features of this excitation system include a high bandwidth inner loop regulating generator field voltage or exciter current (<i>KF</i>2, <i>KF</i>1), a fast exciter current limit, <i>VFEMAX</i>, to protect the field of the ac alternator, and the PID generator voltage regulator (AVR). An alternative rate feedback loop (<i>KF</i>, <i>TF</i>) is provided for stabilization if the AVR does not include a derivative term. If a PSS control is supplied, the Type PSS2B or PSS3B models are appropriate.
    """
    # <<< exc_ac7_b
    # @generated
    def __init__(self, kd=0.0, kc=0.0, vrmin=0.0, kdr=0.0, vrmax=0.0, kpr=0.0, vemin=0.0, kl=0.0, kf1=0.0, kia=0.0, kf3=0.0, se1=0.0, vfemax=0.0, kf2=0.0, te=0.0, tf=0.0, ke=0.0, kpa=0.0, e2=0.0, se2=0.0, kp=0.0, e1=0.0, kir=0.0, tr=0.0, tdr=0.0, vamin=0.0, vamax=0.0, *args, **kw_args):
        """ Initialises a new 'ExcAC7B' instance.

        @param kd: Exciter internal reactance (&gt;= 0.) 
        @param kc: Rectifier regulation factor (&gt;= 0.) 
        @param vrmin: Minimum regulator output (&lt; 0.) 
        @param kdr: Regulator derivative gain (&gt;= 0.) 
        @param vrmax: Maximum regulator output (&gt; 0.) 
        @param kpr: Regulator proportional gain (&gt; 0. if kir = 0.) 
        @param vemin: Minimum exciter ouput voltage (&lt;= 0.) 
        @param kl: Exciter field voltage lower limit parameter 
        @param kf1: Field voltage feedback gain (&gt;= 0.) 
        @param kia: Amplifier integral gain (&gt;= 0.) 
        @param kf3: Rate feedback gain (&gt;= 0.) 
        @param se1: Saturation factor at e1  (&gt;= 0.) 
        @param vfemax: Exciter field current limit parameter 
        @param kf2: Exciter field current feedback gain (&gt;= 0.) 
        @param te: Exciter time constant, sec. (&gt; 0.) 
        @param tf: Rate feedback time constant (&gt; 0.) 
        @param ke: Exciter field resistance constant 
        @param kpa: Amplifier proportional gain (&gt; 0. if kia = 0.) 
        @param e2: Field voltage value 2.    (&gt; 0.) 
        @param se2: Saturation factor at e2   (&gt;= 0.) 
        @param kp: Exciter field voltage source gain (&gt; 0.) 
        @param e1: Field voltage value 1   (&gt; 0.) 
        @param kir: Regulator integral gain (&gt;= 0.) 
        @param tr: Filter time constant (&gt;= 0.) 
        @param tdr: Derivative gain washout time constant (&gt;= 0.) 
        @param vamin: Minimum amplifier output (&lt; 0.) 
        @param vamax: Maximum amplifier output (&gt; 0.) 
        """
        # Exciter internal reactance (&gt;= 0.) 
        self.kd = kd

        # Rectifier regulation factor (&gt;= 0.) 
        self.kc = kc

        # Minimum regulator output (&lt; 0.) 
        self.vrmin = vrmin

        # Regulator derivative gain (&gt;= 0.) 
        self.kdr = kdr

        # Maximum regulator output (&gt; 0.) 
        self.vrmax = vrmax

        # Regulator proportional gain (&gt; 0. if kir = 0.) 
        self.kpr = kpr

        # Minimum exciter ouput voltage (&lt;= 0.) 
        self.vemin = vemin

        # Exciter field voltage lower limit parameter 
        self.kl = kl

        # Field voltage feedback gain (&gt;= 0.) 
        self.kf1 = kf1

        # Amplifier integral gain (&gt;= 0.) 
        self.kia = kia

        # Rate feedback gain (&gt;= 0.) 
        self.kf3 = kf3

        # Saturation factor at e1  (&gt;= 0.) 
        self.se1 = se1

        # Exciter field current limit parameter 
        self.vfemax = vfemax

        # Exciter field current feedback gain (&gt;= 0.) 
        self.kf2 = kf2

        # Exciter time constant, sec. (&gt; 0.) 
        self.te = te

        # Rate feedback time constant (&gt; 0.) 
        self.tf = tf

        # Exciter field resistance constant 
        self.ke = ke

        # Amplifier proportional gain (&gt; 0. if kia = 0.) 
        self.kpa = kpa

        # Field voltage value 2.    (&gt; 0.) 
        self.e2 = e2

        # Saturation factor at e2   (&gt;= 0.) 
        self.se2 = se2

        # Exciter field voltage source gain (&gt; 0.) 
        self.kp = kp

        # Field voltage value 1   (&gt; 0.) 
        self.e1 = e1

        # Regulator integral gain (&gt;= 0.) 
        self.kir = kir

        # Filter time constant (&gt;= 0.) 
        self.tr = tr

        # Derivative gain washout time constant (&gt;= 0.) 
        self.tdr = tdr

        # Minimum amplifier output (&lt; 0.) 
        self.vamin = vamin

        # Maximum amplifier output (&gt; 0.) 
        self.vamax = vamax



        super(ExcAC7B, self).__init__(*args, **kw_args)
    # >>> exc_ac7_b



class ExcWT4E(ExcitationSystem):
    """ Type 4 standard wind turbine convertor control model
    """
    pass
    # <<< exc_wt4_e
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'ExcWT4E' instance.

        """


        super(ExcWT4E, self).__init__(*args, **kw_args)
    # >>> exc_wt4_e



class ExcST1A(ExcitationSystem):
    """ IEEE (1992/2005) ST1A Model  The computer model of the Type ST1A potential-source controlled-rectifier excitation system represents systems in which excitation power is supplied through a transformer from the generator terminals (or the unit's auxiliary bus) and is regulated by a controlled rectifier. The maximum exciter voltage available from such systems is directly related to the generator terminal voltage.
    """
    # <<< exc_st1_a
    # @generated
    def __init__(self, vrmin=0.0, kc=0.0, vimin=0.0, uelin=0.0, tf=0.0, kf=0.0, tc1=0.0, pssin=0.0, tc=0.0, tb=0.0, ka=0.0, ta=0.0, tr=0.0, ilr=0.0, vamin=0.0, klr=0.0, tb1=0.0, vamax=0.0, vrmax=0.0, vimax=0.0, *args, **kw_args):
        """ Initialises a new 'ExcST1A' instance.

        @param vrmin: Excitation voltage lower limit (&lt; 0.) 
        @param kc: Excitation system regulation factor (&gt;= 0.) 
        @param vimin: Minimum error (&lt; 0.) 
        @param uelin: = 2 ? UEL input added to error signal = 1 ? UEL input HV gate with error signal = -1 ? UEL input HV gate with volt. reg. output = 0 ? ignore UEL signal 
        @param tf: Rate feedback time constant (&gt;= 0.) 
        @param kf: Rate feedback gain (&gt;= 0.) 
        @param tc1: Lead time constant 
        @param pssin: = 0 ? PSS input (Vs) added to error signal not 0 ? PSS input (Vs) added to voltage regulator output 
        @param tc: Lead time constant 
        @param tb: Lag time constant (&gt;= 0.) 
        @param ka: Gain (&gt; 0.) 
        @param ta: Time constant (&gt;= 0.) 
        @param tr: Voltage transducer time constant (&gt;= 0.) 
        @param ilr: Maximum field current 
        @param vamin: Minimum control element output (&lt; 0.) 
        @param klr: Gain on field current limit 
        @param tb1: Lag time constant (&gt;= 0.) 
        @param vamax: Maximum control element output (&gt; 0.) 
        @param vrmax: Excitation voltage upper limit (&gt; 0.) 
        @param vimax: Maximum error (&gt; 0.) 
        """
        # Excitation voltage lower limit (&lt; 0.) 
        self.vrmin = vrmin

        # Excitation system regulation factor (&gt;= 0.) 
        self.kc = kc

        # Minimum error (&lt; 0.) 
        self.vimin = vimin

        # = 2 ? UEL input added to error signal = 1 ? UEL input HV gate with error signal = -1 ? UEL input HV gate with volt. reg. output = 0 ? ignore UEL signal 
        self.uelin = uelin

        # Rate feedback time constant (&gt;= 0.) 
        self.tf = tf

        # Rate feedback gain (&gt;= 0.) 
        self.kf = kf

        # Lead time constant 
        self.tc1 = tc1

        # = 0 ? PSS input (Vs) added to error signal not 0 ? PSS input (Vs) added to voltage regulator output 
        self.pssin = pssin

        # Lead time constant 
        self.tc = tc

        # Lag time constant (&gt;= 0.) 
        self.tb = tb

        # Gain (&gt; 0.) 
        self.ka = ka

        # Time constant (&gt;= 0.) 
        self.ta = ta

        # Voltage transducer time constant (&gt;= 0.) 
        self.tr = tr

        # Maximum field current 
        self.ilr = ilr

        # Minimum control element output (&lt; 0.) 
        self.vamin = vamin

        # Gain on field current limit 
        self.klr = klr

        # Lag time constant (&gt;= 0.) 
        self.tb1 = tb1

        # Maximum control element output (&gt; 0.) 
        self.vamax = vamax

        # Excitation voltage upper limit (&gt; 0.) 
        self.vrmax = vrmax

        # Maximum error (&gt; 0.) 
        self.vimax = vimax



        super(ExcST1A, self).__init__(*args, **kw_args)
    # >>> exc_st1_a



class ExcBBC(ExcitationSystem):
    """ Static Excitation System Model with ABB regulator
    """
    pass
    # <<< exc_bbc
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'ExcBBC' instance.

        """


        super(ExcBBC, self).__init__(*args, **kw_args)
    # >>> exc_bbc



class ExcDC3A(ExcitationSystem):
    """ IEEE (1992/2005) DC3A Model  The Type DC3A model is used to represent older systems, in particular those dc commutator exciters with non-continuously acting regulators that were commonly used before the development of the continuously acting varieties. These systems respond at basically two different rates, depending upon the magnitude of voltage error. For small errors, adjustment is made periodically with a signal to a motor-operated rheostat. Larger errors cause resistors to be quickly shorted or inserted and a strong forcing signal applied to the exciter. Continuous motion of the motor-operated rheostat occurs for these larger error signals, even though it is bypassed by contactor action.
    """
    # <<< exc_dc3_a
    # @generated
    def __init__(self, vrmax=0.0, ke=0.0, te=0.0, exclim=0.0, se1=0.0, se2=0.0, trh=0.0, kv=0.0, e1=0.0, e2=0.0, vrmin=0.0, tr=0.0, *args, **kw_args):
        """ Initialises a new 'ExcDC3A' instance.

        @param vrmax: Maximum control element output (&gt; 0.) 
        @param ke: Exciter field resistance line slope 
        @param te: Exciter field time constant (&gt; 0.) 
        @param exclim: If not 0, apply lower limit of 0. to exciter output 
        @param se1: Saturation factor at e1 (&gt;= 0.) 
        @param se2: Saturation factor at e2  (&gt;= 0.) 
        @param trh: Rheostat full range travel time (&gt; 0.) 
        @param kv: Voltage error threshold min/max control action (&gt; 0.) 
        @param e1: Field voltage value 1    (&gt; 0.) 
        @param e2: Field voltage value 2.     (&gt; 0.) 
        @param vrmin: Minimum control element output (&lt;= 0.) 
        @param tr: Filter  time constant (&gt;= 0.) 
        """
        # Maximum control element output (&gt; 0.) 
        self.vrmax = vrmax

        # Exciter field resistance line slope 
        self.ke = ke

        # Exciter field time constant (&gt; 0.) 
        self.te = te

        # If not 0, apply lower limit of 0. to exciter output 
        self.exclim = exclim

        # Saturation factor at e1 (&gt;= 0.) 
        self.se1 = se1

        # Saturation factor at e2  (&gt;= 0.) 
        self.se2 = se2

        # Rheostat full range travel time (&gt; 0.) 
        self.trh = trh

        # Voltage error threshold min/max control action (&gt; 0.) 
        self.kv = kv

        # Field voltage value 1    (&gt; 0.) 
        self.e1 = e1

        # Field voltage value 2.     (&gt; 0.) 
        self.e2 = e2

        # Minimum control element output (&lt;= 0.) 
        self.vrmin = vrmin

        # Filter  time constant (&gt;= 0.) 
        self.tr = tr



        super(ExcDC3A, self).__init__(*args, **kw_args)
    # >>> exc_dc3_a



class ExcST3A(ExcitationSystem):
    """ IEEE (1992/2005) ST3A Model  Some static systems utilize a field voltage control loop to linearize the exciter control characteristic. This also makes the output independent of supply source variations until supply limitations are reached. These systems utilize a variety of controlled-rectifier designs: full thyristor complements or hybrid bridges in either series or shunt configurations. The power source may consist of only a potential source, either fed from the machine terminals or from internal windings. Some designs may have compound power sources utilizing both machine potential and current. These power sources are represented as phasor combinations of machine terminal current and voltage and are accommodated by suitable parameters in the model Type ST3A.
    """
    # <<< exc_st3_a
    # @generated
    def __init__(self, vrmin=0.0, kc=0.0, ka=0.0, vbmax=0.0, vimin=0.0, xl=0.0, vgmax=0.0, angp=0.0, vmmin=0.0, vrmax=0.0, kp=0.0, km=0.0, vimax=0.0, tr=0.0, vmmax=0.0, ki=0.0, tm=0.0, ta=0.0, tb=0.0, kg=0.0, tc=0.0, *args, **kw_args):
        """ Initialises a new 'ExcST3A' instance.

        @param vrmin: Minimum AVR output (&lt; 0.) 
        @param kc: Exciter regulation factor (&gt;= 0.) 
        @param ka: AVR gain (&gt; 0.) 
        @param vbmax: Maximum excitation voltage (&gt; 0.) 
        @param vimin: Minimum error (&lt; 0.) 
        @param xl: P-bar reactance (&gt;= 0.) 
        @param vgmax: Maximum inner loop feedback voltage (&gt;= 0.) 
        @param angp: Phase angle of potential source 
        @param vmmin: Minimum inner loop output (&lt;= 0.) 
        @param vrmax: Maximum AVR output (&gt; 0.) 
        @param kp: Potential source gain (&gt; 0.) 
        @param km: Inner loop forward gain (&gt; 0.) 
        @param vimax: Maximum error (&gt; 0.) 
        @param tr: Voltage transducer time constant (&gt;= 0.) 
        @param vmmax: Maximum inner loop output (&gt; 0.) 
        @param ki: Current source gain (&gt;= 0.) 
        @param tm: Inner loop time constant (&gt; 0.) 
        @param ta: AVR time constant (&gt;= 0.) 
        @param tb: AVR lag time constant (&gt;= 0.) 
        @param kg: Inner loop feedback gain (&gt;= 0.) 
        @param tc: AVR lead time constant 
        """
        # Minimum AVR output (&lt; 0.) 
        self.vrmin = vrmin

        # Exciter regulation factor (&gt;= 0.) 
        self.kc = kc

        # AVR gain (&gt; 0.) 
        self.ka = ka

        # Maximum excitation voltage (&gt; 0.) 
        self.vbmax = vbmax

        # Minimum error (&lt; 0.) 
        self.vimin = vimin

        # P-bar reactance (&gt;= 0.) 
        self.xl = xl

        # Maximum inner loop feedback voltage (&gt;= 0.) 
        self.vgmax = vgmax

        # Phase angle of potential source 
        self.angp = angp

        # Minimum inner loop output (&lt;= 0.) 
        self.vmmin = vmmin

        # Maximum AVR output (&gt; 0.) 
        self.vrmax = vrmax

        # Potential source gain (&gt; 0.) 
        self.kp = kp

        # Inner loop forward gain (&gt; 0.) 
        self.km = km

        # Maximum error (&gt; 0.) 
        self.vimax = vimax

        # Voltage transducer time constant (&gt;= 0.) 
        self.tr = tr

        # Maximum inner loop output (&gt; 0.) 
        self.vmmax = vmmax

        # Current source gain (&gt;= 0.) 
        self.ki = ki

        # Inner loop time constant (&gt; 0.) 
        self.tm = tm

        # AVR time constant (&gt;= 0.) 
        self.ta = ta

        # AVR lag time constant (&gt;= 0.) 
        self.tb = tb

        # Inner loop feedback gain (&gt;= 0.) 
        self.kg = kg

        # AVR lead time constant 
        self.tc = tc



        super(ExcST3A, self).__init__(*args, **kw_args)
    # >>> exc_st3_a



class ExcCZ(ExcitationSystem):
    """ Czech proportional/integral excitation system model.
    """
    pass
    # <<< exc_cz
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'ExcCZ' instance.

        """


        super(ExcCZ, self).__init__(*args, **kw_args)
    # >>> exc_cz



# <<< excitation_systems
# @generated
# >>> excitation_systems
