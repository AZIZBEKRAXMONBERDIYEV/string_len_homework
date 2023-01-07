def main(s1,s2):
    """
    Given two strings, s1 and s2. Return the shortest length between them.
    Args:
        s1: string
        s2: string
    Returns:
        shortest string
    """
    
    x=len(s1)
    d=len(s2)
    if x>d:
       i=s2
    elif d>x:
       i=s1
    return i
print(main('bsavjh','hvac'))

