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

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#Package_TurbineGovernors"

class TurbineGovernor(Element):
    """ The turbine-governor determines the mechanical power (Pm) supplied to the generator model
    """
    pass
    # <<< turbine_governor
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'TurbineGovernor' instance.

        """


        super(TurbineGovernor, self).__init__(*args, **kw_args)
    # >>> turbine_governor



class GovHydro3(TurbineGovernor):
    pass
    # <<< gov_hydro3
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'GovHydro3' instance.

        """


        super(GovHydro3, self).__init__(*args, **kw_args)
    # >>> gov_hydro3



class GovHydro2(TurbineGovernor):
    # <<< gov_hydro2
    # @generated
    def __init__(self, bturb=0.0, rtemp=0.0, tw=0.0, rperm=0.0, gv1=0.0, gv2=0.0, tr=0.0, aturb=0.0, tp=0.0, uo=0.0, gv6=0.0, gv5=0.0, pgv5=0.0, gv4=0.0, pgv6=0.0, gv3=0.0, pgv2=0.0, pgv1=0.0, db1=0.0, pgv4=0.0, kturb=0.0, db2=0.0, tg=0.0, pmax=0.0, pgv3=0.0, mwbase=0.0, uc=0.0, pmin=0.0, eps=0.0, *args, **kw_args):
        """ Initialises a new 'GovHydro2' instance.

        @param bturb: Turbine denominator multiplier 
        @param rtemp: Temporary droop 
        @param tw: Water inertia time constant 
        @param rperm: Permanent droop 
        @param gv1: Nonlinear gain point 1, p.u. gv 
        @param gv2: Nonlinear gain point 2, p.u. gv 
        @param tr: Dashpot time constant 
        @param aturb: Turbine numerator multiplier 
        @param tp: Pilot servo valve time constant 
        @param uo: Maximum gate opening velocity 
        @param gv6: Nonlinear gain point 6, p.u. gv 
        @param gv5: Nonlinear gain point 5, p.u. gv 
        @param pgv5: Nonlinear gain point 5, p.u. power 
        @param gv4: Nonlinear gain point 4, p.u. gv 
        @param pgv6: Nonlinear gain point 6, p.u. power 
        @param gv3: Nonlinear gain point 3, p.u. gv 
        @param pgv2: Nonlinear gain point 2, p.u. power 
        @param pgv1: Nonlinear gain point 1, p.u. power 
        @param db1: Intentional deadband width 
        @param pgv4: Nonlinear gain point 4, p.u. power 
        @param kturb: Turbine gain 
        @param db2: Unintentional deadband 
        @param tg: Gate servo time constant 
        @param pmax: Maximum gate opening 
        @param pgv3: Nonlinear gain point 3, p.u. power 
        @param mwbase: Base for power values (&gt; 0.) 
        @param uc: Maximum gate closing velocity (&lt;0.) 
        @param pmin: Minimum gate opening 
        @param eps: Intentional db hysteresis 
        """
        # Turbine denominator multiplier 
        self.bturb = bturb

        # Temporary droop 
        self.rtemp = rtemp

        # Water inertia time constant 
        self.tw = tw

        # Permanent droop 
        self.rperm = rperm

        # Nonlinear gain point 1, p.u. gv 
        self.gv1 = gv1

        # Nonlinear gain point 2, p.u. gv 
        self.gv2 = gv2

        # Dashpot time constant 
        self.tr = tr

        # Turbine numerator multiplier 
        self.aturb = aturb

        # Pilot servo valve time constant 
        self.tp = tp

        # Maximum gate opening velocity 
        self.uo = uo

        # Nonlinear gain point 6, p.u. gv 
        self.gv6 = gv6

        # Nonlinear gain point 5, p.u. gv 
        self.gv5 = gv5

        # Nonlinear gain point 5, p.u. power 
        self.pgv5 = pgv5

        # Nonlinear gain point 4, p.u. gv 
        self.gv4 = gv4

        # Nonlinear gain point 6, p.u. power 
        self.pgv6 = pgv6

        # Nonlinear gain point 3, p.u. gv 
        self.gv3 = gv3

        # Nonlinear gain point 2, p.u. power 
        self.pgv2 = pgv2

        # Nonlinear gain point 1, p.u. power 
        self.pgv1 = pgv1

        # Intentional deadband width 
        self.db1 = db1

        # Nonlinear gain point 4, p.u. power 
        self.pgv4 = pgv4

        # Turbine gain 
        self.kturb = kturb

        # Unintentional deadband 
        self.db2 = db2

        # Gate servo time constant 
        self.tg = tg

        # Maximum gate opening 
        self.pmax = pmax

        # Nonlinear gain point 3, p.u. power 
        self.pgv3 = pgv3

        # Base for power values (&gt; 0.) 
        self.mwbase = mwbase

        # Maximum gate closing velocity (&lt;0.) 
        self.uc = uc

        # Minimum gate opening 
        self.pmin = pmin

        # Intentional db hysteresis 
        self.eps = eps



        super(GovHydro2, self).__init__(*args, **kw_args)
    # >>> gov_hydro2



