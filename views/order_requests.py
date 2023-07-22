import sqlite3
import json
from models import Order

ORDERS = [
     {
      "metalId": 1,
      "sizeId": 3,
      "styleId": 2,
      "id": 1
    },
    {
      "metalId": 4,
      "sizeId": 1,
      "styleId": 2,
      "id": 2
    },
    {
      "metalId": 1,
      "sizeId": 1,
      "styleId": 2,
      "id": 3
    },
    {
      "metalId": 1,
      "sizeId": 1,
      "styleId": 1,
      "id": 4
    },
    {
      "metalId": 1,
      "sizeId": 2,
      "styleId": 2,
      "id": 5
    },
    {
      "metalId": 1,
      "sizeId": 1,
      "styleId": 2,
      "id": 6
    }
]

def get_all_orders():
    """ Gets all orders """
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
       SELECT
            o.id,
            o.metal_id,
            o.size_id,
            o.style_id
        FROM Orders o
        """)

        # Initialize an empty list to hold all order representations
        orders = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an order instance from the current row
            order = Order(row['id'], row['metal_id'], row['size_id'], row['style_id'])

            # Add the dictionary representation of the order to the list
            orders.append(order.__dict__)

    return orders

def get_single_order(id):
    """ Gets a single order """
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            o.id,
            o.metal_id,
            o.size_id,
            o.style_id
        FROM Orders o
        WHERE o.id = ?
        """, (id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an order instance from the current row
        order = Order(data['id'], data['metal_id'], data['size_id'],
                        data['style_id'])

        return order.__dict__

def create_order(new_order):
    """ Creates new order """
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Orders
            ( metal_id, size_id, style_id )
        VALUES
            ( ?, ?, ? );
        """, (new_order['metal_id'], new_order['size_id'], new_order['style_id']))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the order dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_order['id'] = id


    return new_order

def delete_order(id):
    """ Deletes order """
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Orders
        WHERE id = ?
        """, (id, ))

def update_order(id, new_order):
    """ Edits order """
    # Iterate the ORDERS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            # Found the order. Update the value.
            ORDERS[index] = new_order
            break
