# PostIt

![PostIt logo](/assets/POSTIT.png)

PostIt is a blog application designed for conception, deliberation and implementation of ideas. PostIt is designed for creative thinkers, writers and experts to expose their ideas to the world. A platform where readers and writers collaborate on important ideas leading to discovery and growth.

*“We write to taste life twice, in the moment and in retrospect.”*
― **Anais Nin**

## Medium blog

For a general overview of PostIt, in-depth description, and more about the inspiration for PostIt, read the following Medium article: 

[Introducing PostIt](https://medium.com/@salmonmbuchi/introducing-postit-blog-application-783055413de5)

## Architecture

### Back-end

PostIt's back-end is written primarily in Python. Python was used as the backend language because it has a wide variety of web application frameworks such as Flask. Flask was used as the web framework to build a RESTful API because it is light, flexible and was covered in previous projects so this was a chance to show what I learnt.

For the database I used a MySQL server because the relational database is most suited for structured data in this application. Below is a data diagram that illustrates how the data is stored: 

![data-diagram](/assets/postit_data_diagram.drawio.png)

### Front-end

For the front-end, I used HTML and CSS for the earlier parts of the project, however, as more features kept coming up I decided to use Bootstrap. Native implementations of features such as navigation bars were styled with Bootstrap. Some creative freedom was lost in the process but this was what worked best in the project timeline.

Here we have a diagram that shows the tech stack that make up PostIt:

![Tech stack](./assets/PostIt_tech_stack.png)

## Getting Started

1. Clone this repository
2. Activate the virtual environment by running `source [full path]/PostIt/env/bin/activate`
3. Run `flask run`. Once this is done you are ready to run **PostIt**. Navigate to your web browser and enter `localhost:5000`. Enjoy PostIt!

## Deployment

PostIt is deployed on Render. Render is a unified cloud to build and run web apps and web sites with free TLS certificates, protection and auto deploys from Git. Learn more about them [here](https://render.com/)

Try [PostIt](https://postit-web-app.onrender.com)
:warning: Your browser might through an error: **Deceptive site ahead**. Kindly ignore this. I am currently working on a solution for this problem.

## User Experience

Below is a simple flow for the user experience on PostIt:

![User experience](/assets/PostIt%20user%20xp.png)

**Sign-in page**
![sign-in](/assets/Sign-in.png)

**Home page**
![homepage](/assets/Home-page.png)

**Explore page**
![explore](/assets/Explore-page.png)

**Profile page**
![profile](/assets/Profile-page.png)

## Dependencies

The dependencies necessary for running PostIt are listed [here](requirements.txt)

## Author

**Salmon:** [Github](https://github.com/SalmonMbuchi) / [LinkedIn](https://www.linkedin.com/in/salmon-mbuchi/)
