import pytest
from mockito import mock
from typing import (
    Iterable,
)

from wi.customer_repository import (
    Customer,
    CustomerRepository,
)


class FakeCollection:
    def __init__(self, customers: Iterable[Customer]):
        self._customers = set(customers)

    def replace_one(self, customer: Customer):
        self._customers.update([customer])

    def find_one(self, customer_id: Customer.customer_id):
        return next(
            customer for customer in self._customers
            if customer.customer_id == customer_id
        )

    def find_one_and_delete(self, customer_id: Customer.customer_id):
        customer = self.find_one(customer_id)
        self._customers.discard(customer)

    def find(self, name: Customer.name):
        return [
            customer for customer in self._customers
            if customer.name == name
        ]


class TestCustomerRepository:
    @pytest.fixture
    def customer0(self):
        return Customer(0, "Mike")

    @pytest.fixture
    def customer1(self):
        return Customer(1, "Eva")

    @pytest.fixture
    def customer2(self):
        return Customer(2, "Eva")

    @pytest.fixture
    def fake_collection(self, customer0, customer1):
        return FakeCollection([customer0, customer1])

    # @pytest.fixture TODO
    # def mocked_collection(self, when):
    #     db = mock(pymongo.collection.Collection)
    #     when(db).replace_one(...).thenReturn(None)
    #     return repo_db

    def test_set_customer_in_repo_updates_fake_collection(
            self, fake_collection, customer0, customer1, customer2
    ):
        repo = CustomerRepository(fake_collection)
        repo.set(customer2)

        expected = {customer0, customer1, customer2}
        assert repo._collection == expected

    def test_get_customer_in_repo_returns_customer_dto(
            self, fake_collection, customer0
    ):
        repo = CustomerRepository(fake_collection)
        actual = repo.get(customer0.customer_id)
        expected = customer0

        assert actual == expected

    def test_pop_customer_in_repo_returns_customer_dto_and_removes_from_collection(
            self, fake_collection, customer0, customer1
    ):
        repo = CustomerRepository(fake_collection)
        actual = repo.pop(customer0.customer_id)
        expected = customer0
        expected_collection = {customer1}

        assert actual == expected
        assert repo._collection == expected_collection

    def test_find_customer_in_repo_returns_list_customer_dto(
            self, fake_collection, customer1
    ):
        repo = CustomerRepository(fake_collection)
        actual = repo.find(customer1.name)
        expected = [customer1]

        assert actual == expected




