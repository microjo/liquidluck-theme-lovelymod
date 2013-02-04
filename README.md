# Lovely Theme for Felix Felicis

This is the mod of liquidluck classic theme **Lovely** (original for liquidluck 0.2/0.3).



## Installation

Tested in Felix Felicis 3.5+


### Install with liquidluck

```bash
$ liquidluck install microjo/lovelymod
$ liquidlcuk install microjo/lovelymod -g
```

### Install by yourself

Git clone this repo, and place it in your blog:

```
your_blog/
    settings.py
    content/
    _themes/
        lovelymod/
```

### Install with git submodule

You can use git submodule for convience:

```bash
$ git submodule add git://github.com/microjo/liquidluck-theme-lovelymod.git _themes/lovelymod
```


## Configuration

Edit your settings:

1. change your theme to ``lovelymod``

	```python
	theme = {
		'name': 'lovelymod',
	}
	```

2. set category template to ``category.html``

	```python
	writer = {
	    'vars': {
	        'category_template': 'category.html',
	    }
	}
	```

## Customize

You can customize your theme with ``theme.vars``.

+ Change Navigation (default)

	```python
	theme = {
	    'vars': [
	        'navigation': [
				{'id': 'nav-home', 'icon': 'icon-home', 'name': 'Home', 'link': '/'},
				{'id': 'nav-about', 'icon': 'icon-info-sign', 'name': 'About', 'link': '/about.html'},
				{'id': 'nav-tags', 'icon': 'icon-tag', 'name': 'Tags', 'link': '/tag/'}
	        ]
	    ]
	}
	```
	1. id: navigation item id, unique, for css id atrribute.
	2. icon: leave it blank or you can use any icon in [Font Awesome](http://fortawesome.github.com/Font-Awesome/).

+ Google Analytics

	```python
	theme = {
	    'vars': {
	        'analytics': 'UA-xxxx',
	    }
	}
	```

+ Disqus Comment Support

	```python
	theme = {
	    'vars': {
	        'disqus': 'your-disqus-shortname',
	    }
	}
	```

+ Gravatar

	```python
	theme = {
	    'vars': {
	        'gravatar': 'your-gravatar-email',
	    }
	}
	```


## Allow comment

If you post is not public, this post will not be allowed to comment.
If you want to allow people to comment on your secret post, set

```python
theme = {
    'vars': {
        'allow_comment_on_secret_post': True,
    }
}
```
