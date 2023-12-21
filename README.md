# cloud_db_mgmt_pooling_migrations

Gain practical experience in managing a cloud-based MySQL database with a focus on implementing connection pooling and performing database migrations. You will work with both Azure and Google Cloud Platform (GCP) for this assignment.

## Connection Pooling Set Up 

**GCP:**  
- Log in with stonybrook email and in SQL, create a new mySQL instance 
- Create a name and password
- Under Cloud DQL edition, select Enterprise
- For Preset, select Sandbox
- Click "Show Configuration Options" which will bring a dropdown menu 
- Change Machine Configuration settings to the following: Shared core, 1 vCPU, 0.614 GB
- Under Connections, add network named "Allow All" set to <code>0.0.0.0/0</code>
- Click on Create Instance
- Once the instance is created, navigate to menu bar on the left and select "Databases"
- Create a new database and give the database a name
- Character set: utf8
- Coallation: Default

**Azure:** 
- Once logged into Azure, go to Azure Database for MySQL servers and click on create a new Flexible server
- Choose a resource group or create one if necessary 
- Compute + storage: standard b1s
- Availabilty: no preference 
- Create a username and password. Take note of this 
- Networking configurations: Select <code>+ Add 0.0.0.0 - 255.255.255.255</code>
- Then click Review + create 
- When the instance is created, navigate to left menu bar and click "Server Parameters"
- Make the following changes and hit save
    - Max_connections: 20
    - Connect_timeout: 3
    - require_secure_transport: OFF 
- After saving changes, navigate to "Databases" from the left menu bar 
- Click on add a new database
- Give the database a name 
- Character set: utf8
- Collation: utf8-general-ci

## Database Schema and Data Creation 

### GCP:

**Database Schema:**

