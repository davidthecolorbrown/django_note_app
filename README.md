# Note-taking Web Application
## Description
* A simple web app for taking, storing, and reviewing notes (plus learning how to use Django!)

## API
* API was created using Django RESTful framework.
* Login as a user and use following API endpoints to brows
* Link to Django's Browserable API page:
```html
http://{localhost}/note_manager/note_manager/api/
```
* GET (or POST to) all user's notes ('.note_manager/api/{base_name}/'):
```html
http://{localhost}/note_manager/note_manager/api/notes/
```
* GET (or UPDATE/DELETE) a single note ('.note_manager/api/{base_name}/<:id>'):
```html
http://{localhost}/note_manager/note_manager/api/notes/<:id>
```
* The format of the response as json:
```json
{
    "title": "",
    "body": "",
    "categories": "",
    "author": "",
}
```

## Todo
* [] Re-organize the routes.
* [] Fix 'NoteDetails' view. The function-based version allows commenting on a post, but the class-based version does not.
* [] Fix 'login' page to route to all user's notes formatted with pagination (currently only uses pagination when user clicks "Home" in navbar).
* [] Encrypt backup files.
* [] API endpoint for getting notes by date range.
* [] API endpoint for getting notes by user, category.
* [] Remove API endpoints for post, update, and delete.
* [] Only allow API access as admin user or with API key.
