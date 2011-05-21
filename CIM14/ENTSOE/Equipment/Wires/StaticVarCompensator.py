# Copyright (C) 2010-2011 Richard Lincoln
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

from CIM14.ENTSOE.Equipment.Wires.RegulatingCondEq import RegulatingCondEq

class StaticVarCompensator(RegulatingCondEq):
    """A facility for providing variable and controllable shunt reactive power. The SVC typically consists of a stepdown transformer, filter, thyristor-controlled reactor, and thyristor-switched capacitor arms.  The SVC may operate in fixed MVar output mode or in voltage control mode.  When in voltage control mode, the output of the SVC will be proportional to the deviation of voltage at the controlled bus from the voltage setpoint.  The SVC characteristic slope defines the proportion.  If the voltage at the controlled bus is equal to the voltage setpoint, the SVC MVar output is zero.-  The value of the “inductiveRating” attribute must always be negative. -  The value of the “capactiveRating” attribute must always be positive. -  [R9.3] is satisfied by navigation to ConnectivityNode and Substation 
    """

    def __init__(self, voltageSetPoint=0.0, capacitiveRating=0.0, slope=0.0, inductiveRating=0.0, sVCControlMode="voltage", *args, **kw_args):
        """Initialises a new 'StaticVarCompensator' instance.

        @param voltageSetPoint: The reactive power output of the SVC is proportional to the difference between the voltage at the regulated bus and the voltage setpoint.  When the regulated bus voltage is equal to the voltage setpoint, the reactive power output is zero. 
        @param capacitiveRating: Maximum available capacitive reactive power 
        @param slope: The characteristics slope of an SVC defines how the reactive power output changes in proportion to the difference between the regulated bus voltage and the voltage setpoint. 
        @param inductiveRating: Maximum available inductive reactive power 
        @param sVCControlMode: SVC control mode. Values are: "voltage", "reactivePower", "off"
        """
        #: The reactive power output of the SVC is proportional to the difference between the voltage at the regulated bus and the voltage setpoint.  When the regulated bus voltage is equal to the voltage setpoint, the reactive power output is zero.
        self.voltageSetPoint = voltageSetPoint

        #: Maximum available capacitive reactive power
        self.capacitiveRating = capacitiveRating

        #: The characteristics slope of an SVC defines how the reactive power output changes in proportion to the difference between the regulated bus voltage and the voltage setpoint.
        self.slope = slope

        #: Maximum available inductive reactive power
        self.inductiveRating = inductiveRating

        #: SVC control mode. Values are: "voltage", "reactivePower", "off"
        self.sVCControlMode = sVCControlMode

        super(StaticVarCompensator, self).__init__(*args, **kw_args)

    _attrs = ["voltageSetPoint", "capacitiveRating", "slope", "inductiveRating", "sVCControlMode"]
    _attr_types = {"voltageSetPoint": float, "capacitiveRating": float, "slope": float, "inductiveRating": float, "sVCControlMode": str}
    _defaults = {"voltageSetPoint": 0.0, "capacitiveRating": 0.0, "slope": 0.0, "inductiveRating": 0.0, "sVCControlMode": "voltage"}
    _enums = {"sVCControlMode": "SVCControlMode"}
    _refs = []
    _many_refs = []

