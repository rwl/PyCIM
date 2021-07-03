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

from CIM15.CDPSM.Asset.IEC61968.AssetModels.CableInfo import CableInfo

class ConcentricNeutralCableInfo(CableInfo):
    """Concentric neutral cable data.
    """

    def __init__(self, diameterOverNeutral=0.0, neutralStrandCount=0, *args, **kw_args):
        """Initialises a new 'ConcentricNeutralCableInfo' instance.

        @param diameterOverNeutral: Diameter over the concentric neutral strands. 
        @param neutralStrandCount: Number of concentric neutral strands. 
        """
        #: Diameter over the concentric neutral strands.
        self.diameterOverNeutral = diameterOverNeutral

        #: Number of concentric neutral strands.
        self.neutralStrandCount = neutralStrandCount

        super(ConcentricNeutralCableInfo, self).__init__(*args, **kw_args)

    _attrs = ["diameterOverNeutral", "neutralStrandCount"]
    _attr_types = {"diameterOverNeutral": float, "neutralStrandCount": int}
    _defaults = {"diameterOverNeutral": 0.0, "neutralStrandCount": 0}
    _enums = {}
    _refs = []
    _many_refs = []