class GovGAST(TurbineGovernor):
    pass
    # <<< gov_gast
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'GovGAST' instance.

        """


        super(GovGAST, self).__init__(*args, **kw_args)
    # >>> gov_gast



class GovWT1T(TurbineGovernor):
    pass
    # <<< gov_wt1_t
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'GovWT1T' instance.

        """


        super(GovWT1T, self).__init__(*args, **kw_args)
    # >>> gov_wt1_t



class GovWT2P(TurbineGovernor):
    pass
    # <<< gov_wt2_p
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'GovWT2P' instance.

        """


        super(GovWT2P, self).__init__(*args, **kw_args)
    # >>> gov_wt2_p



class GovHydroDD(TurbineGovernor):
    pass
    # <<< gov_hydro_dd
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'GovHydroDD' instance.

        """


        super(GovHydroDD, self).__init__(*args, **kw_args)
    # >>> gov_hydro_dd



class GovHydroWEH(TurbineGovernor):
    pass
    # <<< gov_hydro_weh
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'GovHydroWEH' instance.

        """


        super(GovHydroWEH, self).__init__(*args, **kw_args)
    # >>> gov_hydro_weh



class GovWT3T(TurbineGovernor):
    pass
    # <<< gov_wt3_t
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'GovWT3T' instance.

        """


        super(GovWT3T, self).__init__(*args, **kw_args)
    # >>> gov_wt3_t



class GovHydroPID(TurbineGovernor):
    pass
    # <<< gov_hydro_pid
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'GovHydroPID' instance.

        """


        super(GovHydroPID, self).__init__(*args, **kw_args)
    # >>> gov_hydro_pid



class GovHydro4(TurbineGovernor):
    pass
    # <<< gov_hydro4
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'GovHydro4' instance.

        """


        super(GovHydro4, self).__init__(*args, **kw_args)
    # >>> gov_hydro4



class GovDUM(TurbineGovernor):
    pass
    # <<< gov_dum
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'GovDUM' instance.

        """


        super(GovDUM, self).__init__(*args, **kw_args)
    # >>> gov_dum



class GovHydroWPID(TurbineGovernor):
    pass
    # <<< gov_hydro_wpid
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'GovHydroWPID' instance.

        """


        super(GovHydroWPID, self).__init__(*args, **kw_args)
    # >>> gov_hydro_wpid



class GovWT4P(TurbineGovernor):
    pass
    # <<< gov_wt4_p
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'GovWT4P' instance.

        """


        super(GovWT4P, self).__init__(*args, **kw_args)
    # >>> gov_wt4_p



class TLCFB1(TurbineGovernor):
    pass
    # <<< tlcfb1
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'TLCFB1' instance.

        """


        super(TLCFB1, self).__init__(*args, **kw_args)
    # >>> tlcfb1



class GovGASM(TurbineGovernor):
    pass
    # <<< gov_gasm
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'GovGASM' instance.

        """


        super(GovGASM, self).__init__(*args, **kw_args)
    # >>> gov_gasm



class GovHydroR(TurbineGovernor):
    pass
    # <<< gov_hydro_r
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'GovHydroR' instance.

        """


        super(GovHydroR, self).__init__(*args, **kw_args)
    # >>> gov_hydro_r



class GovSteamFV2(TurbineGovernor):
    pass
    # <<< gov_steam_fv2
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'GovSteamFV2' instance.

        """


        super(GovSteamFV2, self).__init__(*args, **kw_args)
    # >>> gov_steam_fv2



class GovRAV(TurbineGovernor):
    pass
    # <<< gov_rav
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'GovRAV' instance.

        """


        super(GovRAV, self).__init__(*args, **kw_args)
    # >>> gov_rav



