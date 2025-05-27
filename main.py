import boto3

def restore_db_from_snapshot():
    rds_client = boto3.client('rds')
    
    snapshot_id = input("Enter the snapshot ID to restore from: ").strip()
    db_instance_id = f"{snapshot_id}-restored-instance".replace('_', '-')
                  
    engine = 'mysql'                                  
    allocated_storage = 20 # Example storage size in GB
    
    try:
        response = rds_client.restore_db_instance_from_db_snapshot(
            DBInstanceIdentifier=db_instance_id,
            DBSnapshotIdentifier=snapshot_id,
            DBInstanceClass=db_instance_class,
            Engine=engine,
            AllocatedStorage=allocated_storage,
            PubliclyAccessible=True
        )
        print("DB instance restoration initiated successfully.")
        print("Response:", response)
    except Exception as e:
        print("Error restoring DB instance from snapshot:", e)

if __name__ == '__main__':
    restore_db_from_snapshot()  
