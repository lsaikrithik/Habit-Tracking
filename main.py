import requests
from datetime import datetime

# Replace with your Pixela information
USERNAME = "YOUR USERNAME"
TOKEN = "YOUR SELF GENERATED TOKEN"
GRAPH_ID = "YOUR GRAPH ID"

pixela_endpoint = "https://pixe.la/v1/users"

# Headers for authentication
headers = {
    "X-USER-TOKEN": TOKEN
}

# Function to add pixel data
def add_pixel():
    pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
    today = datetime.now().strftime("%Y%m%d")
    quantity = input("How many kilometers did you cycle today? ")
    pixel_data = {
        "date": today,
        "quantity": quantity,
    }
    response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
    print(response.text)

# Function to update pixel data
def update_pixel(date: str, quantity: str):
    update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"
    new_pixel_data = {
        "quantity": quantity
    }
    response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
    print(response.text)

# Function to delete pixel data
def delete_pixel(date: str):
    delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"
    response = requests.delete(url=delete_endpoint, headers=headers)
    print(response.text)

# Function to retrieve and display graph statistics
def get_graph_stats():
    stats_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/stats"
    response = requests.get(url=stats_endpoint, headers=headers)
    if response.status_code == 200:
        stats = response.json()
        print("Graph Statistics:")
        print(f"Total Distance: {stats['totalQuantity']} Km")
        print(f"Max Quantity: {stats['maxQuantity']} Km")
        print(f"Min Quantity: {stats['minQuantity']} Km")
        print(f"Count: {stats['count']}")
        print(f"Today's Quantity: {stats['todayQuantity']} Km")
    else:
        print("Failed to retrieve statistics.")

# Main function with menu interface
def main():
    while True:
        print("\nPixela Habit Tracker")
        print("1. Add Pixel Data")
        print("2. Update Pixel Data")
        print("3. Delete Pixel Data")
        print("4. View Statistics")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_pixel()

        elif choice == '2':
            date = input("Enter the date (YYYYMMDD) to update: ")
            quantity = input("Enter new quantity: ")
            update_pixel(date, quantity)

        elif choice == '3':
            date = input("Enter the date (YYYYMMDD) to delete: ")
            delete_pixel(date)

        elif choice == '4':
            get_graph_stats()

        elif choice == '5':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
