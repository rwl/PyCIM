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

from CIM14.IEC61970.Core.Equipment import Equipment

class CurrentTransformer(Equipment):
    """Instrument transformer used to measure electrical qualities of the circuit that is being protected and/or monitored. Typically used as current transducer for the purpose of metering or protection. A typical secondary current rating would be 5A.
    """

    def __init__(self, maxRatio=0.0, accuracyClass='', coreCount=0, ctClass='', usage='', accuracyLimit='', *args, **kw_args):
        """Initialises a new 'CurrentTransformer' instance.

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

        super(CurrentTransformer, self).__init__(*args, **kw_args)

    _attrs = ["maxRatio", "accuracyClass", "coreCount", "ctClass", "usage", "accuracyLimit"]
    _attr_types = {"maxRatio": float, "accuracyClass": str, "coreCount": int, "ctClass": str, "usage": str, "accuracyLimit": str}
    _defaults = {"maxRatio": 0.0, "accuracyClass": '', "coreCount": 0, "ctClass": '', "usage": '', "accuracyLimit": ''}
    _enums = {}
    _refs = []
    _many_refs = []

