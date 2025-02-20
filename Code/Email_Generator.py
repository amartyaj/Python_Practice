#!/usr/bin/env python3

import re
import os
import sys

if sys.stdin.isatty():
    print("Here")
    terminal_size = os.get_terminal_size()
    terminal_width = terminal_size.columns
else:
    terminal_width = 80


def read_and_split_by_tab(file_path):
    pattern = r"^R-"
    try:
        with open(file_path, "r") as file:
            for line in file:
                my_str = "-" * terminal_width
                print(my_str)
                fields = line.strip().split(";")
                sub_fields = [field.split("\t") for field in fields]
                hiring_manager_first_name = ""
                hiring_manager_email = ""
                requisition_ids = []
                recruiter_first_name = []
                recruiter_email = []
                manager_recruiter = []
                addressing = ""
                for sub_field in sub_fields:
                    if re.match(pattern, str(sub_field[0])) and len(sub_field) == 3:
                        requisition_ids.append(sub_field[0])
                        recruiter_first_name.append(sub_field[1].split(" ")[0])
                        recruiter_email.append(sub_field[2])
                    elif len(sub_field) == 2:
                        hiring_manager_first_name = sub_field[0].split(" ")[0]
                        hiring_manager_email = sub_field[1]
                    else:
                        requisition_ids.append(sub_field[0])
                manager_recruiter = [hiring_manager_first_name]
                manager_recruiter.extend(recruiter_first_name)
                manager_recruiter = list(dict.fromkeys(manager_recruiter))
                if len(manager_recruiter) == 1:
                    addressing = str(manager_recruiter[0])
                else:
                    addressing = "/".join(manager_recruiter)
                email_addresses = [hiring_manager_email]
                email_addresses.extend(recruiter_email)
                requisition_ids = ", ".join(requisition_ids)
                print(f"Regarding Job Opening: {requisition_ids}")
                email_addresses = list(dict.fromkeys(email_addresses))
                email_addresses = "; ".join(email_addresses)
                print(f"{email_addresses}")
                print(f"\nHi {addressing},\n")
                print(
                    f"I hope you are doing well. I work in the Pricing team of Walmart International and am the technical lead for 2 of our products. I have about 14 years of experience in total (6 years with Walmart), working with application design and development, data, various databases and ETL. I have strong experience with languages such as Python, Shell scripting, Java, Perl, SQL, PL/SQL and R. I also work a lot with RDBMS databases, NoSQL databases, Big Data (Hadoop), Spark, Google Cloud Platform (BigQuery), Kafka and Airflow. I have experience working with CI/CD pipelines, data pipelines and WCNP as well.\n\nI came across the job posting for {requisition_ids} on Workday and am very interested. I would like to learn more about this role and your team. Please find my resume attached and let me know if you have any questions for me. I’ll be looking forward to hearing back from you.\n\nRegards,\nJagat\n(Jagatpran Amartya)"
                )
                print("\n")
        file.close()
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    file_path = "./tmp/final_list_for_script.txt"
    read_and_split_by_tab(file_path)

