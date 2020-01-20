# Book Inventory Django Application

1. User logging In using LinkedIn.
2. Then the user can Add Inventory using Create Inventory Button.
3. Enter the category name in the search bar to get the list of books associated with the respective.
### Note:
1. Use the control key to select multiple categories while entering books in Inventory.
2. As we do not have any Inventory out date, so I assumed the searching date as Inventory out date and updated the Inventory out date accordingly.
 

## Installation

run command to install all requirements using the command

```bash
pip install -r requirements.txt
```

## LinkedIN Authentication
### Add below code in setting.py file

```python
AUTHENTICATION_BACKENDS = (
    'social_core.backends.linkedin.LinkedinOAuth2', # for LinkedIn Authentication 
    'django.contrib.auth.backends.ModelBackend',  # default authentication classes
)

```
```
INSTALLED_APPS = [ 
      ...., 
      'social_django',
      ....,

]
```
### To create developer app:
#### Let’s visit the Linkedin developers, i.e:- https://www.linkedin.com/developers/
#### Once the app has successfully been created you'll get Client ID and Secret
#### Update Client ID and Client Secret in setting file
```
SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY = '*************'  # Client ID
SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET = '*************'  # Client Secret
SOCIAL_AUTH_LINKEDIN_OAUTH2_SCOPE = ['r_basicprofile', 'r_emailaddress']
SOCIAL_AUTH_LINKEDIN_OAUTH2_FIELD_SELECTORS = ['email-address', 'formatted-name', 'public-profile-url', 'picture-url']
SOCIAL_AUTH_LINKEDIN_OAUTH2_EXTRA_DATA = [
    ('id', 'id'),
    ('formattedName', 'name'),
    ('emailAddress', 'email_address'),
    ('pictureUrl', 'picture_url'),
    ('publicProfileUrl', 'profile_url'),
]
```
```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # The social_django context processors help in adding backend and associations data to template context
                'social_django.context_processors.backends',  # add this
                'social_django.context_processors.login_redirect',  # add this
            ],
        },
    },
]
```

## Command To Run Program:
#### To create migration
```
python manage.py makemigration
```
#### To run migration
```
python manage.py migrate
```
#### To Create Category run management command
```
python manage.py create_inventory_category
```