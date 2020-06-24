from datetime import date, timedelta
import pytest

# from model import ...
from model import Batch, OrderLine

today = date.today()
tomorrow = today + timedelta(days=1)
later = tomorrow + timedelta(days=10)


def test_allocating_to_a_batch_reduces_the_available_quantity():
    # batch attributes : Unique ID, SKU, Quantity, ETA
    batch = Batch("batch-001", "SMALL-TABLE", qty=20, eta=today)
    # Order Line attributes : Order Reference, Product SKU, Quantity
    line = OrderLine('order-ref', "SMALL-TABLE", 2)
    batch.allocate(line)
    assert batch.available_quantity == 18


def test_can_allocate_if_available_greater_than_required():
    batch = Batch("batch-001", "SMALL-TABLE", qty=3, eta=today)
    line = OrderLine('order-ref', "SMALL-TABLE", 2)
    batch.allocate(line)

    assert batch.available_quantity == 1


def make_batch_and_line(sku, batch_qty, line_qty):
    return (
        Batch("batch-001", sku, batch_qty, eta=today),
        OrderLine("order-ref", sku, line_qty)
    )


def test_cannot_allocate_if_available_smaller_than_required():
    batch = Batch("batch-001", "SMALL-TABLE", qty=1, eta=today)
    line = OrderLine('order-ref', "SMALL-TABLE", 2)
    batch.allocate(line)

    assert batch.available_quantity == 1


def test_can_allocate_if_available_equal_to_required():
    batch = Batch("batch-001", "SMALL-TABLE", qty=2, eta=today)
    line = OrderLine('order-ref', "SMALL-TABLE", 2)
    batch.allocate(line)

    assert batch.available_quantity == 0


def test_cannot_allocate_if_skus_do_not_match():
    batch = Batch("batch-001", "SMALL-TABLE", qty=10, eta=today)
    line = OrderLine('order-ref', "BIG-TABLE", 2)
    batch.allocate(line)

    assert batch.available_quantity == 10


def test_allocation_is_idempotent():
    batch, line = make_batch_and_line("SMALL-TABLE", 10, 2)
    batch.allocate(line)
    batch.allocate(line)

    assert batch.available_quantity == 18

def test_deallocate():
    pass


def test_can_only_deallocate_allocated_lines():
    pass
