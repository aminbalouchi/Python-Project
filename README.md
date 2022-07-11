
# Finance Management of a Building
## Video Demo:  <https://youtu.be/KgBHkQYhUbg>
## Description:
### Group members : 
Amir Hossein Ghazi Moradi, Mohammad Amin Balouchi, Marzieh Ghanbari

---  

### Contents :
1.Introduction
  
2.Program guide
  
3.Reference to the code (modules, how each section works and visual output)
  
4.Describe the process of doing and dividing the work and the challenges of the team 

---

### Introduction
With the expansion of cities, there have been significant changes in the way people living in large cities live. The number of floors of buildings has increased, and with this dramatic increase, the problems are also increasing. With the increasing advancement of technology, building management software as a modern solution to prevent problems and disagreements among the residents of a building or residential complex, came to the aid of the manager or building managers.
  
 Building management software provides the ability to manage the building charge and solve the problems that arise in the building that today more or less all people are in contact with them.
  
Our program has the ability to record various transactions of the building, both in part and in general, and the types of reports in the user's desired areas such as invoices, financial balances, cost sharing of groups and subgroups, display Provides a visual trend of costs, estimating the amount of building charge for next year in terms of inflation rate, etc. In all these cases, the user can select and categorize the desired time period and the desired residential units.

---

### Guide to working with the program
In this part of the report, we refer to how to work with the program and how to order it
At the beginning of the program, two different commands can be given to the program:

1. ***append***: to record various transactions

By entering this command, a new transaction can be added to the list of building transactions

