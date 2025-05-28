# Luhn Credit Card Validator

This Python script validates credit card numbers using the **Luhn algorithm**, a widely used checksum formula that helps detect errors in identification numbers.

## 📌 Features

- Accepts credit card numbers with or without spaces or dashes
- Implements the Luhn algorithm
- Interactive user input
- Input cleaning and validation
- Command-line interface

## 🚀 How It Works

1. The user is prompted to enter a credit card number.
2. All non-digit characters are removed.
3. The number is processed in reverse:
   - Odd-position digits are added directly.
   - Even-position digits are doubled and split if over 9.
4. If the total modulo 10 is `0`, the number is **valid**.

## ✅ Example