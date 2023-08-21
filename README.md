# Stogram backend part

This is a backend part of Stogram application. Main idea of this app is a social networking for photo exchange.

To test this api you need to pull repository on your linux machine(Ubuntu via WSL will do the trick) and install Docker there.

There is already .env file with database passwords and user passwords. Because it is not deployed yet :)

After that you need to cd to the project directory on linux and use the following commands:

```
docker compose build
docker compose up
```

You can use localhost:8070/admin url and login there using url and password from .env file. There you can create or delete entities in database.

Than you can use the following urls to test the api:

api/user/<int:user_id> - GET request to get user by id
api/user_posts/<int:id - GET request to get user posts by user id
api/votes/<int:post_id - GET request to see how many likes are on post
api/register - URL for registration
api-auth/ - URL for auth

There also are voting for posts, with "already vote" validation
