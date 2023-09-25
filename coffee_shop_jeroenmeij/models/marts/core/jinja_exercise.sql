{% set product_categories = ['coffee beans', 'merch', 'brewing supplies'] %}

select
    date_trunc(sold_at, month) as date_month,

    {% for category in product_categories %}
        sum(case when product_category = '{{ category }}' then amount end) as {{ category | replace(" ", "_") }}_amount
        {% if not loop.last %},{% endif %}
    {% endfor %}

from {{ ref('item_sales') }}
group by 1

--   sum(case when product_category = 'coffee beans' then amount end) as coffee_beans_amount,
--   sum(case when product_category = 'merch' then amount end) as merch_amount,
--   sum(case when product_category = 'brewing supplies' then amount end) as brewing_supplies_amount