# PostgreSQL Schema Migration Tool

A powerful and flexible PostgreSQL schema migration tool that generates SQL migrations from YAML schema definitions.

## Features

- **YAML Schema Definitions**: Define your database schema in easy-to-read YAML files
- **Differential Migrations**: Automatically detect changes and generate incremental migrations
- **Full Schema Migrations**: Generate complete schema migrations for initial setup
- **Rollback Support**: Create rollback migrations to undo changes
- **Schema Validation**: Comprehensive validation of YAML schema definitions
- **Foreign Key Support**: Full support for foreign key constraints and relationships
- **Index Management**: Create and manage database indexes
- **PostgreSQL Functions**: Support for stored procedures and functions
- **Entity Class Generation**: Generate entity classes in multiple programming languages
- **Modular Architecture**: Clean, maintainable codebase split into logical modules

## Installation

```bash
# Install dependencies
pip install PyYAML

# Clone or download the project
cd migration_tool
```

## Quick Start

1. **Create schema files** in the `schemas/` directory:

```yaml
# schemas/users.yaml
tables:
  users:
    columns:
      id:
        type: SERIAL
        primary_key: true
      username:
        type: VARCHAR(50)
        not_null: true
        unique: true
      email:
        type: VARCHAR(255)
        not_null: true
        unique: true
      created_at:
        type: TIMESTAMP
        not_null: true
        default: CURRENT_TIMESTAMP
    indexes:
      - columns: [username]
        name: idx_users_username
        unique: true
```

2. **Validate your schemas**:

```bash
python3 migrate.py --validate
```

3. **Generate your first migration**:

```bash
python3 migrate.py --name "initial_setup" --full
```

4. **Make changes to schemas and generate differential migrations**:

```bash
python3 migrate.py --name "add_user_profiles"
```

5. **Create rollback migrations when needed**:

```bash
python3 migrate.py --rollback --name "undo_profiles"
```

## Project Structure

```
migration_tool/
├── migrate.py                 # Main entry point
├── migration_tool/            # Core package
│   ├── __init__.py           # Package initialization
│   ├── config.py             # Configuration constants
│   ├── exceptions.py         # Custom exceptions
│   ├── validator.py          # Schema validation
│   ├── sql_generator.py      # SQL generation
│   ├── migration_manager.py  # Migration management
│   └── main.py              # Main tool class
├── schemas/                   # YAML schema definitions
├── migrations/               # Generated SQL migrations
├── tests/                    # Test files
└── README.md
```

## Usage

### Command Line Options

```bash
python3 migrate.py [OPTIONS]

Options:
  --schemas-dir DIR     Directory containing YAML schema files (default: schemas)
  --migrations-dir DIR  Directory to store migration files (default: migrations)
  --name NAME          Optional name for the migration
  --full              Generate full migration instead of differential
  --validate          Only validate schemas without creating migrations
  --rollback          Create a rollback migration to undo the last migration
  --generate-entities LANG Generate entity classes for specified language
  --entities-dir DIR      Directory to store generated entity files
  -h, --help          Show help message
```

### Schema Definition Format

#### Tables

```yaml
tables:
  table_name:
    columns:
      column_name:
        type: DATA_TYPE
        primary_key: true/false    # Optional
        not_null: true/false       # Optional
        unique: true/false         # Optional
        default: "value"           # Optional
    indexes:                       # Optional
      - columns: [col1, col2]
        name: index_name           # Optional
        unique: true/false         # Optional
    foreign_keys:                  # Optional
      - columns: [local_column]
        references_table: other_table
        references_columns: [other_column]
        name: fk_name              # Optional
        on_delete: CASCADE         # Optional
        on_update: CASCADE         # Optional
```

#### Functions

```yaml
functions:
  function_name:
    parameters:                    # Optional
      param_name: DATA_TYPE
    returns: RETURN_TYPE           # Optional, defaults to 'void'
    language: plpgsql             # Optional, defaults to 'sql'
    body: |
      -- SQL function body
      BEGIN
        -- Function logic here
      END;
```

### Supported Data Types

- Numeric: `SERIAL`, `BIGSERIAL`, `INTEGER`, `BIGINT`, `DECIMAL`, `NUMERIC`, `REAL`, `DOUBLE PRECISION`
- Text: `VARCHAR`, `CHAR`, `TEXT`
- Date/Time: `TIMESTAMP`, `TIMESTAMPTZ`, `DATE`, `TIME`, `INTERVAL`
- Boolean: `BOOLEAN`, `BOOL`
- Binary: `BYTEA`
- Network: `INET`, `CIDR`, `MACADDR`
- JSON: `JSON`, `JSONB`
- And many more PostgreSQL types...

### Supported Function Languages

- `sql`
- `plpgsql`
- `c`
- `python`
- `perl`
- `tcl`

### Entity Generation

Generate entity classes from your schema definitions:

```bash
# Generate TypeScript interfaces and classes
python3 migrate.py --generate-entities typescript

# Generate Python dataclasses
python3 migrate.py --generate-entities python

# Generate Dart classes with JSON serialization
python3 migrate.py --generate-entities dart

# Generate Java POJOs with getters/setters
python3 migrate.py --generate-entities java

# Generate C++ classes with getters/setters
python3 migrate.py --generate-entities cpp

# Generate C# classes with properties
python3 migrate.py --generate-entities csharp

# Generate Go structs with JSON tags
python3 migrate.py --generate-entities go

# Specify custom output directory
python3 migrate.py --generate-entities typescript --entities-dir src/models
```

### Supported Languages for Entity Generation

- **TypeScript**: Generates interfaces and classes with proper typing
- **Python**: Generates dataclasses with type hints
- **Dart**: Generates classes with JSON serialization methods
- **Java**: Generates POJOs with getters/setters and proper imports
- **C++**: Generates header files with getters/setters
- **C#**: Generates classes with properties and proper attributes
- **Go**: Generates structs with JSON tags for serialization

## Architecture

The tool is built with a modular architecture for maintainability:

- **Config**: Centralized configuration and constants
- **Validator**: Schema validation logic
- **SQL Generator**: SQL generation for tables, functions, and modifications
- **Migration Manager**: Migration file management and state tracking
- **Main Tool**: High-level orchestration and user interface

## Benefits of Refactoring

1. **Maintainability**: Each module has a single responsibility
2. **Testability**: Smaller, focused modules are easier to test
3. **Extensibility**: Easy to add new features or modify existing ones
4. **Readability**: Clear separation of concerns
5. **Reusability**: Components can be used independently

## Examples

See the `schemas/` directory for complete examples including:
- User management system
- Product catalog
- Order processing
- System auditing and configuration

## License

MIT License - see LICENSE file for details.
