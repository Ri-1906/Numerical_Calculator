import tkinter as tk


PLOT_BACKGROUND = "#fffdf8"
AXIS_COLOR = "#50636f"
CURVE_COLOR = "#1c658c"
POINT_COLORS = ["#d94841", "#2f7d32", "#d97706", "#6d28d9", "#0f766e", "#be185d"]


def _safe_float(value):
    try:
        numeric = float(value)
        if numeric != numeric:
            return None
        if numeric == float("inf") or numeric == float("-inf"):
            return None
        return numeric
    except Exception:
        return None


def _compute_samples(f, x_min, x_max, count=240):
    if x_min == x_max:
        x_min -= 1
        x_max += 1

    step = (x_max - x_min) / max(count - 1, 1)
    samples = []
    y_values = []

    for index in range(count):
        x = x_min + index * step
        y = _safe_float(f(x))
        samples.append((x, y))
        if y is not None:
            y_values.append(y)

    if not y_values:
        y_values = [-1.0, 1.0]

    y_min = min(y_values)
    y_max = max(y_values)
    if y_min == y_max:
        y_min -= 1
        y_max += 1

    return samples, y_min, y_max


def _transform(x, y, x_min, x_max, y_min, y_max, width, height, padding):
    plot_width = width - (2 * padding)
    plot_height = height - (2 * padding)
    canvas_x = padding + ((x - x_min) / (x_max - x_min)) * plot_width
    canvas_y = height - padding - ((y - y_min) / (y_max - y_min)) * plot_height
    return canvas_x, canvas_y


def _draw_plot(title, f, x_min, x_max, highlighted_points, details_lines):
    samples, y_min, y_max = _compute_samples(f, x_min, x_max)

    for _, y in highlighted_points:
        safe_y = _safe_float(y)
        if safe_y is not None:
            y_min = min(y_min, safe_y)
            y_max = max(y_max, safe_y)

    y_padding = max((y_max - y_min) * 0.12, 1.0)
    y_min -= y_padding
    y_max += y_padding

    window = tk.Toplevel()
    window.title(title)
    window.geometry("900x620")
    window.configure(bg="#f4efe6")

    header = tk.Label(
        window,
        text=title,
        bg="#16324f",
        fg="white",
        font=("Segoe UI", 16, "bold"),
        anchor="w",
        padx=16,
        pady=12
    )
    header.pack(fill="x")

    info = tk.Label(
        window,
        text="\n".join(details_lines),
        bg="#efe3d3",
        fg="#223843",
        justify="left",
        anchor="w",
        padx=16,
        pady=10
    )
    info.pack(fill="x")

    canvas = tk.Canvas(window, width=860, height=460, bg=PLOT_BACKGROUND, highlightthickness=0)
    canvas.pack(fill="both", expand=True, padx=16, pady=16)

    width = 860
    height = 460
    padding = 52

    zero_x = None
    zero_y = None
    if x_min <= 0 <= x_max:
        zero_x, _ = _transform(0, y_min, x_min, x_max, y_min, y_max, width, height, padding)
    if y_min <= 0 <= y_max:
        _, zero_y = _transform(x_min, 0, x_min, x_max, y_min, y_max, width, height, padding)

    if zero_y is not None:
        canvas.create_line(padding, zero_y, width - padding, zero_y, fill=AXIS_COLOR, width=1)
    if zero_x is not None:
        canvas.create_line(zero_x, padding, zero_x, height - padding, fill=AXIS_COLOR, width=1)

    canvas.create_rectangle(padding, padding, width - padding, height - padding, outline="#b8b3aa")

    previous = None
    for x, y in samples:
        if y is None:
            previous = None
            continue
        current = _transform(x, y, x_min, x_max, y_min, y_max, width, height, padding)
        if previous is not None:
            canvas.create_line(previous[0], previous[1], current[0], current[1], fill=CURVE_COLOR, width=2)
        previous = current

    for index, (x_value, y_value) in enumerate(highlighted_points):
        safe_y = _safe_float(y_value)
        if safe_y is None:
            continue
        px, py = _transform(x_value, safe_y, x_min, x_max, y_min, y_max, width, height, padding)
        color = POINT_COLORS[index % len(POINT_COLORS)]
        canvas.create_line(px, py, px, height - padding, fill=color, dash=(4, 3))
        canvas.create_oval(px - 5, py - 5, px + 5, py + 5, fill=color, outline=color)
        canvas.create_text(px + 10, py - 12, text=f"x={x_value:.4f}", anchor="w", fill=color, font=("Segoe UI", 9, "bold"))

    canvas.create_text(width / 2, height - 18, text="x", fill="#38454f", font=("Segoe UI", 10))
    canvas.create_text(20, height / 2, text="f(x)", angle=90, fill="#38454f", font=("Segoe UI", 10))


