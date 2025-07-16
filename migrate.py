#!/usr/bin/env python3
"""
PostgreSQL Schema Migration Tool

Generate PostgreSQL migrations from YAML schema definitions.
"""

import argparse
import sys
from pathlib import Path

# Add the current directory to the path to import our module
sys.path.insert(0, str(Path(__file__).parent))

from migration_tool import SchemaMigrationTool


def main():
    parser = argparse.ArgumentParser(description="Generate PostgreSQL migrations from YAML schemas")
    parser.add_argument('--schemas-dir', default='schemas', help='Directory containing YAML schema files')
    parser.add_argument('--migrations-dir', default='migrations', help='Directory to store migration files')
    parser.add_argument('--name', help='Optional name for the migration')
    parser.add_argument('--full', action='store_true', help='Generate full migration instead of differential')
    parser.add_argument('--validate', action='store_true', help='Only validate schemas without creating migrations')
    parser.add_argument('--rollback', action='store_true', help='Create a rollback migration to undo the last migration')
    parser.add_argument('--generate-entities', 
                       choices=['typescript', 'python', 'dart', 'java', 'cpp', 'csharp', 'go'],
                       help='Generate entity classes for the specified language')
    parser.add_argument('--entities-dir', default='entities', help='Directory to store generated entity files')
    
    args = parser.parse_args()
    
    tool = SchemaMigrationTool(args.schemas_dir, args.migrations_dir)
    
    if args.validate:
        success = tool.validate_schemas_only()
        sys.exit(0 if success else 1)
    elif args.rollback:
        tool.create_rollback_migration(args.name)
    elif args.generate_entities:
        success = tool.generate_entities(args.generate_entities, args.entities_dir)
        sys.exit(0 if success else 1)
    else:
        tool.create_migration(args.name, differential=not args.full)


if __name__ == "__main__":
    main()
