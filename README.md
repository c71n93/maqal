# Мақал-мәтелдер

A database of proverbs in the Kazakh language.

## How to use

### Launch
1. clone this repo
```sh
git clone https://github.com/c71n93/maqal.git
```
2. install requirements
```sh
pip install -r requirements.txt
```
3. set up database

    create table structure
    ```sh
    python manage.py migrate
    ```

    load initial data
    ```sh
    python manage.py loaddata maqal/fixtures/initial_data.json
    ```
4. run server
```sh
python manage.py runserver
```
### Optional

- create a superuser
```sh
python manage.py createsuperuser
```
