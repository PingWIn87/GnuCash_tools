/*SELECT substr(t.post_date, 0, 11) AS date,
       a.name AS category,
       replace(s.value_num / 100.0,'.',',') AS value
  FROM accounts a,
       splits s,
       transactions t
 WHERE s.account_guid = a.guid AND 
       s.tx_guid = t.guid AND 
       a.account_type = 'EXPENSE' AND 
       strftime('%Y-%m-%d', substr(t.post_date, 0, 11) ) >= strftime('%Y-%m-%d', '2022-09-01') 
 ORDER BY date;*/




SELECT strftime('%W',substr(t.post_date, 0, 11)) AS date,
       a.name AS category,
       sum(replace(s.value_num / 100.0,'.',',')) AS value
  FROM accounts a 
       left join  splits s on  s.account_guid = a.guid
       left join transactions t on s.tx_guid = t.guid
 WHERE a.account_type = 'EXPENSE' AND 
       strftime('%Y-%m-%d', substr(t.post_date, 0, 11) ) >= strftime('%Y-%m-%d', '2022-01-01') 
group by 1,2
ORDER BY date;
