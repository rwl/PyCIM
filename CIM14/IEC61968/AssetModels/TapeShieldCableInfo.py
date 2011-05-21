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

from CIM14.IEC61968.AssetModels.CableInfo import CableInfo

class TapeShieldCableInfo(CableInfo):
    """Tape shield cable data.
    """

    def __init__(self, tapeThickness=0.0, tapeLap=0.0, *args, **kw_args):
        """Initialises a new 'TapeShieldCableInfo' instance.

        @param tapeThickness: Thickness of the tape shield, before wrapping. 
        @param tapeLap: Percentage of the tape shield width that overlaps in each wrap, typically 10% to 25%. 
        """
        #: Thickness of the tape shield, before wrapping.
        self.tapeThickness = tapeThickness

        #: Percentage of the tape shield width that overlaps in each wrap, typically 10% to 25%.
        self.tapeLap = tapeLap

        super(TapeShieldCableInfo, self).__init__(*args, **kw_args)

    _attrs = ["tapeThickness", "tapeLap"]
    _attr_types = {"tapeThickness": float, "tapeLap": float}
    _defaults = {"tapeThickness": 0.0, "tapeLap": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

