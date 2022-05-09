import pytest
from dataclasses import asdict
from mockito import mock, ANY
from typing import (
    Iterable,
)
import pymongo

from wi.customer_repository import (
    Customer,
    CustomerRepository,
)


class FakeCollection:
    def __init__(self, customers: dict):
        self._customers = customers  # {customer_id: name, ...}

    def replace_one(self, filter: dict, replacement: dict, **kwargs):
        self._customers.update({replacement['customer_id']: replacement['name']})

    def find_one(self, filter: dict, **kwargs):
        return {
            'customer_id': filter['customer_id'],
            'name': self._customers.get(filter['customer_id']),
        }

    def find_one_and_delete(self, filter: dict, **kwargs):
        ret = self.find_one(filter)
        self._customers.pop(filter['customer_id'])
        return ret

    def find(self, filter: dict, **kwargs):
        name = filter['name']
        return [
            {'customer_id': k, 'name': v} for k, v in self._customers.items() if v == name
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
    def customer0_dict(self) -> dict:
        return {0: "Mike"}

    @pytest.fixture
    def customer1_dict(self):
        return {1: "Eva"}

    @pytest.fixture
    def customer2_dict(self):
        return {2: "Eva"}

    @pytest.fixture
    def fake_collection(self, customer0_dict, customer1_dict):
        return FakeCollection({**customer0_dict, **customer1_dict})

    def test_set_customer_in_repo_updates_fake_collection(
            self, fake_collection, customer0, customer1, customer2,
            customer0_dict, customer1_dict, customer2_dict,
    ):
        repo = CustomerRepository(fake_collection)
        repo.set(customer2)

        expected = {**customer0_dict, **customer1_dict, **customer2_dict}
        assert repo._collection == expected

    def test_get_customer_in_repo_returns_customer_dto(
            self, fake_collection, customer0
    ):
        repo = CustomerRepository(fake_collection)
        actual = repo.get(customer0.customer_id)
        expected = asdict(customer0)

        assert actual == expected

    def test_pop_customer_in_repo_returns_customer_dto_and_removes_from_collection(
            self, fake_collection, customer0, customer1_dict
    ):
        repo = CustomerRepository(fake_collection)
        actual = repo.pop(customer0.customer_id)
        expected = asdict(customer0)
        expected_collection = {customer1_dict}

        assert actual == expected
        assert repo._collection == expected_collection

    def test_find_customer_in_repo_returns_list_customer_dto(
            self, fake_collection, customer1
    ):
        repo = CustomerRepository(fake_collection)
        actual = repo.find(customer1.name)
        expected = [asdict(customer1)]

        assert actual == expected

    @pytest.fixture
    def mocked_collection(self, when):
        collection = mock(pymongo.collection.Collection)
        when(collection).replace_one(...).thenReturn(None)
        when(collection).find_one().thenReturn(None)
        return collection


