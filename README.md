# Advertisement Website - Django Project

A comprehensive advertisement website built with Django, featuring property listings and general classified ads.

## Features

- 📝 **Advertisement Management**: Post and manage classified ads across multiple categories
- 🏠 **Property Listings**: Dedicated property advertisement system
- 📱 **Responsive Design**: Mobile-friendly interface
- 🔍 **Search & Filter**: Advanced filtering and search capabilities
- 📸 **Image Gallery**: Multiple images per advertisement
- 👨‍💼 **Admin Panel**: Full admin interface for content management
- 📊 **Analytics**: View counting and featured ads

## Categories

- Property
- Vehicles
- Electronics
- Furniture
- Clothing
- Services
- Jobs
- Education
- Pets
- Other

## Local Development

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd advertisement
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run migrations**
```bash
python manage.py migrate
```

4. **Create superuser**
```bash
python manage.py createsuperuser
```

5. **Run development server**
```bash
python manage.py runserver
```

6. **Access the application**
- Website: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

## Deployment on Render

### Step 1: Push to GitHub

1. Create a new repository on GitHub
2. Push your code:
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin <your-github-repo-url>
git push -u origin main
```

### Step 2: Deploy on Render

1. **Go to [Render.com](https://render.com)** and sign up/login
2. **Click "New +"** and select "Web Service"
3. **Connect your GitHub repository**
4. **Configure deployment settings:**

   - **Name**: `advertisement-website`
   - **Environment**: `Python`
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn advertisement.wsgi:application`
   - **Instance Type**: `Free` (or choose paid for better performance)

### Step 3: Environment Variables

Add these environment variables in Render:

```
RENDER=True
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=your-app-name.onrender.com
DATABASE_URL=postgresql://... (Render will provide this)
```

### Step 4: Database Setup

1. **Create PostgreSQL database** in Render
2. **Copy the DATABASE_URL** from your PostgreSQL service
3. **Add DATABASE_URL** to your web service environment variables

## Deployment Troubleshooting

### Common Issues and Solutions

1. **"web:: command not found" Error**
   - This occurs when there's a conflict between Procfile and render.yaml
   - Solution: Use only render.yaml for configuration, remove Procfile
   - Ensure startCommand in render.yaml is: `gunicorn advertisement.wsgi:application --bind 0.0.0.0:$PORT`

2. **ALLOWED_HOSTS Error**
   - Django requires proper host configuration in production
   - The production_settings.py automatically configures RENDER_EXTERNAL_HOSTNAME
   - Ensure DJANGO_SETTINGS_MODULE is set to advertisement.production_settings

3. **Static Files Not Loading**
   - Make sure WhiteNoise is in MIDDLEWARE
   - Run `python manage.py collectstatic` in build.sh
   - Check STATIC_ROOT and STATICFILES_STORAGE settings

4. **Database Connection Issues**
   - Verify DATABASE_URL environment variable is set
   - Check that psycopg2-binary is in requirements.txt
   - Ensure PostgreSQL service is running in Render

### Environment Variables Required for Render

```
RENDER=true
DJANGO_SETTINGS_MODULE=advertisement.production_settings
DEBUG=false
DATABASE_URL=(your PostgreSQL URL)
SECRET_KEY=(generate a secure key)
```

## Project Structure

```
advertisement/
├── ad/                     # Main app
│   ├── models.py          # Advertisement & Property models
│   ├── views.py           # Views for listings and details
│   ├── admin.py           # Admin configuration
│   └── urls.py            # URL patterns
├── advertisement/         # Project settings
│   ├── settings.py        # Development settings
│   ├── production_settings.py  # Production settings
│   └── urls.py            # Main URL configuration
├── templates/             # HTML templates
├── static/               # CSS, JS, images
├── media/                # User uploaded files
├── requirements.txt      # Python dependencies
├── build.sh             # Build script for Render
├── Procfile             # Process file
└── runtime.txt          # Python version
```

## Technologies Used

- **Backend**: Django 5.2.1
- **Database**: SQLite (development), PostgreSQL (production)
- **Frontend**: Bootstrap 5, HTML5, CSS3
- **Deployment**: Render
- **Media Storage**: WhiteNoise (static files)

## Admin Features

- **Advertisement Management**: Add, edit, delete ads
- **Image Management**: Upload multiple images per ad
- **User Management**: Admin users and permissions
- **Analytics**: Track views and manage featured content
- **Categories**: Organize ads by category and type

## API Endpoints

- `/` - Home page with featured ads
- `/advertisements/` - All advertisements listing
- `/advertisement/<id>/` - Advertisement detail page
- `/properties/` - Property listings
- `/property/<id>/` - Property detail page
- `/search/` - Search functionality
- `/admin/` - Admin panel

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the MIT License.