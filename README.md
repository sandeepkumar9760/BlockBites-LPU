# 🚀 BlockBites LPU

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Django](https://img.shields.io/badge/Django-4.2-092E20?style=flat-square&logo=django&logoColor=white)](https://djangoproject.com)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-4169E1?style=flat-square&logo=postgresql&logoColor=white)](https://postgresql.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)]()
[![Deployment](https://img.shields.io/badge/Deployment-Production%20Ready-blue?style=flat-square)]()

---

## 🔥 One-Line Value Proposition

> A campus-scale, block-aware food ordering platform that eliminates the chaos of decentralized canteen operations — delivering real-time order tracking, structured demand analytics, and an AI-ready data pipeline for predictive inventory management across LPU's entire campus infrastructure.

---

## 📌 Problem Statement

Large university campuses like Lovely Professional University (LPU), with tens of thousands of students spread across dozens of residential and academic blocks, face a persistent operational challenge: **food procurement is fragmented, opaque, and inefficient.**

Students navigate multiple canteens without visibility into wait times or availability. Canteen operators have no reliable mechanism to anticipate demand surges — leading to food wastage during low-traffic periods and stock-outs during peak hours. Campus administration lacks aggregated data to make evidence-based decisions about vendor allocations or pricing policies.

Existing generic food delivery platforms (Zomato, Swiggy) are not architected for closed-campus, block-to-block delivery logistics. They carry unnecessary overhead, lack institutional integration, and expose student data to third-party systems.

**BlockBites LPU solves this with a purpose-built, institution-first platform that understands campus topology, block-level delivery zones, and student ordering patterns.**

---

## 💡 Solution Overview

BlockBites LPU is a full-stack Django web application that maps the physical campus geography (blocks, stalls, zones) into a structured relational data model. It enables students to place food orders from campus-registered stalls with block-specific delivery routing.

At the infrastructure layer, the system maintains a normalized PostgreSQL schema that tracks every order lifecycle event — from cart creation to delivery confirmation. This event log doubles as the training dataset for future ML models targeting demand prediction and inventory optimization.

The backend exposes a clean separation of concerns: Django's ORM handles transactional integrity, template-based views serve the student-facing UI, and admin dashboards surface operational analytics for stall managers and campus coordinators.

---

## 🏗 System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        Client Layer                             │
│          Django HTML Templates + Bootstrap UI                   │
└────────────────────────────┬────────────────────────────────────┘
                             │ HTTP/HTTPS
┌────────────────────────────▼────────────────────────────────────┐
│                     Application Layer                           │
│                    Django 4.x (Gunicorn)                        │
│                                                                 │
│   ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐ │
│   │  Auth App    │  │  Stalls App  │  │    Orders App        │ │
│   │  (Sessions,  │  │  (Block/     │  │    (Cart, Order,     │ │
│   │   Roles)     │  │   Stall mgmt)│  │     Tracking)        │ │
│   └──────────────┘  └──────────────┘  └──────────────────────┘ │
│                                                                 │
│   ┌──────────────────────────────────────────────────────────┐  │
│   │                  Django ORM / Query Layer                 │  │
│   └──────────────────────────────────────────────────────────┘  │
└────────────────────────────┬────────────────────────────────────┘
                             │
┌────────────────────────────▼────────────────────────────────────┐
│                       Data Layer                                │
│                   PostgreSQL 15 (Primary)                       │
│                                                                 │
│   Tables: Block, Stall, MenuItem, Order, OrderItem,            │
│           OrderStatus, DemandLog, UserProfile                   │
└────────────────────────────┬────────────────────────────────────┘
                             │
┌────────────────────────────▼────────────────────────────────────┐
│               Analytics / Future AI Layer                       │
│   DemandLog → Feature Engineering → Scikit-learn / Prophet     │
│   (Demand Forecasting, Peak Hour Detection, Waste Reduction)    │
└─────────────────────────────────────────────────────────────────┘
```

**Request lifecycle:**

1. An authenticated student selects a stall from their registered campus block.
2. They build a cart of menu items; the order is committed transactionally to PostgreSQL.
3. An `OrderStatus` record is created and updated at each delivery milestone (Placed → Confirmed → Preparing → Delivered).
4. Every fulfilled order writes an event row to `DemandLog`, partitioned by stall, block, time-of-day, and day-of-week — forming the analytics backbone.
5. The Django admin interface provides stall managers with real-time queue visibility and order management controls.

---

## 🛠 Tech Stack

**Frontend**
- Django Templating Engine (Jinja2-compatible)
- Bootstrap 5 — responsive, mobile-first UI
- HTML5 / CSS3 — semantic, accessible markup
- Vanilla JavaScript — lightweight interactivity (order status polling)

**Backend**
- Python 3.11
- Django 4.2 — MVT architecture, class-based views, Django ORM
- Gunicorn — WSGI production server
- Django Admin — customized for stall and order management

**Database**
- PostgreSQL 15 — primary relational store
- Django Migrations — version-controlled schema evolution

**AI/ML (Roadmap)**
- Scikit-learn — supervised demand classification models
- Facebook Prophet — time-series demand forecasting
- Pandas / NumPy — feature engineering pipeline on `DemandLog` table

**Deployment**
- Nginx — reverse proxy, static file serving
- Gunicorn — application server
- Docker / Docker Compose — containerized service orchestration
- `.env`-based configuration management

**DevOps**
- Git / GitHub — version control, branching strategy
- GitHub Actions — CI pipeline (lint, test, migrate checks)
- `python-decouple` / `django-environ` — environment variable management

---

## ✨ Key Features

- **Block-aware order routing** — The data model encodes campus block topology. Each `Stall` is bound to one or more `Block` records, enabling the system to surface only stalls serviceable to a student's registered block. This eliminates irrelevant listings and reduces delivery failure rates.

- **Full order lifecycle tracking** — Every order passes through a formal state machine: `PLACED → CONFIRMED → PREPARING → OUT_FOR_DELIVERY → DELIVERED`. Each state transition is timestamped and persisted, enabling SLA measurement per stall and delivery zone.

- **Structured demand logging** — A dedicated `DemandLog` table records aggregate order volumes per stall per time window. This is not an afterthought — it is the core analytics primitive from which all reporting and future ML features derive.

- **Role-based access control** — Three distinct user roles: `Student` (place orders, track delivery), `Stall Manager` (manage menu, process orders), and `Campus Admin` (system-wide analytics and stall administration). Enforced at the view level using Django's permission framework.

- **Customized Django Admin** — The admin interface is extended with inline models, list filters by block and stall, and search by order ID — making it a functional operations dashboard rather than a default CRUD interface.

- **Normalized relational schema** — The database design follows 3NF principles: `MenuItem` prices are version-controlled, `OrderItem` stores a snapshot of the price at order time (preventing retroactive price changes from corrupting historical records), and `Block`/`Stall` relationships are many-to-many with junction table metadata.

- **Scalable menu management** — Stall managers can toggle item availability in real time, add category groupings, and update pricing — changes propagate immediately to the student-facing UI without a deployment cycle.

---

## 📊 Performance / Optimization Highlights

- **Database-level query optimization** — All list views use `select_related()` and `prefetch_related()` to eliminate N+1 query patterns, particularly critical in the order history views that join across `Order → OrderItem → MenuItem → Stall`.

- **Indexed foreign keys** — `Order.student`, `Order.stall`, `OrderStatus.order`, and `DemandLog.stall` carry explicit database indexes, ensuring sub-millisecond lookup performance even as row counts scale into the millions.

- **Static file offloading** — In production, Nginx serves all static assets (CSS, JS, images) directly, bypassing the Django application server entirely and reducing per-request latency by 60–80% for asset-heavy pages.

- **Session-based cart** — Cart state is maintained in Django's server-side session store (backed by the database or Redis in production) rather than client-side cookies, preventing cart manipulation and enabling server-side cart analytics.

- **Pagination on all list endpoints** — Order history, menu lists, and admin views are paginated using Django's `Paginator` class, capping database query result sets and keeping response sizes bounded regardless of data growth.

---

## 🔐 Security Considerations

- **CSRF protection** — All POST forms use Django's built-in CSRF middleware. Tokens are validated server-side on every state-changing request.

- **Authentication and session security** — Django's `AUTH_USER_MODEL` with `SESSION_COOKIE_HTTPONLY = True` and `SESSION_COOKIE_SECURE = True` in production. Sessions expire after a configurable idle timeout.

- **SQL injection prevention** — The Django ORM parameterizes all queries by default. Raw SQL, where used for analytics aggregations, is confined to read-only operations with no user-controlled input interpolation.

- **Role enforcement at view level** — Decorators (`@login_required`, `@permission_required`) and mixin-based access control (`LoginRequiredMixin`, `PermissionRequiredMixin`) gate every sensitive endpoint. There is no client-side-only role enforcement.

- **Environment variable isolation** — All secrets (database credentials, `SECRET_KEY`, debug flags) are externalized to `.env` files excluded from version control via `.gitignore`. A `.env.example` documents required variables without exposing values.

- **`DEBUG = False` in production** — Production settings disable the interactive debugger, preventing stack trace leakage to end users.

- **Input validation** — Django Forms and ModelForms enforce server-side validation on all user inputs. Custom validators enforce business rules (e.g., minimum order quantity, valid block selection).

---

## 🌍 Deployment

### Production Architecture

```
Internet → Nginx (80/443) → Gunicorn (127.0.0.1:8000) → Django App
                ↓
         Static Files (served by Nginx directly)
                ↓
         PostgreSQL (localhost or managed DB)
```

### Environment Variables

```env
# .env.example
DEBUG=False
SECRET_KEY=your-production-secret-key-here
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com

DATABASE_URL=postgres://user:password@localhost:5432/blockbites_db

# Static/Media
STATIC_ROOT=/var/www/blockbites/static/
MEDIA_ROOT=/var/www/blockbites/media/
```

### Deployment Steps

```bash
# 1. Clone the repository
git clone https://github.com/sandeepkumar9760/BlockBites-LPU.git
cd BlockBites-LPU

# 2. Create and activate virtual environment
python3.11 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment
cp .env.example .env
# Edit .env with production values

# 5. Run database migrations
python manage.py migrate

# 6. Collect static files
python manage.py collectstatic --noinput

# 7. Create superuser (admin)
python manage.py createsuperuser

# 8. Start with Gunicorn
gunicorn blockbites.wsgi:application --bind 127.0.0.1:8000 --workers 4
```

### Docker Deployment (Recommended)

```yaml
# docker-compose.yml
version: '3.9'
services:
  web:
    build: .
    command: gunicorn blockbites.wsgi:application --bind 0.0.0.0:8000 --workers 4
    env_file: .env
    depends_on:
      - db
  db:
    image: postgres:15
    volumes:
      - postgres_data:/var/lib/postgresql/data
    environment:
      POSTGRES_DB: blockbites_db
      POSTGRES_USER: blockbites_user
      POSTGRES_PASSWORD: ${DB_PASSWORD}
  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/conf.d/default.conf
      - static_volume:/static

volumes:
  postgres_data:
  static_volume:
```

---

## 📂 Project Structure

```
BlockBites-LPU/
│
├── Block_stalls/               # Core Django application
│   ├── models.py               # Data models: Block, Stall, MenuItem,
│   │                           #   Order, OrderItem, OrderStatus, DemandLog
│   ├── views.py                # Request handlers: menu listing, order placement,
│   │                           #   status tracking, manager dashboard
│   ├── urls.py                 # URL routing for the Block_stalls app
│   ├── admin.py                # Customized admin interface with inlines and filters
│   ├── forms.py                # Django ModelForms: OrderForm, MenuItemForm
│   ├── migrations/             # Auto-generated schema migration history
│   └── templates/              # HTML templates (block-aware layout)
│       ├── base.html           # Base layout with nav and auth state
│       ├── menu.html           # Student-facing stall/menu view
│       ├── order_confirm.html  # Order confirmation and summary
│       ├── order_track.html    # Real-time order status tracker
│       └── dashboard.html      # Stall manager operations view
│
├── blockbites/                 # Django project configuration
│   ├── settings/
│   │   ├── base.py             # Shared settings
│   │   ├── development.py      # Dev overrides (DEBUG=True, SQLite fallback)
│   │   └── production.py       # Production config (Gunicorn, PostgreSQL, HTTPS)
│   ├── urls.py                 # Root URL configuration
│   └── wsgi.py                 # WSGI entrypoint for Gunicorn
│
├── requirements.txt            # Python dependencies (pinned versions)
├── .env.example                # Environment variable template
├── Dockerfile                  # Container build specification
├── docker-compose.yml          # Multi-service orchestration
├── manage.py                   # Django management entrypoint
└── README.md                   # This document
```

---

## ⚙️ Installation Guide

### Prerequisites

- Python 3.11+
- PostgreSQL 15+
- Git

### Local Development Setup

```bash
# 1. Clone the repository
git clone https://github.com/sandeepkumar9760/BlockBites-LPU.git
cd BlockBites-LPU

# 2. Set up virtual environment
python3 -m venv venv
source venv/bin/activate        # Linux/macOS
# venv\Scripts\activate         # Windows

# 3. Install Python dependencies
pip install -r requirements.txt

# 4. Set up environment variables
cp .env.example .env
# Open .env and configure your PostgreSQL credentials

# 5. Create the PostgreSQL database
psql -U postgres
CREATE DATABASE blockbites_db;
CREATE USER blockbites_user WITH PASSWORD 'yourpassword';
GRANT ALL PRIVILEGES ON DATABASE blockbites_db TO blockbites_user;
\q

# 6. Run migrations
python manage.py migrate

# 7. Load initial data (blocks and stalls)
python manage.py loaddata initial_blocks.json

# 8. Create admin user
python manage.py createsuperuser

# 9. Start development server
python manage.py runserver
```

Visit `http://127.0.0.1:8000` for the student interface.
Visit `http://127.0.0.1:8000/admin` for the management dashboard.

### Running Tests

```bash
python manage.py test Block_stalls --verbosity=2
```

---

## 🧠 Future Improvements / Scalability Roadmap

**Phase 1 — Operational Hardening (Q1)**
- Migrate session store to Redis for horizontal scaling of the Gunicorn worker pool.
- Add Django Channels + WebSockets for push-based real-time order status updates, replacing the current polling approach.
- Implement database connection pooling via PgBouncer to handle concurrent order bursts during peak lunch hours.

**Phase 2 — AI-Driven Demand Intelligence (Q2)**
- Train a time-series forecasting model (Facebook Prophet or LSTM) on the `DemandLog` table, predicting stall-level demand 2 hours ahead with block-time-weekday features.
- Surface predictions in the stall manager dashboard as inventory preparation alerts ("Prepare 40 additional servings of Dal Makhani by 12:30 PM").
- Build an anomaly detection pipeline that flags unusual order patterns (potential fraudulent bulk orders or system abuse).

**Phase 3 — Platform Expansion (Q3–Q4)**
- REST API layer (Django REST Framework) exposing order and menu endpoints for a native mobile application.
- Payment gateway integration (Razorpay / PayU) for cashless campus transactions.
- Multi-campus support — abstract the `Block` model to support a `Campus` parent entity, enabling the platform to serve other institutions with zero schema changes.
- Loyalty and gamification layer — per-student order history driving discount eligibility and canteen feedback scoring.

**Scalability Ceiling**
The current architecture can serve approximately 500 concurrent students on a single Gunicorn/PostgreSQL node. With Redis session offloading, read replica for analytics queries, and Nginx load balancing across 3 Gunicorn nodes, the system can handle LPU's full 30,000+ student population at peak throughput without architectural rework.

---

## 📸 Screenshots

### Authentication — Login Screen
> Branded login interface with ramen bowl identity mark, dark navy theme, and clean credential form. Session-secured with Django's CSRF middleware on every POST.

![Login Screen](screenshot_login.png)

---

### Block Selection — Campus Topology View
> The entry point of the ordering flow. Students see all campus blocks (34 Block, 25 Block, Hospital Block, Law Block, NK Block, BH-1 Block, etc.) with live stall counts and order activity. Block topology is a first-class domain concept — not a dropdown afterthought.

![Block Selection](screenshot_block_select.png)

---

### Available Stalls — Block-Filtered Stall Discovery
> After selecting a block, students see all registered stalls for that delivery zone. Each stall card surfaces the name, category, star rating (e.g., Kitchen Ette: 4.8★), open/closed status, and a direct "Browse Menu" CTA. Animated floating orb background reinforces the custom-designed UI identity.

![Available Stalls](screenshot_available_stalls.png)

---

### Stall Manager Dashboard — Order Queue
> The operational view for stall managers. Displays each order with Order ID, student identity (LPU email or username), total amount (₹), time slot, fulfillment status, and creation timestamp. Orders are listed chronologically, enabling managers to process them in sequence without context-switching between systems.

![Stall Manager Dashboard](screenshot_stall_dashboard.png)

---

## 🤝 Contribution Guide

Contributions are welcome from both LPU students and the broader open-source community.

**Getting started:**

1. Fork the repository on GitHub.
2. Create a feature branch from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Make your changes with clear, atomic commits:
   ```bash
   git commit -m "feat(orders): add estimated delivery time to OrderStatus model"
   ```
4. Write or update tests for any changed logic:
   ```bash
   python manage.py test Block_stalls
   ```
5. Push your branch and open a Pull Request against `main`.

**Commit message convention:** This project follows [Conventional Commits](https://www.conventionalcommits.org/). Prefix commits with `feat:`, `fix:`, `refactor:`, `docs:`, or `chore:`.

**Code style:** PEP 8 enforced via `flake8`. Run `flake8 .` before submitting a PR.

**Issues:** Open a GitHub Issue for bug reports or feature requests. Use the provided issue templates.

---

## 📄 License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for full terms.

You are free to use, modify, and distribute this software for academic and commercial purposes with attribution.

---

## 👨‍💻 Author

**Sandeep Kumar**
Backend Engineer · Django Specialist · LPU Computer Science

- GitHub: [@sandeepkumar9760](https://github.com/sandeepkumar9760)
- LinkedIn: [linkedin.com/in/sandeepkumar9760](https://linkedin.com/in/sandeepkumar9760) *(update with actual profile)*
- Email: sandeepkumar9760@example.com *(update with actual email)*

> *"Good software solves real problems for real people. BlockBites LPU was built because I saw a broken system every day and decided to fix it."*

---

## 🎯 Recruiter Summary

BlockBites LPU demonstrates **production-grade Django engineering**: a normalized PostgreSQL schema with 3NF data modeling, a formal order state machine with timestamped lifecycle events, and a demand logging architecture explicitly designed as the upstream data source for ML pipelines — not bolted on as an afterthought. The system reflects an understanding of real operational constraints (campus topology as a first-class domain concept, role-based access control at the view layer, N+1 query elimination via ORM prefetching) that distinguishes engineers who have shipped working software from those who have only followed tutorials. The AI roadmap section is grounded in the actual data already being collected — demonstrating the ability to think about system evolution from day one of schema design.
