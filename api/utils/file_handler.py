import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Any
import hashlib
import logging


logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

from api.core.config import settings


class FileHandler:
    """Handle file operations for data storage."""

    def __init__(self):
        self.data_dir = Path(settings.DATA_DIR)
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.hash_salt = "torq52_seasalt"

    def _hash_sum(self, data: str) -> str:
        """Generate a simple hash sum for the given data string."""

        return hashlib.sha256((data + self.hash_salt).encode("utf-8")).hexdigest()

    def list_all_files(self) -> Dict[str, str]:
        """
        List all files in the data directory

        """
        files = []
        for file_path in self.data_dir.iterdir():
            if file_path.is_file():
                files.append((file_path.name, file_path.read_text(encoding="utf-8")))
        return files

    def save_data(self, data: Dict[str, Any], filename: str = ".json") -> None:
        """
        Save data to a JSON file with a timestamp.

        Args:
            data: The data to save
            filename: The filename to save to OPTIONAL
        """
        # Generate unique filename if default is used
        hash_value = self._hash_sum(json.dumps(data, sort_keys=True))
        if filename == ".json":
            filename = datetime.now().strftime("%Y%m%d%H") + "_" + hash_value + filename
        file_path = self.data_dir / filename

        # Add timestamp to data
        data_with_timestamp = {
            "received_at": datetime.now(timezone.utc).isoformat(),
            **data,
        }

        def _make_json_safe(obj):
            if isinstance(obj, dict):
                return {k: _make_json_safe(v) for k, v in obj.items()}
            if isinstance(obj, (list, tuple)):
                return [_make_json_safe(v) for v in obj]
            if isinstance(obj, (str, int, float, bool)) or obj is None:
                return obj
            return str(obj)

        # Ensure the data is JSON-serializable (convert non-serializable values to strings)
        data_with_timestamp = _make_json_safe(data_with_timestamp)
        logger.debug("Data sanitized for JSON serialization.")
        # If file exists, overwrite it (atomic replace will be used below)
        if file_path.exists():
            logger.info("Replacing existing file: %s", file_path)
        else:
            logger.info("Creating new file: %s", file_path)
        # Atomic write: write to temp file first, then rename
        temp_path = file_path.with_suffix(".tmp")
        temp_path.write_text(
            json.dumps(data_with_timestamp, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        temp_path.replace(file_path)

    # Global instance


file_handler = FileHandler()
