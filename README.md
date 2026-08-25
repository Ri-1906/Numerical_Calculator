# Numerical Methods Calculator

A desktop-based **Numerical Methods Calculator** built with Python and Tkinter for solving nonlinear equations using different numerical root-finding techniques.

The application provides an interactive GUI where users can enter an equation, select a numerical method, configure tolerance and iteration limits, view the calculated root and error, inspect iteration steps, and optionally visualize the method using graphs.

---

## 📌 Features

* 🧮 Solve nonlinear equations using multiple numerical methods
* 🖥️ User-friendly Tkinter graphical interface
* 📊 Optional graph visualization of the numerical methods
* 📝 Display detailed iteration steps
* ⚙️ Adjustable tolerance and maximum iterations
* 🔄 Dynamic input fields depending on the selected method
* 🧹 Clear previous results easily
* 📋 Load a predefined example
* 🔍 Automatic validation of user inputs
* 🔠 Zoom in/out controls for better accessibility
* ⚠️ Error and overflow handling
* 🎯 Results displayed up to 6 decimal places

The GUI supports the following methods: **Bisection, False Position, Secant, Newton-Raphson, and Simple Fixed-Point Iteration**.

---

## 🧠 Numerical Methods Implemented

### 1. Bisection Method

The Bisection Method repeatedly divides an interval into two halves and selects the subinterval containing the root.

**Required inputs:**

* Function `f(x)`
* Lower bound `a`
* Upper bound `b`
* Tolerance
* Maximum iterations

---

### 2. False Position Method

The False Position Method, also known as **Regula Falsi**, uses a straight line between two points to estimate the root.

**Required inputs:**

* Function `f(x)`
* Lower bound `a`
* Upper bound `b`
* Tolerance
* Maximum iterations

---

### 3. Secant Method

The Secant Method uses two initial approximations and does not require the derivative of the function.

**Required inputs:**

* Function `f(x)`
* Initial approximation `x0`
* Initial approximation `x1`
* Tolerance
* Maximum iterations

The GUI automatically changes the second input label to `Initial Approximation (x1)` when Secant is selected.

---

### 4. Newton-Raphson Method

The Newton-Raphson Method uses the derivative of the function to iteratively approach the root.

**Required inputs:**

* Function `f(x)`
* Initial approximation `x0`
* Tolerance
* Maximum iterations

---

### 5. Simple Fixed-Point Iteration

The Simple Fixed-Point Iteration method repeatedly applies an iteration function to approximate a root.

**Required inputs:**

* Function `f(x)`
* Initial approximation `x0`
* Tolerance
* Maximum iterations

---

## 🖥️ Application Interface

The application provides:

* **Method Selection**
* **Function Input**
* **Initial/Boundary Values**
* **Tolerance**
* **Maximum Iterations**
* **Calculate button**
* **Clear Output button**
* **Load Example button**
* **Iteration Steps option**
* **Graph Window option**
* **Replace Previous Popups option**
* **Zoom In / Zoom Out controls**

The interface is implemented using Tkinter and has a minimum window size of 760×500 pixels.

---

## 📂 Project Structure

```text
Numerical-Methods-Calculator/
│
├── main.py
├── gui.py
├── calculations.py
├── requirements.txt
│
├── methods/
│   ├── bisection.py
│   ├── false_position.py
│   ├── secant.py
│   ├── newton_raphson.py
│   └── simple_fixed_point_iteration.py
│
└── plot_methods/
    └── tk_plot.py
```

### File Description

| File / Folder      | Description                                                        |
| ------------------ | ------------------------------------------------------------------ |
| `main.py`          | Entry point of the application                                     |
| `gui.py`           | Builds and manages the Tkinter GUI                                 |
| `calculations.py`  | Handles input processing and connects the GUI to numerical methods |
| `methods/`         | Contains implementations of the numerical root-finding algorithms  |
| `plot_methods/`    | Contains graph/visualization functions                             |
| `requirements.txt` | Contains Python package dependencies                               |

The application's entry point creates a Tkinter root window and passes it to `create_gui()`.

---

## ⚙️ Technologies Used

* **Python**
* **Tkinter** — Graphical User Interface
* **SymPy** — Mathematical expression parsing and symbolic computation
* **Regular Expressions (`re`)** — Input validation and expression preprocessing

The project currently specifies **SymPy 1.12** as its external dependency.

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/numerical-methods-calculator.git
cd numerical-methods-calculator
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/macOS:**

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

The current requirements file contains:

```text
sympy==1.12
```

Tkinter is normally included with standard Python installations on Windows.

---

## ▶️ Running the Application

Run the main file:

```bash
python main.py
```

The application will open the **Numerical Methods Calculator** GUI.

---

## 🧪 Example

You can enter:

```text
x^3 - x - 2
```

with:

```text
a = 1
b = 2
Tolerance = 0.0001
Maximum Iterations = 20
```

The application also includes a **Load Example** button that automatically loads these values.

The calculator then displays:

```text
Root: ...
Error: ...
```

and can optionally show the complete iteration process.

---

## ✏️ Supported Expression Format

The application supports mathematical expressions such as:

```text
x^2 - 4
x^3 - x - 2
2x^2 + 3x - 5
sin(x)
x^2 + 2*x + 1
```

The application converts:

```text
^
```

to Python/SymPy exponentiation:

```text
**
```

It also preprocesses expressions such as:

```text
2x
```

into:

```text
2*x
```

## before evaluating the function.

## 📈 Graph Visualization

Users can enable **Open Graph Window** from the Options section.

When enabled, the application calls the corresponding plotting function for the selected numerical method.

This helps visualize how the selected algorithm approaches the root.

---

## 📝 Iteration Steps

The **Show Steps of Iteration** option displays the intermediate calculations in a separate window.

This is especially useful for:

* Understanding numerical methods
* Debugging convergence
* Studying numerical analysis
* Demonstrating calculations in academic projects

The application creates a separate window containing the iteration information.

---

## 🛡️ Input Validation

The application performs several checks before calculating the root.

It validates:

* Empty equations
* Invalid mathematical expressions
* Invalid tolerance values
* Invalid iteration counts
* Missing bounds/initial approximations
* Excessive iteration counts
* Numerical overflow

For example, the maximum number of iterations is restricted to prevent excessively large computations.

---

## 🎯 Output

After a successful calculation, the application displays:

```text
Root: <calculated root>
Error: <calculated error>
```

Results are displayed to **6 decimal places**.

---

## 🎓 Educational Purpose

This project is particularly useful for students learning:

* Numerical Analysis
* Root-Finding Algorithms
* Computational Mathematics
* Python GUI Development
* Symbolic Mathematics
* Algorithm Visualization

Instead of performing each numerical calculation manually, users can interactively experiment with different methods and compare their behavior.

---

## 🔮 Future Improvements

Possible improvements include:

* Add more numerical methods such as:

  * Newton's Forward Interpolation
  * Newton's Backward Interpolation
  * Lagrange Interpolation
  * Gauss-Seidel
  * Jacobi Method
  * Runge-Kutta
* Add comparison between multiple methods
* Display convergence graphs together
* Export iteration results to CSV/PDF
* Add dark mode
* Add more advanced mathematical expression support
* Add automatic method convergence detection
* Add unit tests for each numerical method
* Package the application as a standalone `.exe`

---

