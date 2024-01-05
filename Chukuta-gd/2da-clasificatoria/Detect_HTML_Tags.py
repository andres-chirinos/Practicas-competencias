import re

def detect_tags(html):
    tags = re.findall(r'<\s*([a-z0-9]+)(?:\s+[^>]+)*\s*>', html, re.I)
    return tags

if __name__ == '__main__':
    n = int(input())
    html = ''
    for _ in range(n):
        html += input()
    tags = detect_tags(html)
    print(';'.join(sorted(set(tags))))