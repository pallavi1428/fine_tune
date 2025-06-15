import json

input_file = r'C:\Users\PALLAVI\Desktop\magic_ui\fine_tune\shadcn.jsonl'   # Replace with your JSONL file name
output_file = r'C:\Users\PALLAVI\Desktop\magic_ui\fine_tune\shadcnd.jsonl'

with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
    for line in infile:
        data = json.loads(line)
        # Check if already wrapped to avoid double wrapping
        if not data['completion'].strip().startswith('```'):
            data['completion'] = f'```tsx\n{data["completion"]}\n```'
        json.dump(data, outfile, ensure_ascii=False)
        outfile.write('\n')

print(f'Markdown wrapping completed. Output saved to {output_file}')
