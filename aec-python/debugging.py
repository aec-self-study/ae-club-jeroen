def divide(x):
    try:
        y = 5 / x
    except ZeroDivisionError:
        import pdb; pdb.set_trace()
        print(f"Warning: denominator of 0. Returning 0 instead of infinity.")


divide(0)