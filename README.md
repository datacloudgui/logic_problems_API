# logic_problems_API

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#testing">Testing</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

This API solve two logical problems:

Can be reviewed: [https://smklogic.herokuapp.com/index/](https://smklogic.herokuapp.com/index/)

This project uses the following libraries and technologies:

* Python3
* Pandas - To analize the txt file
* Django
* PostgresQL - Two tablas created in Ping Pong problem
* GIT
* AWS - The deployed postgres DB attached to heroku settings

### Ping pong problem

 Ana, Jose and Juan play ping pong, each of them play the quantity of games viewed below.

If a player lose the game, in the next game the waiting player plays against the winner.

| Player name   | Score |
| ------------- | ------------- |
| Ana  | 17  |
| José  | 15  |
| Juan | 10 |

 **Question:** Who is the loser of the second game? and which games this person lose?

 ### Second problem: Find Password

Find the shortest password based in a .txt file, that contain sequences of the password.

A sequence contain some characters of the password keeping the order.

**password:** 34879 one possible **sequence:** 389

The input file must contain a sequence per line. An example file can be dowloaded from:

Right clic and Save Link As ...:

[https://raw.githubusercontent.com/datacloudgui/logic_problems_API/main/keylog.txt](Link_to_keylog.txt)

<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/datacloudgui/logic_problems_API.git
   ```
2. Don forget setup your virtual environment with your favorite tool

3. Activate the virtual environment and install the dependencies

4. Install requirements
   ```python
   pip install -r requirements.txt
   ```
4. Setup a Postgres DB, the recommended way is using a
   ```sh
   docker run --rm --name core-postgres -p 5432:5432 -e POSTGRES_PASSWORD=secret -d postgres
   ```

<!-- USAGE EXAMPLES -->
## Usage

To use locally just run the server

```bash
python manage.py runserver
```

<!-- TESTING -->
## Testing

The two main files that contain the solution to the problems can be tested:

1. Test the Ping Pong problem

Those test was writen using the Django dedicated file tests.py and can be run with:

```python
python manage.py test logic.tests
```

2. Test the Password finder

Those test was writen into the file that define the Class writen and can be run with:

```python
python logic/password_finder.py
```

<!-- CONTACT -->
## Contact

Guillermo Sanchez - [@datacloudgui](https://twitter.com/datacloudgui) - guillermo@datacloudgui.com

Personal page: [datacloudgui.com](https://datacloudgui.com)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [Othneil Drew](https://github.com/othneildrew) by this amazing template.