def plot_bisection_method(f, a, b, max_iterations, tolerance):
    left = a
    right = b
    midpoint = (left + right) / 2

    for _ in range(max_iterations):
        midpoint = (left + right) / 2
        if abs(right - left) < tolerance:
            break
        if _safe_float(f(left)) * _safe_float(f(midpoint)) < 0:
            right = midpoint
        else:
            left = midpoint

    x_min = min(a, b) - 2
    x_max = max(a, b) + 2
    _draw_plot(
        "Bisection Graph",
        f,
        x_min,
        x_max,
        [(left, f(left)), (right, f(right)), (midpoint, f(midpoint))],
        [
            f"Initial interval: [{a:.4f}, {b:.4f}]",
            f"Current midpoint: {midpoint:.6f}",
            f"Tolerance: {tolerance}"
        ]
    )


def plot_false_position_method(f, a, b, max_iterations, tolerance):
    left = a
    right = b
    estimate = a

    for _ in range(max_iterations):
        fa = _safe_float(f(left))
        fb = _safe_float(f(right))
        if fa is None or fb is None or fb == fa:
            break
        estimate = (left * fb - right * fa) / (fb - fa)
        if abs(estimate - left) < tolerance:
            break
        fx = _safe_float(f(estimate))
        if fx is None:
            break
        if fx * fa < 0:
            right = estimate
        else:
            left = estimate

    x_min = min(a, b) - 2
    x_max = max(a, b) + 2
    _draw_plot(
        "False Position Graph",
        f,
        x_min,
        x_max,
        [(left, f(left)), (right, f(right)), (estimate, f(estimate))],
        [
            f"Initial interval: [{a:.4f}, {b:.4f}]",
            f"Current estimate: {estimate:.6f}",
            f"Tolerance: {tolerance}"
        ]
    )


def plot_secant_method(f, x0, x1, max_iterations, tolerance):
    previous = x0
    current = x1
    next_value = x1

    for _ in range(max_iterations):
        f_previous = _safe_float(f(previous))
        f_current = _safe_float(f(current))
        if f_previous is None or f_current is None or f_current == f_previous:
            break
        next_value = current - (f_current * (current - previous)) / (f_current - f_previous)
        if abs(next_value - current) < tolerance:
            break
        previous, current = current, next_value

    x_min = min(x0, x1, next_value) - 2
    x_max = max(x0, x1, next_value) + 2
    _draw_plot(
        "Secant Graph",
        f,
        x_min,
        x_max,
        [(previous, f(previous)), (current, f(current)), (next_value, f(next_value))],
        [
            f"Starting values: x0={x0:.4f}, x1={x1:.4f}",
            f"Latest secant estimate: {next_value:.6f}",
            f"Tolerance: {tolerance}"
        ]
    )


def plot_newton_raphson_method(f, x0, max_iterations, tolerance):
    current = x0
    next_value = x0

    for _ in range(max_iterations):
        fx = _safe_float(f(current))
        if fx is None:
            break
        derivative = _safe_float((f(current + tolerance) - f(current)) / tolerance)
        if derivative in (None, 0):
            break
        next_value = current - fx / derivative
        if abs(next_value - current) < tolerance:
            break
        current = next_value

    x_min = min(x0, current, next_value) - 3
    x_max = max(x0, current, next_value) + 3
    _draw_plot(
        "Newton-Raphson Graph",
        f,
        x_min,
        x_max,
        [(x0, f(x0)), (current, f(current)), (next_value, f(next_value))],
        [
            f"Initial guess: {x0:.4f}",
            f"Latest estimate: {next_value:.6f}",
            f"Tolerance: {tolerance}"
        ]
    )


def plot_simple_fixed_point_iteration(f, x0, max_iterations, tolerance):
    current = x0
    next_value = x0

    for _ in range(max_iterations):
        fx = _safe_float(f(current))
        if fx is None:
            break
        next_value = fx
        if abs(next_value - current) < tolerance:
            break
        current = next_value

    x_min = min(x0, current, next_value) - 3
    x_max = max(x0, current, next_value) + 3
    _draw_plot(
        "Fixed-Point Graph",
        f,
        x_min,
        x_max,
        [(x0, f(x0)), (current, f(current)), (next_value, f(next_value))],
        [
            f"Initial guess: {x0:.4f}",
            f"Latest estimate: {next_value:.6f}",
            f"Tolerance: {tolerance}"
        ]
    )
