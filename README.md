# <img src="https://img.icons8.com/color/48/000000/pyramids.png" width="32" height="32"/> اكتشف مصر (Explore Egypt)

> **Your AI-Powered Guide to Egypt's Majestic Wonders**

[![Django](https://img.shields.io/badge/Django-4.1-092E20?logo=django)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)](https://www.python.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-4.4-7952B3?logo=bootstrap)](https://getbootstrap.com/)
[![SQLite](https://img.shields.io/badge/SQLite-3-003B57?logo=sqlite)](https://www.sqlite.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

![Explore Egypt Demo](https://placehold.co/800x400/1B435D/FFFFFF/png?text=Explore+Egypt&font=raleway)

## 🏛️ Overview

اكتشف مصر (Explore Egypt) is a comprehensive tourist guide platform that showcases historical sites and attractions across Egypt. The website provides detailed information about various locations including descriptions, images, pricing, opening hours, and map locations. Users can create accounts to enhance their experience, explore sites, and find the best tourist destinations in Egypt.

<b>🌟 Key Features</b>

- 🏛️ **Detailed Site Listings** - Comprehensive information about Egypt's historical sites and attractions
- 🌐 **Interactive Maps** - Integrated maps to help visitors locate sites easily
- 🖼️ **Image Galleries** - Multiple images for each location to showcase its beauty and significance
- 💰 **Pricing Information** - Clear pricing details to help tourists plan their budget
- 🕒 **Opening Hours** - Up-to-date information about when sites are open to visitors
- 👤 **User Accounts** - Personalized experience with user registration and profiles
- 🔍 **Site Search** - Find specific locations quickly and easily
- 📱 **Responsive Design** - Optimized for all devices, from mobile to desktop
- 🌙 **Multilingual Support** - Content available in both Arabic and English
- 📍 **Location Details** - Comprehensive information about each site's location and how to get there

## 🔧 Tech Stack

<div align="center">
  <table>
    <tr>
      <td align="center" width="96">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg" alt="Django" width="48" height="48" />
        <br/>Django
      </td>
      <td align="center" width="96">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" alt="Python" width="48" height="48" />
        <br/>Python
      </td>
      <td align="center" width="96">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bootstrap/bootstrap-plain.svg" alt="Bootstrap" width="48" height="48" />
        <br/>Bootstrap
      </td>
      <td align="center" width="96">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" alt="HTML5" width="48" height="48" />
        <br/>HTML5
      </td>
      <td align="center" width="96">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg" alt="CSS3" width="48" height="48" />
        <br/>CSS3
      </td>
      <td align="center" width="96">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" alt="JavaScript" width="48" height="48" />
        <br/>JavaScript
      </td>
    </tr>
    <tr>
      <td align="center" width="96">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlite/sqlite-original.svg" alt="SQLite" width="48" height="48" />
        <br/>SQLite
      </td>
      <td align="center" width="96">
        <img src="https://cdn.worldvectorlogo.com/logos/jquery-4.svg" alt="jQuery" width="48" height="48" />
        <br/>jQuery
      </td>
      <td align="center" width="96">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/font-awesome/font-awesome-original.svg" alt="Font Awesome" width="48" height="48" />
        <br/>Font Awesome
      </td>
      <td align="center" width="96">
        <img src="https://michalsnik.github.io/aos/img/aos-logo.png" alt="AOS" width="48" height="48" />
        <br/>AOS
      </td>
      <td align="center" width="96">
        <img src="https://djangopackages.org/static/img/package-apps.png" alt="Django Countries" width="48" height="48" />
        <br/>Django Countries
      </td>
      <td align="center" width="96">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/480px-No_image_available.svg.png" alt="Media Files" width="48" height="48" />
        <br/>Media Files
      </td>
    </tr>
  </table>
</div>

<b>⚙️ Backend</b>

- Django 4.1 - High-level Python web framework
- Python 3.x - Programming language
- SQLite - Lightweight database engine
- Django Countries - Country field for Django models
- Django Bootstrap Form - Bootstrap integration for Django forms

<b>🖌️ Frontend</b>

- HTML5 - Standard markup language
- CSS3 - Style sheet language
- JavaScript - Programming language
- Bootstrap 4.4 - Frontend framework
- jQuery - JavaScript library
- Font Awesome - Icon toolkit
- AOS - Animate On Scroll library

## 📂 Project Structure

```
explore-egypt/
├── accounts/                 # User authentication and profile management
│   ├── migrations/           # Database migrations
│   ├── templates/            # Account-related templates
│   ├── forms.py              # User forms
│   ├── models.py             # User profile models
│   ├── urls.py               # Account URLs
│   └── views.py              # Account views
├── main/                     # Main application
│   ├── migrations/           # Database migrations
│   ├── models.py             # Site and related models
│   ├── urls.py               # Main URLs
│   └── views.py              # Main views
├── media/                    # User-uploaded media files
│   └── sites/                # Site images
├── project/                  # Project configuration
│   ├── static/               # Project-wide static files
│   ├── settings.py           # Django settings
│   └── urls.py               # Project URLs
├── static/                   # Static files (CSS, JS, images)
│   ├── css/                  # Stylesheets
│   ├── img/                  # Images
│   └── js/                   # JavaScript files
├── templates/                # HTML templates
│   ├── main/                 # Main app templates
│   │   ├── about.html        # About page
│   │   ├── add-site.html     # Add site form
│   │   ├── index.html        # Homepage
│   │   ├── site.html         # Single site page
│   │   └── sites.html        # Sites listing
│   └── base.html             # Base template
├── teams/                    # Teams application
├── db.sqlite3                # SQLite database
├── manage.py                 # Django management script
└── README.md                 # Project documentation
```

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- pip (Python package manager)

### Installation

1️⃣ **Clone the repository:**
```sh
git clone https://github.com/yourusername/explore-egypt.git
cd explore-egypt
```

2️⃣ **Create a virtual environment:**
```sh
python -m venv venv
```

3️⃣ **Activate the virtual environment:**

On Windows:
```sh
venv\Scripts\activate
```

On macOS/Linux:
```sh
source venv/bin/activate
```

4️⃣ **Install dependencies:**
```sh
pip install -r requirements.txt
```

5️⃣ **Apply migrations:**
```sh
python manage.py migrate
```

6️⃣ **Create a superuser:**
```sh
python manage.py createsuperuser
```

7️⃣ **Run the development server:**
```sh
python manage.py runserver
```

8️⃣ **Open your browser:**
Navigate to `http://127.0.0.1:8000`

## 🌐 Site Administration

To access the admin panel:

1. Navigate to `http://127.0.0.1:8000/admin/`
2. Log in with your superuser credentials
3. Manage sites, users, and other content

## 🔍 Features in Detail

### Site Management
- Add, edit, and delete tourist sites
- Upload multiple images for each site
- Specify location details, pricing, and opening hours
- Add interactive maps through map links

### User Management
- User registration and authentication
- User profiles with personal information
- Country selection for user profiles
- Secure login and logout functionality

### Content Browsing
- Browse all sites with pagination
- View detailed information about each site
- Interactive elements with scroll animations
- Responsive design for all device sizes

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

- Django for the powerful web framework
- Bootstrap for the responsive design components
- AOS library for smooth scrolling animations
- Django Countries for country field support
- All contributors who helped with development and content

---

<div align="center">
  <img src="https://img.icons8.com/color/48/000000/pyramids.png" width="24" height="24"/>
  <p>Made with ❤️ for the Egyptian tourism community</p>
</div> 
