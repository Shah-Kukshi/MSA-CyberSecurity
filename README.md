Got it — here’s a **short, clean, workshop-ready README**
Perfect for students and demos.



# Insecure Flask Web App – Cybersecurity Demo

This is a **simple Python Flask application** intentionally built with **basic security flaws** for learning purposes.

It is used in a **cybersecurity workshop** to demonstrate:

* How insecure apps behave in the cloud
* How data gets exposed due to misconfiguration
* How to secure applications using **Microsoft Defender for Cloud** and **Identity & Access Management (Microsoft Entra ID)**



## Tech Stack

* Python 3
* Flask
* Azure Virtual Machine
* Microsoft Defender for Cloud
* Microsoft Entra ID (IAM)



## How to Run

```bash
pip install flask
python app.py
```

App runs at:
`http://127.0.0.1:5000`



## Intentional Security Issues

* Hardcoded credentials
* No authentication on sensitive endpoints
* Public cloud deployment
* Debug mode enabled

These represent **common real-world mistakes**, not hacking.



## Workshop Goal

* Deploy the app on Azure
* Identify security gaps
* Fix them using Microsoft security tools
* Verify that data is no longer publicly accessible



## Disclaimer

For **educational use only**.
Not production-ready.
