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

from CIM14.IEC61970.Core.Equipment import Equipment

class CurrentTransformer(Equipment):
    """Instrument transformer used to measure electrical qualities of the circuit that is being protected and/or monitored. Typically used as current transducer for the purpose of metering or protection. A typical secondary current rating would be 5A.
    """

    def __init__(self, maxRatio=0.0, accuracyClass='', coreCount=0, ctClass='', usage='', accuracyLimit='', **kw_args):
        """Initializes a new 'CurrentTransformer' instance.

        @param maxRatio: For multi-ratio CT's, the maximum permissable ratio attainable. 
        @param accuracyClass: CT accuracy classification. 
        @param coreCount: Number of cores. 
        @param ctClass: CT classification; i.e. class 10P. 
        @param usage: Intended usage of the CT; i.e. metering, protection. 
        @param accuracyLimit: Percent of rated current for which the CT remains accurate within specified limits. 
        """
        #: For multi-ratio CT's, the maximum permissable ratio attainable.
        self.maxRatio = maxRatio

        #: CT accuracy classification.
        self.accuracyClass = accuracyClass

        #: Number of cores.
        self.coreCount = coreCount

        #: CT classification; i.e. class 10P.
        self.ctClass = ctClass

        #: Intended usage of the CT; i.e. metering, protection.
        self.usage = usage

        #: Percent of rated current for which the CT remains accurate within specified limits.
        self.accuracyLimit = accuracyLimit

        super(CurrentTransformer, self).__init__(**kw_args)

