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

from CIM14.IEC61970.Wires.ProtectedSwitch import ProtectedSwitch

class LoadBreakSwitch(ProtectedSwitch):
    """A mechanical switching device capable of making, carrying, and breaking currents under normal operating conditions.
    """

    def __init__(self, ratedCurrent=0.0, *args, **kw_args):
        """Initialises a new 'LoadBreakSwitch' instance.

        @param ratedCurrent: Current carrying capacity of a wire or cable under stated thermal conditions. 
        """
        #: Current carrying capacity of a wire or cable under stated thermal conditions.
        self.ratedCurrent = ratedCurrent

        super(LoadBreakSwitch, self).__init__(*args, **kw_args)

    _attrs = ["ratedCurrent"]
    _attr_types = {"ratedCurrent": float}
    _defaults = {"ratedCurrent": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

