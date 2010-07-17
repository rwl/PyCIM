# Copyright (C) 2010 Richard Lincoln
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

""" This package contains the core information classes that support work management and network extension planning applications.
"""

from cim.iec61968.common import Document

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim.work"

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#Work"

class Work(Document):
    """ Document used to request, initiate, track and record work. This is synonymous with Work Breakdown Structure (WBS), which is traversed through the (currently informative) recursive association of Work. Note that the work name is equal to the WBS name, which is given in the inherited 'name' attribute.
    """
    # <<< work
    # @generated
    def __init__(self, kind='service', request_date_time='', priority='', work_flow_steps=None, customers=None, work_tasks=None, erp_project_accounting=None, project=None, designs=None, business_case=None, work_billing_info=None, work_cost_details=None, request=None, **kw_args):
        """ Initialises a new 'Work' instance.
        """
        # Kind of work. Values are: "service", "reconnect", "disconnect", "other", "meter", "construction", "inspection", "maintenance"
        self.kind = 'service'

        # Date and time work was requested. 
        self.request_date_time = request_date_time

        # Priority of work. 
        self.priority = priority


        self._work_flow_steps = []
        if work_flow_steps is not None:
            self.work_flow_steps = work_flow_steps
        else:
            self.work_flow_steps = []

        self._customers = []
        if customers is not None:
            self.customers = customers
        else:
            self.customers = []

        self._work_tasks = []
        if work_tasks is not None:
            self.work_tasks = work_tasks
        else:
            self.work_tasks = []

        self._erp_project_accounting = None
        self.erp_project_accounting = erp_project_accounting

        self._project = None
        self.project = project

        self._designs = []
        if designs is not None:
            self.designs = designs
        else:
            self.designs = []

        self._business_case = None
        self.business_case = business_case

        self._work_billing_info = None
        self.work_billing_info = work_billing_info

        self._work_cost_details = []
        if work_cost_details is not None:
            self.work_cost_details = work_cost_details
        else:
            self.work_cost_details = []

        self._request = None
        self.request = request


        super(Work, self).__init__(**kw_args)
    # >>> work

    # <<< work_flow_steps
    # @generated
    def get_work_flow_steps(self):
        """ 
        """
        return self._work_flow_steps

    def set_work_flow_steps(self, value):
        for x in self._work_flow_steps:
            x._work = None
        for y in value:
            y._work = self
        self._work_flow_steps = value

    work_flow_steps = property(get_work_flow_steps, set_work_flow_steps)

    def add_work_flow_steps(self, *work_flow_steps):
        for obj in work_flow_steps:
            obj._work = self
            self._work_flow_steps.append(obj)

    def remove_work_flow_steps(self, *work_flow_steps):
        for obj in work_flow_steps:
            obj._work = None
            self._work_flow_steps.remove(obj)
    # >>> work_flow_steps

    # <<< customers
    # @generated
    def get_customers(self):
        """ All the customers for which this work is performed.
        """
        return self._customers

    def set_customers(self, value):
        for p in self._customers:
            filtered = [q for q in p.works if q != self]
            self._customers._works = filtered
        for r in value:
            if self not in r._works:
                r._works.append(self)
        self._customers = value

    customers = property(get_customers, set_customers)

    def add_customers(self, *customers):
        for obj in customers:
            if self not in obj._works:
                obj._works.append(self)
            self._customers.append(obj)

    def remove_customers(self, *customers):
        for obj in customers:
            if self in obj._works:
                obj._works.remove(self)
            self._customers.remove(obj)
    # >>> customers

    # <<< work_tasks
    # @generated
    def get_work_tasks(self):
        """ 
        """
        return self._work_tasks

    def set_work_tasks(self, value):
        for x in self._work_tasks:
            x._work = None
        for y in value:
            y._work = self
        self._work_tasks = value

    work_tasks = property(get_work_tasks, set_work_tasks)

    def add_work_tasks(self, *work_tasks):
        for obj in work_tasks:
            obj._work = self
            self._work_tasks.append(obj)

    def remove_work_tasks(self, *work_tasks):
        for obj in work_tasks:
            obj._work = None
            self._work_tasks.remove(obj)
    # >>> work_tasks

    # <<< erp_project_accounting
    # @generated
    def get_erp_project_accounting(self):
        """ 
        """
        return self._erp_project_accounting

    def set_erp_project_accounting(self, value):
        if self._erp_project_accounting is not None:
            filtered = [x for x in self.erp_project_accounting.works if x != self]
            self._erp_project_accounting._works = filtered

        self._erp_project_accounting = value
        if self._erp_project_accounting is not None:
            self._erp_project_accounting._works.append(self)

    erp_project_accounting = property(get_erp_project_accounting, set_erp_project_accounting)
    # >>> erp_project_accounting

    # <<< project
    # @generated
    def get_project(self):
        """ 
        """
        return self._project

    def set_project(self, value):
        if self._project is not None:
            filtered = [x for x in self.project.works if x != self]
            self._project._works = filtered

        self._project = value
        if self._project is not None:
            self._project._works.append(self)

    project = property(get_project, set_project)
    # >>> project

    # <<< designs
    # @generated
    def get_designs(self):
        """ 
        """
        return self._designs

    def set_designs(self, value):
        for x in self._designs:
            x._work = None
        for y in value:
            y._work = self
        self._designs = value

    designs = property(get_designs, set_designs)

    def add_designs(self, *designs):
        for obj in designs:
            obj._work = self
            self._designs.append(obj)

    def remove_designs(self, *designs):
        for obj in designs:
            obj._work = None
            self._designs.remove(obj)
    # >>> designs

    # <<< business_case
    # @generated
    def get_business_case(self):
        """ 
        """
        return self._business_case

    def set_business_case(self, value):
        if self._business_case is not None:
            filtered = [x for x in self.business_case.works if x != self]
            self._business_case._works = filtered

        self._business_case = value
        if self._business_case is not None:
            self._business_case._works.append(self)

    business_case = property(get_business_case, set_business_case)
    # >>> business_case

    # <<< work_billing_info
    # @generated
    def get_work_billing_info(self):
        """ 
        """
        return self._work_billing_info

    def set_work_billing_info(self, value):
        if self._work_billing_info is not None:
            filtered = [x for x in self.work_billing_info.works if x != self]
            self._work_billing_info._works = filtered

        self._work_billing_info = value
        if self._work_billing_info is not None:
            self._work_billing_info._works.append(self)

    work_billing_info = property(get_work_billing_info, set_work_billing_info)
    # >>> work_billing_info

    # <<< work_cost_details
    # @generated
    def get_work_cost_details(self):
        """ 
        """
        return self._work_cost_details

    def set_work_cost_details(self, value):
        for p in self._work_cost_details:
            filtered = [q for q in p.works if q != self]
            self._work_cost_details._works = filtered
        for r in value:
            if self not in r._works:
                r._works.append(self)
        self._work_cost_details = value

    work_cost_details = property(get_work_cost_details, set_work_cost_details)

    def add_work_cost_details(self, *work_cost_details):
        for obj in work_cost_details:
            if self not in obj._works:
                obj._works.append(self)
            self._work_cost_details.append(obj)

    def remove_work_cost_details(self, *work_cost_details):
        for obj in work_cost_details:
            if self in obj._works:
                obj._works.remove(self)
            self._work_cost_details.remove(obj)
    # >>> work_cost_details

    # <<< request
    # @generated
    def get_request(self):
        """ 
        """
        return self._request

    def set_request(self, value):
        if self._request is not None:
            filtered = [x for x in self.request.works if x != self]
            self._request._works = filtered

        self._request = value
        if self._request is not None:
            self._request._works.append(self)

    request = property(get_request, set_request)
    # >>> request


    def __str__(self):
        """ Returns a string representation of the Work.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< work.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Work.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Work", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.work_flow_steps:
            s += '%s<%s:Work.work_flow_steps rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.customers:
            s += '%s<%s:Work.customers rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.work_tasks:
            s += '%s<%s:Work.work_tasks rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.erp_project_accounting is not None:
            s += '%s<%s:Work.erp_project_accounting rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_project_accounting.uri)
        if self.project is not None:
            s += '%s<%s:Work.project rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.project.uri)
        for obj in self.designs:
            s += '%s<%s:Work.designs rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.business_case is not None:
            s += '%s<%s:Work.business_case rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.business_case.uri)
        if self.work_billing_info is not None:
            s += '%s<%s:Work.work_billing_info rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.work_billing_info.uri)
        for obj in self.work_cost_details:
            s += '%s<%s:Work.work_cost_details rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.request is not None:
            s += '%s<%s:Work.request rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.request.uri)
        s += '%s<%s:Work.kind>%s</%s:Work.kind>' % \
            (indent, ns_prefix, self.kind, ns_prefix)
        s += '%s<%s:Work.request_date_time>%s</%s:Work.request_date_time>' % \
            (indent, ns_prefix, self.request_date_time, ns_prefix)
        s += '%s<%s:Work.priority>%s</%s:Work.priority>' % \
            (indent, ns_prefix, self.priority, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        for obj in self.activity_records:
            s += '%s<%s:Document.activity_records rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_organisation_roles:
            s += '%s<%s:Document.erp_organisation_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.scheduled_events:
            s += '%s<%s:Document.scheduled_events rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.from_document_roles:
            s += '%s<%s:Document.from_document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.location_roles:
            s += '%s<%s:Document.location_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.power_system_resource_roles:
            s += '%s<%s:Document.power_system_resource_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.network_data_sets:
            s += '%s<%s:Document.network_data_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_person_roles:
            s += '%s<%s:Document.erp_person_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_items:
            s += '%s<%s:Document.change_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.measurements:
            s += '%s<%s:Document.measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.doc_status is not None:
            s += '%s<%s:Document.doc_status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.doc_status.uri)
        for obj in self.schedule_parameter_infos:
            s += '%s<%s:Document.schedule_parameter_infos rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.electronic_address is not None:
            s += '%s<%s:Document.electronic_address rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.electronic_address.uri)
        for obj in self.to_document_roles:
            s += '%s<%s:Document.to_document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.status is not None:
            s += '%s<%s:Document.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        for obj in self.asset_roles:
            s += '%s<%s:Document.asset_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_sets:
            s += '%s<%s:Document.change_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Document.subject>%s</%s:Document.subject>' % \
            (indent, ns_prefix, self.subject, ns_prefix)
        s += '%s<%s:Document.revision_number>%s</%s:Document.revision_number>' % \
            (indent, ns_prefix, self.revision_number, ns_prefix)
        s += '%s<%s:Document.category>%s</%s:Document.category>' % \
            (indent, ns_prefix, self.category, ns_prefix)
        s += '%s<%s:Document.last_modified_date_time>%s</%s:Document.last_modified_date_time>' % \
            (indent, ns_prefix, self.last_modified_date_time, ns_prefix)
        s += '%s<%s:Document.title>%s</%s:Document.title>' % \
            (indent, ns_prefix, self.title, ns_prefix)
        s += '%s<%s:Document.created_date_time>%s</%s:Document.created_date_time>' % \
            (indent, ns_prefix, self.created_date_time, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Work")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> work.serialize


# <<< work
# @generated
# >>> work
