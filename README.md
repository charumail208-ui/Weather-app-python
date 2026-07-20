# 🌦️ Weather App

A simple Python-based Weather App that fetches real-time weather information using the **OpenWeather API**. This project is part of my **90 Days of Coding** challenge to learn Python, APIs, and software development.

---

## 📌 Features

- 🌍 Get current weather by entering a city name
- 🌡️ Display temperature in Celsius
- ☁️ Display weather condition
- 💧 Display humidity
- 💨 Display wind speed
- 🚨 Handle invalid city names and API errors

---

## 🛠️ Technologies Used

- Python 3
- Requests Library
- OpenWeather API
- Git & GitHub

---

## 📁 Project Structure

```
WEATHER-APP/
│── main.py             # Main application
│── config.py           # Stores API key (not uploaded to GitHub)
│── requirements.txt    # Project dependencies
│── README.md           # Project documentation
└── screenshots/        # Application screenshots
```

---

## ⚙️ Installation

1. Clone this repository:

```bash
git clone <your-github-repository-link>
```

2. Move into the project folder:

```bash
cd WEATHER-APP
```

3. Install the required library:

```bash
pip install -r requirements.txt
```

4. Create a file named `config.py` and add your OpenWeather API key:

```python
API_KEY = "YOUR_API_KEY"
```

5. Run the application:

```bash
python main.py
```

---

## 📸 Sample Output

```
Enter city name: Kochi

Weather in Kochi
--------------------------
Temperature : 29°C
Condition   : Broken Clouds
Humidity    : 82%
Wind Speed  : 3.5 m/s
```

---

## 📚 Concepts Learned

- Working with APIs
- REST API fundamentals
- HTTP GET requests
- JSON parsing
- Status codes
- Python dictionaries and lists
- Error handling
- Git and GitHub

---

## 🚀 Future Improvements

- 🌤️ 5-day weather forecast
- 📍 Detect current location automatically
- ❤️ Save favourite cities
- 📊 Search history
- 🖥️ Graphical User Interface (GUI)
- 🌐 Better error messages

---

## 👨‍💻 Author

**Charutha Rajeevan**

B.Tech in Artificial Intelligence & Data Science

Learning Python through a **90 Days of Coding** challenge.

---

⭐ If you found this project interesting, feel free to star the repository!