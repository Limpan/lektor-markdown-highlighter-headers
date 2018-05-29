# -*- coding: utf-8 -*-
from lektor.pluginsystem import Plugin


class MarkdownHighlighterHeadersPlugin(Plugin):
    name = u'Markdown Highlighter Headers'
    description = u'Lektor plugin that adds language headers to markdown blocks.'

    def add_header(self, text, lang):
        return '<div class="lang lang-%(lang)s"><span>%(lang)s</span>%(text)s</div>' % {'lang':lang, 'text':text}

    def on_markdown_config(self, config, **extra):
        class HeaderMixin(object):
            def block_code(ren, text, lang):
                if not lang:
                    return super(HeaderMixin, ren).block_code(text, lang)
                return self.add_header(super(HeaderMixin, ren).block_code(text, lang), lang)
        config.renderer_mixins.append(HeaderMixin)
