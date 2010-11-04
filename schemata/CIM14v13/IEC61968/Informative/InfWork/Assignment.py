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

from CIM14v13.IEC61968.Common.Document import Document

class Assignment(Document):
    """An assignment is given to an ErpPerson, Crew, Organisation, Equipment Item, Tool, etc. and may be used to perform Work, WorkTasks, Procedures, etc. TimeSchedules may be set up directly for Assignments or indirectly via the associated WorkTask. Note that these associations are all inherited through the recursive relationship on Document.
    """

    def __init__(self, Crews=None, effectivePeriod=None, **kw_args):
        """Initializes a new 'Assignment' instance.

        @param Crews: All Crews having this Assignment.
        @param effectivePeriod: Period between the assignment becoming effective and its expiration.
        """
        self._Crews = []
        self.Crews = [] if Crews is None else Crews

        self.effectivePeriod = effectivePeriod

        super(Assignment, self).__init__(**kw_args)

    def getCrews(self):
        """All Crews having this Assignment.
        """
        return self._Crews

    def setCrews(self, value):
        for p in self._Crews:
            filtered = [q for q in p.Assignments if q != self]
            self._Crews._Assignments = filtered
        for r in value:
            if self not in r._Assignments:
                r._Assignments.append(self)
        self._Crews = value

    Crews = property(getCrews, setCrews)

    def addCrews(self, *Crews):
        for obj in Crews:
            if self not in obj._Assignments:
                obj._Assignments.append(self)
            self._Crews.append(obj)

    def removeCrews(self, *Crews):
        for obj in Crews:
            if self in obj._Assignments:
                obj._Assignments.remove(self)
            self._Crews.remove(obj)

    # Period between the assignment becoming effective and its expiration.
    effectivePeriod = None

