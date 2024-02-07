# Color Universal Design colourblind-friendly python matplotlib palette

This repository contains a python file [`cud.py`](./cud.py) which contains a dictionary, list, and associated function for creating a palette based on the [Color Universal Design][cud].

## Usage

Copy and paste the contents of `cud.py` into your project and use the `cud()` function as follows.

The standard 8-colour palette

```
palette = cud()
plot_colourtable(palette)
```

![standard palette](./imgs/standard.png)

Or you can offset and start from the second colour

```
palette = cud(start=1)
plot_colourtable(palette)
```

![offset palette](./imgs/offset.png)

Or only select three colours

```
palette = cud(n=3)
plot_colourtable(palette)
```

![three palette](./imgs/three.png)

See [`utils.py`](./utils.py) for the code used to generate the above plots.

[cud]: https://jfly.uni-koeln.de/color/