class GovCT2(TurbineGovernor):
    pass
    # <<< gov_ct2
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'GovCT2' instance.

        """


        super(GovCT2, self).__init__(*args, **kw_args)
    # >>> gov_ct2



class GovSteam1(TurbineGovernor):
    """ IEEE steam turbine/governor model  (with optional deadband and nonlinear valve gain added)
    """
    # <<< gov_steam1
    # @generated
    def __init__(self, eps=0.0, uc=0.0, mwbase=0.0, pmin=0.0, k3=0.0, k=0.0, k2=0.0, k1=0.0, pgv1=0.0, k7=0.0, k6=0.0, pmax=0.0, k5=0.0, k4=0.0, gv6=0.0, t6=0.0, pgv6=0.0, gv5=0.0, t7=0.0, k8=0.0, gv1=0.0, t1=0.0, t2=0.0, pgv3=0.0, db1=0.0, t3=0.0, uo=0.0, pgv2=0.0, gv4=0.0, pgv5=0.0, t4=0.0, gv2=0.0, gv3=0.0, t5=0.0, pgv4=0.0, db2=0.0, *args, **kw_args):
        """ Initialises a new 'GovSteam1' instance.

        @param eps: Intentional db hysteresis 
        @param uc: Maximum valve closing velocity, p.u./sec (&lt; 0.) 
        @param mwbase: Base for power values (&gt; 0.) 
        @param pmin: Minimum valve opening (&gt;= 0.) 
        @param k3: Fraction of HP shaft power after second boiler pass 
        @param k: Governor gain (reciprocal of droop) (&gt; 0.) 
        @param k2: Fraction of LP shaft power after first boiler pass 
        @param k1: Fraction of HP shaft power after first boiler pass 
        @param pgv1: Nonlinear gain power value point 1 
        @param k7: Fraction of HP shaft power after fourth boiler pass 
        @param k6: Fraction of LP shaft power after third boiler pass 
        @param pmax: Maximum valve opening (&gt; Pmin) 
        @param k5: Fraction of HP shaft power after third boiler pass 
        @param k4: Fraction of LP shaft power after second boiler pass 
        @param gv6: Nonlinear gain valve position point 6 
        @param t6: Time constant of third boiler pass 
        @param pgv6: Nonlinear gain power value point 6 
        @param gv5: Nonlinear gain valve position point 5 
        @param t7: Time constant of fourth boiler pas 
        @param k8: Fraction of LP shaft power after fourth boiler pass 
        @param gv1: Nonlinear gain valve position point 1 
        @param t1: Governor lag time constant 
        @param t2: Governor lead time constant 
        @param pgv3: Nonlinear gain power value point 3 
        @param db1: Intentional deadband width 
        @param t3: Valve positioner time constant (&gt; 0.) 
        @param uo: Maximum valve opening velocity (&gt; 0.) 
        @param pgv2: Nonlinear gain power value point 2 
        @param gv4: Nonlinear gain valve position point 4 
        @param pgv5: Nonlinear gain power value point 5 
        @param t4: Inlet piping/steam bowl time constant 
        @param gv2: Nonlinear gain valve position point 2 
        @param gv3: Nonlinear gain valve position point 3 
        @param t5: Time constant of second boiler pass 
        @param pgv4: Nonlinear gain power value point 4 
        @param db2: Unintentional deadband 
        """
        # Intentional db hysteresis 
        self.eps = eps

        # Maximum valve closing velocity, p.u./sec (&lt; 0.) 
        self.uc = uc

        # Base for power values (&gt; 0.) 
        self.mwbase = mwbase

        # Minimum valve opening (&gt;= 0.) 
        self.pmin = pmin

        # Fraction of HP shaft power after second boiler pass 
        self.k3 = k3

        # Governor gain (reciprocal of droop) (&gt; 0.) 
        self.k = k

        # Fraction of LP shaft power after first boiler pass 
        self.k2 = k2

        # Fraction of HP shaft power after first boiler pass 
        self.k1 = k1

        # Nonlinear gain power value point 1 
        self.pgv1 = pgv1

        # Fraction of HP shaft power after fourth boiler pass 
        self.k7 = k7

        # Fraction of LP shaft power after third boiler pass 
        self.k6 = k6

        # Maximum valve opening (&gt; Pmin) 
        self.pmax = pmax

        # Fraction of HP shaft power after third boiler pass 
        self.k5 = k5

        # Fraction of LP shaft power after second boiler pass 
        self.k4 = k4

        # Nonlinear gain valve position point 6 
        self.gv6 = gv6

        # Time constant of third boiler pass 
        self.t6 = t6

        # Nonlinear gain power value point 6 
        self.pgv6 = pgv6

        # Nonlinear gain valve position point 5 
        self.gv5 = gv5

        # Time constant of fourth boiler pas 
        self.t7 = t7

        # Fraction of LP shaft power after fourth boiler pass 
        self.k8 = k8

        # Nonlinear gain valve position point 1 
        self.gv1 = gv1

        # Governor lag time constant 
        self.t1 = t1

        # Governor lead time constant 
        self.t2 = t2

        # Nonlinear gain power value point 3 
        self.pgv3 = pgv3

        # Intentional deadband width 
        self.db1 = db1

        # Valve positioner time constant (&gt; 0.) 
        self.t3 = t3

        # Maximum valve opening velocity (&gt; 0.) 
        self.uo = uo

        # Nonlinear gain power value point 2 
        self.pgv2 = pgv2

        # Nonlinear gain valve position point 4 
        self.gv4 = gv4

        # Nonlinear gain power value point 5 
        self.pgv5 = pgv5

        # Inlet piping/steam bowl time constant 
        self.t4 = t4

        # Nonlinear gain valve position point 2 
        self.gv2 = gv2

        # Nonlinear gain valve position point 3 
        self.gv3 = gv3

        # Time constant of second boiler pass 
        self.t5 = t5

        # Nonlinear gain power value point 4 
        self.pgv4 = pgv4

        # Unintentional deadband 
        self.db2 = db2



        super(GovSteam1, self).__init__(*args, **kw_args)
    # >>> gov_steam1



class GovSteamCC(TurbineGovernor):
    pass
    # <<< gov_steam_cc
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'GovSteamCC' instance.

        """


        super(GovSteamCC, self).__init__(*args, **kw_args)
    # >>> gov_steam_cc



