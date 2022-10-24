def check_input_data(val: str):
    if val.replace('-', '').isdigit():
        return int(val)
    elif val.replace('-', '').replace('.', '').isdigit():
        return float(val)
    else:
        return None


