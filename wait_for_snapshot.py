import boto3

def wait_for_snapshot_availability(snapshot_id):
    """
    Waits for the manual RDS snapshot to become available.

    Parameters:
        snapshot_id (str): The identifier of the snapshot to wait for.

    Uses a waiter to poll the snapshot status until it becomes available,
    with a timeout of up to 1 hour.
    """
    
    rds_client = boto3.client('rds')
    
    # Wait for snapshot to become available
    waiter = rds_client.get_waiter('db_snapshot_available')
    print(f"Waiting for snapshot {snapshot_id} to become available...")
    
    # Counter
    waiter.wait(
        DBSnapshotIdentifier=snapshot_id,
        WaiterConfig={
            'Delay': 30,  # seconds between checks
            'MaxAttempts': 120  # 120 x 30 seconds = 3600 seconds (1 hr)
        }
    )
    
    print(f"Snapshot {snapshot_id} is now available.")