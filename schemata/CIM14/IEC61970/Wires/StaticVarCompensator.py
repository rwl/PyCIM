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

class StaticVarCompensator(RegulatingCondEq):
    """A facility for providing variable and controllable shunt reactive power. The SVC typically consists of a stepdown transformer, filter, thyristor-controlled reactor, and thyristor-switched capacitor arms.  The SVC may operate in fixed MVar output mode or in voltage control mode.  When in voltage control mode, the output of the SVC will be proportional to the deviation of voltage at the controlled bus from the voltage setpoint.  The SVC characteristic slope defines the proportion.  If the voltage at the controlled bus is equal to the voltage setpoint, the SVC MVar output is zero.
    """

    def __init__(self, sVCControlMode='reactivePower', voltageSetPoint=0.0, capacitiveRating=0.0, inductiveRating=0.0, slope=0.0, **kw_args):
        """Initializes a new 'StaticVarCompensator' instance.

        @param sVCControlMode: SVC control mode. Values are: "reactivePower", "off", "voltage"
        @param voltageSetPoint: The reactive power output of the SVC is proportional to the difference between the voltage at the regulated bus and the voltage setpoint.  When the regulated bus voltage is equal to the voltage setpoint, the reactive power output is zero. 
        @param capacitiveRating: Maximum available capacitive reactive power 
        @param inductiveRating: Maximum available inductive reactive power 
        @param slope: The characteristics slope of an SVC defines how the reactive power output changes in proportion to the difference between the regulated bus voltage and the voltage setpoint. 
        """
        #: SVC control mode.Values are: "reactivePower", "off", "voltage"
        self.sVCControlMode = sVCControlMode

        #: The reactive power output of the SVC is proportional to the difference between the voltage at the regulated bus and the voltage setpoint.  When the regulated bus voltage is equal to the voltage setpoint, the reactive power output is zero.
        self.voltageSetPoint = voltageSetPoint

        #: Maximum available capacitive reactive power
        self.capacitiveRating = capacitiveRating

        #: Maximum available inductive reactive power
        self.inductiveRating = inductiveRating

        #: The characteristics slope of an SVC defines how the reactive power output changes in proportion to the difference between the regulated bus voltage and the voltage setpoint.
        self.slope = slope

        super(StaticVarCompensator, self).__init__(**kw_args)

