PROJECT OVERVIEW
This is a replica of the Travello Project done by Telusko.
This project demonstrates how Django can interact with HTML to build dynamic web pages. The project makes use of both static and dynamic files, which are seamlessly integrated using Django's templating system. The development environment was set up in Visual Studio Code (VSCode), leveraging the Django-HTML extension for a better coding experience.

KEY FEATURES
1) Django-HTML Integration: Utilizes Django's templating engine to render HTML pages dynamically.
2) Static Files: Incorporates CSS, JavaScript, and image files to enhance the user interface and experience.
3) Dynamic Content: Uses Django views and context to pass dynamic content into HTML templates.

Installation

1) Clone the repository:
  ```bash
   git clone https://github.com/princessetowe/Travello.git
   ```
2) Navigate to the project directory:
   ```bash
   cd Travello
    ```

3)  Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
4) Run migrations**:
   ```bash
   python manage.py migrate
   ```

5) Start the development server:
   ```bash
   python manage.py runserver
   ```

6) Access the project in your browser:
    ```bash
   Open your browser and navigate to `http://127.0.0.1:8000/`.
    ```

USAGE
. Static Files: Static files like CSS and JavaScript are stored in the `static/` directory and can be linked in your HTML templates using Django's `{% static %}` tag.
. Dynamic Content: Allows passing of dynamic data from your Django views to your HTML templates using context dictionaries.

