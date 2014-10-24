# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1414172404.492
_enable_loop = True
_template_filename = 'C:\\DjangoMako\\ITILITY\\homepage\\templates/locations.html'
_template_uri = 'locations.html'
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
        locations = context.get('locations', UNDEFINED)
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
        locations = context.get('locations', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\r\n    \r\n    \r\n    <div class="main-text">\r\n        <h2>Locations\r\n            <div class="float-right">\r\n                <a href="/homepage/new_location">New Location</a>\r\n                <!--<a class="btn btn-info" href="/store/stores/">Active</a>-->\r\n                <!--<a class="btn btn-info" href="/store/stores/archive/">Inactive</a>-->\r\n                <!--<a class="btn btn-info" href="/store/stores/all/">All</a>-->\r\n            </div>\r\n        </h2>\r\n        \r\n\r\n        <table>\r\n            <thead>\r\n                <tr>\r\n                    <th>UID</th>\r\n                    <th>Name</th>\r\n                    <th>Address</th>\r\n                    <th>Phone</th>\r\n                </tr>\r\n            </thead>\r\n            <tbody>\r\n            \r\n')
        for l in locations:
            __M_writer(u'                    <tr>\r\n                        <td>')
            __M_writer(unicode( l.UID ))
            __M_writer(u'</td>\r\n                        <td>')
            __M_writer(unicode( l.name ))
            __M_writer(u'</td>\r\n                        <td>')
            __M_writer(unicode( l.address ))
            __M_writer(u'</td>\r\n                        <td>')
            __M_writer(unicode( l.phone ))
            __M_writer(u'</td>\r\n                        <td><a href="/homepage/edit_location/')
            __M_writer(unicode( l.UID ))
            __M_writer(u'">Edit</a></td>\r\n                        <td><a href="/homepage/delete_location/')
            __M_writer(unicode( l.UID ))
            __M_writer(u'">Delete</a></td>\r\n                    </tr>\r\n')
        __M_writer(u'            </tbody>\r\n        </table>\r\n        \r\n        \r\n    </div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"64": 34, "65": 35, "66": 35, "35": 1, "73": 67, "45": 3, "59": 32, "67": 38, "52": 3, "53": 28, "54": 29, "55": 30, "56": 30, "57": 31, "58": 31, "27": 0, "60": 32, "61": 33, "62": 33, "63": 34}, "uri": "locations.html", "filename": "C:\\DjangoMako\\ITILITY\\homepage\\templates/locations.html"}
__M_END_METADATA
"""
