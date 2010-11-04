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

class InfoQuestion(Document):
    """Questions and answers associated with a type of document for purposes of clarification. Questions may be predefined or ad hoc.
    """

    def __init__(self, questionRemark='', answer='', questionCategory='', questionCode='', answerDateTime='', questionText='', answerRemark='', *args, **kw_args):
        """Initializes a new 'InfoQuestion' instance.

        @param questionRemark: Remarks to qualify the question in this situation. 
        @param answer: Answer to question. 
        @param questionCategory: The category of the question. 
        @param questionCode: The question code. If blank, refer to questionText. 
        @param answerDateTime: The date and time the quesiton was answered. 
        @param questionText: For non-coded questions, the question is provided here. 
        @param answerRemark: Remarks to qualify the answer. 
        """
        #: Remarks to qualify the question in this situation.
        self.questionRemark = questionRemark

        #: Answer to question.
        self.answer = answer

        #: The category of the question.
        self.questionCategory = questionCategory

        #: The question code. If blank, refer to questionText.
        self.questionCode = questionCode

        #: The date and time the quesiton was answered.
        self.answerDateTime = answerDateTime

        #: For non-coded questions, the question is provided here.
        self.questionText = questionText

        #: Remarks to qualify the answer.
        self.answerRemark = answerRemark

        super(InfoQuestion, self).__init__(*args, **kw_args)

