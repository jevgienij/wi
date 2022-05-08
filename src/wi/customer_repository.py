from dataclasses import dataclass


@dataclass
class Customer:
    customer_id: int
    name: str


class CustomerRepository:
    def __init__(self, collection):
        self._collection = collection

    def set(self, customer: Customer):
        raise NotImplementedError

    def get(self, customer: Customer.customer_id):
        raise NotImplementedError

    def pop(self, customer: Customer.customer_id):
        raise NotImplementedError

    def find(self, username: Customer.name):
        raise NotImplementedError