class GovSteamSGO(TurbineGovernor):
    pass
    # <<< gov_steam_sgo
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'GovSteamSGO' instance.

        """


        super(GovSteamSGO, self).__init__(*args, **kw_args)
    # >>> gov_steam_sgo



class GovSteamFV3(TurbineGovernor):
    pass
    # <<< gov_steam_fv3
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'GovSteamFV3' instance.

        """


        super(GovSteamFV3, self).__init__(*args, **kw_args)
    # >>> gov_steam_fv3



class GovWT3P(TurbineGovernor):
    pass
    # <<< gov_wt3_p
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'GovWT3P' instance.

        """


        super(GovWT3P, self).__init__(*args, **kw_args)
    # >>> gov_wt3_p



class GovWT1P(TurbineGovernor):
    pass
    # <<< gov_wt1_p
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'GovWT1P' instance.

        """


        super(GovWT1P, self).__init__(*args, **kw_args)
    # >>> gov_wt1_p



class GovSteam0(TurbineGovernor):
    """ A simplified steam turbine-governor model.
    """
    # <<< gov_steam0
    # @generated
    def __init__(self, t2=0.0, t3=0.0, t1=0.0, vmax=0.0, dt=0.0, r=0.0, vmin=0.0, mwbase=0.0, *args, **kw_args):
        """ Initialises a new 'GovSteam0' instance.

        @param t2: Numerator time constant of T2/T3 block 
        @param t3: Reheater time constant 
        @param t1: Steam bowl time constant 
        @param vmax: Maximum valve position, p.u. of mwcap 
        @param dt: Turbine damping coefficient 
        @param r: Permanent droop 
        @param vmin: Minimum valve position, p.u. of mwcap 
        @param mwbase: Base for power values  (&gt; 0.) 
        """
        # Numerator time constant of T2/T3 block 
        self.t2 = t2

        # Reheater time constant 
        self.t3 = t3

        # Steam bowl time constant 
        self.t1 = t1

        # Maximum valve position, p.u. of mwcap 
        self.vmax = vmax

        # Turbine damping coefficient 
        self.dt = dt

        # Permanent droop 
        self.r = r

        # Minimum valve position, p.u. of mwcap 
        self.vmin = vmin

        # Base for power values  (&gt; 0.) 
        self.mwbase = mwbase



        super(GovSteam0, self).__init__(*args, **kw_args)
    # >>> gov_steam0



