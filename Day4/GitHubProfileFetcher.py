import requests
import sys

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    username = input("Enter Github username: ")

url = f"https://api.github.com/users/{username}"

try:
    response = requests.get(url)

    if response.status_code == 404:
        print("User not found")
        exit()

    elif response.status_code == 403:
        print("Rate limit hit, try later")
        exit()

    data = response.json()

    print("\n==== Github Profile ===")
    print("Username:", data.get("login"))
    print("Bio:", data.get("bio"))
    print("Public repose:", data.get("public_repos"))
    print("Followers:", data.get("followers"))

except requests.exceptions.RequestException:
    print("Network error")

repose_url = data.get("repos_url")

repos_response = requests.get(repose_url)

repos = repos_response.json()

sorted_repos = sorted(repos, key=lambda x: x["stargazers_count"], reverse=True)

for repo in sorted_repos[:5]:
    print("\n==== Repo ===")
    print("Name:", repo.get("name"))
    print("Stars:", repo.get("stargazers_count"))
    print("Forks:", repo.get("forks_count"))
