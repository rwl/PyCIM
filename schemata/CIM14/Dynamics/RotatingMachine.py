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

from CIM14.IEC61970.Wires.RegulatingCondEq import RegulatingCondEq

class RotatingMachine(RegulatingCondEq):
    """A rotating machine which may be used as a generator or motor.
    """

    def __init__(self, parametersFormType='timeConstantReactance', d=0.0, rs=0.0, h=0.0, s12=0.0, ratedS=0.0, s1=0.0, xls=0.0, mechanicalLoad0=None, **kw_args):
        """Initializes a new 'RotatingMachine' instance.

        @param parametersFormType: Values are: "timeConstantReactance", "equivalentCircuit"
        @param d: Damping torque coefficient. <b>D</b> represents a linearized approximation of damping torque effects. This value is often zero when the sources of damping torques (generator damper windings, load damping effects, etc.) are modeled in detail 
        @param rs: Stator (armature) resistance (&gt;= 0.) - Equivalent resistance when used for GenEquiv model 
        @param h: Inertia constant of generator or motor and mechanical load (&gt;0). <b>H</b> is the stored energy in the rotating mass. For a generator, this includes the <b>generator plus all other elements (turbine, exciter) on the same shaft</b> and has units of MW-sec. For a motor, it includes the motor plus its mechanical load. Conventional units are per unit on the generator MVA base, usually expressed as MW-sec./MVA or just sec. 
        @param s12: Saturation factor at 120% of rated term.voltage (&gt;=S1) 
        @param ratedS: Nameplate apparent power rating for the unit 
        @param s1: Saturation factor at rated term. voltage (&gt;= 0.) 
        @param xls: Stator leakage reactance (&gt; 0.) 
        @param mechanicalLoad0:
        """
        #: Values are: "timeConstantReactance", "equivalentCircuit"
        self.parametersFormType = parametersFormType

        #: Damping torque coefficient. <b>D</b> represents a linearized approximation of damping torque effects. This value is often zero when the sources of damping torques (generator damper windings, load damping effects, etc.) are modeled in detail
        self.d = d

        #: Stator (armature) resistance (&gt;= 0.) - Equivalent resistance when used for GenEquiv model
        self.rs = rs

        #: Inertia constant of generator or motor and mechanical load (&gt;0). <b>H</b> is the stored energy in the rotating mass. For a generator, this includes the <b>generator plus all other elements (turbine, exciter) on the same shaft</b> and has units of MW-sec. For a motor, it includes the motor plus its mechanical load. Conventional units are per unit on the generator MVA base, usually expressed as MW-sec./MVA or just sec.
        self.h = h

        #: Saturation factor at 120% of rated term.voltage (&gt;=S1)
        self.s12 = s12

        #: Nameplate apparent power rating for the unit
        self.ratedS = ratedS

        #: Saturation factor at rated term. voltage (&gt;= 0.)
        self.s1 = s1

        #: Stator leakage reactance (&gt; 0.)
        self.xls = xls

        self._mechanicalLoad0 = []
        self.mechanicalLoad0 = [] if mechanicalLoad0 is None else mechanicalLoad0

        super(RotatingMachine, self).__init__(**kw_args)

    def getmechanicalLoad0(self):
        
        return self._mechanicalLoad0

    def setmechanicalLoad0(self, value):
        for p in self._mechanicalLoad0:
            filtered = [q for q in p.rotatingMachine0 if q != self]
            self._mechanicalLoad0._rotatingMachine0 = filtered
        for r in value:
            if self not in r._rotatingMachine0:
                r._rotatingMachine0.append(self)
        self._mechanicalLoad0 = value

    mechanicalLoad0 = property(getmechanicalLoad0, setmechanicalLoad0)

    def addmechanicalLoad0(self, *mechanicalLoad0):
        for obj in mechanicalLoad0:
            if self not in obj._rotatingMachine0:
                obj._rotatingMachine0.append(self)
            self._mechanicalLoad0.append(obj)

    def removemechanicalLoad0(self, *mechanicalLoad0):
        for obj in mechanicalLoad0:
            if self in obj._rotatingMachine0:
                obj._rotatingMachine0.remove(self)
            self._mechanicalLoad0.remove(obj)

