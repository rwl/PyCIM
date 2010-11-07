# Copyright (C) 2010 Richard Lincoln
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA, USA

from CIM14.Dynamics.TurbineGovernors.TurbineGovernor import TurbineGovernor

class GovCT1(TurbineGovernor):
    """General model for any prime mover with a PID governor, used primarily for combustion turbine and combined cycle units.
    """

    def __init__(self, tdgov=0.0, tb=0.0, kdgov=0.0, db=0.0, vmin=0.0, kturb=0.0, teng=0.0, minerr=0.0, aset=0.0, maxerr=0.0, tsa=0.0, mwbase=0.0, wfspd=False, kiload=0.0, kpgov=0.0, ldref=0.0, vmax=0.0, rup=0.0, r=0.0, tpelec=0.0, ta=0.0, ropen=0.0, kimw=0.0, ka=0.0, rdown=0.0, rclose=0.0, dm=0.0, tsb=0.0, kigov=0.0, kpload=0.0, tfload=0.0, tact=0.0, tc=0.0, wfnl=0.0, pmwset=0.0, rselect=False, **kw_args):
        """Initializes a new 'GovCT1' instance.

        @param tdgov: Governor derivative controller time constant 
        @param tb: Turbine lag time constant, sec.  (&gt;0.) 
        @param kdgov: Governor derivative gain 
        @param db: Speed governor dead band 
        @param vmin: Minimum valve position limit 
        @param kturb: Turbine gain  (&gt;0.) 
        @param teng: Transport time delay for diesel engine 
        @param minerr: Minimum value for speed error signal 
        @param aset: Acceleration limiter setpoint 
        @param maxerr: Maximum value for speed error signal 
        @param tsa: Temperature detection lead time constant 
        @param mwbase: Base for power values (&gt; 0.) 
        @param wfspd: Switch for fuel source characteristic = 0 for fuel flow independent of speed = 1 fuel flow proportional to speed 
        @param kiload: Load limiter integral gain for PI controller 
        @param kpgov: Governor proportional gain 
        @param ldref: Load limiter reference value 
        @param vmax: Maximum valve position limit 
        @param rup: Maximum rate of load limit increase 
        @param r: Permanent droop 
        @param tpelec: Electrical power transducer time constant, sec. (&gt;0.) 
        @param ta: Acceleration limiter time constant (&gt;0.) 
        @param ropen: Maximum valve opening rate 
        @param kimw: Power controller (reset) gain 
        @param ka: Acceleration limiter gain 
        @param rdown: Maximum rate of load limit decrease 
        @param rclose: Minimum valve closing rate 
        @param dm: Speed sensitivity coefficient 
        @param tsb: Temperature detection lag time constant 
        @param kigov: Governor integral gain 
        @param kpload: Load limiter proportional gain for PI controller 
        @param tfload: Load Limiter time constant (&gt;0.) 
        @param tact: Actuator time constant 
        @param tc: Turbine lead time constant, sec. 
        @param wfnl: No load fuel flow 
        @param pmwset: Power controller setpoint 
        @param rselect: Feedback signal for droop  = 1 electrical power = 0 none (isochronous governor) = -1 fuel valve stroke ( true stroke) = -2 governor output ( requested stroke) 
        """
        #: Governor derivative controller time constant
        self.tdgov = tdgov

        #: Turbine lag time constant, sec.  (&gt;0.)
        self.tb = tb

        #: Governor derivative gain
        self.kdgov = kdgov

        #: Speed governor dead band
        self.db = db

        #: Minimum valve position limit
        self.vmin = vmin

        #: Turbine gain  (&gt;0.)
        self.kturb = kturb

        #: Transport time delay for diesel engine
        self.teng = teng

        #: Minimum value for speed error signal
        self.minerr = minerr

        #: Acceleration limiter setpoint
        self.aset = aset

        #: Maximum value for speed error signal
        self.maxerr = maxerr

        #: Temperature detection lead time constant
        self.tsa = tsa

        #: Base for power values (&gt; 0.)
        self.mwbase = mwbase

        #: Switch for fuel source characteristic = 0 for fuel flow independent of speed = 1 fuel flow proportional to speed
        self.wfspd = wfspd

        #: Load limiter integral gain for PI controller
        self.kiload = kiload

        #: Governor proportional gain
        self.kpgov = kpgov

        #: Load limiter reference value
        self.ldref = ldref

        #: Maximum valve position limit
        self.vmax = vmax

        #: Maximum rate of load limit increase
        self.rup = rup

        #: Permanent droop
        self.r = r

        #: Electrical power transducer time constant, sec. (&gt;0.)
        self.tpelec = tpelec

        #: Acceleration limiter time constant (&gt;0.)
        self.ta = ta

        #: Maximum valve opening rate
        self.ropen = ropen

        #: Power controller (reset) gain
        self.kimw = kimw

        #: Acceleration limiter gain
        self.ka = ka

        #: Maximum rate of load limit decrease
        self.rdown = rdown

        #: Minimum valve closing rate
        self.rclose = rclose

        #: Speed sensitivity coefficient
        self.dm = dm

        #: Temperature detection lag time constant
        self.tsb = tsb

        #: Governor integral gain
        self.kigov = kigov

        #: Load limiter proportional gain for PI controller
        self.kpload = kpload

        #: Load Limiter time constant (&gt;0.)
        self.tfload = tfload

        #: Actuator time constant
        self.tact = tact

        #: Turbine lead time constant, sec.
        self.tc = tc

        #: No load fuel flow
        self.wfnl = wfnl

        #: Power controller setpoint
        self.pmwset = pmwset

        #: Feedback signal for droop  = 1 electrical power = 0 none (isochronous governor) = -1 fuel valve stroke ( true stroke) = -2 governor output ( requested stroke)
        self.rselect = rselect

        super(GovCT1, self).__init__(**kw_args)

