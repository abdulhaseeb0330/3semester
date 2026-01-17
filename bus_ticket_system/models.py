"""
Module containing data model classes for the Bus Ticket System
"""

class TicketCategory:
    """Represents a category of tickets"""
    def __init__(self, category_id, name, description=""):
        self.category_id = category_id
        self.name = name
        self.description = description
        self.ticket_types = []  # List of TicketType objects
    
    def add_ticket_type(self, ticket_type):
        """Add a ticket type to this category"""
        self.ticket_types.append(ticket_type)
    
    def display_info(self):
        """Display category information"""
        print(f"\n{'='*50}")
        print(f"Category: {self.name}")
        print(f"{'='*50}")
        if self.description:
            print(f"Description: {self.description}")
        print(f"Number of ticket types: {len(self.ticket_types)}")
        return self
    
    def __str__(self):
        return f"{self.category_id}: {self.name} ({len(self.ticket_types)} types)"


class TicketType:
    """Represents a specific ticket type/top-up"""
    def __init__(self, type_id, name, category, price, duration_type, 
                 duration_value, entitlement_type, max_persons=1, notes=""):
        self.type_id = type_id
        self.name = name
        self.category = category
        self.price = float(price)
        self.duration_type = duration_type  # 'minutes', 'days', 'annual'
        self.duration_value = duration_value
        self.entitlement_type = entitlement_type  # 'fixed' or 'flexible'
        self.max_persons = int(max_persons)
        self.notes = notes
    
    def calculate_cost(self, quantity=1):
        """Calculate total cost for given quantity"""
        return self.price * quantity
    
    def display_details(self):
        """Display detailed ticket information"""
        print(f"\n{'-'*40}")
        print(f"Ticket: {self.name}")
        print(f"{'-'*40}")
        print(f"Category: {self.category}")
        print(f"Price: £{self.price:.2f}")
        print(f"Duration: {self.duration_value} {self.duration_type}")
        print(f"Entitlement: {self.entitlement_type}")
        print(f"Max Persons: {self.max_persons}")
        if self.notes:
            print(f"Notes: {self.notes}")
        return self
    
    def __str__(self):
        return f"{self.type_id}: {self.name} - £{self.price:.2f}"


class User:
    """Represents a system user/customer"""
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.purchase_history = []  # List of Purchase objects
    
    def make_purchase(self, ticket_type, quantity, purchase_manager):
        """Create a purchase record"""
        from datetime import datetime
        purchase_id = f"P{datetime.now().strftime('%Y%m%d%H%M%S')}"
        purchase = Purchase(purchase_id, self.user_id, ticket_type, quantity)
        self.purchase_history.append(purchase)
        purchase_manager.save_purchase(purchase)
        return purchase
    
    def view_history(self):
        """Display user's purchase history"""
        if not self.purchase_history:
            print(f"\nNo purchase history for {self.name}")
            return
        
        print(f"\n{'='*60}")
        print(f"Purchase History for {self.name}")
        print(f"{'='*60}")
        total_spent = 0
        for purchase in self.purchase_history:
            purchase.display_receipt()
            total_spent += purchase.total_cost
        
        print(f"\nTotal spent: £{total_spent:.2f}")
        print(f"Total purchases: {len(self.purchase_history)}")
    
    def __str__(self):
        return f"User: {self.name} (ID: {self.user_id})"


class Purchase:
    """Represents a ticket purchase transaction"""
    def __init__(self, purchase_id, user_id, ticket_type, quantity):
        self.purchase_id = purchase_id
        self.user_id = user_id
        self.ticket_type = ticket_type
        self.quantity = int(quantity)
        self.total_cost = ticket_type.calculate_cost(quantity)
        from datetime import datetime
        self.timestamp = datetime.now()
    
    def display_receipt(self):
        """Display purchase receipt"""
        print(f"\nReceipt #{self.purchase_id}")
        print(f"Date: {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Ticket: {self.ticket_type.name}")
        print(f"Quantity: {self.quantity}")
        print(f"Unit Price: £{self.ticket_type.price:.2f}")
        print(f"Total: £{self.total_cost:.2f}")
    
    def to_dict(self):
        """Convert purchase to dictionary for JSON serialization"""
        return {
            'purchase_id': self.purchase_id,
            'user_id': self.user_id,
            'ticket_type_id': self.ticket_type.type_id,
            'ticket_name': self.ticket_type.name,
            'quantity': self.quantity,
            'unit_price': self.ticket_type.price,
            'total_cost': self.total_cost,
            'timestamp': self.timestamp.strftime('%Y-%m-%d %H:%M:%S')
        }
    
    def __str__(self):
        return f"Purchase {self.purchase_id}: {self.quantity} x {self.ticket_type.name}"