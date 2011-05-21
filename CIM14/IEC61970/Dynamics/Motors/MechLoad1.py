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

from CIM14.IEC61970.Dynamics.Motors.MechanicalLoad import MechanicalLoad

class MechLoad1(MechanicalLoad):
    """Mechanical load model 1
    """

    def __init__(self, e=0.0, b=0.0, d=0.0, a=0.0, *args, **kw_args):
        """Initialises a new 'MechLoad1' instance.

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

        super(MechLoad1, self).__init__(*args, **kw_args)

    _attrs = ["e", "b", "d", "a"]
    _attr_types = {"e": float, "b": float, "d": float, "a": float}
    _defaults = {"e": 0.0, "b": 0.0, "d": 0.0, "a": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

