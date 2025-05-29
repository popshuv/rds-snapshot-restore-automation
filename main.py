from dotenv import load_dotenv
load_dotenv()

from copy_snapshot import create_manual_snapshot_from_automated
from wait_for_snapshot import wait_for_snapshot_availability
from restore_snapshot import restore_db_from_snapshot

if __name__ == "__main__":
    
    source_id = input("Enter the snapsshot ID to restore from\nFormat: (rds:[SnapshotIdentifier]-[YYYY]-[MM]-[DD]-[HH]-[MM]) ").strip() # RDS snapshot ID format

    new_snapshot_id = create_manual_snapshot_from_automated(source_id)
    
    wait_for_snapshot_availability(new_snapshot_id)
    
    restore_db_from_snapshot(new_snapshot_id)
        