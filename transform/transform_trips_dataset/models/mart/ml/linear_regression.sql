{{
  config(
    materialized='table' 
    )
}}

select
    trip_id,
    trip_duration_minutes,
    trip_distance,
    passenger_count,
    fare_amount,   
    total_amount,
    tip_amount,
    extract(hour from pickup_datetime) as pickup_hour,
    extract(dayofweek from pickup_datetime) as pickup_day_of_week,
    case 
        when extract(dayofweek from pickup_datetime) in (0, 6) 
        then 1 
        else 0 
    end as is_weekend,
    case 
        when extract(hour from pickup_datetime) between 7 and 9
        or extract(hour from pickup_datetime) between 16 and 19
        then 1 else 0
    end as is_rush_hour,
    trip_distance / nullif(trip_duration_minutes,0) * 60 as avg_speed_mph,
    tip_amount / nullif(fare_amount,0) as tip_percentage,
    pickup_borough as pickup_borough,
    dropoff_borough as dropoff_borough,
    concat(pickup_borough,'_',dropoff_borough) as borough_pair,
    case
        when pickup_zone like '%Airport%'
        or dropoff_zone like '%Airport%'
        then 1 else 0
    end as is_airport_trip

from {{ ref('fct_trips') }} as linear_trips