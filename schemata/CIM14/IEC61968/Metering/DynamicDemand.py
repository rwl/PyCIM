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

from CIM14.Element import Element

class DynamicDemand(Element):
    """Dynamic demand description. The formula by which demand is measured is an important underlying definition to the measurement. Generally speaking, all of the meters in a given utility will be configured to measure demand the same way. Nevertheless, it must be defined. An 'interval' of 60, 30, 15, 10, or 5 minutes must be defined to describe the interval of time over which usage is measured. When demand is defined to be DemandKind.rollingBlock, both an 'interval' and a 'subinterval' must be defined, where the 'subinterval' must be a multiple of the 'interval' which contains it. A common setting is '15-minute rolling block with 5-minute subintervals.'
    """

    def __init__(self, kind='logarithmic', interval=0.0, subInterval=0.0, **kw_args):
        """Initializes a new 'DynamicDemand' instance.

        @param kind: Kind of demand. Values are: "logarithmic", "fixedBlock", "rollingBlock"
        @param interval: Demand interval. 
        @param subInterval: (if 'kind'=rollingBlock) Subinterval, must be multiple of 'interval' that contains it. 
        """
        #: Kind of demand.Values are: "logarithmic", "fixedBlock", "rollingBlock"
        self.kind = kind

        #: Demand interval.
        self.interval = interval

        #: (if 'kind'=rollingBlock) Subinterval, must be multiple of 'interval' that contains it.
        self.subInterval = subInterval

        super(DynamicDemand, self).__init__(**kw_args)

