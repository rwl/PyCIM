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

class DiagnosisDataSet(ProcedureDataSet):
    """The result of a problem (typically an asset failure) diagnosis.
    """

    def __init__(self, phaseCode='BC', failureMode='', rootRemark='', rootCause='', finalOrigin='', finalCause='', preliminaryCode='', effect='', preliminaryRemark='', rootOrigin='', finalCode='', finalRemark='', preliminaryDateTime='', **kw_args):
        """Initializes a new 'DiagnosisDataSet' instance.

        @param phaseCode: Phase(s) diagnosed. Values are: "BC", "AB", "B", "AC", "ABC", "splitSecondary1N", "ABN", "ABCN", "CN", "AN", "splitSecondary12N", "BCN", "splitSecondary2N", "ACN", "A", "C", "N", "BN"
        @param failureMode: Failuer mode, for example: Failure to Insulate; Failure to conduct; Failure to contain oil; Failure to provide ground plane; Other. 
        @param rootRemark: Remarks pertaining to root cause findings during problem diagnosis. 
        @param rootCause: Root cause of problem determined during diagnosis. 
        @param finalOrigin: Origin of problem determined during diagnosis. 
        @param finalCause: Cause of problem determined during diagnosis. 
        @param preliminaryCode: Code for problem category determined during preliminary assessment. 
        @param effect: Effect of problem. 
        @param preliminaryRemark: Remarks pertaining to preliminary assessment of problem. 
        @param rootOrigin: Root origin of problem determined during diagnosis. 
        @param finalCode: Code for diagnosed probem category. 
        @param finalRemark: Remarks pertaining to findings during problem diagnosis. 
        @param preliminaryDateTime: Date and time preliminary assessment of problem was performed. 
        """
        #: Phase(s) diagnosed.Values are: "BC", "AB", "B", "AC", "ABC", "splitSecondary1N", "ABN", "ABCN", "CN", "AN", "splitSecondary12N", "BCN", "splitSecondary2N", "ACN", "A", "C", "N", "BN"
        self.phaseCode = phaseCode

        #: Failuer mode, for example: Failure to Insulate; Failure to conduct; Failure to contain oil; Failure to provide ground plane; Other.
        self.failureMode = failureMode

        #: Remarks pertaining to root cause findings during problem diagnosis.
        self.rootRemark = rootRemark

        #: Root cause of problem determined during diagnosis.
        self.rootCause = rootCause

        #: Origin of problem determined during diagnosis.
        self.finalOrigin = finalOrigin

        #: Cause of problem determined during diagnosis.
        self.finalCause = finalCause

        #: Code for problem category determined during preliminary assessment.
        self.preliminaryCode = preliminaryCode

        #: Effect of problem.
        self.effect = effect

        #: Remarks pertaining to preliminary assessment of problem.
        self.preliminaryRemark = preliminaryRemark

        #: Root origin of problem determined during diagnosis.
        self.rootOrigin = rootOrigin

        #: Code for diagnosed probem category.
        self.finalCode = finalCode

        #: Remarks pertaining to findings during problem diagnosis.
        self.finalRemark = finalRemark

        #: Date and time preliminary assessment of problem was performed.
        self.preliminaryDateTime = preliminaryDateTime

        super(DiagnosisDataSet, self).__init__(**kw_args)

