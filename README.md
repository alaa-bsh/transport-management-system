![Project_Image](swift.png)


## Table of contents
- [Overview](#overview)
- [Project Structure](#project-structure)
- [Architecture and Design Choices](#architecture-and-design-choices)
- [Usage](#usage)
- [Tech stack](#tech-stack)
- [Setup & Run](#setup--run)

## Overview
This project is an information system for a transport and delivery company.  
It handles clients, expeditions, tours, billing, payments, and incidents.



## Project Structure
```mermaid
graph LR
    A[transport-management-system] --> B[manage.py]
    A --> C[requirements.txt]
    A --> D[db.sqlite3]
    A --> E[package.json]
    A --> F[package-lock.json]
    A --> G[README.md]
    A --> H[.gitignore]
    A --> I[backend]
    A --> J[config]
    A --> K[frontend]
    A --> L[node_modules]
    I --> M1[clients]
    I --> M2[historique]
    I --> M3[incidents]
    I --> M4[logistics]
    I --> M5[manageExpedition]
    I --> M6[manageColis]
    I --> M7[manageDestination]
    I --> M8[reclamations]
    I --> M9[typeservice]
    I --> M10[trajet]
    I --> M11[tarification]
    J --> J1[__init__.py]
    J --> J2[asgi.py]
    J --> J3[settings.py]
    J --> J4[urls.py]
    J --> J5[wsgi.py]
    K --> K1[static]
    K --> K2[templates]
    L --> L1[bootstrap-icons]
    L --> L2[.package-lock.json]
    K2 -->K3[components]
    K2 -->K4[pages]
    K3 -->K5[.html components]
    K4 -->K6[dashboard.html]
    K4 -->K7[favoris.html]
    K4 -->K8[main.html]
    N1[models.py]
    N2[views.py]
    N3[urls.py]
    N4[admin.py]
    M1 --> N1
    M1 --> N2
    M1 --> N3
    M1 --> N4
    M2 --> N1
    M2 --> N2
    M2 --> N3
    M2 --> N4
    M3 --> N1
    M3 --> N2
    M3 --> N3
    M3 --> N4
    M4 --> N1
    M4 --> N2
    M4 --> N3
    M4 --> N4
    M5 --> N1
    M5 --> N2
    M5 --> N3
    M5 --> N4
    M6 --> N1
    M6 --> N2
    M6 --> N3
    M6 --> N4
    M7 --> N1
    M7 --> N2
    M7 --> N3
    M7 --> N4
    M8 --> N1
    M8 --> N2
    M8 --> N3
    M8 --> N4
    M9 --> N1
    M9 --> N2
    M9 --> N3
    M9 --> N4
    M10 --> N1
    M10 --> N2
    M10 --> N3
    M10 --> N4
    M11 --> N1
    M11 --> N2
    M11 --> N3
    M11 --> N4

```


## Architecture and Design Choices
- MVC pattern (Model–View–Controller)
- Separation between business logic and presentation
- Centralized database access via Django ORM
### High level architecture diagram
```mermaid
graph LR
    subgraph Frontend [Client Layer]
        direction TB
        A[Web Browser / User Interface]
        B[HTML, CSS, JS, Bootstrap]
        C[AJAX requests / JSON responses]
        A --> B --> C
    end
    subgraph Backend [Server Layer: Django]
        direction TB
        D[Business Logic / Controllers]
        E[JSON API Endpoints]
        D --> E
    end
    subgraph Database [Database Layer]
        F[(SQLite3 Database)]
    end
    C -->|AJAX / JSON| E
    E --> D
    D -->|ORM Queries| F
```
### User Flow Diagram
```mermaid
flowchart LR
    Home["Home Page"]
    Home -->|Navigate| News["Today's News"]
    Home -->|Navigate| Features["Favorite Features"]
    Home -->|Navigate| Sections["Sections / Categories"]
    Home -->|Access| TablesData["Tables & Data"]
    Home -->|Access| Expeditions["Gestion des Expéditions"]
    Home -->|Access| Tournees["Gestion des Tournées"]
    Home -->|Access| Facturation["Facturation & Paiement"]
    Home -->|Access| Incidents["Gestion des Incidents"]
    Home -->|Access| Reclamations["Gestion des Réclamations"]
    Home -->|Access| Analyse["Analyse Commerciale & Opérationnelle"]
    TablesData --> TableOps["View / Add / Modify / Delete"]
    Expeditions --> ExpeditionOps["Create / View / Modify / Add to Tournee"]
    ExpeditionOps -->|Generates| ExpeditionID["ID & Status"]
    ExpeditionOps -->|Calculates| ExpeditionAmount["Amount"]
    Tournees --> TourneeOps["View / Modify / Delete / Search"]
    Facturation --> FactureOps["Add / Modify / View / Delete Factures"]
    Facturation --> PaiementOps["Add / Modify / View / Delete Payments"]
    Incidents --> IncidentOps["Add / Modify / View / Delete"]
    Reclamations --> ReclamationOps["Add / Modify / View / Delete"]
    Analyse --> Commercial["Top Clients, Popular Destinations, Revenue Trends"]
    Analyse --> Operational["Delivery Success Rate, Top Drivers, Active Periods, Incident Zones"]
```



## Usage

### 1. Access the Application

- Start the development server:
```bash
python manage.py runserver
```

- Open a browser and go to: `http://127.0.0.1:8000`

### 2. Navigate Modules

* **Clients:** view, add, edit, or delete client records.
* **Expeditions:** manage shipments, track statuses.
* **Tournee:** assign drivers and vehicles.
* **Billing & Payments:** manage invoices and payments.
* **Incidents & Reclamations:** log and track incidents or complaints.

### 3. Common Actions

* **Search:** look up specific records.
* **Filter:** refine data based on the NEW & OLD criteria. 
* **Pagination:** navigate through pages of records.

### 4. Data Management

* **Add New Record:** click “Add” buttons, fill in forms, submit.
* **Edit Record:** modify existing records via edit forms.
* **Delete Record:** remove records (with confirmation).
* **Export / Print:** download or print table data (if implemented).




## Tech stack
- **Backend:** Django (Python 3)  
- **Frontend:** HTML, CSS, JavaScript, Bootstrap  
- **Database:** SQLite3  
- **Dynamic interactions:** AJAX  
- **Conception :** Looping, Visual paradigm


## Setup & Run
1. Clone the repository:  
```bash
git clone <repo-url>
```
2. Install dependencies 
```bash
pip install -r requirements.txt
```
3. Apply migrations
```bash 
python manage.py migrate
```
4. Run the development server
```bash
python manage.py runserver
```
5. Access the project at : http://127.0.0.1:8000
## Team Members

- **Aissat Lyna**  
  Frontend & UI/UX design, interface implementation, backend linking

- **Boussaha Sara Alaa**  
  Data models, business logic, backend development, dashboard logic

- **Hachi Kawthar Khadidja**  
  Backend modules (Expeditions, Invoicing, Tours, Destinations, Incidents),
  data modeling (MCD, MLD), use cases, and documentation

