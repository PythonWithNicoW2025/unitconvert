# **unitconvert** 📏🌡️  

*A simple Python package for converting temperature, length, and weight units.*

*This is a demonstration project for the "Python Package Development". Do not confuse this project with the unitconver package in Pypi.org*

## **🔹 Features**
- Convert **Celsius to Fahrenheit** and vice versa.
- Convert **inches to centimeters** and vice versa.
- Convert **kilograms to pounds** and vice versa.
- Easy-to-use functions with accurate conversions.

---

## **📦 Installation**

### **Using pip (from PyPI)**
If published on PyPI, install it with:

```sh
pip install unitconvert
```

### **For Local Development**

If you're developing the package, install it in **editable mode**:

```sh
pip install -e .
```

---

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

---

## **🛠️ Running Tests**

Run all unit tests using `pytest`:

```sh
pytest tests/
```

---

## **📤 Building**

To build the package:

```sh
python -m build
```

---

## **📄 License**
This project is licensed under the MIT License.

---

### **🌟 Contribute & Support**
Feel free to submit issues or contribute by forking the repository!  
For suggestions, reach out via **GitHub Issues**.