class GovCT1(TurbineGovernor):
    """ General model for any prime mover with a PID governor, used primarily for combustion turbine and combined cycle units.
    """
    # <<< gov_ct1
    # @generated
    def __init__(self, rdown=0.0, vmax=0.0, wfnl=0.0, tdgov=0.0, aset=0.0, r=0.0, wfspd=False, kpgov=0.0, minerr=0.0, tsa=0.0, tact=0.0, tsb=0.0, ldref=0.0, kimw=0.0, maxerr=0.0, vmin=0.0, mwbase=0.0, rclose=0.0, tpelec=0.0, rup=0.0, tb=0.0, ka=0.0, ta=0.0, kdgov=0.0, kturb=0.0, db=0.0, teng=0.0, tc=0.0, ropen=0.0, dm=0.0, kiload=0.0, pmwset=0.0, rselect=False, kigov=0.0, kpload=0.0, tfload=0.0, *args, **kw_args):
        """ Initialises a new 'GovCT1' instance.

        @param rdown: Maximum rate of load limit decrease 
        @param vmax: Maximum valve position limit 
        @param wfnl: No load fuel flow 
        @param tdgov: Governor derivative controller time constant 
        @param aset: Acceleration limiter setpoint 
        @param r: Permanent droop 
        @param wfspd: Switch for fuel source characteristic = 0 for fuel flow independent of speed = 1 fuel flow proportional to speed 
        @param kpgov: Governor proportional gain 
        @param minerr: Minimum value for speed error signal 
        @param tsa: Temperature detection lead time constant 
        @param tact: Actuator time constant 
        @param tsb: Temperature detection lag time constant 
        @param ldref: Load limiter reference value 
        @param kimw: Power controller (reset) gain 
        @param maxerr: Maximum value for speed error signal 
        @param vmin: Minimum valve position limit 
        @param mwbase: Base for power values (&gt; 0.) 
        @param rclose: Minimum valve closing rate 
        @param tpelec: Electrical power transducer time constant, sec. (&gt;0.) 
        @param rup: Maximum rate of load limit increase 
        @param tb: Turbine lag time constant, sec.  (&gt;0.) 
        @param ka: Acceleration limiter gain 
        @param ta: Acceleration limiter time constant (&gt;0.) 
        @param kdgov: Governor derivative gain 
        @param kturb: Turbine gain  (&gt;0.) 
        @param db: Speed governor dead band 
        @param teng: Transport time delay for diesel engine 
        @param tc: Turbine lead time constant, sec. 
        @param ropen: Maximum valve opening rate 
        @param dm: Speed sensitivity coefficient 
        @param kiload: Load limiter integral gain for PI controller 
        @param pmwset: Power controller setpoint 
        @param rselect: Feedback signal for droop  = 1 electrical power = 0 none (isochronous governor) = -1 fuel valve stroke ( true stroke) = -2 governor output ( requested stroke) 
        @param kigov: Governor integral gain 
        @param kpload: Load limiter proportional gain for PI controller 
        @param tfload: Load Limiter time constant (&gt;0.) 
        """
        # Maximum rate of load limit decrease 
        self.rdown = rdown

        # Maximum valve position limit 
        self.vmax = vmax

        # No load fuel flow 
        self.wfnl = wfnl

        # Governor derivative controller time constant 
        self.tdgov = tdgov

        # Acceleration limiter setpoint 
        self.aset = aset

        # Permanent droop 
        self.r = r

        # Switch for fuel source characteristic = 0 for fuel flow independent of speed = 1 fuel flow proportional to speed 
        self.wfspd = wfspd

        # Governor proportional gain 
        self.kpgov = kpgov

        # Minimum value for speed error signal 
        self.minerr = minerr

        # Temperature detection lead time constant 
        self.tsa = tsa

        # Actuator time constant 
        self.tact = tact

        # Temperature detection lag time constant 
        self.tsb = tsb

        # Load limiter reference value 
        self.ldref = ldref

        # Power controller (reset) gain 
        self.kimw = kimw

        # Maximum value for speed error signal 
        self.maxerr = maxerr

        # Minimum valve position limit 
        self.vmin = vmin

        # Base for power values (&gt; 0.) 
        self.mwbase = mwbase

        # Minimum valve closing rate 
        self.rclose = rclose

        # Electrical power transducer time constant, sec. (&gt;0.) 
        self.tpelec = tpelec

        # Maximum rate of load limit increase 
        self.rup = rup

        # Turbine lag time constant, sec.  (&gt;0.) 
        self.tb = tb

        # Acceleration limiter gain 
        self.ka = ka

        # Acceleration limiter time constant (&gt;0.) 
        self.ta = ta

        # Governor derivative gain 
        self.kdgov = kdgov

        # Turbine gain  (&gt;0.) 
        self.kturb = kturb

        # Speed governor dead band 
        self.db = db

        # Transport time delay for diesel engine 
        self.teng = teng

        # Turbine lead time constant, sec. 
        self.tc = tc

        # Maximum valve opening rate 
        self.ropen = ropen

        # Speed sensitivity coefficient 
        self.dm = dm

        # Load limiter integral gain for PI controller 
        self.kiload = kiload

        # Power controller setpoint 
        self.pmwset = pmwset

        # Feedback signal for droop  = 1 electrical power = 0 none (isochronous governor) = -1 fuel valve stroke ( true stroke) = -2 governor output ( requested stroke) 
        self.rselect = rselect

        # Governor integral gain 
        self.kigov = kigov

        # Load limiter proportional gain for PI controller 
        self.kpload = kpload

        # Load Limiter time constant (&gt;0.) 
        self.tfload = tfload



        super(GovCT1, self).__init__(*args, **kw_args)
    # >>> gov_ct1



