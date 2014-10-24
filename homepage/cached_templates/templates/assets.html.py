# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1414173647.814
_enable_loop = True
_template_filename = 'C:\\DjangoMako\\ITILITY\\homepage\\templates/assets.html'
_template_uri = 'assets.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = [u'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        assets = context.get('assets', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        assets = context.get('assets', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\r\n    \r\n    \r\n    <div class="main-text">\r\n        <h2>Assets\r\n            <div class="float-right">\r\n                <a href="/homepage/new_asset">New Asset</a>\r\n                <!--<a class="btn btn-info" href="/store/stores/">Active</a>-->\r\n                <!--<a class="btn btn-info" href="/store/stores/archive/">Inactive</a>-->\r\n                <!--<a class="btn btn-info" href="/store/stores/all/">All</a>-->\r\n            </div>\r\n        </h2>\r\n        \r\n\r\n        <table>\r\n            <thead>\r\n                <tr>\r\n                    <th>UID</th>\r\n                    <th>Org. Tag</th>\r\n                    <th>Man. Part #</th>\r\n                    <th>Description</th>\r\n                    <th>Maintenance Notes</th>\r\n                    <th>Date Implemented</th>\r\n                    <th>Location</th>\r\n                    <th>Manufacturer</th>\r\n                </tr>\r\n            </thead>\r\n            <tbody>\r\n            \r\n')
        for a in assets:
            __M_writer(u'                    <tr>\r\n                        <td>')
            __M_writer(unicode( a.UID ))
            __M_writer(u'</td>\r\n                        <td>')
            __M_writer(unicode( a.organizationalTag ))
            __M_writer(u'</td>\r\n                        <td>')
            __M_writer(unicode( a.manufacturerPartNumber ))
            __M_writer(u'</td>\r\n                        <td>')
            __M_writer(unicode( a.description ))
            __M_writer(u'</td>\r\n                        <td>')
            __M_writer(unicode( a.maintenanceNotes ))
            __M_writer(u'</td>\r\n                        <td>')
            __M_writer(unicode( a.dateImplemented ))
            __M_writer(u'</td>\r\n                        <td>')
            __M_writer(unicode( a.currentAssignedLocation.name ))
            __M_writer(u'</td>\r\n                        <td>')
            __M_writer(unicode( a.manufacturer.name ))
            __M_writer(u'</td>\r\n                        <td><a href="/homepage/edit_asset/')
            __M_writer(unicode( a.UID ))
            __M_writer(u'">Edit</a></td>\r\n                        <td><a href="/homepage/delete_asset/')
            __M_writer(unicode( a.UID ))
            __M_writer(u'">Delete</a></td>\r\n                    </tr>\r\n')
        __M_writer(u'            </tbody>\r\n        </table>\r\n        \r\n        \r\n    </div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"27": 0, "35": 1, "45": 3, "52": 3, "53": 32, "54": 33, "55": 34, "56": 34, "57": 35, "58": 35, "59": 36, "60": 36, "61": 37, "62": 37, "63": 38, "64": 38, "65": 39, "66": 39, "67": 40, "68": 40, "69": 41, "70": 41, "71": 42, "72": 42, "73": 43, "74": 43, "75": 46, "81": 75}, "uri": "assets.html", "filename": "C:\\DjangoMako\\ITILITY\\homepage\\templates/assets.html"}
__M_END_METADATA
"""
