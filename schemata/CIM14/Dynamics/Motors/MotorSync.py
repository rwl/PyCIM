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

