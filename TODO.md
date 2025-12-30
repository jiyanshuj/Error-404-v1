# TODO List for Django Render Deployment Fix

- [x] Update ALLOWED_HOSTS in project/settings.py to include 'error-404-v1.onrender.com'
- [x] Set DEBUG = False in project/settings.py for production security
- [x] Add 'gunicorn' to requirements.txt
- [ ] Commit and push changes to trigger redeploy on Render
- [ ] Update Start Command in Render dashboard to: gunicorn project.wsgi:application --bind 0.0.0.0:$PORT
