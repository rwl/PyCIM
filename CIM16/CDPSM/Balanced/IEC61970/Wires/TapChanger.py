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

from CIM16.CDPSM.Balanced.IEC61970.Core.IdentifiedObject import IdentifiedObject

class TapChanger(IdentifiedObject):
    """Mechanism for changing transformer winding tap positions.
    """

    def __init__(self, neutralU=0.0, lowStep=0, normalStep=0, neutralStep=0, highStep=0, *args, **kw_args):
        """Initialises a new 'TapChanger' instance.

        @param neutralU: Voltage at which the winding operates at the neutral tap setting. 
        @param lowStep: Lowest possible tap step position, retard from neutral 
        @param normalStep: The tap step position used in 'normal' network operation for this winding. For a 'Fixed' tap changer indicates the current physical tap setting. 
        @param neutralStep: The neutral tap step position for this winding. 
        @param highStep: Highest possible tap step position, advance from neutral 
        """
        #: Voltage at which the winding operates at the neutral tap setting.
        self.neutralU = neutralU

        #: Lowest possible tap step position, retard from neutral
        self.lowStep = lowStep

        #: The tap step position used in 'normal' network operation for this winding. For a 'Fixed' tap changer indicates the current physical tap setting.
        self.normalStep = normalStep

        #: The neutral tap step position for this winding.
        self.neutralStep = neutralStep

        #: Highest possible tap step position, advance from neutral
        self.highStep = highStep

        super(TapChanger, self).__init__(*args, **kw_args)

    _attrs = ["neutralU", "lowStep", "normalStep", "neutralStep", "highStep"]
    _attr_types = {"neutralU": float, "lowStep": int, "normalStep": int, "neutralStep": int, "highStep": int}
    _defaults = {"neutralU": 0.0, "lowStep": 0, "normalStep": 0, "neutralStep": 0, "highStep": 0}
    _enums = {}
    _refs = []
    _many_refs = []

