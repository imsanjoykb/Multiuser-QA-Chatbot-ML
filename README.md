# Simple-multiuser-Q&A chatbot-web-server in flask

In this project I present a simple multiuser chatbot web server using flash and python. Multiples users can ask questions to the chatbot and all people see all questions and answers.

The added value of this chatbot is simplicity. Usually machine learning techniques are applied for chatbot causing to have huge datasets.

In this chatbot I provide an alternative method using python dictionaries and simple CSV files as the main mechanism of the core of the solution. 

For finding the answers it allows partial matching to find out an answer and in this way keep simple the CSV file. 



**Entries in dataset: (-;- csv file separator)**

good morning-;-good morning

good afternoon-;-good afternoon

good evenning-;-good evenning

good night-;-good night

goodbye-;-goodbye


**Example1:**

Question =>  "good"

Answer ==> Any of the above matches this pattern so any response can be selected.


**Example2:**

Question =>  "good "

Answer ==> Except for the last answer all matches this pattern so any of the first 4 answers can be selected.


**Example3:**

Question =>  "good afternoon"

Answer ==> good afternoon





  
