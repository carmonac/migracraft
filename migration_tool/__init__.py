"""
Migration Tool Package

A PostgreSQL schema migration tool that generates SQL migrations from YAML schema definitions.
"""

from .exceptions import SchemaValidationError
from .validator import SchemaValidator
from .sql_generator import SQLGenerator
from .migration_manager import MigrationManager
from .entity_generator import EntityGenerator
from .main import SchemaMigrationTool

__version__ = "1.0.0"
__all__ = [
    "SchemaValidationError",
    "SchemaValidator", 
    "SQLGenerator",
    "MigrationManager",
    "EntityGenerator",
    "SchemaMigrationTool"
]
