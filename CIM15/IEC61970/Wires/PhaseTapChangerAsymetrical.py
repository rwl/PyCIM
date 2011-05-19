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

from CIM15.IEC61970.Wires.PhaseTapChangerNonLinear import PhaseTapChangerNonLinear

class PhaseTapChangerAsymetrical(PhaseTapChangerNonLinear):
    """In a PhaseTapChangerAsymetrical tranformer the difference voltage vector adds to the primary side voltage. The angle between the primary side voltage and the difference voltage is named the winding connection angle. The phase shift, &alpha;, depends on both the difference voltage magnitude, &Delta;U, and the winding connection angle.In a PhaseTapChangerAsymetrical tranformer the difference voltage vector adds to the primary side voltage. The angle between the primary side voltage and the difference voltage is named the winding connection angle. The phase shift, &alpha;, depends on both the difference voltage magnitude, &Delta;U, and the winding connection angle.
    """

    def __init__(self, windingConnectionAngle=0.0, *args, **kw_args):
        """Initialises a new 'PhaseTapChangerAsymetrical' instance.

        @param windingConnectionAngle: The phase angle between the in-phase winding and the out-of -phase winding used for creating phase shift.   It is only possible to have a symmemtrical transformer if this angle is 90 degrees. 
        """
        #: The phase angle between the in-phase winding and the out-of -phase winding used for creating phase shift.   It is only possible to have a symmemtrical transformer if this angle is 90 degrees.
        self.windingConnectionAngle = windingConnectionAngle

        super(PhaseTapChangerAsymetrical, self).__init__(*args, **kw_args)

    _attrs = ["windingConnectionAngle"]
    _attr_types = {"windingConnectionAngle": float}
    _defaults = {"windingConnectionAngle": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

