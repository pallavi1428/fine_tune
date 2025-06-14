import json
from typing import List
from collections import defaultdict

# Configuration
MIN_CODE_LENGTH = 10  # Skip very short code snippets
VALID_CATEGORIES = {"button", "card", "navbar"}

# Optional: Map hex codes to human-readable color names
COLOR_MAP = {
    "#552da8": "purple",
    "#ffffff": "white",
    "#1c1c1c": "dark gray",
    "#06b6d4": "teal",
    "#60a5fa": "light blue"
}

def format_colors(colors: List[str]) -> List[str]:
    """Convert hex codes to readable names with hex fallback."""
    return [f"{COLOR_MAP.get(c.lower(), c)} ({c})" for c in colors]

def clean_text(text: str) -> str:
    """Clean and normalize text."""
    return ' '.join(text.strip().split()).replace('“', '"').replace('”', '"')

# Load dataset
with open(r'C:\Users\PALLAVI\Desktop\magic_ui\fine_tune\training_data00.jsonl', 'r', encoding='utf-8') as f:
    data = [json.loads(line) for line in f if line.strip()]

processed_data = []
skipped = 0
unknown_categories = defaultdict(int)

for item in data:
    code = item.get('code', '')
    if not code or len(code) < MIN_CODE_LENGTH:
        skipped += 1
        continue

    metadata = item.get('metadata', {})
    raw_category = clean_text(metadata.get('category', 'component')).lower()

    # Keep category even if it's not in the valid list
    category = raw_category
    if category not in VALID_CATEGORIES:
        unknown_categories[category] += 1

    tags = list({clean_text(tag).lower() for tag in metadata.get('tags', []) if tag})
    colors = format_colors([c for c in metadata.get('colors', []) if c])

    # Build prompt (without framework)
    prompt_parts = [
        f"Create a {category}",
        f"Features: {', '.join(tags)}" if tags else None,
        f"Colors: {', '.join(colors)}" if colors else None
    ]
    prompt = '. '.join(filter(None, prompt_parts)) + '.'

    processed_data.append({
        "prompt": prompt,
        "completion": clean_text(code),
        "meta": {
            "category": category
        }
    })

# Save processed dataset
with open('magic_ui_dataset_general.jsonl', 'w', encoding='utf-8') as f:
    for item in processed_data:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')

# Summary log
print(f"✅ Processing complete.\nProcessed: {len(processed_data)} entries\nSkipped: {skipped} entries")

if unknown_categories:
    print("\n⚠️ Unknown categories encountered:")
    for cat, count in unknown_categories.items():
        print(f"- {cat}: {count} times")
