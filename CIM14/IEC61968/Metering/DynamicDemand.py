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

from CIM14.Element import Element

class DynamicDemand(Element):
    """Dynamic demand description. The formula by which demand is measured is an important underlying definition to the measurement. Generally speaking, all of the meters in a given utility will be configured to measure demand the same way. Nevertheless, it must be defined. An 'interval' of 60, 30, 15, 10, or 5 minutes must be defined to describe the interval of time over which usage is measured. When demand is defined to be DemandKind.rollingBlock, both an 'interval' and a 'subinterval' must be defined, where the 'subinterval' must be a multiple of the 'interval' which contains it. A common setting is '15-minute rolling block with 5-minute subintervals.'
    """

    def __init__(self, kind="logarithmic", interval=0.0, subInterval=0.0, *args, **kw_args):
        """Initialises a new 'DynamicDemand' instance.

        @param kind: Kind of demand. Values are: "logarithmic", "fixedBlock", "rollingBlock"
        @param interval: Demand interval. 
        @param subInterval: (if 'kind'=rollingBlock) Subinterval, must be multiple of 'interval' that contains it. 
        """
        #: Kind of demand. Values are: "logarithmic", "fixedBlock", "rollingBlock"
        self.kind = kind

        #: Demand interval.
        self.interval = interval

        #: (if 'kind'=rollingBlock) Subinterval, must be multiple of 'interval' that contains it.
        self.subInterval = subInterval

        super(DynamicDemand, self).__init__(*args, **kw_args)

    _attrs = ["kind", "interval", "subInterval"]
    _attr_types = {"kind": str, "interval": float, "subInterval": float}
    _defaults = {"kind": "logarithmic", "interval": 0.0, "subInterval": 0.0}
    _enums = {"kind": "DemandKind"}
    _refs = []
    _many_refs = []

