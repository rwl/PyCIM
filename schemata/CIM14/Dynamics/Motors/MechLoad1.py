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

from CIM14.Dynamics.Motors.MechanicalLoad import MechanicalLoad

class MechLoad1(MechanicalLoad):
    """Mechanical load model 1
    """

    def __init__(self, e=0.0, b=0.0, d=0.0, a=0.0, **kw_args):
        """Initializes a new 'MechLoad1' instance.

        @param e: Exponent 
        @param b: Speed squared coefficient 
        @param d: Speed to the exponent coefficient 
        @param a: Speed squared coefficient 
        """
        #: Exponent
        self.e = e

        #: Speed squared coefficient
        self.b = b

        #: Speed to the exponent coefficient
        self.d = d

        #: Speed squared coefficient
        self.a = a

        super(MechLoad1, self).__init__(**kw_args)

