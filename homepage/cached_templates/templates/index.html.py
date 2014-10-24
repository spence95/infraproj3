# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1414110621.696
_enable_loop = True
_template_filename = u'C:\\DjangoMako\\ITILITY\\homepage\\templates/index.html'
_template_uri = u'index.html'
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
        __M_writer = context.writer()
        __M_writer(u'\r\n    \r\n    \r\n    <div class="main-text">\r\n        <h2>Welcome to Itility!</h2>\r\n        <p>\r\n            Interdum et malesuada fames ac ante ipsum primis in faucibus. Aliquam bibendum magna odio, sed consequat est dignissim vel. Aenean sapien justo, suscipit eu est et, ullamcorper dictum risus. Suspendisse potenti. Suspendisse quis turpis nibh. Mauris vitae mattis nulla. Sed vitae pellentesque orci. Vivamus lacinia iaculis tincidunt.\r\n        </p>\r\n        <p>\r\n            Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Donec porttitor tempus sem, cursus consequat risus lacinia quis. Nam sapien urna, convallis sed quam at, placerat pretium odio. Cras nec ipsum arcu. Aenean consectetur volutpat diam eu commodo. Nunc augue ipsum, ultrices at orci hendrerit, auctor sodales neque. Donec cursus lectus dignissim quam lacinia scelerisque. Nunc dapibus, dolor in tincidunt scelerisque, dolor odio pulvinar ipsum, id suscipit massa nulla vel sem. Nulla ac mollis ligula. Donec accumsan tellus sed neque efficitur tristique quis id enim. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Duis scelerisque lacinia elit tristique faucibus. Quisque viverra malesuada lobortis. Suspendisse potenti. Curabitur id venenatis ex. Fusce mollis auctor justo nec auctor.\r\n        </p>\r\n        <p>\r\n            Nulla fermentum libero eu congue accumsan. Maecenas a consequat velit, quis venenatis lectus. Maecenas egestas condimentum nulla non sollicitudin. Vestibulum nisl justo, dapibus nec nunc at, consectetur lobortis orci. Nullam quis turpis risus. Quisque vel facilisis mauris. Vivamus fringilla, dui vel scelerisque tincidunt, purus ipsum sagittis mauris, ac dapibus erat sem et ipsum. Pellentesque ut neque ullamcorper, maximus dolor nec, lacinia mi. Donec id magna laoreet, pharetra purus a, congue nisi. Duis facilisis et lacus nec sodales. In non blandit mauris, eu auctor turpis. In elementum luctus mi, eu vehicula lorem elementum at. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Nullam consectetur nunc vitae quam efficitur, ut eleifend felis ultricies. In imperdiet iaculis metus in vestibulum.\r\n        </p>\r\n        <p>\r\n            Sed semper pellentesque malesuada. Ut nulla ante, finibus in nibh sed, convallis viverra orci. Nulla feugiat scelerisque lorem, quis pulvinar dui lacinia in. Donec feugiat leo et nibh varius, sit amet varius mauris aliquam. Pellentesque pharetra massa ac nulla fringilla, sit amet finibus felis bibendum. Vestibulum non velit eu leo aliquam molestie. Vestibulum vestibulum dui non felis laoreet, eu pellentesque justo ullamcorper. Cras volutpat dignissim nisl, sit amet laoreet felis elementum ac.\r\n        </p>\r\n        <p>\r\n            Mauris gravida neque id tincidunt elementum. Interdum et malesuada fames ac ante ipsum primis in faucibus. Vivamus vulputate lacus libero, vitae sagittis nunc aliquam eu. Aenean non dui enim. Duis et egestas nibh. Cras ut vulputate est, sit amet tempor lectus. Nam pharetra sed turpis eget mollis. Nam nibh lacus, aliquet vel lacus at, ullamcorper consectetur felis. Aliquam venenatis aliquet facilisis.\r\n        </p>\r\n        <p>\r\n            Suspendisse in bibendum orci. Integer sodales ornare ipsum eu bibendum. Pellentesque id consectetur ipsum, id maximus lorem. Duis lobortis enim ac blandit dictum. Nullam fringilla sapien quis condimentum scelerisque. Integer ex sapien, consequat at ex et, dictum volutpat odio. Donec et imperdiet nunc. Duis eu luctus turpis. Curabitur dignissim tellus id euismod sodales. Integer vel sem sit amet libero tristique luctus. Maecenas eu sapien diam.\r\n        </p>\r\n    </div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"56": 50, "34": 1, "27": 0, "44": 3, "50": 3}, "uri": "index.html", "filename": "C:\\DjangoMako\\ITILITY\\homepage\\templates/index.html"}
__M_END_METADATA
"""
