
/*
    Welcome to your first dbt model!
    Did you know that you can also configure models directly within SQL files?
    This will override configurations stated in dbt_project.yml

    Try changing "table" to "view" below
*/

{{ config(materialized='table') }}

with customer_orders as (
  select
     customer_id
     , count(*) as n_orders
     , min(created_at) as first_order_at

  from `analytics-engineers-club.coffee_shop.orders` 
  group by 1
)

select 
  customers.id as customer_id
  , customers.name
  , customers.email
  , coalesce(customer_orders.n_orders, 0) as n_orders
  , customer_orders.first_order_at
from `analytics-engineers-club.coffee_shop.customers` as customers
left join  customer_orders
  on  customers.id = customer_orders.customer_id 

/*
    Uncomment the line below to remove records with null `id` values
*/

-- where id is not null
