import json
from pathlib import Path

def export_to_json(data: dict, output_path: str):
    path = Path(output_path)
    path.write_text(json.dumps(data, indent=2))
