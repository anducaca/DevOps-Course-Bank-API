"""Unit tests for bank.py"""

import pytest
from datetime import datetime

from bank_api.bank import Bank


@pytest.fixture
def bank() -> Bank:
    return Bank()


def test_create_account_raises_error_if_name_blank(bank: Bank):
    # This means: assert an exception is raised during the following block
    with pytest.raises(Exception):
        bank.create_account('')


def test_bank_creates_empty(bank: Bank):
    assert len(bank.accounts) == 0
    assert len(bank.transactions) == 0


def test_can_create_and_get_account(bank: Bank):
    bank.create_account('Test')
    account = bank.get_account('Test')

    assert len(bank.accounts) == 1
    assert account.name == 'Test'


def test_get_account_raises_error_if_no_account_matches(bank: Bank):
    bank.create_account('Name 1')

    # This means: assert an exception is raised during the following block
    with pytest.raises(ValueError):
        bank.get_account('Name 2')


def test_add_funds_creates_transaction(bank: Bank):
    """Ensure add_funds appends a Transaction with the correct account, amount and a datetime."""
    account_name = 'Alice'
    bank.create_account(account_name)

    before = datetime.now()
    bank.add_funds(account_name, 100)

    assert len(bank.transactions) == 1
    tx = bank.transactions[0]
    assert tx.account.name == account_name
    assert tx.amount == 100
    assert isinstance(tx.date, datetime)
    # The transaction date should be at or after the recorded 'before' time
    assert tx.date >= before


def test_add_funds_nonexistent_account_raises(bank: Bank):
    """Adding funds to an account that doesn't exist should raise ValueError (via get_account)."""
    with pytest.raises(ValueError):
        bank.add_funds('NoSuchAccount', 50)


def test_add_funds_allows_negative_amount(bank: Bank):
    """Current behaviour: negative amounts are recorded as transactions.
    This test documents that behavior; if you want to disallow negatives, add validation and update the test.
    """
    name = 'Bob'
    bank.create_account(name)

    bank.add_funds(name, -20)

    assert len(bank.transactions) == 1
    tx = bank.transactions[0]
    assert tx.account.name == name
    assert tx.amount == -20


