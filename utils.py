# adapted from https://gist.github.com/KerryHalupka/df046b971136152b526ffd4be2872b9d
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

def hex_to_rgb(value):
    """
    Converts hex to rgb colours
    value: string of 6 characters representing a hex colour.
    Returns: list length 3 of RGB values"""
    value = value.strip("#")  # removes hash symbol if present
    lv = len(value)
    return tuple(int(value[i : i + lv // 3], 16) for i in range(0, lv, lv // 3))


def rgb_to_dec(value):
    """
    Converts rgb to decimal colours (i.e. divides each value by 256)
    value: list (length 3) of RGB values
    Returns: list (length 3) of decimal values"""
    return [v / 256 for v in value]


def plot_colourtable(hex_list):

    cell_width = 150
    cell_height = 50
    swatch_width = 48
    margin = 12
    topmargin = 40

    rgb_list = [hex_to_rgb(value) for value in hex_list]
    dec_list = [rgb_to_dec(value) for value in rgb_list]
    name_list = [
        list(named_colors.keys())[list(named_colors.values()).index(value)]
        for value in hex_list
    ]
    names = [
        f"HEX: {col[0]}\nRGB: {col[1]}\nNAME: {col[2]}"
        for col in zip(hex_list, rgb_list, name_list)
    ]
    n = len(names)
    ncols = 3
    nrows = n // ncols + int(n % ncols > 0)

    width = cell_width * 8 + 2 * margin
    height = cell_height * nrows + margin + topmargin
    dpi = 72

    fig, ax = plt.subplots(figsize=(width / dpi, height / dpi), dpi=dpi)
    fig.subplots_adjust(
        margin / width,
        margin / height,
        (width - margin) / width,
        (height - topmargin) / height,
    )
    ax.set_xlim(0, cell_width * 4)
    ax.set_ylim(cell_height * (nrows - 0.5), -cell_height / 2.0)
    ax.yaxis.set_visible(False)
    ax.xaxis.set_visible(False)
    ax.set_axis_off()

    for i, name in enumerate(names):
        row = i % nrows
        col = i // nrows
        y = row * cell_height

        swatch_start_x = cell_width * col
        swatch_end_x = cell_width * col + swatch_width
        text_pos_x = cell_width * col + swatch_width + 7

        ax.text(
            text_pos_x,
            y,
            name,
            fontsize=14,
            horizontalalignment="left",
            verticalalignment="center",
        )

        ax.hlines(y, swatch_start_x, swatch_end_x, color=dec_list[i], linewidth=18)