![image](https://user-images.githubusercontent.com/78914703/147603262-31483e0a-fd62-43ed-a636-88993aa2c02d.png)

1.1 **for all**: To record a specific transaction that is subject to all units (or several specific units)

![image](https://user-images.githubusercontent.com/78914703/147603342-f953f395-1f29-43fb-8aaa-eec202163d41.png)
 
By entering the command for all, we enter the details of the transaction in order

1.1.2 **time**: the time of the transaction which is entered in two forms;

now: Automatically receives the current time from the system

Or a numeric set in the form of 12-05-1398 (line between year and month and day) that is entered manually

1.1.3 **amount**: takes the cost of the transaction from the user

![image](https://user-images.githubusercontent.com/78914703/147603401-5c6b0784-aaa5-4354-b544-9b5923fd77e0.png)

1.1.4 **category**: Receives the transaction related category from the user

(bill, elevator, cleaning, parking, repairing, others)

![image](https://user-images.githubusercontent.com/78914703/147603510-35f80bce-e443-47cc-8280-8a340e13727c.png)

1.1.5: **sub category**: receives the transaction related category from the user

For bill: (gas, electricity, water, city hall)

For other categories: undefined

![image](https://user-images.githubusercontent.com/78914703/147603539-e1fde625-24c9-4398-a9b6-4ced80386c91.png)

1.1.6 **type of division**: How to divide the cost between units

e: Equally

s: In terms of house area

r: In terms of the number of areas

p: Depending on the number of parking spaces

percent: In terms of percentages that the user assigns to each unit

For example for a five-person building: 20-40-0-15-25 (percentages respectively, single and with one dash are separated)

![image](https://user-images.githubusercontent.com/78914703/147603663-e680fbfc-6a76-4d99-804e-66ffd21d147a.png)

d: Default segmentation for each category

![image](https://user-images.githubusercontent.com/78914703/147603578-24f6ada9-1cef-405f-b8ae-3bc9c4ce198a.png)

1.1.7 **responsible unit**: Specifies the unit responsible for the transaction

![image](https://user-images.githubusercontent.com/78914703/147603708-fab55a0c-7198-49d3-9b45-9373a42583db.png)

And thus the transaction is entered into the list of transactions

1.2 **for one**: To record a specific transaction that is subject to one of the units

1.2.1 **time**

1.2.2 **amount**

1.2.3 **category**

1.2.4 **sub category**

1.2.5 **related unit**: The unit related to the reaction

1.2.6 **resposible unit**

![image](https://user-images.githubusercontent.com/78914703/147606265-b3bcd9e7-cfa3-4e9b-a4af-4a0d453a17b8.png)

2. ***report***: Get a report of the program

2.1 **financial balance**: To get the financial balance of the desired units in the desired time period (which is the output for the user
Displays on console also saves as csv file)

2.1.1 **start time**: The start time of the interval

2.1.2 **end time**: The end time of the interval

2.1.3 **units**: the desired units

all: All units. Or as a set of numbers separated by a hyphen

![image](https://user-images.githubusercontent.com/78914703/147606488-0c8010c1-14ca-4bd2-8b82-672f8e24103f.png)

2.2 **portion**: To show the share below the category

![image](https://user-images.githubusercontent.com/78914703/147606621-9f3dcc6d-f611-497f-ab45-dd26b85f1818.png)

2.2.1 **in total**: Shows the share of the following categories in all categories

2.2.1.1 **sub categories**: Enter the desired categories (a set of numbers separated by a hyphen)

![image](https://user-images.githubusercontent.com/78914703/147606640-8238d151-d53e-4636-a5e7-c7327ceb8fa7.png)
  
Output:

![image](https://user-images.githubusercontent.com/78914703/147606650-57f17016-5e8a-4749-af81-96ff0e21aa27.png)

2.2.2 **in group**: Shows the share of subcategory in its category (for bill category only)

2.2.2.1 **sub categories**: Enter the desired categories (a set of numbers separated by a hyphen)

![image](https://user-images.githubusercontent.com/78914703/147606756-037d33b4-3261-41a2-9b37-ba931498ae71.png)

Output:

![image](https://user-images.githubusercontent.com/78914703/147606775-b2dc15b3-e1d0-4ccc-b8e2-349cb679368c.png)

2.3 **cost trend**: Shows cost trends in the form of aggregate charts

![image](https://user-images.githubusercontent.com/78914703/147607020-4bc8569d-0927-47ad-b001-93af17d0e023.png)

2.3.1 **units** (cost trend for units):

2.3.1.1 **units list**: Receives the desired units

2.3.1.2 **sub categories list**: Receives the desired categories

2.3.1.3 **start time**

2.3.1.4 **end time**

![image](https://user-images.githubusercontent.com/78914703/147607042-282dd7ca-c038-4204-8477-38b2c5f26869.png)

Output:

![image](https://user-images.githubusercontent.com/78914703/147607054-8f95c1c0-ee52-4994-aeae-aaf36c2b7bb7.png)

2.3.2 **sub categories** (cost trend for categories)

2.3.2.1 **sub categories list**

2.3.2.2 **start time**

2.3.2.3 **end time**

![image](https://user-images.githubusercontent.com/78914703/147607197-39c10287-cce7-45f0-9b85-88fad858e723.png)

Output:

![image](https://user-images.githubusercontent.com/78914703/147607213-128a73db-fec3-43bd-a369-606053c0e6db.png)

2.4 **predicting the charge cost**: Shows the charge cost of the building next year in terms of previous data and inflation rate

2.4.1 **start time**

2.4.2 **end time**

2.4.3 **inflation rate**: Receives the inflation rate as input

![image](https://user-images.githubusercontent.com/78914703/147607412-2fb9d202-69a4-4457-a5a9-1754b4cff21d.png)

---

### Modules functions
1. sub_cat: A function for detecting subcategories

2. e: Equivalent cost distribution function

3. s: Distribution function by area

4. p: Distribution function according to the number of parking spaces

5. r: Distribution function according to the number of inhabitants

6. d: Distribution function by default

7. percent: Distribution function in terms of percentages that the user enters as a number

8. operation: This function determines which distribution method to use based on the command given by the user

9. budget: This function tells the manager about the inventory status of the building at the beginning of the program






