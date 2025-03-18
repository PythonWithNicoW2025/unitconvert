# UnitConvert - Python Package Demonstration

*This is a demonstration project for "Python Package Development". Some parts of this project are intentionally unfinished. Check out the [Instruction.md](./Instruction.md) file for the step-by-step guide.*

## Overview
This project serves as a guide for setting up a Python package, structuring modules, and distributing it. The package, `unitconvert`, provides basic unit conversion functions for:
- Temperature (Celsius ↔ Fahrenheit)
- Length (Inches ↔ Centimeters)
- Weight (Kilograms ↔ Pounds)

## Installation

### **1. Clone the Repository**
```bash
git clone <your-repo-url>
cd unitconvert
```

### **2. Create a Virtual Environment (Recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### **3. Install the Package in Editable Mode**
```bash
pip install -e .
```

## **🚀 Usage**

### **Import the package in Python**

```python
import unitconvert

# Convert temperature
print(unitconvert.celsius_to_fahrenheit(100))  # Output: 212.0
print(unitconvert.fahrenheit_to_celsius(32))   # Output: 0.0

# Convert length
print(unitconvert.inches_to_cm(10))  # Output: 25.4
print(unitconvert.cm_to_inches(25.4))  # Output: 10.0

# Convert weight
print(unitconvert.kg_to_pounds(5))  # Output: 11.0231
print(unitconvert.pounds_to_kg(11.0231))  # Output: 5.0
```

### **Using the CLI**
```bash
python cli.py
```
This will launch an interactive command-line interface for unit conversions.

## Project Structure
```
unitconvert/
│── src/
│   ├── unitconvert/
│   │   ├── __init__.py
│   │   ├── temperature.py
│   │   ├── length.py
│   │   ├── weight.py
│── cli.py
│── setup.py
│── pyproject.toml
│── requirements.txt
│── README.md
│── Instruction.md  # Step-by-step guide
```

## **🛠️ Running Tests**

Run all unit tests using `pytest`:

```sh
pytest tests/
```

## **📤 Building**

To build the package:

```sh
python -m build
```

## License
This project is released under the MIT License.

