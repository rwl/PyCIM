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

from CIM15.IEC61970.Core.IdentifiedObject import IdentifiedObject

class Limit(IdentifiedObject):
    """Specifies one limit value for a Measurement. A Measurement typically has several limits that are kept together by the LimitSet class. The actual meaning and use of a Limit instance (i.e., if it is an alarm or warning limit or if it is a high or low limit) is not captured in the Limit class. However the name of a Limit instance may indicate both meaning and use.Specifies one limit value for a Measurement. A Measurement typically has several limits that are kept together by the LimitSet class. The actual meaning and use of a Limit instance (i.e., if it is an alarm or warning limit or if it is a high or low limit) is not captured in the Limit class. However the name of a Limit instance may indicate both meaning and use.
    """

    def __init__(self, Procedures=None, *args, **kw_args):
        """Initialises a new 'Limit' instance.

        @param Procedures:
        """
        self._Procedures = []
        self.Procedures = [] if Procedures is None else Procedures

        super(Limit, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["Procedures"]
    _many_refs = ["Procedures"]

    def getProcedures(self):
        
        return self._Procedures

    def setProcedures(self, value):
        for p in self._Procedures:
            filtered = [q for q in p.Limits if q != self]
            self._Procedures._Limits = filtered
        for r in value:
            if self not in r._Limits:
                r._Limits.append(self)
        self._Procedures = value

    Procedures = property(getProcedures, setProcedures)

    def addProcedures(self, *Procedures):
        for obj in Procedures:
            if self not in obj._Limits:
                obj._Limits.append(self)
            self._Procedures.append(obj)

    def removeProcedures(self, *Procedures):
        for obj in Procedures:
            if self in obj._Limits:
                obj._Limits.remove(self)
            self._Procedures.remove(obj)

