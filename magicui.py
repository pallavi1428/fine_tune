import json

input_file = r'C:\Users\PALLAVI\Desktop\magic_ui\fine_tune\magicui.jsonl'       # Your input file
output_file = r'C:\Users\PALLAVI\Desktop\magic_ui\fine_tune\magic-ui.jsonl'  # Output file with changes

with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
    for line in infile:
        data = json.loads(line)
        # Add source field
        data['source'] = 'magic ui'
        # Wrap completion in markdown if not already wrapped
        if not data['completion'].strip().startswith('```'):
            data['completion'] = f'```tsx\n{data["completion"]}\n```'
        # Write to output file
        json.dump(data, outfile, ensure_ascii=False)
        outfile.write('\n')

print(f'✅ Processing complete. Output saved to {output_file}')
