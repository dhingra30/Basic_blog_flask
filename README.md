<<<<<<< HEAD
# Basic_blog_flask
Simple Blog Application with Flask, Bootstrap, HTML &amp; CSS

Here's a **GitHub README** template for the provided HTML code:

---

=======
>>>>>>> c5d5c8feebb597267d7f90439359aba85e202438
# Rahul's Blog - A Bootstrap Themed Blog Template

This is a simple blog template powered by **Bootstrap**, **Jinja2** templating, and **FontAwesome** icons. It is designed to display blog posts dynamically with a responsive and clean interface.

## Features

- **Dynamic Blog Posts**: Blog content is dynamically rendered using Jinja2 templating. Each post includes a title, subtitle, author, and date.
- **Responsive Design**: The template uses **Bootstrap** for responsive design, ensuring the blog looks great on all devices.
- **FontAwesome Icons**: Integrated FontAwesome icons for easy addition of social media links.
- **Navigation Bar**: A responsive navbar that collapses on smaller screens, offering easy navigation across the blog.
- **Pagination**: Includes a button to load older posts for better content management.

## File Structure

- **Header**: The header contains a masthead with an image background and a blog title.
- **Main Content**: The blog posts are dynamically rendered using Jinja2, with placeholders for blog data (title, subtitle, author, date, and body).
- **Footer**: The footer includes links to social media profiles (Twitter, Facebook, GitHub) and copyright information.
- **Assets**: The template uses Google Fonts for typography and Bootstrap for CSS.

## Prerequisites

- **Python** with Flask (if you are serving dynamic content)
- **Bootstrap 5.x**
- **Jinja2** templating engine
- **FontAwesome** for icons

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/rahuls-blog.git
   ```
2. Navigate to the project directory:
   ```bash
   cd rahuls-blog
   ```

3. Install dependencies (if applicable, such as Flask):
   ```bash
   pip install flask
   ```

4. Run your Flask app (if using Flask for backend):
   ```bash
   flask run
   ```

5. Open your browser and navigate to `http://127.0.0.1:5000/` to see the blog.

## HTML Structure

### Header Section
The blog header includes a masthead with an image background and dynamic blog title:
```html
<header class="masthead" style="background-image: url('./static/assets/img/img.png')">
    <h1>Rahul's Blog</h1>
    <span class="subheading">A collection of random stupid posts</span>
</header>
```

### Blog Post Rendering
Blog posts are dynamically rendered in the main content section:
```html
{% for data in blog_data %}
    <div class="post-preview">
        <a href="{{url_for('post', blog_id=data['id'])}}">
            <h2>{{data.title}}</h2>
            <h3>{{data.subtitle}}</h3>
        </a>
        <p class="post-meta">Posted by {{data.Author}} on {{data.date}}</p>
    </div>
{% endfor %}
```

### Footer Section
Includes social media links and copyright:
```html
<footer class="border-top">
    <ul class="list-inline text-center">
        <li class="list-inline-item">
            <a href="#!">
                <span class="fa-stack fa-lg">
                    <i class="fas fa-circle fa-stack-2x"></i>
                    <i class="fab fa-twitter fa-stack-1x fa-inverse"></i>
                </span>
            </a>
        </li>
        <!-- Add more social icons as needed -->
    </ul>
    <div class="small text-center text-muted fst-italic">Copyright &copy; Your Website 2023</div>
</footer>
```

## Dependencies

- **Bootstrap**: For responsive layout and components.
- **Google Fonts**: Lora and Open Sans for typography.
- **FontAwesome**: For icons in the footer and navigation.

## Contributing

Feel free to submit issues or pull requests if you want to contribute to the project.
