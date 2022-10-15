def convert_minutes_to_time(minutes: int) -> str:
    hrs = int(minutes // 60)
    minutes = int(minutes - hrs * 60)
    if hrs:
        return f"{hrs}H {minutes}M"

    return f"{minutes}M"
