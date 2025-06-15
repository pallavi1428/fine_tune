input_files = [r'C:\Users\PALLAVI\Desktop\magic_ui\fine_tune\acternity.jsonl', r'C:\Users\PALLAVI\Desktop\magic_ui\fine_tune\magic-ui.jsonl', r'C:\Users\PALLAVI\Desktop\magic_ui\fine_tune\shadcn.jsonl']  # Replace with your actual file names
output_file = 'combined_dataset.jsonl'

with open(output_file, 'w', encoding='utf-8') as outfile:
    for file in input_files:
        with open(file, 'r', encoding='utf-8') as infile:
            for line in infile:
                outfile.write(line)

print(f'✅ All files combined into {output_file}')
