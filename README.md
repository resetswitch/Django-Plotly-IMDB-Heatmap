<h1>Django-Plotly-IMDB-Heatmap</h1>

<h2>Website Demo</h2>
<h6>

Link: to be added shortly...

Demonstration .gif:

<img src="Images/TheOfficePlotly.gif" width=500>

</h6>

<h2>About</h2>

<h4>Current</h4>
<h6>

The current version displays an IMDB Plotly heatmap of a single pre-chosen TV show where the data has already been scrapped from IMDB website on .csv files. Plotly is a free and awesome tool for interactive data visualization. In the heatmap provided you can hover your mouse over cells to see more specific episodal information.

To change the TV Show displayed, go to `pages/views.py` and change the `filename` assignment to any file in the `pages/data/` folder

```python
    ...
    filename = '/data/Dark (2017-2020) - IMDB.csv'
    ...
```

Current Selection of TV Shows:
- <strong>`Dark`</strong> `(2017-2020) - IMDB.csv`
- <strong>`Family Guy`</strong> `(1999- ) - IMDB.csv`
- <strong>`SpongeBob SquarePants`</strong> `(1999- ) - IMDB.csv`
- <strong>`The Office`</strong> `(2005-2013) - IMDB.csv`

</h6>
<h4>Future Plans</h4>
<h6>

Copy-Paste any of your favorite IMDB TV show URLs and plug them into this website to display a Plotly episodal heatmap.
</h6>

<h2>Installation</h2>
<h6>

Requirements are in the `requirements.txt` file.

Use `pipenv`:

```bash
$ cd Django-Plotly-IMDB-Heatmap
$ pipenv install -r requirements.txt
```
</h6>

<h2>Run it<h2>
<h6>

```bash
$ cd Django-Plotly-IMDB-Heatmap
$ pipenv shell
(Django-Plotly-IMDB-Heatmap) $ python manage.py makemigrations
(Django-Plotly-IMDB-Heatmap) $ python manage.py migrate
(Django-Plotly-IMDB-Heatmap) $ python manage.py runserver
```
Then click on the link: <a href="http://127.0.0.1:8000">http://127.0.0.1:8000</a>
</h6>