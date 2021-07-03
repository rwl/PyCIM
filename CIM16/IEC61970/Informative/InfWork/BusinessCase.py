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

from CIM16.IEC61968.Common.Document import Document

class BusinessCase(Document):
    """Business justification for capital expenditures, usually addressing operations and maintenance costs as well.Business justification for capital expenditures, usually addressing operations and maintenance costs as well.
    """

    def __init__(self, corporateCode='', Projects=None, Works=None, *args, **kw_args):
        """Initialises a new 'BusinessCase' instance.

        @param corporateCode: A codified representation of the business case (i.e., codes for highway relocation, replace substation transformers, etc.). 
        @param Projects:
        @param Works:
        """
        #: A codified representation of the business case (i.e., codes for highway relocation, replace substation transformers, etc.).
        self.corporateCode = corporateCode

        self._Projects = []
        self.Projects = [] if Projects is None else Projects

        self._Works = []
        self.Works = [] if Works is None else Works

        super(BusinessCase, self).__init__(*args, **kw_args)

    _attrs = ["corporateCode"]
    _attr_types = {"corporateCode": str}
    _defaults = {"corporateCode": ''}
    _enums = {}
    _refs = ["Projects", "Works"]
    _many_refs = ["Projects", "Works"]

    def getProjects(self):
        
        return self._Projects

    def setProjects(self, value):
        for x in self._Projects:
            x.BusinessCase = None
        for y in value:
            y._BusinessCase = self
        self._Projects = value

    Projects = property(getProjects, setProjects)

    def addProjects(self, *Projects):
        for obj in Projects:
            obj.BusinessCase = self

    def removeProjects(self, *Projects):
        for obj in Projects:
            obj.BusinessCase = None

    def getWorks(self):
        
        return self._Works

    def setWorks(self, value):
        for x in self._Works:
            x.BusinessCase = None
        for y in value:
            y._BusinessCase = self
        self._Works = value

    Works = property(getWorks, setWorks)

    def addWorks(self, *Works):
        for obj in Works:
            obj.BusinessCase = self

    def removeWorks(self, *Works):
        for obj in Works:
            obj.BusinessCase = None

