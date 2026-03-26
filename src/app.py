import requests

def main():
    print("Running app")
    response = requests.get("https://httpbin.org/get")
    print(f"Status: {response.status_code}")

if __name__ == "__main__":
    main()