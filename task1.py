'''
##### Task 1 Percent Error
Ask the user to input the following:
* the expected number
* the actual result
Calculate the percent difference between the two results. Round your answer to 2 decimal places

```
https://www.skillsyouneed.com/num/percent-change.html

Sample Output:
Enter expected: 10
Enter actual : 9
The percent difference is -10.0%

Enter expected: 12
Enter actual : 14
The percent difference is 16.67%
```
'''
import math 
Eo = (float(input("expected number ")))
Ao = (float(input("the actual output ")))
Pd = -100*(1.0-(Ao/Eo))
Pd = round(Pd,2)
print(f"the percent difference is {Pd}%")