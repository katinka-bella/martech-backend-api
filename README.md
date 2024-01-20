# martech-backend-api

The API repository is an essential component of [the martech platform](https://github.com/katinka-bella/martech-platform), serving as the backend engine. Additionally, it automates the process of uploading files to the GCP bucket, ensuring seamless data management.

## Structure

The repository is organized into modules representing different marketing technology. Each module contains specific functionalities related to data analytics, tag management, and more. Here's a high-level overview of the structure:

```
martech-backend-api/
├─ api/
│  ├─ google/
│  |  |  ├─ analytics
│  |  |  |  ├─ main.py/
│  |  |  |  ├─ utils.py/
│  |  |  ├─ tag-manager
│  |  |  |  ├─ main.py/
│  |  |  ├─ bigquery
│  |  |  |  ├─ main.py/
│  ├─ adobe/
│  |  |  ├─ analytics
│  |  |  |  ├─ main.py/
│  |  |  ├─ tag-manager
│  |  |  |  ├─ main.py/
│  ├─ ...
├─ README.md
```
