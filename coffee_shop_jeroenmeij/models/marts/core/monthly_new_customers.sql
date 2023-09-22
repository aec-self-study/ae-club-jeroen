
-- Use the `ref` function to select from other models
with customers as (
    select * from {{ ref('customers') }}
),

final as (
    select
        date_trunc(first_order_at, month) as signup_month,
        count(*) as new_customers

    from customers
    group by 1
)

Select *
from final