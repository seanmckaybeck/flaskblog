# flaskblog

This project serves as a simple example of how to make a blog using Python 3 and Flask.
It's only dependency not in the standard library is Flask.
This project has an included database called `my.db`.
It serves no purpose other than to give example posts so any users can see how the program works.
The script `insert_post_to_db.py` provides a simple way to insert new post data into the database specified in `config.py`.
Enter a title for the post, a URL slug (something simple), the day the post was created, and a file containing the html content to be displayed.

To run, simply run `python app.py` and access the blog on `http://127.0.0.1:5000`.

If a user were to try and use this to host a blog, all that would need to be changed are the templates.

It should also be noted that before running this, your database must be initialized.
In the same directory as `app.py`, execute the following.

```
$ python
>>> import app
>>> app.init_db()
>>> quit()
```

Now the database is initialized and ready to go.

If you desire to add more variables to the posts, such as summaries or tags, just modify `schema.sql` to include those fields,
modify `post_to_dict()` in `app.py` to get them, modify the templates to display them, and modify `insert_post_to_db.py` to
aid in adding them to the database.

## Dependencies

```
$ virtualenv venvs/flaskblog
$ source venvs/flaskblog/bin/activate
$ cd flaskblog
$ pip install -r requirements.txt
```
