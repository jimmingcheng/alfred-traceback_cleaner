import os
import re


def main():
    dirty = os.environ['dirty_stacktrace']

    clean = unescape_newlines(dirty)

    print(clean)


def unescape_newlines(dirty):
    cleaned_2x_escaped_newlines = re.sub(r'\\\\n', '\n', dirty)
    return re.sub(r'\\n', '\n', cleaned_2x_escaped_newlines)


if __name__ == '__main__':
    main()
