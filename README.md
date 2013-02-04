# Lovely Theme for Felix Felicis

This is the mod for liquidluck classic theme Lovely (original for liquidluck 0.2/0.3).



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

Edit your settings, change your theme to ``lovelymod``.


## Customize

You can customize your theme with ``theme.vars``.

+ Change Navigation (example)

```python
theme = {
    'vars': [
        'navigation': [
            {'name': 'Home', 'link': '/'},
            {'name': 'Life', 'link': '/life/'},
        ]
    ]
}
```

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
        'allow_comment_on_secret_post': True
    }
}
```
