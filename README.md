# FYPC - Fix Your PC! 

## Sections

1.  [Introduction](Introduction)
2.  [Overview](Overview)
3.  [Progress & Issues](Progress-&-Issues)
4.  [FYPC Deployment](FYPC-Deployment)

## Introduction

FYPC (full name is "Fix Your PC - For All Your PC Needs!") is a web application that serves as PC, Laptops and Accessories for them shop and also as maintenance service center. The site is built using Django and HTML, CSS, and JavaScript. It offers a simple way to find whatever you PC needs!

## Overview

FYPC - is an online electronics store focused on PC and related products. On the site, you can create orders, add items to your cart, and save items to your favorites. The site also features a custom admin panel built with Bootstrap, which is easier to use than the standard Django admin panel.

To build this site I used: 
- HTML
- CSS (SCSS)
- fontawesome icons
- JQuery
- SwiperJS
- Django 4.1.5
  - django-spurl
  - django-filter
  - djnago-phonenumber-field
  - mysqlclient

Here are some screenshots:

### Home page, user isn't logged in
![Home page user is not logged in](https://i.imgur.com/20Yxf93.png)

[Go Back to sections](Sections)

### Home page 2nd scroll
![Home page 2nd scroll](https://i.imgur.com/SODWta5.png)

[Go Back to sections](Sections)

### Catalog
![Catalog](https://i.imgur.com/lVlzDLK.png)

[Go Back to sections](Sections)

### Login page
![Login page](https://i.imgur.com/QXokyo1.png)

[Go Back to sections](Sections)

### Contacts page
![Contacts mobile](https://i.imgur.com/3iruVFk.png)

[Go Back to sections](Sections)

### User favourites mobile
![User favourites mobile](https://i.imgur.com/odRSfR7.png)

[Go Back to sections](Sections)

### Admin // Products tab
![Admin | Products tab](https://i.imgur.com/V121mSM.png)

[Go Back to sections](Sections)

### Admin // Product view
![Admin | Product view](https://i.imgur.com/dUXFdJc.png)

[Go Back to sections](Sections)

## Progress & Issues 

### Things that i will add in future!
1.  Bundles
2.  Pagination and filters wherever they are placed (atm they're only at catalog page)
3.  Working "Callback" form on home page, which is not funcltional
4.  Add worker cabinet
5.  Add all admin pages that are currently missing
6.  env file to config database connection to yours
7.  and of course fixes

### Issues that won't be fixed
1.  Bad mobile adaptivity (since it was my first site ever ive made some big mistakes that will be annoying to fix)
2.  Mistakes in styling (like images on home page, catalog card position in the middle, when theres odd number of them


## FYPC deployment

I will provide docker-compose file here later on to deploy this site with only a few moves.