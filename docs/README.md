## Endpoints description

## `"employees/":`
#### Methods: `[GET, POST]`
#### Get all or create new employee

## `"employees/<int:pk>":`
#### Methods: `[GET, PUT, DELETE]`
#### Get, update or delete employee with id `pk` (employee can edit himself or `is_stuff` required or readonly)

## `"restaurants/":`  
#### Methods: `[GET, POST]`
#### Get all or create new restraunt (`is_stuff` required or readonly)
## `"restaurants/<int:pk>/":`  
#### Methods: `[GET, PUT, DELETE]`
#### Get, update or delete restraunt with id `pk` (`is_stuff` required or readonly)

## `"restaurants/<int:pk>/menus/":`
#### Methods: `[GET, POST]`
#### Get all or create menu for restraunt (`is_stuff` required or readonly)
#### `dishes` receives array of `dish`'s ids

## `"menus/<int:pk>/":`
#### Methods: `[GET, PUT, DELETE]`
#### Get, update or delete menu with id `pk` (`is_stuff` required or readonly)

## `"offers/":`
#### Methods: `[GET]`
#### Get all menus for today (auth required)

##  `"offers/result/":`
#### Methods: `[GET]`
#### Get menu with most votes or Http404 (auth required)

## `"offers/<int:pk>/vote/":`
#### Methods: `[POST]`
#### Vote for one of today's menu (auth required)

## `"dishes/":`
#### Methods: `[GET, POST]`
#### Get all or create new dish (`is_stuff` required)

## `"dishes/<int:pk>/":`
#### Methods: `[GET, PUT, DELETE]`
#### Get, update or delete dish with id `pk` (`is_stuff` required)