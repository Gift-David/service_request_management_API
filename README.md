# Service Request Management API

## Overview
The **Service Request Management API** is a custom built RESTful backend service for handling client service requests for service-based businesses. It supports authentication, request tracking, client/staff management, and feedback collection.

---

## Features
- ### User Authentication:
- User registration and login (for admins, staff, and clients).
- JWT authentication for secure API access.

- ### User Authorization
- #### Admin:
- Access to all features
- #### Staffs:
- View requests they are assigned to
- Send request notes to their assigned requests
- View clients feedbacks for their assigned requests
- #### Clients:
- View their service requests
- Send feedbacks for their requests

- ### Client Management:
- Create, update, and delete client profiles.
- Store client details ( name, contact info, address).

- ### Service Request Management:
- Create, update, and delete service requests.
- Assign requests to staff members.
- Track request status (e.g., Pending, In Progress, Completed, Cancelled).
- Add notes or comments to requests for communication.

- ### Staff Management:
- Register and manage staff profiles.
- Assign staff to specific service requests.

---

## Tech Stack
- **Backend:** Django REST Framework / Django
- **Database:** SQLite
- **Auth:** JWT Authentication

---

## Installation

1. **Clone the repo**
```bash
git clone https://github.com/yourusername/service-request-api.git
cd service-request-api
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

<!-- 3. **Setup environment variables**
Create a `.env` file:
```
SECRET_KEY=your_secret_key
DATABASE_URL=postgres://user:password@localhost:5432/servicerequests
``` -->

3. **Run migrations**
```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```


4. **Start server**
```bash
python manage.py runserver
```

---

## Usage

### Authentication
1. Register via `/api/auth/register/`
2. Login via `/api/token/`
3. Use the returned JWT token in headers:
```http
Authorization: Bearer <token>
```

---

## API Endpoints

| Resource        | Endpoint                              | Method | Role       |
|-----------------|---------------------------------------|--------|------------|
| Auth            | `/api/auth/register/`                 | POST   | Public     |
|                 | `/api/auth/login/`                    | POST   | Public     |
|-----------------|---------------------------------------|--------|------------|
| Clients         | `/api/clients/`                       | GET    | Admin      |
|                 | `/api/clients/{id}/requests/`         | GET    | Admin      |
|                 | `/api/clients/{id}/`                  | GET    | Admin      |
|                 | `/api/clients/create/`                | POST   | Admin      |
|                 | `/api/clients/edit/{id}/`             | POST   | Admin      |
|                 | `/api/clients/delete/<int:pk>/`       | POST   | Admin      |
|-----------------|---------------------------------------|--------|------------|
| Requests        | `/api/requests/`                      | GET    | Admin      |
|                 | `/api/requests/{id}/`                 | GET    | Admin, Assigned Staff |
|                 | `/api/requests/create/`               | POST   | Admin      |
|                 | `/api/requests/edit/{id}/`            | POST   | Admin      |
|                 | `/api/requests/delete/<int:pk>/`      | POST   | Admin      |
|                 | `/api/requests/delete/<int:pk>/`      | POST   | Admin      |
| Requests Notes  | `/api/requests/notes/`                | GET    | Admin, Assigned Staff |
|                 | `/api/requests/notes/{id}/`           | GET    | Admin, Assigned Staff |
|                 | `/api/requests/notes/delete/{id}/`    | POST   | Admin, Author |
|                 | `/api/requests/notes/create/`         | POST   | Admin, Assigned Staffs |
|Requests Feedback| `/api/requests/feedbacks/`            | GET    | Admin, Assigned Staff/Client |
|                 | `/api/requests/feedbacks/{id}/`       | GET    | Admin, Assigned Staff/Client |
|                 | `/api/requests/feedbacks/delete/{id}/`| POST   | Admin, Author |
|                 | `/api/requests/feedbacks/create/`     | POST   | Admin, Assigned Client |
|-----------------|---------------------------------------|--------|------------|
| Staff           | `/api/staffs/`                        | GET    | Admin      |
|                 | `/api/staffs/{id}/requests/`          | GET    | Admin      |
|                 | `/api/staffs/{id}/`                   | GET    | Admin      |
|                 | `/api/staffs/create/`                 | POST   | Admin      |
|                 | `/api/staffs/edit/{id}/`              | POST   | Admin      |
|                 | `/api/staffs/delete/<int:pk>/`        | POST   | Admin      |
|-----------------|---------------------------------------|--------|------------|

---

## Contributing
1. Fork the repository  
2. Create a new branch (`feature/your-feature`)  
3. Commit your changes  
4. Push the branch and open a Pull Request  

---

## License
MIT License 

## Author: David Gift
Backend Developer. View his portfolio here
