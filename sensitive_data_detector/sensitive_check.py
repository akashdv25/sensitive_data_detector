from typing import Union
from pathlib import Path
from .load_patterns import load_patterns
from .file_reader import get_file_content
from .content_analyze import analyze_content

def has_sensitive_info(file_path: Union[str, Path]) -> bool:
    """Check if file contains any sensitive information."""
    patterns = load_patterns()
    content = get_file_content(file_path)
    results = analyze_content(content, patterns)
    return len(results) > 0