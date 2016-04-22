.. automodule:: registrasion.models

Inventory Management
====================

Registrasion uses an inventory model to keep track of tickets, and the other various products that attendees of your conference might want to have, such as t-shirts and dinner tickets.

The inventory model is split up into Categories and Products. Categories are used to group Products.

Registrasion uses conditionals to build up complex tickets, or enable/disable specific items to specific users:

Often, you will want to offer free items, such as t-shirts or dinner tickets to your attendees. Registrasion has a Discounts facility that lets you automatically offer free items to your attendees as part of their tickets. You can also automatically offer promotional discounts, such as Early Bird discounts.

Sometimes, you may want to restrict parts of the conference to specific attendees, for example, you might have a Speakers Dinner to only speakers. Or you might want to restrict certain Products to attendees who have purchased other items, for example, you might want to sell Comfy Chairs to people who've bought VIP tickets. You can control showing and hiding specific products using Flags.


Categories
----------

Categories are logical groups of Products. Generally, you should keep like products in the same category, and use as many categories as you need.

You will need at least one Category to be able to sell tickets to your attendees.

Each category has the following attributes:

.. autoclass :: Category


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


Discounts
---------

Discounts serve multiple purposes: they can be used to build up complex tickets by automatically waiving the costs for sub-products; they can be used to offer freebie tickets to specific people, or people who hold voucher codes; or they can be used to enable short-term promotional discounts.

Registrasion has several types of discounts, which enable themselves under specific conditions. We'll explain how these work later on, but first:

Common features
~~~~~~~~~~~~~~~
Each discount type has the following common attributes:

description
    Display text that appears on the attendee's Invoice when the discount is applied to a Product on that invoice.

You can apply a discount to individual products, or to whole categories, or both. All of the products and categories affected by the discount are displayed on the discount's admin page.

If you choose to specify individual products, you have these options:

product
    The product that this discount line will apply to.

percentage
    The percentage discount that will be *taken off* this product if this discount applies.

price
    The currency value that will be *taken off* this product if this discount applies.

quantity
    The number of times that each user may apply this discount line. This applies across every valid Invoice that the user has.

If you choose to specify whole categories, you have these options:

category
    The category whose products that this discount line will apply to.

percentage
    The percentage discount that will be *taken off* a product if this discount applies.

quantity
    The number of times that each user may apply this discount line. This applies across every valid Invoice that the user has.

Note that you cannot have a discount apply to both a category, and a product within that category.

Product Inclusions
~~~~~~~~~~~~~~~~~~
Product inclusion discounts allow you to enable a discount when an attendee has selected a specific enabling Product. For example, if you want to give everyone with a ticket a free t-shirt, you can use a product inclusion to offer a 100% discount on the t-shirt category, if the attendee has selected one of your ticket Products.

Once a discount has been enabled in one Invoice, it is available until the quantities are exhausted for that attendee.

You can set the following attributes:

enabling_products
    The products that enable the discount.

Time/stock limit discounts
~~~~~~~~~~~~~~~~~~~~~~~~~~
These discounts allow you to offer a limited promotion that is automatically offered to all attendees. You can specify a time range for when the discount should be enabled, you can also specify a stock limit.

start_time
    (Optional) When the discount should start being offered

end_time
    (Optional) When the discount should stop being offered

limit
    (Optional) How many times the discount is allowed to be applied -- to all users.

Voucher discounts
~~~~~~~~~~~~~~~~~
It's possible to offer voucher codes to attendees to enable a discount. We'll describe these later.

How discounts get applied
~~~~~~~~~~~~~~~~~~~~~~~~~
It's possible for multiple discounts to be available on any given Product. This means there need to be rules for how discounts get applied. It works like so:

#. Take all of the Product that the user currently has selected, and sort them by so that the most expensive comes first.
#. Apply the highest-value discount line for the first Product, until either all such products have a discount applied, or the discount's Quantity has been exhausted for that user for that Product.
#. Repeat until all products have been processed.

In summary, the system greedily applies the highest-value discounts for each product. This may not provide a global optimum, but it'll do.

As an example: say a user has a voucher available for a 100% discount of tickets, and there's a promotional discount for 15% off tickets. In this case, the 100% discount will apply, and the 15% discount will not be disturbed.


Flags
-----

Flags are conditions that can be used to enable or disable Products or Categories, depending on whether conditions are met. They can be used to restrict specific products to specific people, or to place time limits on availability for products.

Common Features
~~~~~~~~~~~~~~~

All flags have some common features:

description
    A human-readable description that is used to identify the flag to staff in the admin interface. It's not seen anywhere else in Registrasion.

condition
    This determines the effect of this flag's condition being met. There are two types of condition:

    **Enable if true** conditions switch on the products and categories included under this flag if *any* such condition is met.

    **Disable if false** conditions *switch off* the products and categories included under this flag is any such condition *is not* met.

    If you have both types of conditions attached to a Product, every *Disable if false* condition must be met, along with one *Enable if true* condition.

products
    The Products affected by this flag.

categories
    The Categories whose Products are affected by this flag.

Dependencies on products from category
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Category Dependency flags have their condition met if a product from the enabling category has been selected by the attendee. For example, if there is an *Accommodation* Category, this flag could be used to enable an *Accommodation Breakfast* category, allowing only attendees with accommodation to purchase breakfast.

The only attribute is

enabling_category
    The category that causes this condition to be met.

Dependencies on products
~~~~~~~~~~~~~~~~~~~~~~~~
Product dependency flags have their condition met if one of the enabling products have been selected by the attendee.

The only attribute is

enabling_products
    The products that cause this condition to be met.

Time/stock limit flags
~~~~~~~~~~~~~~~~~~~~~~
These flags allow the products that they cover to be made available for a limited time, or to set a global ceiling on the products covered. These can be used to remove items from sale once a sales deadline has been met, or if a venue for a specific event has reached capacity.  If there are items that fall under multiple such groupings, it makes sense to set all of these flags to be *disable if false*.

The attributes you can set are:

start_time
    This condition is only met after this time.

end_time
    This condition is only met before this time.

limit
    The number of products that *all users* can purchase under this limit, regardless of their per-user limits.

Voucher flags
~~~~~~~~~~~~~
It is possible to allow the holder of a voucher code to have access to a product as well.
