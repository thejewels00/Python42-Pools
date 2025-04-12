def ft_tqdm(lst: range) -> None:
    ''' this function is a generator that prints the progress of a loop '''
    total = len(lst)
    for i, item in enumerate(lst):
        percent = (i + 1) / total * 100
        bar_length = 60
        filled_length = int(bar_length * (i + 1) // total)
        bar = '█' * filled_length + '-' * (bar_length - filled_length - 1)
        print(f'\r{percent:.0f}%|{bar}| {i + 1}/{total}', end='', flush=True)
        yield item
    print()
