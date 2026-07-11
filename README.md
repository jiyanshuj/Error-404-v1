# GoPlan ✈️

A modern Django-based intelligent travel planning and hotel booking application that helps users find the best transportation options based on distance.

**Live Demo:** https://goplan.onrender.com/

## 📋 Description

GoPlan is a comprehensive web application designed to simplify travel planning. The app helps users calculate distances between locations, recommends the most suitable transport mode (Bus, Train, or Flight), and facilitates hotel bookings. It integrates with the TomTom API for accurate geolocation and route calculation services.

## ✨ Features

### Core Features
- **Trip Planning**: Enter your current location and destination to calculate the distance
- **Smart Transport Recommendations**: 
  - 🚌 **Bus** recommended for distances < 70 km
  - 🚂 **Train** recommended for distances 70-1000 km
  - ✈️ **Flight** recommended for distances > 1000 km
- **Real-time Distance Calculation**: Uses TomTom API for accurate routing data
- **Hotel Booking System**: Browse and book hotels at your destination
- **Booking Management**: Complete booking workflow with guest details
- **Payment Integration**: Secure payment processing for bookings

### Technical Features
- Responsive design with modern UI/UX
- Session management for persistent user data
- Error handling and validation
- Production-ready deployment on Render
- PostgreSQL database integration

## 🛠️ Technologies Used

### Backend
- **Django** 6.0.1 - Python web framework
- **Requests** - HTTP library for API calls
- **PostgreSQL** - Database (via psycopg2-binary)
- **Gunicorn** - Production WSGI server
- **SQLite3** - Local development database

### APIs & Services
- **TomTom API** - Geocoding and route calculation
- **Render** - Cloud deployment platform

### Frontend
- **HTML5/CSS3** - Markup and styling
- **JavaScript** - Client-side interactivity
- **Django Templates** - Server-side rendering

## 📦 Installation

### Prerequisites
- Python 3.10 or higher
- pip (Python package manager)
- Git

### Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/jiyanshuj/GoPlan.git
   cd GoPlan
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Start the development server**
   ```bash
   python manage.py runserver
   ```

6. **Access the application**
   - Open your browser and navigate to `http://127.0.0.1:8000/`

## 🚀 Usage

### Planning a Trip
1. **Home Page**: Enter your current location and destination to calculate the distance
2. **Distance Calculation**: The app calculates the distance and shows results
3. **Transport Recommendation**: View the recommended transport mode
4. **Book Transport**: Click "Book Now" to access booking platforms

### Hotel Booking
1. **Select Transport**: Choose your transport and proceed
2. **Browse Hotels**: View available hotels at your destination
3. **Enter Details**: Fill in guest information (name, email, phone, address)
4. **Payment**: Complete payment to finalize booking
5. **Confirmation**: Receive booking confirmation with booking ID

## 📁 Project Structure

```
GoPlan/
├── manage.py                 # Django management script
├── db.sqlite3               # Local SQLite database
├── requirements.txt         # Python dependencies
│
├── goplan/                  # Django project configuration
│   ├── settings.py          # GoPlan settings & configuration
│   ├── urls.py              # URL routing configuration
│   ├── wsgi.py              # WSGI application
│   └── asgi.py              # ASGI application
│
├── web/                     # Main Django application
│   ├── views.py             # View functions and business logic
│   ├── urls.py              # URL patterns
│   ├── forms.py             # Django forms (TripForm)
│   ├── api.py               # TomTom API integration
│   ├── models.py            # Database models
│   ├── api_mock.py          # Mock API for testing
│   └── migrations/          # Database migrations
│
├── templates/               # HTML templates
│   ├── home.html           # Landing page
│   ├── trip_form.html      # Trip planning form
│   ├── success.html        # Results & transport recommendation
│   ├── booking.html        # Hotel booking page
│   ├── form.html           # Guest details form
│   ├── payment.html        # Payment processing
│   ├── booking_success.html # Booking confirmation
│   └── error.html          # Error page
│
└── static/                 # Static files (CSS, JS, images)
```

## 🔧 Configuration

### Environment Variables
Set up the following in your environment or `.env` file:

```
TOMTOM_API_KEY=your_tomtom_api_key_here
DEBUG=False  # Set to True for development
ALLOWED_HOSTS=.onrender.com,localhost,127.0.0.1
```

### TomTom API Setup
1. Sign up at [TomTom Developer Portal](https://developer.tomtom.com/)
2. Get your API key
3. Add the key to `web/api.py`

## 🌐 Deployment

The application is deployed on [Render](https://render.com/) and is live at:
**https://goplan.onrender.com/**

### Deploy Steps
1. Push your code to GitHub
2. Connect your GitHub repository to Render
3. Configure build and start commands:
   - **Build**: `pip install -r requirements.txt && python manage.py migrate`
   - **Start**: `gunicorn goplan.wsgi:application`
4. Set environment variables in Render dashboard
5. Deploy!

## 🧪 Testing

Run tests with:
```bash
python manage.py test
```

### Test Coverage
- Trip form validation
- API integration
- Distance calculation
- Booking workflow

## 📝 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Home page & trip form |
| POST | `/` | Submit trip details |
| GET | `/booking/` | Hotel booking page |
| POST | `/forming/` | Guest details form |
| GET | `/pay/` | Payment page |
| POST | `/pay/` | Process payment |
| GET | `/success/` | Booking confirmation |

## 🐛 Troubleshooting

### Common Issues

**"No such table: django_session"**
```bash
python manage.py migrate
```

**TomTom API errors**
- Verify API key in `web/api.py`
- Check internet connection
- Ensure location names are valid

**Database errors**
- Run migrations: `python manage.py migrate`
- Reset database: `python manage.py flush` (development only)

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Author

**Jiyanshu Jain**

## 🙏 Acknowledgments

- [TomTom API](https://developer.tomtom.com/) - For geolocation and routing services
- [Django Framework](https://www.djangoproject.com/) - For the web framework
- [Render](https://render.com/) - For hosting and deployment
- The open-source community for various tools and libraries

## 📞 Support

For issues, questions, or suggestions, please open a [GitHub Issue](https://github.com/jiyanshuj/GoPlan/issues)

---

**Made with ❤️ by Jiyanshu Jain**
