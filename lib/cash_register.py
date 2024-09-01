#!/usr/bin/env python3
class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction_amount = 0

    def add_item(self, title, price, quantity=1):
        """Adds an item to the register and updates the total."""
        self.items.extend([title] * quantity)
        self.total += price * quantity
        self.last_transaction_amount = price * quantity

    def apply_discount(self):
        """Applies the discount to the total."""
        if self.discount > 0:
            discount_amount = (self.total * self.discount) / 100
            self.total -= discount_amount
            # Adjust the print statement to match the expected format
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        """Subtracts the last transaction amount from the total and removes the items."""
        self.total -= self.last_transaction_amount
        # Calculate the amount for the last transaction
        transaction_amount = self.last_transaction_amount
        # Remove the last transaction's items from the list
        while transaction_amount > 0 and self.items:
            self.items.pop()
            transaction_amount -= self.last_transaction_amount / len(self.items) if len(self.items) > 0 else 0
        self.last_transaction_amount = 0


