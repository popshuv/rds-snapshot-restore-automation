import boto3

def restore_db_from_snapshot():
    rds_client = boto3.client('rds')
    
    snapshot_id = input("Enter the snapshot ID to restore from: ").strip()
    db_instance_id = f"{snapshot_id}-restored-instance".replace('_', '-')
    
    try:
        response = rds_client.restore_db_instance_from_db_snapshot(
            DBInstanceIdentifier=db_instance_id,
            DBSnapshotIdentifier=snapshot_id,
        )
        print("Snapshot restored")
        print("Response:", response)
    except Exception as e:
        print("Error restoring DB instance from snapshot:", e)

if __name__ == '__main__':
    restore_db_from_snapshot()  
