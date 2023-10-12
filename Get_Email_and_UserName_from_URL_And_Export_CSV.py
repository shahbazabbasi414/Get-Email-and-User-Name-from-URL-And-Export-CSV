import csv
import requests
import re
import os
import time
import tkinter as tk
from tkinter import Entry, Label, Button, Frame

def extract_data(url, output_filename):
    response = requests.get(url)

    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    emails = re.findall(email_pattern, response.text)

    unique_emails = list(set(emails))

    modified_data = []

    for email in unique_emails:
        email_without_numeric = re.sub(r'\d+', '', email)
        parts = email_without_numeric.split('@')

        if len(parts) == 2:
            email_without_domain = parts[0]
            modified_data.append([email, email_without_domain])

    download_folder = os.path.join(os.path.expanduser("~"), "Downloads")
    output_path = os.path.join(download_folder, f'{output_filename}.csv')

    with open(output_path, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        if csvfile.tell() == 0:
            writer.writerow(['Email', 'Modified Name'])
        writer.writerows(modified_data)

    print(f'Emails and modified names extracted and saved to {output_path}')

    return modified_data

def extract_and_display():
    website_url = website_url_entry.get()
    output_filename = output_filename_entry.get()
    extracted_data = extract_data(website_url, output_filename)

app = tk.Tk()
app.title("Exterct Emails Form any URL")
app.geometry("1000x600")  
app.configure(bg="black")

form_frame = Frame(app, bg="red") 
form_frame.pack(pady=20)

website_url_label = Label(form_frame, text="Enter the website URL:", bg="black", fg="white")
website_url_label.grid(row=0, column=0, padx=10, pady=10)
website_url_entry = Entry(form_frame)
website_url_entry.grid(row=0, column=1, padx=10, pady=10)

output_filename_label = Label(form_frame, text="Enter the output filename (without extension):", bg="black", fg="white")
output_filename_label.grid(row=1, column=0, padx=10, pady=10)
output_filename_entry = Entry(form_frame)
output_filename_entry.grid(row=1, column=1, padx=10, pady=10)

extract_button = Button(form_frame, text="Extract Emails", command=extract_and_display, bg="black", fg="white")
extract_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

Show_comment =Button(form_frame, text="Important Notice ! ", bg="black", fg="Red")
Show_comment.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

Show_comment =Button(form_frame, text="File name Will Change every time If you Not Change your Emails Stores Same File For Multipul URLS", bg="black", fg="Red")
Show_comment.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

Show_comment =Button(form_frame, text="open a Download Foler and get your Emails", bg="black", fg="Red")
Show_comment.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

app.mainloop()