- Go the the Google Shell environment and open the terminal
- Install all necessary packages using: <code>pip install sqlalchemy alembic mysql-connector-python pymysql</code>
- Note: I also had to <code>pip install Faker</code> and <code>pip install python-dotenv</code>
- Create a gcpDatabase.py file that will be used for database creation: [gcpDatabase.py](https://github.com/zf81/cloud_db_mgmt_pooling_migrations/blob/main/GCP/gcpDatabase.py)
- Create a .env file which will contain the login credentials for the cloud mySQL instance
- Create a .gitignore file to hide the .env file after files are pushed to Github
- Import necessary packages into gcpDatabase.py file
- Load in credentials from .env file
- Create a base
- Create tables with SQLAlchemy. I created a patients table and laboratory orders table 
- Create an engine to connect to the cloud database
- The GCP URL to connect will have this format: <code>mysql+pymysql://root:[password]@[public-ip-of-instance]/[db-name]</code>
  
- To check if the tables have been successfully created, connect to MySQL server using <code>mysql -u root -h[ip-address] -p [password]</code>
- To select the database you created, type: <code>use [database-name];</code>
- <code>show tables;</code> displays a list of tables within the database
- Once you are done checking tables, exit the MySQL monitor using <code>exit</code> 

## Populate Tables With Sample Fake Data:
- Create another .py file (gcpPopulate.py) which will be used for populating the tables: [gcpPopulate.py](https://github.com/zf81/cloud_db_mgmt_pooling_migrations/blob/main/GCP/gcpPopulate.py)
- Import necessary packages into gcpPopulate.py file
- Load in credentials from .env file and create a database engine
- Create a session to interact with the database
- Create a faker instance. This will be used to populate the tables with fake information
- Create functions to generate fake data for the tables in the database
- Insert fake data
- To make sure that the tables are populated with fake data, execute MySQL once again 

### Azure: 

**Create Database Schema:**
- To create database schema for Azure, follow the above steps for GCP
- Some key differences: the AZURE URL has this format: <code>mysql+pymysql://[azure-server-username]:[password]@[server-name]/[db-name]</code>
- To make sure the tables have been successfully created, connect to MySQL server using <code>mysql -u [username] -h[server-name] -p [password]</code>
- Refer to steps above 

**Populate Tables With Sample Fake Data:**
- Follow the same steps as above for GCP but be sure that you are using the AZURE URL format

## Using MySQL Workbench to Generate ERD

- To create a connection, open the MySQL Workbench and create a new connection
- Type in a connection name
- Hostname:
- GCP: [public-ip-address]
- AZURE: [server-name]
- Username:
- GCP: leave as root
- AZURE: [server-username]
- Password: click store in vault and enter the passwords you created in the above steps 
- Click on "Test Connection" to make sure connection is successful
- If the connection is successful, click "OK"
  
**Generate ERD:**
- Enter the connection you created
- In top menu bar, click on "Database"
- THen click "Reverse Engineer"
- For stored connection, select name of current connection
- Click "Next"
- Click on Schema
- Click "Next"
- Select Execute and finish
- You should now see the ERD diagrams
- Scroll to the tables and double click on the dotted line connecting the tables
- At the bottom you will see Relationships tab. Click on "Foreign Key"
- Under Cardinality, select "One-to-One"
- Save pictures of the ERD (Azure ERD and GCP ERD)

## SQLAlchemy and Flask Integration

### GCP Flask:

- Create a new folder for GCP Flask app. Within this folder, create an app.py file, .env file, and a .gitignore file
- Load the same GCP URL credentials into the .env file and place the .env file into .gitignore
- In the app.py file, load in the env credentials and create an engine which will connect to the GCP database
- In this gcpapp.py, create an app with Flask which will contain the tables from the database: [gcpApp.py](https://github.com/zf81/cloud_db_mgmt_pooling_migrations/blob/main/GCPFlask/gcpapp.py)
- Within the GCP Flask folder, create a <code>templates</code> folder to stylize the Flask app
- Homepage styling for the Flask app: [gcpbase.html](https://github.com/zf81/cloud_db_mgmt_pooling_migrations/blob/main/GCPFlask/templates/gcpbase.html) 
- Patients page styling: [gcppatients.html]([html](https://github.com/zf81/cloud_db_mgmt_pooling_migrations/blob/main/GCPFlask/templates/gcppatients.html)) 
- Laboratory Orders page styling: [gcplabs.html](https://github.com/zf81/cloud_db_mgmt_pooling_migrations/blob/main/GCPFlask/templates/gcplabs.html) 
- Here are the resulting pages for the GCP Flask app:
  
  Home page
  ![gcphomepage](https://github.com/zf81/cloud_db_mgmt_pooling_migrations/blob/main/GCP_Flask_Screenshots/gcphomepage.png)
  
  Patients Page
  ![gcppatients](https://github.com/zf81/cloud_db_mgmt_pooling_migrations/blob/main/GCP_Flask_Screenshots/gcppatients.png)

  Laboratory Order Page
  ![gcplabs](https://github.com/zf81/cloud_db_mgmt_pooling_migrations/blob/main/GCP_Flask_Screenshots/gcplabs.png)
  

### Azure: 

+ Create a new folder for the AZURE Flask app and in it, create an app.py file, .env file, and a .gitignore file
    + Load the same GCP URL credentials from before into the .env file and put the .env file into .gitignore
+ In the app.py file, load in the env credentials and create an engine to connect to the AZURE database
+ Create an app with Flask with an appropriate amount of routes matching the number of tables in the database
+ See [AzureApp.py](AzureApp.py) for an example 
+ In the folder, create a "templates" folder to stylize the Flask app
    + [azurebase.html](zurebase.html) stylizes the homepage of the flask app
    + [azurepatients.html](urepatients.html) stylizes the patients table page of the flask app
    + [azurepreferences.html](preferences.html) stylizes the patients' preferences page of the flask app
+ Following the templates created, the finalized Flask app looks like this:
  
  Home page
  ![AZURE Homepage](hFlask/azurehome.png)
  
  Patients Page
  ![AZURE Patientpage](zurepatients.png)

  Preferences Page
  ![AZURE Preferencespage](azurepreferences.png)

## Database Migrations with Alembic

### GCP: 

+ In the terminal run <code>alembic init migrations</code> and this will generate a folder labled "migrations" and a file named "alembic.ini"
+ In "alemic.ini", scroll down to find <code>sqlalchemy.url =</code> and edit the URL to <code>mysql+pymysql://root:[password]@[public-ip-of-instance]/[db-name]</code> for GCP
+ Add "alembic.ini" to .gitignore to protect private information 
+ In the "migrations" folder, there is a file named "env.py"
+ Around line 19 in "env.py", edit to <code>from [db.py-file-name] import Base</code>
+ Edit in <code>target_metadata = Base.metadata</code> and comment out <code>target_metadata = None</code>
+ Go back to terminal and run: <code>alembic revision --autogenerate -m "create tables"</code> to create a migration
+ Run <code>alembic upgrade head</code> to run the migration
+ Run <code>alembic upgrade head --sql > migration.sql</code> to create and save the migration into a "migration.sql" file
+ Go to the database file (in this case, it's gcpDB.py) and make any changes to any of the tables
    + Changes can include creating or deleting tables and columns
+ After making a change, go back into the termimal and rerun code starting from: <code>alembic revision --autogenerate -m "create tables"</code>
+ Run <code>alembic upgrade head</code> to run the migration
+ Run <code>alembic upgrade head --sql > migration.sql</code> to save the changes and migrations into "migration.sql" file
+ If the changes are successful, it will be recorded in "migration.sql"
+ Another way to see if changes are successful, renter the MySQL monitor with <code>mysql -u root -h[ip-address] -p [password]</code>
+ To select database to use: <code>use [database-name];</code>
+ To see a list of tables in the database: <code>show tables;</code>
+ To see a list of column names in a specific table: <code>describe [table-name];</code>
+ To exit from MySQL monitor: <code>exit</code>

### Azure: 

+ Steps are the same as for GCP except in "alemic.ini", the URL should be edited to <code>mysql+pymysql://[server-username]:[password]@[server-name]/[db-name]</code> for AZURE
+ Also for entering the MySQL monitor, use: <code>mysql -u [username] -h[server-name] -p [password]</code>

## Documentations and Errors

**Errors**
