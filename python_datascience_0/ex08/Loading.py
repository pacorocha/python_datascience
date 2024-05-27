def ft_tqdm(lst: range) -> None:
    total = len(lst)
    for i, item in enumerate(lst):
        progress = (i + 1) / total * 100
        bar_width = 142
        bar_fill = int(progress / 100 * bar_width)
        arrow = '=' * bar_fill
        bar_size = ' ' * (bar_width - bar_fill)
        progress_str = f"{progress:.0f}%|[{arrow}>]{bar_size}| {i+1}/{total}"
        print(progress_str, end="\r")
        yield item
    print()
