{bank: 'Unnamed', clients: []}
{bank: 'Unnamed', clients: [('pedro',100)]}
{bank: 'BBVA bank', clients: []}
{bank: 'BBVA bank', clients: [('client1',2000)]}
{bank: 'BBVA bank', clients: [('client1',2000),('client2',500)]}
{bank: 'BBVA bank', clients: [('client1',2000),('client2',500),('juan',200)]}
Error: lupita is not a client of BBVA bank
juan has 200 in its BBVA savings account
pedro withdrew 50 from its Unnamed savings account
{bank: 'Unnamed', clients: [('pedro',50)]}
Error: juan is not a client of Unnamed bank
juan withdrew 100 from its BBVA savings account
{bank: 'BBVA bank', clients: [('client1',2000),('client2',500),('juan',100)]}
Error: client2 is not a client of Unnamed bank
client2 canceled its BBVA savings account
{bank: 'BBVA bank', clients: [('client1',2000),('juan',100)]}
----------------------------------
| * BBVA bank savings accounts * |
----------------------------------
| Client             | Balance   |
----------------------------------
| client1            | $   2,000 |
| juan               | $     100 |
----------------------------------
|              Total | $   2,100 |
----------------------------------
----------------------------------
| * BBVA bank savings accounts * |
----------------------------------
| Client             | Balance   |
----------------------------------
| juan               | $     100 |
----------------------------------
|              Total | $     100 |
----------------------------------
----------------------------------
| * BBVA bank savings accounts * |
----------------------------------
| Client             | Balance   |
----------------------------------
| client1            | $   2,000 |
----------------------------------
|              Total | $   2,000 |
----------------------------------
Added 4 new clients and 1 deposit to BBVA bank
{bank: 'BBVA bank', clients: [('client1',2000),('juan',350)],('client3',450),('hugo',3000),('client4',1500),('isabel',750)}
----------------------------------
| * BBVA bank savings accounts * |
----------------------------------
| Client             | Balance   |
----------------------------------
| client1            | $   2,000 |
| juan               | $     350 |
| client3            | $     450 |
| hugo               | $   3,000 |
| client4            | $   1,500 |
| isabel             | $     750 |
----------------------------------
|              Total | $   8,050 |
----------------------------------
juan canceled its BBVA savings account
Error: roberto is not a client of BBVA bank
isabel canceled its BBVA savings account
----------------------------------
| * BBVA bank savings accounts * |
----------------------------------
| Client             | Balance   |
----------------------------------
| client1            | $   2,000 |
| client3            | $     450 |
| hugo               | $   3,000 |
| client4            | $   1,500 |
----------------------------------
|              Total | $   6,950 |
----------------------------------
Error: juan is not a client of BBVA bank
----------------------------------
| * BBVA bank savings accounts * |
----------------------------------
| Client             | Balance   |
----------------------------------
| hugo               | $   3,000 |
| client1            | $   2,000 |
----------------------------------
|              Total | $   5,000 |
----------------------------------
*** End ***

