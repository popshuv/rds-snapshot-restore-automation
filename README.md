# RDS Snapshot Restore Automation

This script automates the process of restoring an Amazon RDS database from a **system (automated) snapshot** using the Boto3 library.

## Purpose

System snapshots in RDS (automated backups) have identifiers that start with the prefix `rds:`. However, the `restore_db_instance_from_db_snapshot` function only accepts snapshot identifiers that contain **letters, numbers, and hyphens** — it does **not** accept colons (`:`).

To work around this, the script:

1. **Copies the system snapshot** to a manual snapshot with a valid name (converts `rds:` to `rds-` and replaces underscores with hyphens).
2. **Waits for the manual snapshot** to become available.
3. **Restores a new DB instance** from the manual snapshot.
4. **Waits for the restored DB instance** to be available.

## Requirements

- Python 3
- `boto3` installed (`pip install boto3`)
- `awscli` installed (`pip install awscli`)
- AWS credentials configured with permission to access RDS (either through `aws config` or IAM roles)

## Usage

Update the script with your snapshot identifier and run it in your Python environment.
