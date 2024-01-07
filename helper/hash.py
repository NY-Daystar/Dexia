"""Helper to handle sha512 hash"""
from hashlib import sha512
from pathlib import Path


def is_new_file(file1: Path, file2: Path) -> bool:
    """Compare MD5 checksum of both files'''

    Args:
        current_file (Path): file to check
        new_file_content (Path): file to check

    Returns:
        bool: True if content of both files is equal otherwise false
    """
    return file_checksum(file1) != file_checksum(file2)

def file_checksum(source: str, content_type: str = "file") -> str:
    """Return sha512 checksum of a file or a string

    Args:
        source (str): data if `content_type` is str so it's own source, if `content_type` is file then source is the path
        content_type (str, optional): type of content to return sha512 (could be 'file' or 'str'). Defaults to "file".

    Returns:
        str: sha512 of `source` parameter
    """    
    if content_type == "str":
        return sha512(source.encode('utf-8')).hexdigest()

    sha512_hash = sha512() 
    try:
        with open(source, "rb") as document:
            content: bytes = document.read()
            sha512_hash.update(content)
            digest: str = sha512_hash.hexdigest()
            return digest
    except FileNotFoundError:
        return "0"
