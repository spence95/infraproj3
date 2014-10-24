# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1414170582.777
_enable_loop = True
_template_filename = u'C:\\DjangoMako\\ITILITY\\homepage\\templates/base.htm'
_template_uri = u'base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = [u'content']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\r\n')
        __M_writer(u'\r\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\r\n\r\n<!DOCTYPE html>\r\n<html>\r\n  <meta charset="UTF-8">\r\n  <head>\r\n    \r\n    <title>ITILITY</title>\r\n    \r\n')
        __M_writer(u'    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\r\n  \r\n')
        __M_writer(u'    ')
        __M_writer(unicode( static_renderer.get_template_css(request, context)  ))
        __M_writer(u'\r\n  \r\n  </head>\r\n  <body>\r\n    \r\n    <div class="header-color-block">\r\n        \r\n        <a href="/homepage/"><img src="')
        __M_writer(unicode( STATIC_URL ))
        __M_writer(u'homepage/media/ITILITY_LOGO.png" /></a>\r\n        <br><br>\r\n        \r\n        <div class="header-menu-div">\r\n\r\n                &nbsp<a href="/homepage/"><img src="')
        __M_writer(unicode( STATIC_URL ))
        __M_writer(u'homepage/media/ITILITY_LOGO_ARROW.png" style="vertical-align:bottom; float:left" /></a>\r\n                <span class="header-menu-text">\r\n                    <br><br><br><br>\r\n                    <a class="header-menu-link" href="/homepage/assets">Assets</a>\r\n                    &nbsp &nbsp &nbsp &nbsp &nbsp\r\n                    <a class="header-menu-link" href="/homepage/locations">Locations</a>\r\n                    &nbsp &nbsp &nbsp &nbsp &nbsp\r\n                    <a class="header-menu-link" href="/homepage/manufacturers">Manufacturers</a>\r\n                    &nbsp &nbsp &nbsp &nbsp &nbsp\r\n                    <a class="header-menu-link" href="#">Admin</a>\r\n                    &nbsp &nbsp &nbsp &nbsp &nbsp\r\n                    <a class="header-menu-link" href="#">Contact Us</a>\r\n                    &nbsp &nbsp &nbsp &nbsp &nbsp\r\n                </span>\r\n\r\n        </div>\r\n    </div>\r\n    \r\n    <div class="main-half-div">\r\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer(u'  \r\n    </div>\r\n  \r\n')
        __M_writer(u'    ')
        __M_writer(unicode( static_renderer.get_template_js(request, context)  ))
        __M_writer(u'\r\n  \r\n  </body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer(u'\r\n          Site content goes here in sub-templates.\r\n        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"48": 55, "34": 5, "35": 15, "36": 18, "37": 18, "38": 18, "39": 25, "40": 25, "41": 30, "42": 30, "50": 55, "47": 51, "16": 4, "49": 55, "18": 0, "62": 49, "56": 49, "68": 62, "28": 2, "29": 4, "30": 5}, "uri": "base.htm", "filename": "C:\\DjangoMako\\ITILITY\\homepage\\templates/base.htm"}
__M_END_METADATA
"""
