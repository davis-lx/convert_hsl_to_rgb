def convert_hsl_to_rgb(hue: float, sat: float, lum: float, max_input=255.0, max_output=255.0):
    """Converts HSI or HSL colors into RGB.

    Accepts hue, sat, and lum as floats or ints, defaulting to 0.0-255.0 range.
    Returns RGB as a list of three floats, defaulting to 0.0-255.0 range.

    Change max_input and max_output to scale this function to your needs;
    for instance, if your input HSI values are in the range of 0.0-1.0, set max_input to 1.0,
    and if you want to output RGB as 0.0-1.0 values, set max_output to 1.0.
    """

    def normalize(value):
        """limits input values to the range of 0.0 through max_input"""
        return (lambda n: max(min(max_input, n), 0.0))(value)

    hue = normalize(hue) * (360/max_input)  # converts to 0.0-360.0
    sat = normalize(sat) / max_input  # converts to 0.0-1.0
    lum = normalize(lum) / max_input  # converts to 0.0-1.0

    c = lum * sat
    x = c * (1 - abs((hue / 60.0) % 2 - 1))

    hue_to_rgb_options = {
        0: [c, x, 0],
        1: [x, c, 0],
        2: [0, c, x],
        3: [0, x, c],
        4: [x, 0, c],
        5: [c, 0, x],
    }

    hue_option = round((hue - (hue % 60)) / 60) % 6
    rgb_template = hue_to_rgb_options[hue_option]
    rgb = [(n + (lum - c)) * max_output for n in rgb_template]

    return rgb
