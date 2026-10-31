/**
 * 
 *  1581. Customer Who Visited but Did Not Make Any Transactions
 * 
 */

# Write your MySQL query statement below

SELECT Visits.customer_id, COUNT(Visits.customer_id) as count_no_trans
FROM Visits
LEFT JOIN Transactions on Transactions.visit_id = Visits.visit_id
WHERE Transactions.transaction_id IS NULL
GROUP BY Visits.customer_id;
