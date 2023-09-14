"""Helper to handle md5 hash"""
from hashlib import md5
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
    """Return md5 checksum of a file or a string

    Args:
        source (str): data if `content_type` is str so it's own source, if `content_type` is file then source is the path
        content_type (str, optional): type of content to return md5 (could be 'file' or 'str'). Defaults to "file".

    Returns:
        str: md5 of `source` parameter
    """    


    if content_type == "str":
        return md5(source.encode('utf-8')).hexdigest()
    elif content_type == "file":
        md5_hash = md5() 
        try:
            with open(source, "rb") as document:
                content: bytes = document.read()
                md5_hash.update(content)

                digest: str = md5_hash.hexdigest()
                return digest
        except FileNotFoundError:
            return "0"
    else:
        return None