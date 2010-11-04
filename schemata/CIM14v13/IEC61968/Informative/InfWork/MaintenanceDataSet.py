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

from CIM14v13.IEC61968.Informative.InfAssets.ProcedureDataSet import ProcedureDataSet

class MaintenanceDataSet(ProcedureDataSet):
    """The result of a maintenance activity, a type of Procedure, for a given attribute of an asset is documentated in an MaintenanceDataSet.
    """

    def __init__(self, conditionBefore='', maintCode='', conditionAfter='', **kw_args):
        """Initializes a new 'MaintenanceDataSet' instance.

        @param conditionBefore: Description of the condition of the asset just prior to maintenance being performed. 
        @param maintCode: Code for the type of maintenance performed. 
        @param conditionAfter: Condition of asset just following maintenance procedure. 
        """
        #: Description of the condition of the asset just prior to maintenance being performed.
        self.conditionBefore = conditionBefore

        #: Code for the type of maintenance performed.
        self.maintCode = maintCode

        #: Condition of asset just following maintenance procedure.
        self.conditionAfter = conditionAfter

        super(MaintenanceDataSet, self).__init__(**kw_args)

