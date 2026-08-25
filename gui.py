from tkinter import *
import tkinter as tk
import tkinter.font as tkfont
from calculations import calculate_root, clear_results

# Define the function for changing the labels based on the selected method
def on_method_change(*args, method_var, a_label, b_label, b_entry):
    method = method_var.get()

    a_label.config(text="Lower Bound (a):" if method in [
                   "Bisection", "False Position"] else "Initial Approximation (x0):")
    if method in ["Bisection", "False Position"]:
        b_label.config(text="Upper Bound (b):")
        b_entry.config(state=tk.NORMAL)
    elif method == "Secant":
        b_label.config(text="Initial Approximation (x1):")
        b_entry.config(state=tk.NORMAL)
    else:
        b_label.config(text="")
        b_entry.config(state=tk.DISABLED)


def create_gui(root):
    def increase_font_size():
        current_size = base_font.actual()["size"]
        new_size = min(current_size + 2, 20)
        update_font_size(new_size)

    def decrease_font_size():
        current_size = base_font.actual()["size"]
        new_size = max(current_size - 2, 8)
        update_font_size(new_size)

    def update_font_size(size):
        base_font.configure(size=size)
        heading_font.configure(size=size + 6, weight="bold")
        subheading_font.configure(size=size + 1, weight="bold")
        root.update_idletasks()

    root.title("Numerical Methods Calculator")
    root.geometry("860x560")
    root.minsize(760, 500)
    root.configure(bg="#f4efe6")

    base_font = tkfont.nametofont("TkDefaultFont")
    base_font.configure(size=11, family="Segoe UI")
    heading_font = tkfont.Font(root=root, family="Segoe UI", size=17, weight="bold")
    subheading_font = tkfont.Font(root=root, family="Segoe UI", size=12, weight="bold")

    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)

    main_frame = Frame(root, bg="#f4efe6", padx=18, pady=18)
    main_frame.grid(row=0, column=0, sticky="nsew")
    main_frame.grid_columnconfigure(0, weight=3)
    main_frame.grid_columnconfigure(1, weight=2)
    main_frame.grid_rowconfigure(1, weight=1)

    header_frame = Frame(main_frame, bg="#16324f", padx=18, pady=16)
    header_frame.grid(row=0, column=0, columnspan=2, sticky="ew", pady=(0, 16))
    header_frame.grid_columnconfigure(0, weight=1)

    Label(
        header_frame,
        text="Numerical Methods Calculator",
        bg="#16324f",
        fg="white",
        font=heading_font
    ).grid(row=0, column=0, sticky="w")
    Label(
        header_frame,
        text="Solve roots, inspect iteration steps, and draw graphs using built-in Tkinter tools.",
        bg="#16324f",
        fg="#d8e6f2"
    ).grid(row=1, column=0, sticky="w", pady=(6, 0))

    form_frame = Frame(main_frame, bg="#fffaf2", bd=1, relief="solid", padx=16, pady=16)
    form_frame.grid(row=1, column=0, sticky="nsew", padx=(0, 12))
    form_frame.grid_columnconfigure(1, weight=1)
    form_frame.grid_columnconfigure(3, weight=1)

    side_frame = Frame(main_frame, bg="#efe3d3", bd=1, relief="solid", padx=16, pady=16)
    side_frame.grid(row=1, column=1, sticky="nsew")
    side_frame.grid_columnconfigure(0, weight=1)

    Label(form_frame, text="Inputs", bg="#fffaf2", fg="#16324f", font=subheading_font).grid(
        row=0, column=0, columnspan=4, sticky="w", pady=(0, 12)
    )

    method_var = tk.StringVar(value="Bisection")
    method_label = Label(form_frame, text="Select Method:", bg="#fffaf2")
    method_label.grid(row=1, column=0, sticky="w", pady=6)
    methods = ["Bisection", "False Position", "Secant",
               "Newton-Raphson", "Simple Fixed-Point Iteration"]
    method_menu = tk.OptionMenu(form_frame, method_var, *methods)
    method_menu.config(width=26, bg="#f7ecd9", highlightthickness=0)
    method_menu.grid(row=1, column=1, columnspan=3, sticky="ew", pady=6)

    expression_label = Label(form_frame, text="Enter f(x):", bg="#fffaf2")
    expression_label.grid(row=2, column=0, sticky="w", pady=6)
    expression_entry = Entry(form_frame, width=35, bd=2, relief="groove")
    expression_entry.grid(row=2, column=1, columnspan=3, sticky="ew", pady=6)
    expression_entry.insert(0, "-2.3x^2 + 3x + 12")

    a_label = Label(form_frame, text="Lower Bound (a):", width=25, anchor="w", bg="#fffaf2")
    a_label.grid(row=3, column=0, sticky="w", pady=6)
    a_entry = Entry(form_frame, bd=2, relief="groove")
    a_entry.grid(row=3, column=1, sticky="ew", pady=6, padx=(0, 12))
    a_entry.insert(0, "1")

    b_label = Label(form_frame, text="Upper Bound (b):", bg="#fffaf2")
    b_label.grid(row=3, column=2, sticky="w", pady=6)
    b_entry = Entry(form_frame, bd=2, relief="groove")
    b_entry.grid(row=3, column=3, sticky="ew", pady=6)
    b_entry.insert(0, "5")

    tolerance_label = Label(form_frame, text="Tolerance:", bg="#fffaf2")
    tolerance_label.grid(row=4, column=0, sticky="w", pady=6)
    tolerance_entry = Entry(form_frame, bd=2, relief="groove")
    tolerance_entry.insert(0, "0.01")
    tolerance_entry.grid(row=4, column=1, sticky="ew", pady=6, padx=(0, 12))

    max_iterations_label = Label(form_frame, text="Max Iterations:", bg="#fffaf2")
    max_iterations_label.grid(row=4, column=2, sticky="w", pady=6)
    max_iterations_entry = Entry(form_frame, bd=2, relief="groove")
    max_iterations_entry.insert(0, "10")
    max_iterations_entry.grid(row=4, column=3, sticky="ew", pady=6)

    method_var.trace("w", lambda *args: on_method_change(method_var=method_var,
                     a_label=a_label, b_label=b_label, b_entry=b_entry))

    button_row = Frame(form_frame, bg="#fffaf2")
    button_row.grid(row=5, column=0, columnspan=4, sticky="ew", pady=(16, 4))
    button_row.grid_columnconfigure(0, weight=1)
    button_row.grid_columnconfigure(1, weight=1)
    button_row.grid_columnconfigure(2, weight=1)

    calculate_button = Button(
        button_row,
        text="Calculate",
        bg="#1f6f50",
        fg="white",
        activebackground="#2f8f68",
        activeforeground="white",
        padx=12,
        pady=6,
        command=lambda: [clear_results(result_label, error_label, info_label), calculate_root(
        root, method_var, expression_entry, tolerance_entry, max_iterations_entry, a_entry, b_entry, result_label, error_label, info_label, check_var, plot_var, clear_var)])
    calculate_button.grid(row=0, column=0, sticky="ew", padx=(0, 8))

    reset_button = Button(
        button_row,
        text="Clear Output",
        bg="#d6c3a5",
        activebackground="#e2d1b8",
        padx=12,
        pady=6,
        command=lambda: clear_results(result_label, error_label, info_label)
    )
    reset_button.grid(row=0, column=1, sticky="ew", padx=8)

    example_button = Button(
        button_row,
        text="Load Example",
        bg="#d6c3a5",
        activebackground="#e2d1b8",
        padx=12,
        pady=6,
        command=lambda: [expression_entry.delete(0, END), expression_entry.insert(0, "x^3 - x - 2"),
                         a_entry.delete(0, END), a_entry.insert(0, "1"),
                         b_entry.delete(0, END), b_entry.insert(0, "2"),
                         tolerance_entry.delete(0, END), tolerance_entry.insert(0, "0.0001"),
                         max_iterations_entry.delete(0, END), max_iterations_entry.insert(0, "20")]
    )
    example_button.grid(row=0, column=2, sticky="ew", padx=(8, 0))

    Label(side_frame, text="Results", bg="#efe3d3", fg="#16324f", font=subheading_font).grid(
        row=0, column=0, sticky="w"
    )
    Label(
        side_frame,
        text="Run the calculator directly with Python. No separate executable is needed.",
        bg="#efe3d3",
        fg="#4b5d67",
        justify="left",
        wraplength=250
    ).grid(row=1, column=0, sticky="w", pady=(8, 16))

    result_label = Label(side_frame, text="", bg="#efe3d3", anchor="w", justify="left", wraplength=260)
    result_label.grid(row=2, column=0, sticky="ew", pady=(0, 10))
    error_label = Label(side_frame, text="", bg="#efe3d3", anchor="w", justify="left", wraplength=260)
    error_label.grid(row=3, column=0, sticky="ew", pady=(0, 10))
    info_label = Label(
        side_frame,
        text="Note: Results are rounded to 6 decimal places.",
        bg="#efe3d3",
        anchor="w",
        justify="left",
        wraplength=260
    )
    info_label.grid(row=4, column=0, sticky="ew", pady=(0, 18))

    Label(side_frame, text="Options", bg="#efe3d3", fg="#16324f", font=subheading_font).grid(
        row=5, column=0, sticky="w", pady=(0, 8)
    )

    check_var = tk.IntVar(value=1)
    check_button = Checkbutton(
        side_frame, text="Show Steps of Iteration", variable=check_var, bg="#efe3d3", anchor="w")
    check_button.grid(row=6, column=0, sticky="w")

    plot_var = tk.IntVar(value=0)
    plot_button = Checkbutton(side_frame, text="Open Graph Window", variable=plot_var, bg="#efe3d3", anchor="w")
    plot_button.grid(row=7, column=0, sticky="w")

    clear_var = tk.IntVar(value=1)
    clear_button = Checkbutton(side_frame, text="Replace Previous Popups", variable=clear_var, bg="#efe3d3", anchor="w")
    clear_button.grid(row=8, column=0, sticky="w", pady=(0, 18))

    Label(side_frame, text="Accessibility", bg="#efe3d3", fg="#16324f", font=subheading_font).grid(
        row=9, column=0, sticky="w", pady=(0, 8)
    )
    font_row = Frame(side_frame, bg="#efe3d3")
    font_row.grid(row=10, column=0, sticky="ew")
    font_row.grid_columnconfigure(0, weight=1)
    font_row.grid_columnconfigure(1, weight=1)

    zoom_in_button = Button(font_row, text="+ Zoom In", command=increase_font_size, bg="#d6c3a5")
    zoom_in_button.grid(row=0, column=0, sticky="ew", padx=(0, 6))

    zoom_out_button = Button(font_row, text="- Zoom Out", command=decrease_font_size, bg="#d6c3a5")
    zoom_out_button.grid(row=0, column=1, sticky="ew", padx=(6, 0))

    root.protocol("WM_DELETE_WINDOW", lambda: root.destroy())
    
    root.mainloop()

if __name__ == '__main__':
    root = tk.Tk()
    create_gui(root)
