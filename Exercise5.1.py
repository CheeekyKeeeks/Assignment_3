import time

def get_current_time_and_days_since_epoch():
    # Get the current time in seconds since the epoch
    current_time_seconds = time.time()
    
    # Calculate the number of days since the epoch
    days_since_epoch = int(current_time_seconds // 86400)
    
    # Calculate the remaining seconds since the last full day
    remaining_seconds = current_time_seconds % 86400
    
    # Calculate hours, minutes, and seconds from the remaining seconds
    hours = int(remaining_seconds // 3600)
    remaining_seconds %= 3600
    minutes = int(remaining_seconds // 60)
    seconds = remaining_seconds % 60
    
    # Print the number of days since the epoch
    print(f"Days since epoch: {days_since_epoch}")
    
    # Print the current time of day in hours, minutes, and seconds
    print(f"Current time of day: {hours:02}:{minutes:02}:{seconds:06.3f}")

# Call the function to print the current time and days since epoch
get_current_time_and_days_since_epoch()
