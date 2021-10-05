# E-Pradarshini

[![Updated Badge](https://badges.pufler.dev/updated/thewires2/E-Pradarshini?color=purple)](https://badges.pufler.dev) 
[![Commits Badge](https://badges.pufler.dev/commits/yearly/thewires2?color=yellow)](https://badges.pufler.dev)
[![Visits Badge](https://badges.pufler.dev/visits/thewires2/E-Pradarshini?color=red)](https://badges.pufler.dev)
[![Created Badge](https://badges.pufler.dev/created/thewires2/E-Pradarshini?color=blue)](https://badges.pufler.dev)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

---

Backend for the E-Pradarshini portal to showcase projects

![Screenshot](1.png)

---

Steps to run

1. Download zip 

2. Create a virtual enviornment, e.g.
    
  > Linux
  
  ```
  pip install virtualenv  
  virtualenv venv  
  source venv/bin/activate  
  pip install -r requirements.txt
  ```
  
  > Windows
  
  ```
  pip install virtualenv  
  virtualenv venv  
  .\venv\scripts\activate  
  pip install -r requirements.txt
  ```

3. Run the migrations

```
  python manage.py migrate
```

4. Run the local development server on localhost

```
python manage.py runserver
```
    
    