class GovWT2T(TurbineGovernor):
    pass
    # <<< gov_wt2_t
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'GovWT2T' instance.

        """


        super(GovWT2T, self).__init__(*args, **kw_args)
    # >>> gov_wt2_t



class GovHydro1(TurbineGovernor):
    """ Hydro turbine-governor model.
    """
    # <<< gov_hydro1
    # @generated
    def __init__(self, rperm=0.0, tg=0.0, tf=0.0, mwbase=0.0, at=0.0, qnl=0.0, tw=0.0, dturb=0.0, rtemp=0.0, tr=0.0, *args, **kw_args):
        """ Initialises a new 'GovHydro1' instance.

        @param rperm: Permanent droop (R) (&gt;0) 
        @param tg: Gate servo time constant (&gt;0) 
        @param tf: Filter time constant (&gt;0) 
        @param mwbase: Base for power values  (&gt; 0.) 
        @param at: Turbine gain (&gt;0) 
        @param qnl: No-load flow at nominal head (&gt;=0) 
        @param tw: Water inertia time constant (&gt;0) 
        @param dturb: Turbine damping factor (&gt;=0) 
        @param rtemp: Temporary droop (r) (&gt;R) 
        @param tr: Washout time constant (&gt;0) 
        """
        # Permanent droop (R) (&gt;0) 
        self.rperm = rperm

        # Gate servo time constant (&gt;0) 
        self.tg = tg

        # Filter time constant (&gt;0) 
        self.tf = tf

        # Base for power values  (&gt; 0.) 
        self.mwbase = mwbase

        # Turbine gain (&gt;0) 
        self.at = at

        # No-load flow at nominal head (&gt;=0) 
        self.qnl = qnl

        # Water inertia time constant (&gt;0) 
        self.tw = tw

        # Turbine damping factor (&gt;=0) 
        self.dturb = dturb

        # Temporary droop (r) (&gt;R) 
        self.rtemp = rtemp

        # Washout time constant (&gt;0) 
        self.tr = tr



        super(GovHydro1, self).__init__(*args, **kw_args)
    # >>> gov_hydro1



class GovHydroPID2(TurbineGovernor):
    pass
    # <<< gov_hydro_pid2
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'GovHydroPID2' instance.

        """


        super(GovHydroPID2, self).__init__(*args, **kw_args)
    # >>> gov_hydro_pid2



class GovWT4T(TurbineGovernor):
    pass
    # <<< gov_wt4_t
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'GovWT4T' instance.

        """


        super(GovWT4T, self).__init__(*args, **kw_args)
    # >>> gov_wt4_t



class GovSteamEU(TurbineGovernor):
    pass
    # <<< gov_steam_eu
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'GovSteamEU' instance.

        """


        super(GovSteamEU, self).__init__(*args, **kw_args)
    # >>> gov_steam_eu



class GovHydro0(TurbineGovernor):
    pass
    # <<< gov_hydro0
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'GovHydro0' instance.

        """


        super(GovHydro0, self).__init__(*args, **kw_args)
    # >>> gov_hydro0



class GovGASTWD(TurbineGovernor):
    pass
    # <<< gov_gastwd
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'GovGASTWD' instance.

        """


        super(GovGASTWD, self).__init__(*args, **kw_args)
    # >>> gov_gastwd



class GovGAST2(TurbineGovernor):
    pass
    # <<< gov_gast2
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'GovGAST2' instance.

        """


        super(GovGAST2, self).__init__(*args, **kw_args)
    # >>> gov_gast2



# <<< turbine_governors
# @generated
# >>> turbine_governors
