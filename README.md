# 🍔 BlockBites-LPU

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.x-092E20?style=flat&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15+-336791?style=flat&logo=postgresql&logoColor=white)](https://www.postgresql.org/)

> **LPU-BlockBites** is a block-based campus food ordering system developed with **Django** and **PostgreSQL**, incorporating real-time order tracking and demand analysis. The system is architected for scalability, structured data modeling, and future AI-driven demand prediction.

---

## 📖 Project Description

BlockBites-LPU is a smart campus food ordering platform designed specifically for **Lovely Professional University (LPU)**. The system organizes food stalls by campus blocks, enabling students and staff to browse menus, place orders, and track them in real time — all from a single unified interface.

Built with a scalable architecture in mind, the platform also captures order data for demand analytics and is primed for future integration with AI-powered demand forecasting to help stall owners manage inventory and reduce food waste.

---

## ✨ Features

- **Block-wise Stall Organization** — Browse food stalls categorized by campus blocks (e.g., Block 32, Block 38, etc.)
- **Real-Time Order Tracking** — Track order status from placement to fulfillment
- **Menu Management** — Stall owners can add, update, and remove menu items with pricing
- **User Authentication** — Separate roles for students, stall owners, and admins
- **Order History** — View past orders and receipts
- **Demand Analysis Dashboard** — Visualize popular items and peak ordering times
- **Admin Panel** — Django's built-in admin interface for full platform management
- **Responsive UI** — HTML-based templates optimized for both desktop and mobile use
- **Scalable Data Model** — PostgreSQL-backed relational schema designed for growth
- **AI-Ready Architecture** *(Planned)* — Structured to support future ML-based demand prediction models

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | Python 3.10+, Django 4.x |
| **Database** | PostgreSQL 15+ |
| **Frontend** | HTML5, CSS3, Django Templates |
| **ORM** | Django ORM |
| **Admin Panel** | Django Admin |
| **Version Control** | Git & GitHub |
| **Environment** | virtualenv / venv |

> *`[PLACEHOLDER]` — If the project uses additional libraries (e.g., Django REST Framework, Chart.js, Celery), list them here.*

---

## ⚙️ Installation Instructions

### Prerequisites

Make sure you have the following installed on your system:

- Python 3.10 or higher
- PostgreSQL 15 or higher
- Git
- pip (Python package manager)
- virtualenv (recommended)

### 1. Clone the Repository

```bash
git clone https://github.com/sandeepkumar9760/BlockBites-LPU.git
cd BlockBites-LPU
```

### 2. Create and Activate a Virtual Environment

```bash
# On Linux/macOS
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Database

Create a PostgreSQL database for the project:

```sql
CREATE DATABASE blockbites_lpu;
CREATE USER blockbites_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE blockbites_lpu TO blockbites_user;
```

### 5. Set Up Environment Variables

Create a `.env` file in the project root and configure the following:

```env
SECRET_KEY=your_django_secret_key
DEBUG=True
DATABASE_NAME=blockbites_lpu
DATABASE_USER=blockbites_user
DATABASE_PASSWORD=your_password
DATABASE_HOST=localhost
DATABASE_PORT=5432
```

> *`[PLACEHOLDER]` — Adjust variable names to match your Django `settings.py` configuration.*

### 6. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create a Superuser (Admin)

```bash
python manage.py createsuperuser
```

---

## 🚀 How to Run Locally

```bash
# Make sure your virtual environment is activated
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Start the development server
python manage.py runserver
```

The application will be available at: **http://127.0.0.1:8000/**

The admin panel is accessible at: **http://127.0.0.1:8000/admin/**

---

## 💡 Usage Examples

### For Students
1. Register or log in to your account.
2. Browse available food stalls filtered by your campus block.
3. Select items from a stall's menu and add them to your cart.
4. Place your order and monitor its status in real time.
5. View your order history from the dashboard.

### For Stall Owners
1. Log in with stall owner credentials.
2. Manage your menu — add new items, update prices, or mark items as unavailable.
3. View incoming orders and update their status.
4. Access the demand analytics dashboard to review sales trends.

### For Admins
1. Access the Django Admin Panel at `/admin/`.
2. Manage users, stalls, blocks, and orders across the entire platform.

---

## 🗂️ Project Structure

```
BlockBites-LPU/
│
├── Block_stalls/           # Core Django app for stall & block management
│   ├── models.py           # Database models (Block, Stall, MenuItem, Order, etc.)
│   ├── views.py            # View logic for rendering pages
│   ├── urls.py             # URL routing
│   ├── admin.py            # Admin panel configuration
│   └── templates/          # HTML templates
│
├── manage.py               # Django management script
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (not committed)
├── .gitattributes          # Git attributes
└── README.md               # Project documentation
```

> *`[PLACEHOLDER]` — Update this tree to accurately reflect your actual folder structure.*

---

## 🔌 API Endpoints

> *`[PLACEHOLDER]` — If the project exposes REST API endpoints (e.g., via Django REST Framework), document them here. Example format:*

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| `GET` | `/api/blocks/` | List all campus blocks | No |
| `GET` | `/api/blocks/<id>/stalls/` | List stalls in a block | No |
| `GET` | `/api/stalls/<id>/menu/` | Get menu items for a stall | No |
| `POST` | `/api/orders/` | Place a new order | Yes |
| `GET` | `/api/orders/<id>/` | Get order details & status | Yes |
| `PATCH` | `/api/orders/<id>/status/` | Update order status | Yes (Stall Owner) |

---

## 🌐 Deployment Instructions

### Deploy on a Linux Server (e.g., Ubuntu with Gunicorn + Nginx)

```bash
# Install Gunicorn
pip install gunicorn

# Run with Gunicorn
gunicorn BlockBites_LPU.wsgi:application --bind 0.0.0.0:8000
```

Configure **Nginx** as a reverse proxy, then use **Let's Encrypt** for HTTPS.

## 🤝 Contributing

Contributions are welcome! To contribute to BlockBites-LPU:

1. **Fork** this repository.
2. **Create a new branch** for your feature or bug fix:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Commit your changes** with a clear message:
   ```bash
   git commit -m "feat: add your feature description"
   ```
4. **Push** to your forked branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. **Open a Pull Request** against the `main` branch of this repository.

### Guidelines

- Follow [PEP 8](https://pep8.org/) for Python code style.
- Write meaningful commit messages.
- Ensure all migrations are included for model changes.
- Test your changes locally before submitting a PR.
- Document any new features or API endpoints.



## 📬 Contact / Author

**Sandeep Kumar**
- 🐙 GitHub: [@sandeepkumar9760](https://github.com/sandeepkumar9760)
- 🎓 Institution: Lovely Professional University (LPU)
- 📧 Email: *`[PLACEHOLDER — sandeepkumar270724@gmail.com]`*
- 💼 LinkedIn: *`[PLACEHOLDER — https://www.linkedin.com/in/sandeep-kumar-ds/]`*


<p align="center">Made with ❤️ for the LPU Campus Community</p>
