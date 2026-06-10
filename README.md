# 🕒 Digital Clock Application

A modern **Digital Clock Application** built using **Python, Tkinter, TTKBootstrap, and MySQL**. The application supports multiple user profiles, customizable themes, 12-hour and 24-hour time formats, and personalized clock settings stored in a database.

---

## 🚀 Features

### 👤 Multi-User Support
- Multiple user profiles
- User selection screen
- Personalized settings for each user
- Quick user switching

### 🕒 Real-Time Digital Clock
- Live clock updates every second
- Smooth and accurate time display
- Digital clock interface
- Responsive UI

### ⏰ Time Format Options
- 12-Hour Format (AM/PM)
- 24-Hour Format
- User-specific preferences

### 🎨 Dynamic Theme System
- Multiple built-in themes
- One-click theme switching
- Modern TTKBootstrap styling
- Personalized appearance

### 📍 Location Display
- Displays user-selected city
- Personalized dashboard experience

### 🗄️ Database Integration
- MySQL-based user settings storage
- Theme preferences
- Time format preferences
- User profile management

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Core Programming Language |
| Tkinter | GUI Framework |
| TTKBootstrap | Modern UI Styling |
| MySQL | Database Management |
| mysql-connector-python | Database Connectivity |
| Datetime Module | Real-Time Clock Functionality |

---

# 📂 Project Structure

```text
Digital-Clock-App/
│
├── digital_clock.py
├── digital_clock_db.sql
├── README.md
│
└── Database
    └── settings
```

---

# ⚙️ Database Setup

## Step 1: Create Database

```sql
CREATE DATABASE digital_clock_db;
```

## Step 2: Select Database

```sql
USE digital_clock_db;
```

## Step 3: Import SQL File

Import the provided SQL script:

```text
digital_clock_db.sql
```

using MySQL Workbench or any MySQL client.

---

# 🔧 Installation

## Clone Repository

```bash
git clone https://github.com/your-username/digital-clock-app.git
cd digital-clock-app
```

## Install Required Libraries

```bash
pip install ttkbootstrap mysql-connector-python
```

---

# 🗄️ Configure Database Connection

Open:

```python
digital_clock.py
```

Update the database credentials:

```python
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'YOUR_PASSWORD',
    'database': 'digital_clock_db'
}
```

---

# ▶️ Run Application

```bash
python digital_clock.py
```

---

# 👤 User Management

The application loads all available users from the database.

### Features

- User Selection Screen
- Personalized Settings
- Multiple User Profiles
- User Switching Without Restart

---

# 🕒 Clock Features

### Supported Formats

```text
12-Hour Format (AM/PM)
24-Hour Format
```

### Real-Time Updates

- Updates every second
- Accurate system time display
- Smooth refresh mechanism

---

# 🎨 Available Themes

The application supports multiple modern themes:

```text
darkly
superhero
flatly
cosmo
cyborg
journal
minty
```

Users can switch themes dynamically while the application is running.

---

# 📍 Personalized Dashboard

Each user can have:

- Username
- Preferred Theme
- Preferred Time Format
- City Information

These settings are automatically loaded from the database.

---

# 🗃️ Database Structure

### Settings Table

```text
settings
├── username
├── theme
├── time_format
└── city
```

---

# 🔒 Error Handling

The application includes:

- Database Connection Validation
- User Loading Error Handling
- Missing Data Protection
- User-Friendly Error Messages

---

# 🎯 Future Enhancements

- Alarm Clock System
- Stopwatch
- Countdown Timer
- World Clock Support
- Weather Integration
- Custom Theme Creator
- User Registration System
- Time Zone Management
- Sound Notifications
- Desktop Widgets

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the Repository
2. Create a Feature Branch
3. Commit Your Changes
4. Push to GitHub
5. Open a Pull Request

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

Developed using Python, TTKBootstrap, and MySQL to provide a modern, customizable, and user-friendly digital clock experience.

⭐ If you found this project useful, consider giving it a star on GitHub.
