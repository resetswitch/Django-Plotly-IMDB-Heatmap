<h1>Django-Plotly-IMDB-Heatmap</h1>

<h2>Website Demo</h2>
<h6>

Link: <a href="https://django-plotly-imdb-heatmap.herokuapp.com/">https://django-plotly-imdb-heatmap.herokuapp.com/</a>

WARNING 1: May take up to 90 seconds to intially load the website!<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (a limitation due to Heroku's free tier)

WARNING 2: Only 1 person is allowed to visit the site at a time!<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (a limitation due to Heroku's free tier)

WARNING 3: Not optimized for mobile devices!<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (For a better experience, as per .gif below, a desktop is recommended)

Demonstration .gif:

<img src="Images/ActiveWebsiteDemo.gif" width=500>

</h6>

<h2>About</h2>
<h6>

Copy-Paste any of your favorite IMDB TV show URLs and plug them into this website to display a Plotly episodal heatmap. Each cell is colored according to an IMDB TV episode rating on a scale of 1-10 (bad to good or red to green). Plotly is a free and awesome tool for interactive data visualization. In the heatmap provided, you can hover your mouse over cells to see more specific episodal information.
</h6>
<h2>Features</h2>
<h6>

- Interactive plot
- Scrapping Data from IMDB website with `BeautifulSoup`
- Navigation bar with built in loading brand
- Bootstrap styling
- Input handling
- Notifications
</h6>

<h2>Installation and Running</h2>
<h6>

Requirements are in the `requirements.txt` file.

Use `pipenv`:

```bash
$ cd Django-Plotly-IMDB-Heatmap
$ pipenv install -r requirements.txt
```


Run it

```bash
$ cd Django-Plotly-IMDB-Heatmap
$ pipenv shell
(Django-Plotly-IMDB-Heatmap) $ python manage.py makemigrations
(Django-Plotly-IMDB-Heatmap) $ python manage.py migrate
(Django-Plotly-IMDB-Heatmap) $ python manage.py runserver
```
Then click on the link: <a href="http://127.0.0.1:8000">http://127.0.0.1:8000</a>
</h6>
