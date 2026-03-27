# Day 4: APIs + Requests — Python Talking to the World

This day covers interacting with external APIs using Python's `requests` library. You will learn how to fetch data from web APIs, handle responses, and display useful information.

---

## Exercise 1: GitHub Profile Fetcher

### Description

This script fetches a GitHub user's profile and top repositories by stars using the GitHub public API.

* Handles errors like user not found (404), rate limit (403), and network issues.
* Accepts username via **command line argument** or input prompt.

### Usage

```bash
python3 apiAndRequest.py [github_username]
```

### Example Output

```
Enter Github username: wasihaider96

==== Github Profile ===
Username: wasihaider96
Bio: - iOS Engineer | Swift Enthusiast 🚀
- Crafting Sleek APPs 📱
- Passionate About Tech 🔧
Public repos: 7
Followers: 0

==== Top 5 Repositories ====

1. calculator
   ⭐ Stars: 1
   🍴 Forks: 0
   💻 Language: Swift

2. Demo-Travel-UI
   ⭐ Stars: 1
   🍴 Forks: 0
   💻 Language: Swift

3. KSE
   ⭐ Stars: 1
   🍴 Forks: 0
   💻 Language: Swift

4. Tik-Cross-App
   ⭐ Stars: 1
   🍴 Forks: 0
   💻 Language: Swift

5. WeatherApp
   ⭐ Stars: 1
   🍴 Forks: 0
   💻 Language: Swift
```

### Hardest Part

* Understanding the JSON structure returned by GitHub API.
* Sorting repositories by stars and displaying only the top 5.

---

## Exercise 2: Weather CLI

### Description

This script fetches the current weather of any city using the **Open-Meteo API**.

* Requires two API calls:

  1. City name → coordinates (latitude, longitude)
  2. Coordinates → current weather
* Displays temperature (Celsius and Fahrenheit), wind speed, and weather code.

### Usage

```bash
python3 WeatherCLI.py
```

### Example Output

```
Enter your city name: Lahore

==== Weather ====
City: Lahore
Temperature: 26.0 °C / 78.8 °F
Wind Speed: 3.3 km/h
Weather Code: 0
```

### Hardest Part

* Chaining two API calls.
* Understanding the structure of JSON responses to extract the required data.

---

## Notes

* Both exercises demonstrate how to use `requests` to interact with web APIs.
* Always print the raw JSON first while learning, to understand the data structure.
* Proper error handling (404, 403, network errors) is crucial for real-world API calls.
