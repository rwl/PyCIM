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

from CIM14.IEC61970.Dynamics.VoltageCompensator.VoltageCompensator import VoltageCompensator

class VcompIEEE(VoltageCompensator):
    """IEEE Voltage Compensation Model
    """

    def __init__(self, xcomp=0.0, rcomp=0.0, *args, **kw_args):
        """Initialises a new 'VcompIEEE' instance.

        @param xcomp: Compensating (compounding) reactance 
        @param rcomp: Compensating (compounding) resistance 
        """
        #: Compensating (compounding) reactance
        self.xcomp = xcomp

        #: Compensating (compounding) resistance
        self.rcomp = rcomp

        super(VcompIEEE, self).__init__(*args, **kw_args)

    _attrs = ["xcomp", "rcomp"]
    _attr_types = {"xcomp": float, "rcomp": float}
    _defaults = {"xcomp": 0.0, "rcomp": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

