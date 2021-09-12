# Team 2

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
- Schedule (list of appointments) – prints view

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

3. Manager – Dashboarding capabilities
- Create new employee account
- Read all appointments
- Update all records
- *Deactivate* an employee account (must reassign all appointments first)

4. Esthetician
- Read their appointment schedule (with print)

## Business Logic (constraints)

## Language, Framework, and Libraries

- Python – mandated
- Django – built in db management, authentication module

### Django Apps

- Database
-

## Other Considerations

- The receptionist has information pertaining to the Esthetician's schedule. This is ideally synchronized with the payroll system
- Guest can check in from the app to their appointment
- Picking an esthetician
