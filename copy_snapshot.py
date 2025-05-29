import boto3

def create_manual_snapshot_from_automated(src):
    """
    Creates a manual RDS snapshot from an automated snapshot.

    Parameters:
        src (str): The identifier of the automated snapshot to copy.

    The function generates a new snapshot from system snapshots identifier by modifying the source ID,
    copying the snapshot to a manual snapshot, and returns the new identifier.
    """
    
    rds_client = boto3.client('rds')
    
    # Remove underline characters and replace 'rds:' with 'rds-' as restore_db_instance_from_db_snapshot can't handled '_' or ':' characters
    if src.startswith('rds:'):
        dest = "rds-" + src[len("rds:"):].replace('_', '-')
    else:
        dest = src.replace('_', '-')
        
    try:
        # Create a manual snapshot from the automated snapshot
        rds_client.copy_db_snapshot(
            SourceDBSnapshotIdentifier=src,
            TargetDBSnapshotIdentifier=dest,
        )
        print (f"Snapshot {src} copied to {dest}.")
        return dest
        
    except Exception as e:
        print(f"An error occurred while copying the snapshot: {e}")
        return None