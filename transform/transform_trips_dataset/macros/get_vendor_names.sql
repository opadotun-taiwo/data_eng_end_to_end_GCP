{% macro get_vendor_name(vendor_id) -%}
    case
        when {{vendor_id}} = 1 then 'Creative mobile technology llc'
        when {{vendor_id}} = 2 then 'Verfiphone inc'
        when {{vendor_id}} = 4 then 'Unknown Vendor'
    end 
{%- endmacro %} 