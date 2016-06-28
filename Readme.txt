
Details:
The python script 'Generate_Weather.py' pulls current weather information using the API from openweathermap.com.
API keeps the data updated every < 	2 hours.
Script generates weather information for 10 major cities in Australia.
This API is created in a free account, therefore only 60 calls are allowed in a minute.

Required Python Libraries - json, urllib2, datetime, pytz.

How to run:
1. copy Generate_Weather.py to any python installed sever.
2. navigate to the script location.
3. run the script: 'python Generate_Weather.py'
4. you will see the following output on the screen.

Output(pipe separated):
Sydney|2016-06-28 23:00:53|151.21|-33.87|Clear|281.96|1026|53
Melbourne|2016-06-28 23:00:54|144.96|-37.81|Rain|283.74|1026|87
Adelaide|2016-06-28 22:30:54|138.6|-34.93|Clear|281.94|1026|81
Canberra|2016-06-28 23:00:54|149.13|-35.28|Clouds|285.14|1017|88
Wollongong|2016-06-28 23:00:54|150.88|-34.43|Clear|282.85|1026|57
Perth|2016-06-28 21:00:54|115.83|-31.93|Clouds|288.02|1013|93
Brisbane|2016-06-28 23:00:55|153.03|-27.47|Clear|284.57|1024|54
Albury|2016-06-28 23:00:55|146.92|-36.08|Rain|282.59|1018|97
Darwin|2016-06-28 22:30:55|130.84|-12.46|Clear|299.15|1014|74
Eucla|2016-06-28 21:45:55|128.87|-31.72|Clear|284.012|1025.98|72

Output field names:
City name | Local time | longtitude | lattitude | Weather: Condition | Temperature | Pressure | Humidity


