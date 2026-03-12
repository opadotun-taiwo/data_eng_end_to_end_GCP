with trip_unioned as (
    select * from {{ ref("unioned_tripdata")}}
),

vendors as (
    select
        distinct vendor_id,
        {{ get_vendor_name('vendor_id') }} as vendor_name
    from trip_unioned
)

select * from vendors