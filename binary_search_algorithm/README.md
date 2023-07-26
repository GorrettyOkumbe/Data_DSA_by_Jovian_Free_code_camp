Binary search algorithm is one of the algorithms and got the previledge to be working on it first at Free Code Camp.<br>
Just a small explanation on how it works:<br>
----
Say you want to locate a number in a list, Binary search would be the most preferable algorithm to go for as it works on `divide and concur` kind of rule.<br>
Example: The list below and would like to locate the number 2 from the list.<br>
	| 3 | 5 | 6 | 7 | 2 |<br>

For Binary search the list should be sorted either in an increasing or decreasing order.<br>
So in our case when we sort the list say in an increasing order we get something like this:<br>
		| 2 | 3 | 5 | 6 | 7 |<br>
		Note:<br>
			Remember for `Binary Search` the list should always be sorted.<br>
Lists in python are arranged interms of indexes starting from 0 and this indexes are the actual position of a given number in a list.<br>
In our case the number 2 is at index position 0. say our list is called "locate_num" to locate the number 2 we access it by writing locate_num[0] == 2.<br>

In binary search you first ought to dertemine the mid point(using indexes) and if the number you are searching for is same as that located in the middle then return mid.<br>
Otherwise compare if the number at the middle to the number you are looking for in an ascending list like in our case, the mid index is 2 with the number 5 occupying that position.<br>
But we stated that we are searching for the number 2 comparing 5 to 2: 5 > 2 so the number lies on the first half of the list hence we discard the 2nd half.Repeat the above processon the first half of the list.Until the number is located.
