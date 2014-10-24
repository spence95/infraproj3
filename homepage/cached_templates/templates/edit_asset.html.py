# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1414174202.418
_enable_loop = True
_template_filename = 'C:\\DjangoMako\\ITILITY\\homepage\\templates/edit_asset.html'
_template_uri = 'edit_asset.html'
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
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer(u'\n')
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
        __M_writer(u'\n\n    <br><br>\n    <h1>Edit Asset:</h1>\n\n  \n    <br>\n    <form method="POST">\n        <table>\n            <tbody>\n                ')
        __M_writer(unicode( form ))
        __M_writer(u'\n            </tbody>\n        </table>\n        \n        <input type="submit" class = "btn btn-info" value="Save" />\n        <a class="btn btn-info" href="/homepage/assets">Cancel</a>\n    </form>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"35": 1, "40": 21, "46": 3, "53": 3, "54": 13, "55": 13, "27": 0, "61": 55}, "uri": "edit_asset.html", "filename": "C:\\DjangoMako\\ITILITY\\homepage\\templates/edit_asset.html"}
__M_END_METADATA
"""
