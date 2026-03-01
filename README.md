# 📚 Django E-Library

A professional Django-based library management system for technical books.

## ✨ Features

- **Book Management**: Complete CRUD operations for books, authors, and categories
- **Advanced Search**: Search functionality using Django Q objects
- **User Authentication**: Signup, login, logout, and user profiles
- **Favorites System**: Users can save their favorite books
- **Permissions System**: Custom permissions for featured books
- **Admin Panel**: Customized Django admin with Jazzmin theme

## 🛠️ Technologies

- **Backend**: Django 5.1
- **Language**: Python 3.12
- **Database**: SQLite
- **Admin UI**: Jazzmin
- **Authentication**: Django Auth System

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/AbdelrahmanHassan-dev/Django-E-Library.git
cd Django-E-Library
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install django pillow django-jazzmin
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create superuser:
```bash
python manage.py createsuperuser
```

6. Run the server:
```bash
python manage.py runserver
```

Visit: `http://127.0.0.1:8000`

## 📁 Project Structure
```
Django-E-Library/
├── books/              # Books app (models, views, templates)
├── pages/              # Pages app (home, profile, auth)
├── templates/          # Global templates
├── project2/           # Main project settings
└── manage.py          # Django management script
```

## 🎯 Skills Demonstrated

- Django MVT Architecture
- ORM and Database Queries
- User Authentication & Permissions
- Form Handling & Validation
- Template Inheritance
- Static Files Management
- Admin Customization

## 👨‍💻 Author

**Abdelrahman Hassan**
- GitHub: [@AbdelrahmanHassan-dev](https://github.com/AbdelrahmanHassan-dev)

## 📄 License

This project is open source and available for educational purposes.

---

⭐ Star this repo if you found it helpful!
