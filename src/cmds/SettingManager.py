def changeSetting(m:str, prefix:str = "!")->(str|None):
    if m.lower().startswith(f'{prefix}config'):
        return m