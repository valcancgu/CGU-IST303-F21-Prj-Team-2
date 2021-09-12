# Team 2

## Users

1. Receptionist
2. Guest
3. Manager
4. Esthetician

## Objects and Entities

- Employee account (receptionist, manager, esthetician)
- Guest account (guest)
- Appointments
- Schedule (list of appointments)

## User Stories

1. Receptionist
- Create an appointment for a guest
- Create a guest account
- Read financial details for an appointment (with printing)
- Update appointment details
- Update esthetician details
- Delete

2. Guest
- Create their guest account
- Create their own appointments
- Read their upcoming appointments
- Update their own appointments
- *Deactivate* their appointments

3. Manager – Dashboarding capabilities
- Create
- Read
- Update
- Delete

4. Esthetician
- Read their appointment schedule (with print)

## Language, Framework, and Libraries

- Python – mandated
- Django – built in db management, authentication module

### Django Apps

- Database
-

## Other Considerations

- The receptionist has information pertaining to the Esthetician's schedule. This is ideally synchronized with the payroll system
- Guest can check in from the app to their appointment
