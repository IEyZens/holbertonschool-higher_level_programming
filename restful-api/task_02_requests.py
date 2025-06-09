#!/usr/bin/python3
"""
This module fetches and processes data from a REST API (JSONPlaceholder).
It provides functions to print post titles and save post data to a CSV file.
"""
import requests
import csv


def fetch_and_print_posts():
    """
    Fetches all posts from the JSONPlaceholder API and prints their titles.

    If the request is successful (status code 200), the function parses the
    JSON response and prints each post's title to the console.
    Otherwise, it prints an error message.
    """
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts")
    except requests.exceptions.RequestException as error:
        print("Une erreur est survenue lors de la requête:", error)
        return

    print("Status Code:", response.status_code)

    if response.status_code == 200:
        posts = response.json()

        for post in posts:
            print(post["title"])
    else:
        print(f"Échec de la requête - Code retourné: {response.status_code}")


def fetch_and_save_posts():
    """
    Fetches all posts from the JSONPlaceholder API and saves them to a CSV
    file.

    If the request is successful (status code 200), the function filters each
    post
    to include only the id, title, and body fields, and writes the data into a
    'posts.csv' file using the csv module.
    """
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts")
    except requests.exceptions.RequestException as error:
        print("Une erreur est survenue lors de la requête:", error)
        return

    if response.status_code == 200:
        posts = response.json()

        csv_data = []

        for post in posts:
            post_filter = {
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            }

            csv_data.append(post_filter)

        with open("posts.csv", "w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(csv_data)
