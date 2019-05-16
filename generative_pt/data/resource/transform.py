import json
import sys

from_file = open(sys.argv[1], 'r', encoding='utf-8')
to_file = open(sys.argv[2], 'w', encoding='utf-8')

for line in from_file:
    parsered = json.loads(line)
    topic_a = parsered['goal'][0][1].strip()
    topic_b = parsered['goal'][0][2].strip()
    new_topic_a = "_".join(topic_a.split())
    new_topic_b = "_".join(topic_b.split())
    new_line = new_topic_a.join(line.split(topic_a))
    new_line = new_topic_b.join(new_line.split(topic_b))
    to_file.writelines(new_line)
