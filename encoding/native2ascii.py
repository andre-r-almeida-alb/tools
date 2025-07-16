import codecs
import sys

if len(sys.argv) != 3:
    print("Usage: python native2ascii.py <input_file> <output_file>")
    print("Example: python native2ascii.py messages_pt_PT.properties messages_pt_PT_utf8.properties")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

with codecs.open(input_file, 'r', 'unicode_escape') as f:
    content = f.read()

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(content)