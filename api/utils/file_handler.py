import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Any

from api.core.config import settings


class FileHandler:
    """Handle file operations for data storage."""

    def __init__(self):
        self.data_dir = Path(settings.DATA_DIR)
        self.data_dir.mkdir(parents=True, exist_ok=True)

    def save_data(self, data: Dict[str, Any], filename: str = "payload.json") -> None:
        """
        Save data to a JSON file with a timestamp.

        Args:
            data: The data to save
            filename: The filename to save to OPTIONAL
        """

        if filename == "payload.json":
            filename = datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + "_" + filename
        file_path = self.data_dir / filename

        # Add timestamp to data
        data_with_timestamp = {
            "received_at": datetime.now(timezone.utc).isoformat(),
            **data,
        }

        # Atomic write: write to temp file first, then rename
        temp_path = file_path.with_suffix(".tmp")
        temp_path.write_text(
            json.dumps(data_with_timestamp, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        temp_path.replace(file_path)

    # Global instance


file_handler = FileHandler()
