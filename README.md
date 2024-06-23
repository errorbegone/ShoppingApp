# ShopIt
# ShopIt E-Commerce Platform

ShopIt is a full-featured e-commerce platform built using Django. This project enables user authentication, product listings, and category management. It also implements dynamic item filtering, user-specific actions like item creation, editing, and deletion, and integrates Tailwind CSS for a responsive design.

## Features

- **User Authentication**: Sign up, login, and manage user accounts.
- **Product Listings**: Create, read, update, and delete products.
- **Category Management**: Organize products into categories.
- **Dynamic Item Filtering**: Filter products dynamically based on categories.
- **Responsive Design**: Tailwind CSS for a mobile-friendly user interface.

## Tech Stack

- **Backend**: Django, SQLite (or PostgreSQL)
- **Frontend**: Django Templates, Tailwind CSS
- **Authentication**: Django's built-in authentication system

## Installation

### Prerequisites

- Python 3.8+
- Django 3.2+
- Git

### Clone the Repository

```bash
git clone https://github.com/yourusername/ShopIt.git
cd ShopIt
```

### Set Up Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Apply Migrations

```bash
python manage.py migrate
```

### Create a Superuser

```bash
python manage.py createsuperuser
```

### Run the Development Server

```bash
python manage.py runserver
```

Open your browser and navigate to `http://127.0.0.1:8000/` to see the application in action.

## Usage

### Accessing the Admin Panel

Navigate to `http://127.0.0.1:8000/admin` and log in with the superuser credentials to manage users, products, and categories.

### Creating Products and Categories

- Log in to the admin panel.
- Add categories and products using the provided forms.
- Products will appear on the main page under their respective categories.

### User Actions

- **Sign Up**: Users can create a new account.
- **Login**: Existing users can log in.
- **Dashboard**: Users can create, edit, and delete their own products.

## File Structure

```plaintext
ShopIt/
├── core/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
├── item/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
├── ShopIt/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── manage.py
├── requirements.txt
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to customize this README file further based on your specific project requirements and details.
