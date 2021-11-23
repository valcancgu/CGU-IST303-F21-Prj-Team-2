# Team 2

## How to launch the application

1. Clone the repository
2. Creat the venv
<code>  
python3 -m venv .venv  
</code>
3. Activate the venv  
<code> source .venv/bin/activate </code>  
4. install the requirements  
<code> pip3 install -r requirements.txt </code>  
5. go to the correct folder (miye)  
6. run the app  
<code> python manage.py runserver </code>  

## How to migrate  

<code> python manage.py makemigrations </code>  
<code> python manage.py migrate </code>  

## Users

1. Receptionist
2. Guest
3. Manager
4. Esthetician

## Objects and Entities

- Employee account (receptionist, manager, esthetician)
- Guest account (guest)
- Service (1 task, 1 financial unit, est. time to complete)
- Appointments (list of services, 1 esthetician, 1 guest, time)
- Schedule (list of appointments for a specific day) – prints view

## Scope Shift  

![Alt text](img.png?raw=true "Title")


## User Stories

1. Receptionist
- Create an appointment for a guest
- Create a guest account
- Read financial details for an appointment (with printing)
- Update appointment details
- Update esthetician details
- Delete any appointment

2. Guest
- Create their guest account
- Create their own appointments
- Read full list of services
- Read their upcoming appointments
- Update their own appointments
- *Deactivate* their appointments

3. Manager
- Create new employee account
- Create a new service
- Read all appointments
- Update all records
- *Deactivate* an employee account (must reassign all appointments first)

4. Esthetician
- Read their appointment schedule (with print)

## Business Logic (constraints)

1. Creating an appointment
- Guest wants a specific service
- Software displays available start times for the day
- Looks at schedules for all esthetician's displays unclaimed time chunks
- Guest chooses an unclaimed time chunk
- Appoint is registered into the system, and added to esthetician's schedule

2. Change appointment details
- Guest wants to change services or start time
- Check the list of all estheticians
- List available time chunks

3. Cancel appointment
- Guest wants to cancel
- Adds a deactivate flag to appointment record
- Checks if the reservation is within the free-cancelation time window

4. Guest total bill
- Choose time window
- Aggregate total service cost for all appointments in that range

5. Esthetician total revenue
- Choose time window
- Aggregate total service cost for all appointments in that range

6. View all schedules
- Receptionist or manager chooses a time window
- List appointments for all schedules that intersect that time window

7. Create a new service
- Manager can create a service record

8. There can be only one reservation at a time for any service (except mineral baths)

## Language, Framework, and Libraries

- Python – mandated
- Django – built in db management, authentication module
- Docker – deploy application; network connectivity disabled by container

### Why Django
Django is a web framework. We can meet the customer requirement of *no-network connectivity* by deploying a Django app on a docker image that disables all network activity. The application will be accessible by accessing miye:8000 from any browser. The application will run on any machine with Python3 installed.  

This gives us a number of advantages
- Django allows us to deploy software cross platform (MacOS, Windows, Linux)
- User interface is highly familiar
- Updates can be provided remotely

### Django Apps (components)

- Database (ER diagram)
- Service Menu
- Account Creation (Guest and Employee)
- Scheduling Module
- Payment Module

## Roles

- Project Management: Valerie
- Data Model: Ayush
- Service Map: Biany & Alvaro
- Design: Jean & Biany
- Testing: Valerie
- Django Setup: Jacqueline
- Account Creation: Praveen
- Service Menu: Praveen
- Scheduling Module: Jacqueline
- Payment Module: Yikai

## Sprints

1. Setup Django, Start database, Start base.html, Services menu
2. Sprint 2
3. Sprint 3
4. Sprint 4
5. Sprint 5

## Expectations

- Lots of comments (50% comment, 50% code)

## Other Considerations

- The receptionist has information pertaining to the Esthetician's schedule. This is ideally synchronized with the payroll system
- Guest can check in from the app to their appointment
- Picking an esthetician
- Forgotten passwords

# Django Development

## Cloning the repository
- from *Terminal* or *PowerShell* run <code> git clone https://github.com/valcancgu/CGU-IST303-F21-Prj-Team-2.git </code>
- <code> cd CGU-IST303-F21-Prj-Team-2 </code>
- <code> python3 -m venv .venv </code>
- <code> source .venv/bin/activate </code>
- <code> pip install -r requirements.txt </code>

## Activating the Venv
you must be in the director with *.venv* – check by running <code> ls -a</code>
- <code> source .venv/bin/activate </code>
- <code> pip install -r requirements.txt </code>

## Running the App
Inside of the folder with *manage.py* run, with the *venv* active:
<code> python manage.py runserver </code>
Navigate to localhost:8000

## Sqlite3

### Making database migrations
