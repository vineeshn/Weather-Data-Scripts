#Trending topics in Meetups
Load the given Meetup.com JSON feed and Output a top N (where N is also an input parameter) of trending topics.

To Run:
bin\spark-submit <source code> <JSON data feed> <from datetime> <to datetime> <Top N>

Sample Run:
bin\spark-submit pythoncase\meetup_case_final.py C:\spark\spark-2.2.0-bin-hadoop2.7\dataset\meetup.json 2017-03-1915:10:15 2017-03-1917:46:10 10

#Trending Topics and No of interest received:
+------------------+---------------+
|Trending_Topics   |No_of_Interests|
+------------------+---------------+
|Social            |66             |
|New In Town       |60             |
|Social Networking |60             |
|Outdoors          |40             |
|Fitness           |38             |
|Fun Times         |36             |
|Language & Culture|27             |
|Culture Exchange  |27             |
|Dining Out        |27             |
|Self-Improvement  |27             |
+------------------+---------------+

#Trending Topics and No of interest received by Country and City:
+--------------------+---------------+-------+--------+
|Trending_Topics     |No_of_Interests|country|city    |
+--------------------+---------------+-------+--------+
|New In Town         |7              |gb     |London  |
|Social              |7              |gb     |London  |
|Social Networking   |6              |gb     |London  |
|Fitness             |5              |gb     |London  |
|Self-Improvement    |5              |us     |New York|
|Trumpet Players     |5              |gb     |London  |
|Saxophones          |5              |gb     |London  |
|Flute               |5              |gb     |London  |
|Social Networking   |5              |jp     |Tokyo   |
|Rhythm and Blues R&B|5              |gb     |London  |
+--------------------+---------------+-------+--------+

