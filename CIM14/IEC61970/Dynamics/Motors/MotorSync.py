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

from CIM14.IEC61970.Wires.SynchronousMachine import SynchronousMachine

class MotorSync(SynchronousMachine):
    """A large industrial motor or group of similar motors.  They are represented as <b>generators with negative Pgen</b> in the static (power flow) data.
    """

    def __init__(self, synchronousMotorType="salientPole", *args, **kw_args):
        """Initialises a new 'MotorSync' instance.

        @param synchronousMotorType: The type of synchronous motor, such as round rotor or salient pole. Values are: "salientPole", "roundRotor"
        """
        #: The type of synchronous motor, such as round rotor or salient pole. Values are: "salientPole", "roundRotor"
        self.synchronousMotorType = synchronousMotorType

        super(MotorSync, self).__init__(*args, **kw_args)

    _attrs = ["synchronousMotorType"]
    _attr_types = {"synchronousMotorType": str}
    _defaults = {"synchronousMotorType": "salientPole"}
    _enums = {"synchronousMotorType": "SynchronousMotorType"}
    _refs = []
    _many_refs = []

