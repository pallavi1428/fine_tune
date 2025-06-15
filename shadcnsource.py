import json

# Load the JSONL file
with open(r'C:\Users\PALLAVI\Desktop\magic_ui\fine_tune\koko_ui (1).jsonl', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Add the source key
updated_lines = []
for line in lines:
    data = json.loads(line)
    data['source'] = 'Shadcn'
    updated_lines.append(json.dumps(data, ensure_ascii=False))

# Write back to a new file
with open(r'C:\Users\PALLAVI\Desktop\magic_ui\shadcn.jsonl', 'w', encoding='utf-8') as f:
    for line in updated_lines:
        f.write(line + '\n')
