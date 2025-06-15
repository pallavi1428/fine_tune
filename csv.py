import json
import pandas as pd

# Load JSONL data
jsonl_file = r'C:\Users\PALLAVI\Desktop\magic_ui\fine_tune\dataset.jsonl'  # Replace with your file name
data = []

with open(jsonl_file, 'r', encoding='utf-8') as f:
    for line in f:
        entry = json.loads(line)
        # Optional: Add a shortened preview for better Hugging Face display
        preview_length = 200  # You can adjust this length
        entry['preview'] = entry['completion'][:preview_length] + '...' if len(entry['completion']) > preview_length else entry['completion']
        data.append(entry)

# Convert to DataFrame
df = pd.DataFrame(data)

# Save as CSV
csv_file = r'C:\Users\PALLAVI\Desktop\magic_ui\fine_tune\data.csv'
df.to_csv(csv_file, index=False, encoding='utf-8')

print(f'Dataset converted and saved to {csv_file}')
