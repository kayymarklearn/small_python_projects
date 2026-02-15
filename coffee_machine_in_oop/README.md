# Coffee Machine OOP

A command-line coffee machine simulator built using Object-Oriented Programming principles in Python.

## Features
- Interactive menu system for beverage selection (espresso, latte, cappuccino)
- Resource management (water, milk, coffee) tracking
- Payment processing with change calculation
- Machine status reports
- Machine on/off functionality

## Project Structure
- `main.py` - Main application loop
- `menu.py` - Menu class handling beverage options
- `coffee_maker.py` - CoffeeMaker class for resource management
- `money_machine.py` - MoneyMachine class for payment processing

## Requirements
- Python 3.x

## Installation & Setup
1. Clone or download the project
2. No external dependencies required

## Usage
```bash
python main.py
```

### Commands
- Enter a beverage name (espresso, latte, cappuccino) to order
- Type "report" to see machine resources and money balance
- Type "off" to shut down the machine

### Menu Items
- **Espresso**: $1.50 (Requires: water, coffee)
- **Latte**: $2.50 (Requires: water, milk, coffee)
- **Cappuccino**: $3.00 (Requires: water, milk, coffee)

## How It Works
1. User enters their drink order
2. Machine checks if resources are sufficient
3. User inserts coins for payment
4. If payment is complete, the drink is made
5. Machine deducts resources and updates money balance

