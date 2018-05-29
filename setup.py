from setuptools import setup

setup(
    name='lektor-markdown-highlighter-headers',
    version='0.1',
    author=u'Linus T\xf6rngren',
    author_email='linus@etnolit.se',
    license='MIT',
    py_modules=['lektor_markdown_highlighter_headers'],
    entry_points={
        'lektor.plugins': [
            'markdown-highlighter-headers = lektor_markdown_highlighter_headers:MarkdownHighlighterHeadersPlugin',
        ]
    }
)
