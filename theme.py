#!/usr/bin/env python
# -*- coding: utf-8 -*-

from liquidluck.utils import to_datetime

name = 'Lovely'
version = '1.0'
website = 'https://github.com/microjo/liquidluck-theme-lovelymod'
author = {
	'name': 'MiCRoJo',
	'website': 'http://microjo.github.com',
}

lang = 'en'

navigation = [
	{'id': 'nav-home', 'icon': 'icon-home', 'name': {'zh': u'首页', 'en': 'Home'}, 'link': '/'},
	{'id': 'nav-about', 'icon': 'icon-info-sign', 'name': {'zh': u'关于', 'en': 'About'}, 'link': '/about.html'},
	{'id': 'nav-tags', 'icon': 'icon-tag', 'name': {'zh': u'标签', 'en': 'Tags'}, 'link': '/tag/'}
]

#: define strings used in the theme
strings = {
	'zh': {'archive_prev': u'上一页', 'archive_next': u'下一页', 'archive_title': u'Archive/归档',
		'post_newer': u'前一篇', 'post_older': u'后一篇',
		'post_created': u'发布：', 'post_modified': u'修改：',
		'post_tagged': u'标签：', 'post_author': u'作者：',
		'tagcloud_title': u'Tags/标签', 'tag_posts': u'篇'},
	'en': {'archive_prev': 'PREV', 'archive_next': 'NEXT', 'archive_title': 'Archive',
		'post_newer': 'PREV', 'post_older': 'NEXT',
		'post_created': 'Created at:&nbsp;', 'post_modified': 'Modified at:&nbsp;',
		'post_tagged': 'Tagged in:&nbsp;', 'post_author': 'by ',
		'tagcloud_title': 'Tags', 'tag_posts': 'posts'}
}


disqus = None
analytics = None
gravatar = None

allow_comment_on_secret_post = False

display_updated_time_of_post = False
