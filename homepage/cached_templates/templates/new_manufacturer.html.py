# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1414171335.592
_enable_loop = True
_template_filename = 'C:\\DjangoMako\\ITILITY\\homepage\\templates/new_manufacturer.html'
_template_uri = 'new_manufacturer.html'
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
        form = context.get('form', UNDEFINED)
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
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\r\n\r\n    <h1>New Manufacturer:</h1>\r\n\r\n  \r\n    <br>\r\n    <form method="POST">\r\n        <table>\r\n            <tbody>\r\n                ')
        __M_writer(unicode( form ))
        __M_writer(u'\r\n            </tbody>\r\n        </table>\r\n        \r\n        <input type="submit" value="Save" />\r\n        <a href="/homepage/manufacturers">Cancel</a>\r\n    </form>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"35": 1, "45": 3, "52": 3, "53": 12, "54": 12, "27": 0, "60": 54}, "uri": "new_manufacturer.html", "filename": "C:\\DjangoMako\\ITILITY\\homepage\\templates/new_manufacturer.html"}
__M_END_METADATA
"""
