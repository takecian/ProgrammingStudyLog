# https://leetcode.com/problems/combine-two-tables/
# Write your MySQL query statement below
select FirstName, LastName, City, State from Person LEFT OUTER JOIN Address ON Person.PersonId = Address.PersonId;