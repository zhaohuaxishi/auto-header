import re
import vim
import subprocess


def find_missing_header():
    name = vim.current.buffer.name
    try:
        subprocess.check_output(['cpplint.py', name],
                                stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        lint_result = e.output.decode()

        headers = []
        indicator = 'build/include_what_you_use'
        for line in lint_result.splitlines():
            if indicator in line:
                match = re.search(r'(#include <.+?>)', line)
                headers.append(match.group(1))

        return headers
    return []


def skip_head_comment(buf):
    beg, end = 0, 0
    comments = ("//", "/*")
    while buf[end][:2] in comments:
        if buf[end][:2] == "//":
            # skil whole block of c++ comment
            while buf[end].startswith("//"):
                end += 1
        else:
            # skil whole c comment
            while "*/" not in buf[end]:
                end += 1

            # insert at next line
            end += 1

    return end


def insert_missing_header():
    headers = find_missing_header()
    buf = vim.current.buffer
    pos = skip_head_comment(buf)

    for header in headers:
        buf.append(header, pos)
