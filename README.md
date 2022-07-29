# Dsyne

A platform that allows users spin up a basic website - allow as much customizations as possible.

## Background

This project, ***Dsyne***, is a project initiative introduced by the Zuri team. It is a uplatform that allows users spin up a basic website and allow as much customizations as possible.

## Objectives

- 
-

## Technologies Used

- HTML/CSS/Javascript (Frontend)
- POSTGRESQL (Database)
- Django - Framework, Python(Backend)
- FIGMA
- GIT

## Dsyne

- Register to setup a new website
- Browse through available templates
- Ability to create more pages
- Unique address
- Ability to add social media links


## Dsyne Key features and release dates

> Landing page
> FAQ/ContactUs Page
> Create A Website
> About Us
> Documentation Page
> Dashboard:

- *Create A Website*
- *Profile Page*

## Project Status

> Project is : in progress

## Running Locally

```bash
git clone https://github.com/buike5/my_cms.git
```

```bash
pip install -r requirements.txt
```

### Setup Database and make migrations

<https://simpleisbetterthancomplex.com/2015/11/26/package-of-the-week-python-decouple.html>

```bash
python manage.py migrate
```

```bash
python manage.py runserver
```

## **Making Contribution**

### ***Create New Virtual Enviroment***

1. Cd into Project Directory
2. Open New Terminal and Run

```bash
py -m venv venv
```

1. Activate Virtual Env

```bash
.\env\Scripts\activate
```

[Virtual Environment setup guide](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/)

***note: you should be on the same dir as requirements.txt file***

### **Fork and Clone Repository**

1. Visit the Repository to the Project on Github Website: "https://github.com/zuri-training/proj_team_20.git"
2. Fork the repository: Click the "Fork" button on the upper right corner of the Repo page.
3. Make a Local Clone: Clone the forked repository to your local machine (computer)

   - Click on the "Code" button on the Repo page
   - Copy the URL for the forked Repo "https://github.com/zuri-training/proj_team_20.git"
   - Create a Folder on your Local machine / Computer for the project Workspace
   - Open Command prompt / Terminal in the same folder location
   - In your Terminal, type:
     `git clone https://github.com/zuri-training/proj_team_20.git`

### ***Install Requirements***

> cd into project directory

```bash
pip install -r requirements.txt
```

### **Add "Remote To" and "Pull From" Upstream**

4. Add a Remote to Upstream to your Repo:
   - In your terminal, type:
     `git clone https://github.com/zuri-training/proj_team_20.git`
5. Pull from upstream to download all changes in the project using `git pull upstream main`

### **Finish assigned Task / Issue**

6. Open the Project up in your code Editor
7. Complete your assigned task / Feature on your local machine.

8. When you are ready to add and push your feature / task to the Repo,
   <!-- - Create a new branch with your feature / task name you are adding e.g "ft-Add new channel". To do this, type:
     `git checkout -b ft-Add new channel` -->
   - Add your changes using:
     `git add file_name`
   - Commit your changes to the branch with a message using
     `git commit -m "Commit message"`

<!-- - _\* Note: if the Feature is a bug fix, use `bug:message` for your branch and commit message_ -->

### **Push New Branch to "Origin" Repository**

9. To make sure there are no conflict, Pull from upstream using `git pull upstream main`
10. Push your branch changes to the Repo using
    `git push upstream main`

### **Create Pull Request**

11. Once you push the changes to your repo, the **_`Compare & pull request`_** button will appear in GitHub page of your repo.
12. Click the button and make your request. Leave a comment in your request
13. Click Create pull request to open a new pull request

### **`If you are asked to make changes on the same feature, repeat steps 8 to 13 to add more commits to your pull request.`**

"https://github.com/zuri-training/proj_team_20.git"
