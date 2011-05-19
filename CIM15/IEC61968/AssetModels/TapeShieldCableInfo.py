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

from CIM15.IEC61968.AssetModels.CableInfo import CableInfo

class TapeShieldCableInfo(CableInfo):
    """Tape shield cable data.Tape shield cable data.
    """

    def __init__(self, tapeLap=0.0, tapeThickness=0.0, *args, **kw_args):
        """Initialises a new 'TapeShieldCableInfo' instance.

        @param tapeLap: Percentage of the tape shield width that overlaps in each wrap, typically 10% to 25%. 
        @param tapeThickness: Thickness of the tape shield, before wrapping. 
        """
        #: Percentage of the tape shield width that overlaps in each wrap, typically 10% to 25%.
        self.tapeLap = tapeLap

        #: Thickness of the tape shield, before wrapping.
        self.tapeThickness = tapeThickness

        super(TapeShieldCableInfo, self).__init__(*args, **kw_args)

    _attrs = ["tapeLap", "tapeThickness"]
    _attr_types = {"tapeLap": float, "tapeThickness": float}
    _defaults = {"tapeLap": 0.0, "tapeThickness": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

