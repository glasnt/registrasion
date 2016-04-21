Registrasion Inventory
======================

Registrasion uses an inventory model to keep track of tickets, and the other various products that attendees of your conference might want to have, such as t-shirts and dinner tickets.

The inventory model is split up into Categories and Products. Categories are used to group Products.

Registrasion uses a conditional model to build up complex tickets, or enable/disable specific items to specific users.

Often, you will want to offer free items, such as t-shirts or dinner tickets to your attendees. Registrasion has a Discounts facility that lets you automatically offer free items to your attendees as part of their tickets. You can also automatically offer promotional discounts, such as Early Bird discounts.

Sometimes, you may want to restrict parts of the conference to specific attendees, for example, you might have a Speakers Dinner to only speakers. Or you might want to restrict certain Products to attendees who have purchased other items, for example, you might want to sell Comfy Chairs to people who've bought VIP tickets. You can control showing and hiding specific products using Flags.


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

Each product has the following attributes:

name
    The display name for the product

description
    Some descriptive text that will help the user to understand the product when they're at the registration form

category
    The Category that this product will be grouped under

price
    The price that 1 unit of this product will sell for. Note that this should be the full price, before any discounts are applied.

limit_per_user
    (Optional) This restricts the number of this Product that each attendee may claim. This extends across multiple Invoices.

reservation_duration
    When a Product is added to the user's tentative registration, it is marked as unavailable for a period of time. This allows the user to build up their registration and then pay for it. This reservation duration determines how long an item should be allowed to be reserved whilst being unpaid.

display_order
    An ascending order for displaying the Products within each Category.
