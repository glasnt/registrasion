Registrasion Inventory
======================

Registrasion uses an inventory model to keep track of tickets, and the other various products that attendees of your conference might want to have, such as t-shirts and dinner tickets.

The inventory model is split up into Categories and Products. Categories are used to group Products.

It is possible to enable or disable products based on conditions, using Flags; and to automatically apply discounts to products. You can use discounts and flags to offer free items as inclusions as parts of tickets, but this means that you can also sell extra items to your attendees if they want to pay for them.


Categories
----------

Categories are logical groups of Products. Generally, you should keep like products in the same category, and use as many categories as you need.

You will need at least one Category to be able to sell tickets to your attendees.

Each category has the following attributes:

name
    The display name for the category.

description
    Some explanatory text for the category. This is displayed alongside the forms where your attendees choose their items.

required
    Requires a user to select an item from this category during initial registration. You can use this, e.g., for making sure that the user has a ticket before they select whether they want a t-shirt.

render_type
    This is used to determine what sort of form the attendee will be presented with when choosing Products from this category. Currently, there are two types of form that can be displayed:

    **Radio button** presents the Products in the Category as a list of radio buttons. At most one item can be chosen at a time. This works well when setting limit_per_user to 1.

    **Quantity boxes** will show each Product next to an input field, where the user can specify a quantity of each Product type. This is useful for additional extras, like Dinner Tickets.

limit_per_user
    (Optional) This restricts the number of items from this Category that each attendee may claim. This extends across multiple Invoices.

display_order
    An ascending order for displaying the Categories available. By convention, your Category for ticket types should have the lowest display order.


Products
--------

Products represent the different items that comprise a user's conference ticket.
